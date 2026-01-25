# ひとり認証局したい（`mkcert`）

```bash
mkcert example.org
```

[mkcert](https://github.com/FiloSottile/mkcert)は、
ローカル開発環境でHTTPSできるようにするツールです。

ローカルPCに専用の**ローカル認証局（LocalCA）**を自動生成し、
その認証局をブラウザに信頼済みとして登録することで、ローカル環境でも本番と同じようにHTTPSを使うことができます。s

これまでは、SSL自己署名証明書（通称「おれおれ証明書」）を作成・管理するのが一般的でしたが、`mkcert`のおかげで、より簡便にローカル認証局できます。

:::{note}

ローカル認証局は、あくまで自分のPC専用の認証局です。
外部公開したり、本番環境で利用したりすることはできません。

:::

## インストールしたい（`mkcert`）

```console
$ brew install mkcert
$ mkcert --version
v1.4.4
```

`mkcert`はHomebrewでインストールできます。

## 証明書を生成したい

```console
$ mkcert localhost
# Created a new certificate valid for 1 year.
# cert.pem: the certificate
# key.pem: the private key
```

`mkcert localhost`で単一ドメインのローカル証明書を作成できます。
`localhost.pem`（証明書）と
`localhost-key.pem`（秘密鍵）が生成されます。

:::{note}

証明書や秘密鍵の拡張子として
`.pem`、`.crt`/`.cert`、`.key`が利用されます。

`mkcert`のデフォルトの出力形式は、証明書も秘密鍵も`.pem`に統一されています。
実際の運用では、一般的に
証明書には`.crt`（もしくは`.cert`）、
秘密鍵には`.key`が使用されます。

どれもPEM形式のテキストファイルです。
あとからお互いにリネームしても大丈夫です。

:::

## 特定のディレクトリに証明書を生成したい

```console
$ mkcert -cert-file ./certs/server.pem -key-file ./certs/server.key localhost.example.com
```

`-cert-file 証明書.pem`、
`-key-file 秘密鍵.pem`で
任意のパスを指定できます。

## 証明書の有効期限を確認したい

```bash
$ openssl x509 -in localhost.pem -text -noout | grep -A 2 "Validity"
```

証明書の有効期限を確認するには
[openssl](./command-openssl.md)を使います。

## ローカル認証局したい

```console
$ mkcert -CAROOT
~/.local/share/mkcert
```

`mkcert -CAROOT`で現在の認証局のパスを確認できます。

```bash
$ export CAROOT="/custom/path"
$ mkcert -install
```

環境変数`CAROOT`で、認証局のパスを変更できます。

```console
$ mkcert -install
```

`mkcert -install`で、システムのトラストストアにローカル認証局を登録できます。
登録後、このCAで署名した証明書はブラウザで警告なく表示されます。

```console
$ open /Applications/Utilities/Keychain\ Access.app
```

macOSの`Keychain Access.app`で登録内容を確認できます。
（`System Keychains` → `System Roots` → `Certificates`）

```bash
$ mkcert -uninstall
```

`mkcert -install`でシステムのトラストストアから認証局を削除できます。
証明書は再度作成する必要があります。

## 複数のドメインの証明書を作成したい

```console
$ mkcert localhost 127.0.0.1 ::1 example.local
# Created a new certificate valid for localhost, 127.0.0.1, ::1, example.local
```

複数のドメイン・IPアドレスを同時に指定できます。

```console
$ mkcert "*.example.com" example.com
```

ワイルドカードも対応しています。

## Nginxでローカル証明書したい

```nginx
server {
    listen 443 ssl;
    server_name localhost;

    ssl_certificate /path/to/localhost.pem;
    ssl_certificate_key /path/to/localhost-key.pem;
}
```

Nginxでは
`ssl_certificate`に証明書（`localhost.pem`）、
`ssl_certificate_key`に秘密鍵（`localhost-key.pem`）の
パスを指定してください。

## Apacheで証明書したい

```apache
<VirtualHost *:443>
    ServerName localhost

    SSLEngine on
    SSLCertificateFile /path/to/localhost.pem
    SSLCertificateKeyFile /path/to/localhost-key.pem
</VirtualHost>
```

Apache（httpd）では、
`SSLEngine on`でSSL証明書を有効にし、
`SSLCertificateFile`に証明書（`localhost.pem`）、
`SSLCertificateKeyFile`に秘密鍵（`localhost-key.pem`）の
パスを指定してください。

## コンテナーで証明書を使いたい

```yaml
services:
  wordpress:
    image: bitnami/wordpress:latest
    volumes:
      - wordpress_data:/bitnami/wordpress
      - ./certs:/bitnami/apache/conf/bitnami/certs:ro
```

`mkcert`で生成した証明書をDockerコンテナーにマウントして使用できます。
上記は`bitnami/wordpress`イメージを使ってカスタム証明書をマウントしています。

```bash
# 証明書を生成
$ mkcert -cert-file ./certs/server.crt -key-file ./certs/server.key localhost
```

上記で生成した証明書ファイルを`./certs/`ディレクトリに配置してください。

:::{note}

Bitnamiのイメージ（`bitnami/wordpress`）はSSL/TLS対応が簡単です。
WordPressの公式イメージ（`wordpress`）ではApache設定ファイルの編集が必要です。

:::

## 証明書を再発行したい

```console
$ rm localhost.pem localhost-key.pem
$ mkcert localhost
```

証明書の秘密鍵が漏洩したり、証明書の有効期限が切れてしまった場合は、
いったんファイルを削除し、新しく生成する必要があります。

## リファレンス

- [mkcert - GitHub](https://github.com/FiloSottile/mkcert)
- [mkcert - releases](https://github.com/FiloSottile/mkcert/releases)
- [Mozilla CA Certificate Program](https://wiki.mozilla.org/CA/Included_Certificates)
- [Let's Encrypt（本番環境向け）](https://letsencrypt.org/)
