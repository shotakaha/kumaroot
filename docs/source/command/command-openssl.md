# SSL証明書したい（`openssl`）

```console
$ openssl version
OpenSSL 3.4.0 22 Oct 2024 (Library: OpenSSL 3.4.0 22 Oct 2024)
```

`openssl`コマンドで、暗号化やSSL/TLS、証明書操作、鍵作成など、
OpenSSLを使ったさまざまな操作ができます。

## CSRしたい（`openssl req`）

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

`openssl req`コマンドで証明書署名要求（CSR）ファイルを操作できます。
`-new`オプションで、秘密鍵（`.key`）と証明書署名要求（`.csr`）を新規に生成できます。
また、`-keyout`で生成する秘密鍵のファイル名を変更できます。ここでは`server.key`としました。
`-out`で生成するCSRのファイル名を変更できます。ここでは`server.csr`としました。

`-newkey rsa:ビット長`で鍵の長さを変更できます。
デフォルトは`rsa:2048`です。
暗号化アルゴリズムとビット長は、利用する認証局サービスが対応しているかも確認が必要です。

`-nodes`は`No DES`のことでパスワードなしで秘密鍵を生成します。
この秘密鍵はサーバー設定にも必要なファイルです。
サーバーの再起動を自動化するために、パスワードなしにしておきます。



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
// CSRを確認
$ openssl req -in 証明書署名要求.csr -noout -text
```

CSRが承認されると、証明書が発行されます。
おそらくサービスのメールなどで通知があると思います。
通知内容にしたがって`.crt`ファイルを取得します。
必要であれば、中間証明書も取得します。

これらのファイルを、サーバーの適切なパスにアップロードし、サーバーを設定します。
一般的には`/etc/ssl/certs/`に配置すればよいはずですが、
具体的なパスはサーバーの設定ファイル（`/etc/httpd.cnf`など）を確認してください。
正しいパスに証明書を配置したら、サーバーを再起動します。

## 自己署名証明書したい（`-x509`）

```console
// 自己署名証明書
$ openssl req -new -x509 -days 365 -nodes -keyout 秘密鍵.key -out 自己署名証明書.crt
```

`-x509`オプションで、CSRを生成せずにX.509形式の自己署名証明書を発行できます。
`-day`で有効期限を設定できます。デフォルトは30日（`-days 30`）です。

**自己署名証明書** は、正式な認証局を利用せず、自分自身で署名した証明書です。
いわゆる「オレオレ証明書」です。
おもに開発環境やテスト用で利用する証明書で、本番環境での利用は非推奨です。

:::{note}

**X.509証明書** は公開鍵基盤（PKI; Public Key Infrastructure）で使用される標準形式のデジタル証明書です。
サーバー証明書の拡張子は、Linux環境では`.crt`、Windows環境では`.cer`を利用します。

:::

## 証明書を表示したい（`openssl x509`）

```console
// 証明書を表示
$ openssl x509 -in 証明書.pem -noout -text

// 証明書の有効期限を確認
$ openssl x509 -in 証明書.pem -noout -dates
```

`openssl x509`コマンドでX.509形式の証明書を操作できます。
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

:::

## 秘密鍵したい（`genpkey`）

```console
// RSA鍵（古いコマンド）
$ openssl genrsa -out private.key 2048

// RSA鍵（新しいコマンド）
$ openssl genpkey -algorithm RSA -out private.key -pkeyopt rsa_keygen_bits::2048

// ED25519鍵
$ openssl genpkey -algorithm ED25519 -out private_ed25519.key
```

`openssl genpkey`で秘密鍵（private key）を生成できます。

:::{note}

RSA鍵のみを生成する`genrsa`コマンドがありますが、
こちらは古いコマンドだそうで、`genpkey`を使うことが推奨されているそうです。

:::

```console
$ openssl req -new -key private.key -out server.csr
```

事前に作成した秘密鍵を使って、CSRファイルを生成することもできます。
