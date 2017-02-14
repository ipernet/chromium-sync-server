# chromium-sync-server

## ! Experimental

This is the test sync server used in Chromium development that can run in standalone mode.

## Limitations

 * Only one Chrome Sync account is supported by server instance.
 * The test server does not persist data on restart.

## Security

:bangbang: Totally unsafe, use at your own risks :bangbang:

 * Anyone knowing your *sync-url* will be able to fetch your encrypted sync data and brute-force it offline.

 * If you don't use an  **explicit passphrase** when activating sync, your sync data will be in clear text (excepts: `Passwords`, `WiFi Credentials`).

**Notes:**

When using an **explicit passphrase**, the whole set of syncable data types are encrypted:

`Bookmarks, Preferences, Passwords, Autofill Profiles, Autofill, Autofill Wallet Metadata, Themes, Typed URLs, Extensions, Search Engines, Sessions, Apps, App settings, Extension settings, App Notifications, Dictionary, Favicon Images, Favicon Tracking, Articles, App List, WiFi Credentials, Arc Package, Printers, Reading List`

**ref:** chrome://sync-internals/

> **Conclusion:** Use the Google Sync default sync server and set a passphrase there!


## Usage


```bash
$ git clone https://github.com/ipernet/chromium-sync-server.git
$ cd dist/58.0.3011.4/src
$ patch -p1  <../patch/bootstrap.patch
$ python server.py --port=5090 --log-to-console
```

Start Chrome/Chromium with your custom sync URL:

```
chrome --sync-url=http://127.0.0.1:8090/chromiumsync
```


* Settings > Disconnect any existing account (do not delete local data).

* Settings > Sign in in to Chrome

* Settings > Advanced Sync settings > Encrypt all synced data with your own passphrase


**On Android (require root):**

```
echo 'chrome --sync-url=http://127.0.0.1:8090/chromiumsync' > /data/local/tmp/chrome-command-line
```


## Recipe


The Dockerfile is a recipe of how to extract the code of the test sync server from Chromium sources.

```
$ docker build -t dummy/chromium-sync:latest .
$ docker run --rm -it -v ~/sync-server:/data dummy/chromium-sync:latest cp -rp /workdir/sync-server /data
```
