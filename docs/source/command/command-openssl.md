# SSL証明書したい（`openssl`）

```console
$ openssl version
OpenSSL 3.6.0 1 Oct 2025 (Library: OpenSSL 3.6.0 1 Oct 2025)

// 秘密鍵の作成
$ openssl genpkey -out private.key

// CSRの作成
$ openssl req -new -key private.key -out server.csr

// 証明書の作成
$ openssl x509 -in server.csr -signkey private.key -out server.crt
```

`openssl`は、暗号化や秘密鍵の作成、SSL/TLS証明書の操作など、OpenSSLを使ったさまざまな操作ができるコマンドです。

さまざまなサブコマンドがありますが、ここではSSL証明書の作成に必要なコマンドについて重点的に紹介します。

:::{seealso}

- [](./command-gpg.md)
- [](./command-ssh-keygen.md)

:::

## 秘密鍵を生成したい（`openssl genpkey`）

```console
// ed25519鍵
$ openssl genpkey -algorithm ed25519 -out private_ed25519.key

// RSA鍵
$ openssl genpkey -algorithm rsa -out private.key -pkeyopt rsa_keygen_bits:2048

// ECDSA鍵
$ openssl genpkey -algorithm ec -pkeyopt ec_paramgen_curve:P-256 -out private_ec.key

// 古いコマンド
$ openssl genrsa -out private.key 2048
```

`openssl genpkey`で秘密鍵を生成できます。
この秘密鍵を使って、CSRファイルやサーバー証明書を作成できます。

`-algorithm`で鍵アルゴリズムを指定できます。
`RSA | RSA-PSS | EC | X25519 | X448 | ED25519 | ED448`などから選択できます。
大文字／小文字の区別はありません。

`-pkeyopt`オプションで、鍵アルゴリズムのオプションを指定できます。
上記のサンプルでは、RSA鍵の長さを2048ビットに変更しています。

`-out`オプションで秘密鍵を保存するファイル名を変更できます。
デフォルトは標準出力に表示されます。

:::{note}

RSA鍵のみを生成する`genrsa`コマンドがあります。
こちらは古いコマンドで、`genpkey`を使うことが推奨されています。

:::

## 証明書署名要求を作成したい（`openssl req`）

```console
// CSRを新規作成
$ openssl req -new -key private.key -out server.csr -subj "/C=JP/ST=都道府県/L=市町村/O=組織/CN=www.example.com"

// CSRを確認
$ openssl req -in server.csr -text -noout
```

`openssl req -new`コマンドで、証明書署名要求（CSR）ファイルを作成できます。

**証明書署名要求**（CSR; Certificate Signing Request）は、公開鍵基盤（PKI）において証明書を発行してもらうために必要なデータを含んだファイルです。
ユーザー側で作成したCSRファイルを認証局に提出し、サーバー証明書を発行してもらいます。

:::{note}

CSRの提出方法は、利用する認証局の手順を確認してください。

大学や研究機関の場合、UPKI（University Public Key Infrastructure）が利用できるかもしれません。
UPKIは、国立情報学研究所（NII）が運営する
中間認証局を通じて、X.509証明書を発行してもらえるサービスです。

:::

`-key`に秘密鍵を指定します。
上記サンプルでは`private.key`を指定しています。

`-out`にCSRを保存するファイル名を変更できます。
デフォルトは標準出力です。
上記サンプルでは`server.csr`にしています。

`-subj`オプションは、CSRの設定項目です。
`-subj`を指定しない場合は対話的に入力できます。

作成したCSRは`openssl req -in server.csr`で展開して確認できます。
`Subject:...`などが設定した値になっていればOKです。
内容に間違いがなければ、認証局に提出します。

:::{note}

CSRはPEM形式で保存されたテキストファイルです。
`less`コマンドなどで開くことはできますが、内容はBase64でエンコードされているため、人間には判別できません。

:::

## サーバー証明書を確認したい（`openssl x509`）

```console
// 証明書を表示
$ openssl x509 -in server.crt -noout -text

// 証明書の有効期限を確認
$ openssl x509 -in server.crt -noout -dates
```

`openssl x509`コマンドでX.509形式の証明書を操作できます。
`-in`オプションでPEM形式の証明書ファイルを指定します。
`-noout`オプションで出力内容に証明書自身を非表示にできます。

**PEM形式**（Privacy Enhanced Mail）は、Base64でエンコードされたテキスト形式で、秘密鍵／公開鍵や証明書、証明書チェーンを保存する汎用的な形式です。

:::{note}

ファイルの内容は
`-----BEGIN`と
`-----END`で囲まれています。
同じPEM形式でも、用途によって次のような拡張子を使用します。

| 用途 | 秘密鍵 | 公開鍵 | ファイル名 |
| --- | --- | --- | --- |
| 汎用 | `.key` | `.pem` / `.pub` | |
| SSH公開鍵認証 | `.key` / なし | `.pub` | `id_ed25519` / `id_ed25519.pub` |
| SSL/TLS証明書 | `.key` | `.crt` / `.cer` | `server.key` / `server.crt` |
| 証明書チェーン | `.pem` | `.pem` | |

:::

提出したCSRが認証局によって承認されると、サーバー証明書が発行されます。

:::{note}

UPKI証明書サービスの場合、
サーバー証明書はメールで通知があります。
通知内容にしたがって証明書ファイル（`.crt`）を取得します。
必要であれば、中間証明書も取得します。

