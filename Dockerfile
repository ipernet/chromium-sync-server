FROM debian:jessie

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q --fix-missing && \
  apt-get -y update && \
  apt-get -y --force-yes upgrade && \
  apt-get -y --force-yes install \
    git \
    python \
    sudo \
    locales \
    build-essential \
    ninja-build \
    lsb-release \
    libgconf-2-4 \
    libnss3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workdir

RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git

ENV PATH $PATH:/workdir/depot_tools

WORKDIR chromium

# Add "--no-history" to run the experiment on master
RUN fetch --nohooks chromium

WORKDIR src

# RUN bash build/install-build-deps.sh --no-syms --no-arm --no-nacl --no-chromeos-fonts

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q --fix-missing && \
  apt-get -y update && \
  apt-get -y --force-yes upgrade && \
  apt-get -y --force-yes install \
    apache2.2-bin bison cdbs curl devscripts dpkg-dev elfutils fakeroot flex fonts-ipafont fonts-thai-tlwg g++ git-core git-svn gperf lib32gcc1 lib32stdc++6 libapache2-mod-php5 \ 
	libatk1.0-0 libav-tools libbluetooth-dev libbrlapi-dev libbrlapi-dev libbz2-1.0 libbz2-dev libc6 libc6-i386 libcairo2 libcairo2-dev libcap-dev libcap2 \ 
	libcurl4-gnutls-dev libdrm-dev libelf-dev libexpat1 libffi-dev libffi6 libfontconfig1 libfreetype6 libgbm-dev libgconf2-dev libgl1-mesa-dev \ 
	libglib2.0-0 libglib2.0-dev libglu1-mesa-dev libgnome-keyring-dev libgnome-keyring0 libgtk2.0-0 libgtk2.0-dev libjpeg62-turbo-dev libkrb5-dev libnspr4-0d \
	libnss3-1d libnss3-dev libpam0g libpam0g-dev libpango1.0-0 libpci-dev libpci3 libpcre3 libpixman-1-0 libpulse-dev libpulse0 libsctp-dev libspeechd-dev \ 
	libspeechd2 libsqlite3-0 libsqlite3-dev libssl-dev libstdc++6 libudev-dev libudev1 libwww-perl libx11-6 libx11-xcb1 libxau6 libxcb1 libxcomposite1 libxcursor1 libxdamage1 \
	libxext6 libxfixes3 libxi6 libxinerama1 libxkbcommon-dev libxrandr2 libxrender1 libxslt1-dev libxss-dev libxt-dev libxtst-dev libxtst6 mesa-common-dev openbox patch \ 
	php5-cgi pkg-config python python-cherrypy3 python-crypto python-dev python-numpy python-opencv python-openssl python-psutil python-yaml realpath rpm ruby subversion \
	fonts-indic wdiff xcompmgr zip zlib1g ; \
    rm -rf /var/lib/apt/lists/*

	
# Remove this RUN to run the experiment on master
RUN git checkout 58.0.3011.4

RUN gclient runhooks 

# Compile a binary of the test sync server if you don't want the python version (caution: very long)
# RUN gn gen --enable_nacl=false --symbol_level=0 --remove_webcore_debug_symbols=true --is_debug=false out/Default && ninja -C out/Default components/sync:run_sync_testserver

# Build the python app
RUN gn gen --enable_nacl=false --symbol_level=0 --remove_webcore_debug_symbols=true --is_debug=false out/Default && \
    ninja -C out/Default third_party/protobuf:py_proto && \
    ninja -C out/Default components/sync/protocol:protocol
	
WORKDIR /workdir/sync-server

# Import require packages and fix imports for a standalone run
RUN mkdir sync lib && \
    cp -rp /workdir/chromium/src/out/Default/pyproto/components/sync/protocol/ lib/protocol/ && \
    cp -rp /workdir/chromium/src/out/Default/pyproto/google . && \
    cp -rp /workdir/chromium/src/components/sync/tools/testserver/ sync/testserver/ && \
    cp -rp /workdir/chromium/src//net/tools/testserver/ lib/testserver/ && \
    cp -rp /workdir/chromium/src/third_party/tlslite/tlslite/ . && \
	rm -rf /workdir/chromium && \
	rm -rf /workdir/depot_tools && \
    touch lib/testserver/__init__.py && \
	touch lib/protocol/__init__.py && \
	touch sync/testserver/__init__.py && \
    touch sync/__init__.py && \
    touch lib/__init__.py && \
	sed -i 's#import echo_message#from lib.testserver import echo_message#' sync/testserver/sync_testserver.py && \
    sed -i 's#import testserver_base#from lib.testserver import testserver_base#' sync/testserver/sync_testserver.py && \
    /bin/bash -c 'for line in $(find /workdir/sync-server/lib/protocol/ -name "*.py" -type f -exec basename {} .py \;); do sed -i "s/import $line/from lib.protocol import $line/" /workdir/sync-server/sync/testserver/chromiumsync.py; done'
