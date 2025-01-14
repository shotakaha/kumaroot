# SSL証明書したい（`openssl`）

```console
$ openssl version
OpenSSL 3.4.0 22 Oct 2024 (Library: OpenSSL 3.4.0 22 Oct 2024)
```

`openssl`コマンドで、暗号化やSSL/TLS、証明書操作、鍵作成など、
OpenSSLを使ったさまざまな操作ができます。

## 証明書したい（`openssl x509`）

```console
// 証明書を表示
$ openssl x509 -in 証明書.pem -noout -text

// 証明書の有効期限を確認
$ openssl x509 -in 証明書.pem -noout -dates
```

`openssl x509`コマンドで証明書の操作ができます。
`-in`オプションでPEM形式の証明書を指定します。
`-noout`オプションで出力内容に証明書自身を非表示にできます。

:::{note}

**PEM形式**（Privacy Enhanced Mail）は、Base64でエンコードされたテキスト形式で、秘密鍵／公開鍵や証明書、証明書チェーンを保存する汎用的な形式です。
ファイルの内容は
`-----BEGIN`と
`-----END`で囲まれています。

同じPEM形式でも、用途によって次のような拡張子を使用します。

| 用途 | 秘密鍵 | 公開鍵 | ファイル名 |
|---|---|---|---|
| 汎用 | `.key` | `.pem` / `.pub` | |
| SSH公開鍵認証 | `.key` / なし | `.pub` | `id_ed25519` / `id_ed25519.pub` |
| SSL/TLS証明書 | `.key` | `.crt` / `.cer` | `server.key` / `server.crt` |
| 証明書チェーン | `.pem` | `.pem` | |

**X.509証明書** は公開鍵基盤（PKI; Public Key Infrastructure）で使用される標準形式のデジタル証明書です。
サーバー証明書の公開鍵は、Linux環境では`.crt`、Windows環境では`.cer`を利用します。

:::

## CSRしたい（`openssl req`）

```console
// CSRを確認
$ openssl req -in 証明書署名要求.csr -noout -text
```

`openssl req`コマンドで、CSRファイルを操作できます。

```console
// CSRを新規作成
$ openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr
// CSRに必要なDN情報を入力する
// -----
Country Name (2 letter code) []: JP # 国名を2文字で入力する
State or Province Name (full name) [Some-State]: Xxxxx # 県名を入力する
Locality Name (eg, city) []: # 都市名
Organization Name (eg, company) []: # 機関名
Organizational Unit Name (eg, section) []: # スキップ
Common Name (e.g. server FQDN or YOUR name) []: # URLを入力する（一番大事）
Email Address []: # スキップ

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []: # スキップ
An optional company name []: # スキップ
```

`-new`オプションで、秘密鍵とCSRファイルを生成できます。
`-newkey rsa:ビット長`で鍵の長さを変更できます。デフォルトは`rsa:2048`です。
`-nodes`でパスワードなし秘密鍵を生成します。
`-keyout`で生成する秘密鍵のファイル名を変更できます。ここでは`server.key`としました。
`-out`で生成するCSRのファイル名を変更できます。ここでは`server.csr`としました。

コマンドを実行すると、DN（Distinguished Name）を入力するダイアログが表示されます。
必要な情報を適宜入力します。

:::{note}

**証明書署名要求**（CSR; Certificate Signing Request）は、公開鍵基盤（PKI）において証明書を発行してもらうために必要なデータを含んだファイルです。

認証局にCSRファイルを提出し、証明書を発行してもらいます。
CSRの提出方法は、利用する認証局の手順を確認してください。

大学や研究機関の場合、UPKI（University Public Key Infrastructure）が利用できるかもしれません。
UPKIは、国立情報学研究所（NII）が運営する
中間認証局を通じて、X.509証明書を発行してもらえるサービスです。

:::

```console
// 自己証明書
$ openssl req -new -key 秘密鍵.key -out 自己証明書.pem -x509 -nodes -sha256 -days 365
```
