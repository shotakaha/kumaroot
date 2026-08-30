# アクセス制御したい（`.htaccess`）

```apache
# このディレクトリ全体を、指定したIPアドレスからだけ見られるようにする
Require ip 192.168.0.0/16
Require ip 203.0.113.10
```

`.htaccess`は、Apacheのウェブサーバーで「そのディレクトリだけ」に効く設定ファイルです。
ファイルを置いたディレクトリと、その下のすべてに設定が適用されます。

アクセス制限、Basic認証、リダイレクトなどを設定できます。
`httpd.conf`のようなサーバー本体の設定ファイルを触れない環境（研究室サーバーの個人スペースなど）で役立ちます。

:::{seealso}

- [](./webdev-httpd.md)

:::

## `.htaccess`を有効にしたい（`AllowOverride`）

```console
# httpd.conf の場所を探す
$ find / -name httpd.conf 2>/dev/null
```

```apache
# httpd.conf 側の設定
<Directory "/var/www/html">
    AllowOverride All
    Require all granted
</Directory>
```

`.htaccess`が効くのは、サーバー本体の`httpd.conf`でそのディレクトリに`AllowOverride`が許可されている場合だけです。

`AllowOverride All`ですべての上書きを許可、`AllowOverride None`で無効になります。
`.htaccess`を置いたのに設定が反映されないときは、まずここを確認します。

## IPアドレスで許可・拒否したい（`Require ip`）

```apache
# 許可する
Require ip 203.0.113.10
Require ip 192.168.0.0/16

# 拒否する
Require not ip 198.51.100.20
```

`Require ip`で、アクセスを許可するIPアドレスを指定します。
複数行書くと、そのどれかに一致すれば許可されます。

`Require not ip`で、特定のIPアドレスだけを拒否できます。

```apache
Require all granted    # 全員に許可
Require all denied     # 全員を拒否
```

`Require all granted` / `Require all denied`で、一括で許可・拒否できます。

:::{note}

`Require`はApache 2.4で導入されたディレクティブです。
2.2で使われていた`Order` / `Allow` / `Deny`は非推奨で、書き方も分かりにくいため、
2.4以降では`Require`を使います。

:::

## IPアドレスの範囲を指定したい（CIDR）

```apache
Require ip 192.168.0.0/16    # 192.168.0.0 〜 192.168.255.255
Require ip 192.168.1.0/24    # 192.168.1.0 〜 192.168.1.255
Require ip 10.0.0.0/8        # 10.0.0.0   〜 10.255.255.255
```

IPアドレスの後に`/数字`を付けると、範囲を指定できます（CIDR表記）。

`/数字`は「アドレスの先頭から何ビットを固定するか」で、
数字が小さいほど広い範囲、大きいほど狭い範囲になります。

範囲を書くときは、`192.168.1.5/24`のような途中のアドレスではなく、
`192.168.1.0/24`のようにその範囲の先頭アドレスで書きます。

## 特定のファイルだけ制限したい（`<Files>`）

```apache
# wp-login.php へのアクセスを、指定IPからだけに限定する
<Files "wp-login.php">
    Require ip 203.0.113.10
</Files>
```

`<Files>`で囲むと、その中の`Require`は指定したファイルだけに効きます。

WordPressのログイン画面や管理ファイルなど、
ディレクトリ全体ではなく特定のファイルを守りたいときに使います。

## Basic認証でパスワードをかけたい（`AuthType Basic`）

```apache
AuthType Basic
AuthName "Restricted Area"          # 認証ダイアログに表示される文言
AuthUserFile /var/www/etc/.htpasswd  # パスワードファイルの絶対パス
Require valid-user
```

`AuthType Basic`で、アクセス時にIDとパスワードを要求できます。
`Require valid-user`は「パスワードファイルに登録された誰か」を意味します。

パスワードファイルは`htpasswd`コマンドで作ります。

```console
# 新規作成（-c は初回のみ）
$ htpasswd -c /var/www/etc/.htpasswd alice

# 2人目以降は -c を付けない
$ htpasswd /var/www/etc/.htpasswd bob
```

パスワードはハッシュ化して保存されます。
パスワードファイルは、ウェブで公開されるディレクトリの外に置きます。

:::{note}

Basic認証はIDとパスワードをそのまま送るため、HTTP（暗号化なし）では盗聴されます。
HTTPSが有効なサイトであれば、通信が暗号化されるのでBasic認証で問題ありません。

:::

## 社内は素通し、社外はパスワードにしたい（`<RequireAny>`）

```apache
AuthType Basic
AuthName "Restricted Area"
AuthUserFile /var/www/etc/.htpasswd

<RequireAny>
    Require ip 192.168.0.0/16
    Require valid-user
</RequireAny>
```

`<RequireAny>`で囲むと、中の条件の**どれか1つ**を満たせばアクセスできます。

上のサンプルは「社内IPからならそのまま、それ以外はBasic認証」という設定です。
逆に、すべての条件を満たす必要がある場合は`<RequireAll>`を使います。

## リダイレクトしたい（`Redirect`）

```apache
# 301: 恒久的に移動した
Redirect 301 /old-page.html /new-page.html

# 302: 一時的な移動
Redirect 302 /campaign /
```

`Redirect`で、あるURLへのアクセスを別のURLに転送します。
`301`は「完全に移転した」、`302`は「一時的」で、検索エンジンの扱いが変わります。

## HTTPをHTTPSに転送したい（`RewriteRule`）

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>
```

HTTPでアクセスされたら、同じURLのHTTPSへ301リダイレクトする設定です。

`RewriteCond %{HTTPS} off`で「HTTPSでないとき」を条件にし、
`RewriteRule`で転送先を組み立てます。
`mod_rewrite`モジュールが有効である必要があります。

## リファレンス

- [.htaccess ファイル](https://httpd.apache.org/docs/2.4/ja/howto/htaccess.html)
- [アクセス制御](https://httpd.apache.org/docs/2.4/ja/howto/access.html)
- [認証・承認・アクセス制御](https://httpd.apache.org/docs/2.4/ja/howto/auth.html)
- [Require](https://httpd.apache.org/docs/2.4/ja/mod/mod_authz_core.html#require)
- [AllowOverride](https://httpd.apache.org/docs/2.4/ja/mod/core.html#allowoverride)
- [mod_rewrite](https://httpd.apache.org/docs/2.4/ja/mod/mod_rewrite.html)
