# HTTPリクエストしたい（`curl`）

```console
$ curl -o ファイル名 URL
```

`curl`は、HTTPリクエストを送信するコマンドです。

## インストールしたい（`curl`）

```console
$ curl --version
curl 8.7.1 (x86_64-apple-darwin24.0) libcurl/8.7.1 (SecureTransport) LibreSSL/3.3.6 zlib/1.2.12 nghttp2/1.64.0
Release-Date: 2024-03-27
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s rtsp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS GSS-API HSTS HTTP2 HTTPS-proxy IPv6 Kerberos Largefile libz MultiSSL NTLM SPNEGO SSL threadsafe UnixSockets

$ brew install curl
```

`curl`はHomebrewでインストールできます。
macOSには標準でインストールされています。

## ダウンロードしたい（`--remote-name` / `-O`）

```console
// リモートのファイル名を使って保存
$ curl -O https://example.com/index.html
```

`--remote-name`（`-O`）で、指定したURLをそのままファイル名として利用できます。

```console
// ディレクトリまでの指定だとエラー
$ curl -O https://example.com/
curl: Remote file name has no length
curl: (23) Failed writing received data to disk/application
```

HTMLファイルまでのURLパスを指定しないとエラーになります。

## 名前付きダウンロードしたい（`--output` / `-o`）

```console
$ curl -o example.html https://example.com
```

`--output`（`-o`）で、指定したファイル名で保存できます。

## リダイレクトを追跡したい（`--location` / `-L`）

```console
# リダイレクト先を追跡してダウンロード
$ curl -LO https://github.com/shotakaha/kumaroot/archive/refs/tags/v2026.8.3.zip
$ curl -LO https://github.com/shotakaha/kumaroot/archive/refs/tags/v2026.8.3.tar.gz
```

`--location`（`-L`）で、リダイレクト先を追跡してダウンロードできます。

`curl`はデフォルトでリダイレクトを追跡しません。
GitHub Releaseのように、実際のダウンロードURLがリダイレクト先にある場合、`-L`（`--location`）オプションを付けないとファイルを保存できません。
`-O`と組み合わせて`-LO`のように指定することが多いです。

## ヘッダーを取得したい（`--head` / `-I`）

```console
$ curl --head https://httpbin.org/status/200

HTTP/2 200
date: Sun, 09 Nov 2025 01:26:20 GMT
content-type: text/html; charset=utf-8
content-length: 0
server: gunicorn/19.9.0
access-control-allow-origin: *
access-control-allow-credentials: true
```

`--head`（`-I`）オプションでヘッダー情報を取得できます。

```console
$ curl -I https://httpbin.org/status/404
HTTP/2 404
date: Sun, 09 Nov 2025 01:25:37 GMT
content-type: text/html; charset=utf-8
content-length: 0
server: gunicorn/19.9.0
access-control-allow-origin: *
access-control-allow-credentials: true
```

:::{seealso}

- [](./command-httpie.md)
- [](./command-wget.md)
- [](./command-xh.md)

:::
