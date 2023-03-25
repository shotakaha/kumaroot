# ウェブサーバーしたい（``httpd``）

```bash
$ docker run -d -p 8081:80 --name my-httpd httpd
$ docker exec -it my-httpd bash
(my-httpd) $ httpd -v
Server version: Apache/2.4.56 (Unix)
Server built:   Mar  7 2023 20:23:05
(my-httpd) $ pwd
/usr/local/apache2
```

ウェブサーバーとして一般的な``Apache``の設定方法を確認してます。
ここではDockerで起動したApacheサーバーのコンテナを使って、設定内容を調べています。
()[../docker/docker-httpd]

## サーバーを操作したい

```bash
$ httpd -k start
$ httpd -k stop
$ httpd -k graceful-stop
$ httpd -k restart
```

Apacheコンテナ内には``httpd``コマンドがありました。
サーバーを停止（``httpd -k stop``）したらコンテナも停止しました。

一般的なサーバの場合、``service``コマンドや``apachectl``コマンドで操作するような気がします。

## 設定ファイルを確認したい（``httpd.conf``）

```bash
$ find . -name *.conf | grep httpd
./conf/httpd.conf
./conf/extra/httpd-*.conf  # 省略
./conf/original/httpd.conf
./conf/original/extra/httpd-*.conf
```

設定ファイルは``httpd.conf``です。
上のコマンドでは、拡張子が``*.conf``で、``httpd``の文字列を含むパスを検索しています。
メインの設定ファイル（``./conf/httpd.conf``）とモジュール用の設定ファイル（``./conf/extra/httpd-*.conf``）が見つかりました。

また、``./conf/original/``以下のファイルは（たぶん）オリジナルの設定ファイルです。
設定ミスした場合などは、このファイルとの差分を調べたり、このファイルで上書きしてリセットすればよさそうです。

設定ファイルには各種の「ディレクティブ」がすでに書き込まれていて、サーバー設定の確認がができます。
また、このディレクティブを書き換えることで設定を変更できます。

## 設定ファイルのシンタックス確認（``nginx -t``）

```bash
$ httpd -t
```

設定ファイルのシンタックス（＝書き方）が正しいかチェックできます。
設定を書き換えた場合、サーバーを再起動する前には必ずチェックするとよいです。

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
