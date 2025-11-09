# ダンロードしたい（`curl`）

```bash
curl -o <ファイル名> URL
```

## インストールしたい（`curl`）

```console
$ curl --version
curl 8.7.1 (x86_64-apple-darwin24.0) libcurl/8.7.1 (SecureTransport) LibreSSL/3.3.6 zlib/1.2.12 nghttp2/1.64.0
Release-Date: 2024-03-27
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns ldap ldaps mqtt pop3 pop3s rtsp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS GSS-API HSTS HTTP2 HTTPS-proxy IPv6 Kerberos Largefile libz MultiSSL NTLM SPNEGO SSL threadsafe UnixSockets

$ brew install curl
```

`curl`はmacOSに標準でインストールされています。
Homebrewで最新版をインストールできます。

## 保存したい（`-o` / `-O`）

```console
# ファイル名を指定
$ curl -o example.html https://example.com
```

`-o ファイル名`オプションで、指定したURLをファイルとして保存できます。

```console
# リモートのファイル名を使って保存
$ curl -O https://example.com/index.html

# ディレクトリまでの指定だとエラー
$ curl -O https://example.com/
curl: Remote file name has no length
curl: (23) Failed writing received data to disk/application
```

`-O`オプションでURLをそのままファイル名として利用できます。
HTMLファイルまでのURLパスを指定しないとエラーになります。

## ヘッダーを取得したい（`-I`）

```console
$ curl -I https://httpbin.org/status/200

HTTP/2 200
date: Sun, 09 Nov 2025 01:26:20 GMT
content-type: text/html; charset=utf-8
content-length: 0
server: gunicorn/19.9.0
access-control-allow-origin: *
access-control-allow-credentials: true
```

`-I`オプションでヘッダー情報を取得できます。

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
