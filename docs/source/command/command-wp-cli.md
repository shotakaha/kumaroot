# WordPress CLIしたい（`wp-cli`）

```console
$ wp core version
```

`wp-cli`はWordPressを操作するCLIツールです。

## インストールしたい

```console
$ brew install wp-cli
$ wp --version
WP-CLI 2.12.0
```

Homebrewで`wp-cli`をインストールできます。
コマンド名は`wp`です。

:::{note}

`wp --ssh SSH先`オプションで、
ローカルの`wp`で、SSH先のWordPressを操作できるようです。
その際は、SSH先にも`wp-cli`（コマンド名`wp`）がインストールされている必要があります。

:::

## サーバーにインストールしたい

`wp-cli`はWordPressが動いているサーバーで利用します。
そして、それはリモートサーバーであることが多いはずです。
以下はリモートサーバーにインストールするコマンド作業の手順です。

```console
// DL用フォルダにダウンロードして動作を確認
$ cd ~/Downloads
$ curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
$ php wp-cli.phar --info

// ユーザー実行パスに移動
$ chmod +x wp-cli.phar
$ mv wp-cli.phar ~/.local/bin/wp
$ wp --info
```

CLIツールは`wp-cli.phar`というPHP Archive形式の単独バイナリで公開されています。
そのため管理者権限がないサーバーにも簡単にインストールできます。

```console
$ wp cli update
$ wp cli update --nightly
```

一度インストールしたあとは`wp cli update`で`wp-cli`本体を更新できます。

## 本体したい（`wp core`）

```console
$ wp core download
$ wp core install
$ wp core update
```

`wp core`でWordPress本体をインストール・更新できます。

## 設定したい（`wp config`）

```console
$ wp config path    # wp-config.phpのパスを確認
$ wp config list    # wp-config.phpの項目を確認
```

`wp config`でWordPressの設定ファイル（`wp-config.php`）を操作できます。
設定内容を確認したり、更新したりできます。

```console
$ wp options get siteurl
$ wp options get blogname
```

`wp options`で設定データベース（`wp_options`）を操作できます

## データベースしたい（`wp db`）

```console
$ wp db size    # サイズを確認
$ wp db tables  # テーブルを確認
$ wp db export  # エクスポート
$ wp db import  # インポート
$ wp db query < QUERY.sql  # SQLクエリを実行
```

`wp db`でWordPressのデータベースを操作できます。

## プラグインしたい（`wp plugin`）

```console
$ wp plugin list    # プラグインを確認
$ wp plugin path
$ wp plugin status
```

`wp plugin`でプラグインを操作できます。

## テーマしたい（`wp theme`）

```console
$ wp theme list
$ wp theme path
$ wp theme status
```

`wp theme`でテーマを操作できます。

## メンテナンスしたい（`wp maintenance-mode`）

```console
$ wp maintenance-mode status
$ wp maintenance-mode activate
$ wp maintenance-mode deactivate
```

`wp maintenance-mode`でメンテナンスモードを操作できます。

## キャッシュしたい（`wp cache`）

```console
$ wp cache path
$ wp cache flush
```

`wp cache`でキャッシュを操作できます。

## 文字列置換したい（`wp search-replace`）

```console
$ wp search-replace <old> <new>
$ wp search-replace 'http://example.com' 'https://example.com'
```

`wp search-replace`でデータベース内の文字列を置換できます。
`--dry-run`オプションがあったり、
置換対象のテーブル名を指定できたりします。
