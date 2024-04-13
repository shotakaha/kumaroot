# パッケージ管理したい（``apt``）

```console
$ apt
```

Debian系のLinuxでパッケージ管理を行うためのコマンドラインツールです。
昔は``apt-get``と``apt-cache``使っていた記憶がありますが、いまは``apt``を使うみたいです。

## パッケージを検索したい（``apt search``）

```console
# apt-cache search パッケージ名
$ apt search パッケージ名
$ apt search ripgrep
```

## パッケージをインストールしたい（``apt install``）

```console
# apt-get install パッケージ名
$ apt install パッケージ名
$ apt install ripgrep
```

## パッケージリストを更新したい（``apt update``）

```console
# apt-get update
$ apt update
```

## オススメのパッケージ

```console
$ apt install build-essential
$ apt install gdb
$ apt install vim
$ apt install git
$ apt install openssh-client
$ apt install libssl-dev libpq-dev
$ apt install docker.io
$ apt install python3
$ apt install python3-pip
$ apt install nodejs
$ apt install ruby
$ apt install ripgrep
```

## リファレンス

- [apt - manpages.ubuntu.com](https://manpages.ubuntu.com/manpages/noble/en/man8/apt.8.html)
- [apt-get - manages.ubuntu.com](https://manpages.ubuntu.com/manpages/noble/en/man8/apt-get.8.html)
