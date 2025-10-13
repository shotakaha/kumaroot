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
