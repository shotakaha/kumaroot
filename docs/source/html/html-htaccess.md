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

## ブラックリストしたい

```apache
# 特定のIPからのアクセスを拒否
Order Allow,Deny
Deny from 拒否IPアドレス もしくは 拒否ドメイン名
Allow from all

# Apache 2.4以降
<RequireAll>
  Require not ip 拒否IPアドレス
</RequireAll>
```

この設定で`Deny from`で指定したIPアドレスからのアクセスだけを拒否できます。
アクセス源にドメイン名も指定できます。

## ホワイトリストしたい

```apache
# 特定のIPからのアクセスを許可
Order Deny,Allow
Deny from all
Allow from 許可IPアドレス もしくは 許可ドメイン名

# Apache 2.4以降
<RequireAll>
  Require ip 許可IPアドレス（192.168.1.1）
  Require host 許可ドメイン名（example.com）
</RequireAll>

```

この設定で`Allow from`で指定したIPアドレスからのアクセスだけを許可できます。
アクセス源にドメイン名も指定できます。

```apache
# サブネットマスクを指定
Order Deny,Allow
Deny from all
Allow from 許可IPアドレス1
Allow from 許可IPアドレス2/サブネットマスク
```

`IPアドレス/16`のようにサブネットマスクを使って範囲を指定できます。

:::{note}

サブネットマスクは、IPアドレス（IPv4）を**ネットワーク部**と**ホスト部**に分けることで、
巨大なIPアドレス空間を分割・管理するための仕組みです。

サブネットマスクが
`255.255.0.0`（`/16`）の場合は、65534個のホスト、
`255.255.255.0`（`/24`）の場合は、254個のホスト、
がそのネットワーク内で利用できることを表しています。

:::

## 複数アドレスしたい

```apache
# コマンド
<Files "ファイル名">
  Order Deny,Allow
  Deny from 拒否IPアドレス
  Allow from 許可IPアドレス1
  Allow from 許可IPアドレス2/サブネットマスク
</Files>

# Apache 2.4以降
<Files ファイル名>
  <RequireAll>
    Require not ip 拒否IPアドレス
    Require ip 許可IPアドレス1
    Require ip 許可IPアドレス2/サブネットマスク
  </RequireAll>
</Files>
```

`Files`ディレクティブを使って、特定のファイルへのアクセスを制限できます。
ファイル名は正規表現を使って指定できます。

## パスワード保護したい（Basic認証）

```apache
AuthType Basic
AuthName "Restricted Area"
AuthUserFile /path/to/.htpasswd
Require valid-user
```

特定のディレクトリに設置して、パスワード保護できます。
HTTPSが有効なウェブサイトであれば、Basic認証でよいそうです。

```console
// .htpasswdが存在しない場合
$ htpasswd -c /path/to/.htpasswd ユーザー名

// .htpasswdに追記する場合
$ htpasswd /path/to/.htpasswd ユーザー名
```

サーバー内で`htpasswd`コマンドを使って`.htpasswd`ファイルを作成します。
パスワードファイルは、`AuthUserFile`で指定したパスに配置します。
パスワードはハッシュ化されて、このファイルに保存されます。

:::{note}

パスワード保護の手法として`Basic認証`と`Digest認証`という方式があります。
HTTPSが有効なサイトでは、通信が暗号化されているので`Basic認証`でOKです。

:::

## リダイレクトしたい

```htaccess
# 301: 恒久的リダイレクト
Redirect 301 古いURL 新しいURL

# 302: 一時的リダイレクト
Redirect 302 古いURL 新しいURL
```
