# ウェブサーバーしたい（``httpd``）

ウェブサーバーとして一般的な``Apache``の設定方法を確認してみます。
ここではDockerを使って起動したApacheサーバーのコンテナを使っています。
()[../docker/docker-httpd]

## 設定ファイルを確認したい（``httpd.conf``）

```bash
$ find . -name *.conf | grep httpd
./conf/httpd.conf
./conf/extra/httpd-*.conf  # 省略
./conf/original/httpd.conf
./conf/original/extra/httpd-*.conf
```

設定ファイルの拡張子は``*.conf``で、``httpd``の文字列を含むパスを検索しています。
``./conf/httpd.conf``がメインの設定ファイルです。
``./conf/extra/``に入っているファイルは``httpd.conf``で読み込んだモジュールの設定ファイルです。

``./conf/original/``は、（たぶん）デフォルトの設定ファイルです。
設定ミスした場合などは、このファイルとの差分を調べたり、このファイルで上書きしてリセットすればよさそうです。

## 公開用ディレクトリを確認したい（``DocumentRoot``）

```apache
# DocumentRoot 絶対パス
DocumentRoot /usr/local/apache2/htdocs
```

外部に公開するコンテンツをディレクトリは``DocumentRoot``で設定します。
ドキュメントルートは絶対パスで指定します。

## ポート番号を確認したい（``Listen``）

```apache
# Listen ポート番号
Listen 80
Listen 443
```

外部からアクセスするときのポート番号は``Listen``で設定できます。
``Listen ポート番号``を追加することで複数のポートを設定できます。
HTTPは80番、HTTPSは443番がデフォルトのポート番号です。

## ディレクトリのアクセス権を確認したい（``Directory`` / ``File``）

```apache
# <Directory パス>...</Directory>
# <File パス>...</Directory>

# 全体（/）のアクセス権の設定
# システム全体は外部からアクセスできないように設定
<Directory />
    AllowOverride none
    Require all denied
</Directory>

# コンテンツ領域（/usr/local/apache2/htdocs/）のアクセス権の設定
# コンテンツ領域（とその下）は外部からアクセスできるように設定
<Directory "/usr/local/apache2/htdocs">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>

# .htではじまるファイルのアクセス権の設定
# ワイルドカード（*）を使ってパスを指定できる
# .htaccessや.htpasswordは外部からアクセスできないように設定
<File ".ht*">
    Require all denied
</File>
```

外部からのアクセス権限は``Directory``や``File``で設定できます。
ファイルシステム全体や``.htaccess``のようなファイルは外部からのアクセスNGにしつつ、
公開用コンテンツ（＝ドキュメントルート以下）は外部アクセスOKにできます。

## ログフォーマットを確認したい（``LogFormat`` / ``CustomLog``）

```apache
<IfModule log_config_module>
    # LogFormat "フォーマット文字列" ログ形式の名前
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common

    # CustomLog "保存先" ログ形式の名前
    CustomLog "logs/access_log" combined
</IfModule>
```

ログ形式は``LogFormat``で設定できます。
``httpd.conf``には``common``形式と``combined``形式はプリセットとして定義されていました。
アクセスログの保存先とフォーマットは``CustomLog``で設定できます。
保存先を相対パスで指定した場合、``ServerRoot``からの相対パスになります。

## HTTPS使いたい

```apache
LoadModule ssl_module modules/mod_ssl.so
Include conf/extra/httpd-ssl.conf

<IfModule ssl_module>
    # SSL証明書の設定
</IfModule>
```

HTTPSを使いたい場合は、``mod_ssl``モジュールを有効にします。

## ユーザーごとのディレクトリを使いたい

```apache
LoadModule userdir_module modules/mod_userdir.so
Include conf/extra/httpd-userdir.conf
```

ユーザーごとのディレクトリを使いたい場合は、``mod_userdir``モジュールを有効にします。
``LoadModule``でモジュールを有効にし、``Include``で設定ファイルを読み込みます。

ユーザーごとの公開コンテンツ領域は``UserDir``で設定できます。
デフォルトは``public_html``になっているので、``~/public_html/``以下に配置したコンテンツを公開できます。

## パスワードをかけたい

特定のディレクトリに``.htaccess``を配置し、パスワードを使ったアクセス制限を設定できます。
パスワード認証には``BASIC認証``と``Digest認証``の2種類があります。
調べてみると、現在はHTTPS通信ができる場合はBASIC認証でOK、できない場合はDigest認証にするとよいみたいです。


## リファレンス

- [Apache2.4 ドキュメント](https://httpd.apache.org/docs/2.4/)
- [Apache2.4 ディレクティブクイックリファレンス](https://httpd.apache.org/docs/2.4/ja/mod/quickreference.html)
- [Apache2.4 モジュール一覧](https://httpd.apache.org/docs/2.4/ja/mod/)
