# アクセス制御したい（`.htaccess`）

```apache
# 特定のIPからのアクセスを拒否
Order Allow,Deny
Deny from 192.168.1.1
Allow from all

# WordPress管理画面へのアクセスを限定
<Files wp-login.php>
  Order Deny,Allow
  Deny from all
  Allow from 許可IPアドレス
</Files>

# .htaccessファイルへのアクセス禁止
# 外部（＝ブラウザ経由）のアクセスを禁止
# 内部（=ssh経由）のアクセスは可能
<Files .htaccess>
  Order Allow,Deny
  Deny from all
</Files>

# Basic認証
AuthType Basic
AuthName "Restricted Area"
AuthUserFile /path/to/.htpasswd   # .htpasswdのパス
Require valid-user

# リダイレクトの設定
Redirect 301 古いURL 新しいURL
```

`.htaccess`を使って、ウェブサイトに対するアクセスやレスポンスを制御できます。
ファイル／ディレクトリに対するアクセス制限やリダイレクト、パスワード認証などを設定できます。

ディレクトリごとに設置できるため、研究室サーバーの個人スペースなどでにも設置できます。
`httpd.conf`などのサーバー設定ファイルの編集権限がないケースで活躍します。

## アクセス制御を有効にしたい（`AllowOverride`）

```console
// httpd.confのパスを確認
$ find . -name httpd.conf
```

```apache
<Directory "該当のパス">
  AllowOverride All
  Require all granted
</Directory>
```

`.htaccess`を使ってアクセス制御したい場合、
該当ディレクトリに対して`AllowOverride`ディレクティブが有効になっている必要があります。

## アクセス制御したい（`Required`）

```apache
# 一括許可／一括拒否
Require all granted    # Allow from all に相当
Require all denied     # Deny from all に相当

# IPアドレス／ドメインを指定して許可
Require ip 許可IPアドレス    # Allow from 許可IPアドレスに相当
Require host 許可ドメイン名  # Allow from 許可IPドメイン名に相当

# IPアドレス／ドメインを指定して拒否
Require not ip 拒否IPアドレス    # Deny from 拒否IPアドレスに相当
Require not host 拒否ドメイン名  # Deny from 拒否IPアドレスに相当
```

`Require`ディレクティブを使って、アクセス制限を設定しています。

:::{note}

`Require`ディレクティブはApache2.4で追加（改善？）されたディレクティブです。
Apache 2.4からは`Require`ディレクティブを使うことが推奨されています。
Apache 2.2までは`Order`、`Allow`、`Deny`ディレクティブが使われていましたが、
将来的に廃止される予定だそうです。

:::

```apache
Require ip 許可IPアドレス/サブネットマスク
Require ip 192.168.1.1/8    # => 192.  0.0.0 - 192.255.255.255
Require ip 192.168.1.1/16   # => 192.168.0.0 - 192.168.255.255
Require ip 192.168.1.1/24   # => 192.168.1.0 - 192.168.  1.255
```

IPアドレスはサブネットマスクを使って範囲指定できます。

:::{note}

サブネットマスクは、
IPアドレス（IPv4）を**ネットワーク部**と**ホスト部**に分けることで、
巨大なIPアドレス空間を分割・管理するための仕組みです。

サブネットマスクが
`255.255.0.0`（`/16`）の場合は、65534個のホスト、
`255.255.255.0`（`/24`）の場合は、254個のホスト、
がそのネットワーク内で利用できることを表しています。

:::

## 複数条件したい（`RequireAny`）

```apache
<Files "wp-login.php">
  <RequireAny>
    Require all denied
    Require ip 許可IPアドレス1/サブネットマスク
    Require ip 許可IPアドレス2/サブネットマスク
  </RequireAny>
</Files>
```

`RequiredAny`ディレクティブで、複数の条件を設定できます。
上記のサンプルは、WordPressの管理画面へのアクセスを制御しています。
`Files`ディレクティブを使って`wp-login.php`を指定し、
指定したIPアドレスからのアクセスを許可しています。

## パスワード保護したい（Basic認証）

```apache
AuthType Basic
AuthName "Restricted Area"
AuthUserFile /path/to/htpasswd
Require valid-user
```

特定のディレクトリに設置して、パスワード保護できます。
HTTPSが有効なウェブサイトであれば、Basic認証でよいそうです。

```console
// .htpasswdが存在しない場合
$ htpasswd -c /var/www/etc/.htpasswd ユーザー名
// パスワードを入力
// パスワードを入力（確認）

// .htpasswdに追記する場合
$ htpasswd /var/www/etc/.htpasswd ユーザー名
```

サーバー内で`htpasswd`コマンドを使って`.htpasswd`ファイルを作成します。
パスワードファイルは、ウェブで公開されるディレクトリの外に作成し、
`AuthUserFile`で指定したパスに配置します。
パスワードはハッシュ化されて、このファイルに保存されます。

:::{note}

パスワード保護の手法として`Basic認証`と`Digest認証`という方式があります。
HTTPSが有効なサイトでは、通信が暗号化されているので`Basic認証`でOKです。

:::

## リダイレクトしたい（`Redirect`）

```apache
# 301: 恒久的リダイレクト
Redirect 301 古いURL 新しいURL

# 302: 一時的リダイレクト
Redirect 302 古いURL 新しいURL
```

`Redirect`ディレクティブを使ってURLのリダイレクトを設定できます。

## HTTPSリダイレクトしたい（`RewriteRule`）

```apache
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>
```

`RewriteRule`ディレクティブを使って、HTTPSリダイレクトを設定できます。
`RewriteEngine`、`RewriteCond`ディレクティブを合わせて使います。
また、リダイレクトには`mod_rewrite`モジュールが有効になっている必要があります。

## リファレンス

- [Access Control - httpd.apache.org](https://httpd.apache.org/docs/2.4/howto/access.html)
- [認証・承認・アクセス制御 - httpd.apache.org](https://httpd.apache.org/docs/2.4/howto/auth.html)
- [Apacheチュートリアル: .htaccess](https://httpd.apache.org/docs/2.4/ja/howto/htaccess.html)
- [Require](https://httpd.apache.org/docs/2.4/ja/mod/mod_authz_core.html#require)
- [RequireAll](https://httpd.apache.org/docs/2.4/ja/mod/mod_authz_core.html#requireall)
- [AllowOverride](https://httpd.apache.org/docs/2.4/ja/mod/core.html#allowoverride)
