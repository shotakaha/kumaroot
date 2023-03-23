# ウェブサーバーしたい（``httpd``）

## 設定ファイルを確認したい（``httpd.conf``）

```bash
$ find . -name "httpd.conf"
```

## ドキュメントルートを確認したい（``DocumentRoot``）

```apache
DocumentRoot /usr/local/apache2/htdocs
```

公開するコンテンツを配置するディレクトリは``DocumentRoot``ディレクティブで設定します。

## ポート番号を確認したい（``Listen``）

```apache
# Listen ポート番号
Listen 80
Listen 443
```

外部からアクセスするときのポート番号は``Listen``ディレクティブで設定できます。
``Listen ポート番号``を追加することで複数のポートを設定できます。
HTTPは80番、HTTPSは443番がデフォルトのポート番号です。

## ディレクトリのアクセス権を確認したい（``Directory`` / ``File``）

```apache
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
# .htaccessや.htpasswordは外部からアクセスできないように設定
<File ".ht*">
    Require all denied
</File>
```

外部からのアクセス権限は``Directory``ディレクティブと``File``ディレクティブで制御できます。
ファイルシステム全体や``.htaccess``のようなファイルは外部からアクセスNGにしつつ、
公開コンテンツ領域（ドキュメントルート以下）は外部アクセスOKにできます。

## ログフォーマットを確認したい（``LogFormat`` / ``CustomLog``）

```apache
<IfModule log_config_module>
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common
    CustomLog "logs/access_log" combined
</IfModule>
```

ログ形式は``LogFormat``ディレクティブで設定できます。
アクセスログの保存先とフォーマットは``CustomLog``ディレクティブで設定できます。



## SSLを有効化したい

## ユーザーごとのディレクトリを有効にしたい