:::

内容に間違いがなければ、サーバー上の適切なパスにアップロードし、サーバーを設定します。

一般的には`/etc/ssl/certs/`に配置すればよいはずですが、
具体的なパスはサーバーの設定ファイル（`/etc/httpd.cnf`など）を確認してください。
正しいパスに証明書を配置したら、サーバーを再起動します。

## CSRを作成したい（`openssl req -new`）

```console
// CSRを新規作成
$ openssl req -new -noenc -newkey rsa:2048 -keyout server.key -out server.csr
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

// CSRと秘密鍵を確認
$ ls -l
server.csr
server.key

// CSRの中身をテキスト形式で確認
$ openssl req -in server.csr -noout -text
```

`openssl req`コマンドで証明書署名要求（CSR）ファイルを操作できます。

`-new`は、CSRを対話的に新規作成するオプションです。
DN情報を入力するプロンプトが表示されるので、必要な情報を適宜入力します。

:::{note}

DN情報（Distinguished Name）は、証明書の所有者を一意に識別するための情報です。

```text
/C=JP       # Country: 国コード（2文字）
/ST=Aichi   # State/Province: 都道府県名
/L=Nagoya city     # Locality: 市区町村名
/O=Nagoya University    # Organization: 組織名
/OU=[skip]    # Organization Unit: 部署名; スキップ
/CN=www.example.com    # Common Name: 証明書を設定するFQDN（ホスト名）
```

大学や研究機関の場合、CN以外は規定値があるかもしれません。
まず、関連部局の担当者に確認するとよいです。

:::

`-keyout`は、秘密鍵のファイル名を指定するオプションです。
拡張子は`.key`とするのが一般的です。
ここでは秘密鍵を`server.key`としました。
このファイルは、SSL証明書を設置するサーバーに配置します。

`-out`は、CSRのファイル名を指定するオプションです。
拡張子は`.csr`とするのが一般的です。
CSRを`server.csr`としました。
このファイルを認証局に提出します。

`-newkey rsa:ビット長`は、鍵長を変更するオプションです。
デフォルトは`rsa:2048`です。
鍵アルゴリズムと鍵長は、利用する認証局サービスが対応しているかも確認が必要です。
生成された秘密鍵は`-key`オプションで指定した鍵と同様に扱われ、CSRや証明書の作成に使用されます。

`-noenc`は、パスフレーズなしの秘密鍵を生成するオプションです。
パスフレーズありのほうが、セキュリティ的に安全なのですが、ウェブサーバーの再起動時にパスフレーズの手動入力が必要になります。
ここでは、ウェブサーバーの再起動を自動化するため、あえてパスフレーズなしにしています。

:::{caution}

秘密鍵は平文で保存されるため、アクセス権限の管理には注意してください。

:::

## 自己署名証明書したい（`openssl req -x509`）

```console
// 自己署名証明書
$ openssl req -new -x509 -days 365 -noenc -keyout 秘密鍵.key -out 自己署名証明書.crt

// 手順を分解
$ openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out server.key
$ openssl req -new -key server.key -out server.csr
$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
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


## SSLとTLS

暗号化通信のプロトコルにはSSL（Secure Sockets Layer）が利用されていましたが、
セキュリティの問題が多くあったため、現在ではTLS（Transport Layer Security）に置き換わっています。
歴史的経緯から、いまだにSSL証明書と言われますが、利用しているのはTLSプロトコルだそうです。

| 年 | バージョン | RFC | 説明 |
|---|---|---|---|
| 1994 | SSL 1.0 | - | Netscapeが開発したが、セキュリティの問題があり公開されなかった |
| 1995 | SSL 2.0 | - | 広く利用されたバージョン |
| 1996 | SSL 3.0 | - | セキュリティが大幅に改善。TLSの基礎となる技術 |
| 1999 | TLS 1.0 | RFC2246 | SSL 3.0をベースにIETFが標準化 |
| 2006 | TLS 1.1 | RFC4346 | |
| 2009 | TLS 1.2 | RFC5246 | SHA-256をサポート |
| 2011 | SSL 2.0 非推奨化 | RFC6176 | |
| 2014 | SSL 3.0 非推奨化 | RFC7568 | |
| 2018 | TLS 1.3 | RFC8446 | 不要な暗号化方法を削除 |
| 2020 | TLS 1.0/1.1 非推奨化 | | 主要ブラウザがサポートを終了 |

## 暗号化アルゴリズムの変遷

`openssl`コマンドには、`aes-*`、`aria-*`、などの暗号化オプションがいろいろあります。
いくつかについて調べてみたところ、現在ではAESが暗号化の標準となっているみたいです。

| 年 | アルゴリズム名 | ブロックサイズ | 構造 | 説明 |
|---|---|---|---|---|
| 1975 | DES（Data Encryption Standard） | 64bit | フェイステル構造 | IBMとNSAが共同で開発した暗号化アルゴリズム |
| 1991 | IDEA（International Data Encryption Algorithm） | 128bit | MA構造 | DESの代替として開発された |
| 2001 | AES（Advanced Encryption Standard） | 128bit | SPN構造 | 現在も安全性が高く、広く利用されている |
| 2000 | Camellia | 128bit | フェイステル構造 | 三菱電機とNTTが開発。日本で採用例が多い |
| 2004 | ARIA | 128bit | SPN構造 | 韓国情報保安庁が開発。韓国政府が採用 |
