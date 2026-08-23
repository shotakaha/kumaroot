# チェックサムしたい（`shasum` / `sha256sum`）

```console
// チェックサムを計算する
$ shasum ファイル名
$ shasum -a 256 ファイル名

// チェックサムを検証する
$ shasum -c チェックサムファイル名
$ shasum -a 256 -c チェックサムファイル名
```

`shasum`は、ファイルのチェックサムを計算するコマンドです。
`-a 256`オプションでSHA256のチェックサムを計算できます。

`-c`オプションで、チェックサムファイルに記録された値と照合して検証できます。

:::{note}

macOS標準のコマンド名は`shasum`です。
Linuxでは`sha256sum`という名前のコマンドが同等の機能を持っています。

:::

## チェックサムを計算したい（`shasum --algorithm`）

```console
$ shasum --algorithm=256 ファイル名
$ shasum -a 256 ファイル名
```

`--algorithm`（`-a`）で、計算するチェックサムのアルゴリズムを指定できます。
SHA256のチェックサムを計算する場合は、`--algorithm=256`（`-a 256`）を指定します。

## チェックサムを検証したい（`shasum --check`）

```console
$ shasum --check チェックサムファイル名
$ shasum -c チェックサムファイル名
```

`--check`（`-c`）で、チェックサムファイルに記録された値と照合して検証できます。
ダウンロードしたファイルとそのチェックサムは同じディレクトリに配置してください。

## GitHub Releaseを使いたい

```console
$ mkdir -p ~/Downloads/tmp/
$ cd ~/Downloads/tmp/

$ curl -LO https://github.com/ユーザー名/リポジトリ名/releases/download/v1.0.0/ファイル名
$ curl -LO https://github.com/ユーザー名/リポジトリ名/releases/download/v1.0.0/ファイル名.sha256

$ shasum -a 256 -c ファイル名.sha256
```

GitHub Releaseで配布されているアセットを使う場合のサンプルです。
GitHub Releaseで公開されているアセットは、チェックサムファイルも同時に公開されていることが多いです。
