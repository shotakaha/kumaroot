# apt

```bash
$ apt
```

Debian系のLinuxでパッケージ管理を行うためのコマンドラインツールです。
昔は``apt-get``と``apt-cache``使っていた記憶がありますが、いまは``apt``を使うみたいです。

## パッケージを検索したい（``apt search``）

```bash
# apt-cache search パッケージ名
$ apt search パッケージ名
$ apt search ripgrep
```

## パッケージをインストールしたい（``apt install``）

```bash
# apt-get install パッケージ名
$ apt install パッケージ名
$ apt install ripgrep
```

## パッケージリストを更新したい（``apt update``）

```bash
# apt-get update
$ apt update

```
