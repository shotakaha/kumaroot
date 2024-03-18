# コマンドの使い方

コマンドとは、ターミナルと呼ばれる黒い画面に入力する**アレ**です。
プログラミングする上で避けては通れない道ですが、慣れてしまえばマウス操作より楽だったりします。
また、シェルスクリプトのようなスクリプトと組み合わせることで、簡単に時短することもできます。

すべてのコマンドに共通する基本概念は``do it simple, do it well``です。
基本的に、ひとつのコマンドはひとつのことしかできませんが、
パイプやリダイレクトと組み合わせて、いろいろなタスクをこなすことができます。

このドキュメントでは``macOS``を前提として、``Homebrew``でインストールできるコマンドを中心に紹介します。
[Homebrew 公式ページ（日本語）](https://brew.sh/ja)にあるスクリプトをコピペして、ターミナルに貼り付け、
[brew](./command-brew.md)コマンドを使えるようにしましょう。

## 日常したい

```{toctree}
---
maxdepth: 1
---
command-cd
command-date
command-ls
command-lsd
command-open
command-pbcopy
command-pwgen
command-pwd
command-tldr
```

## 環境構築したい

```{toctree}
---
maxdepth: 1
---
command-apt
command-asdf
command-brew
command-docker
command-gem
command-mise
command-npm
command-spack
command-tlmgr
command-ghq
```

## シェルしたい

```{toctree}
---
maxdepth: 1
---
command-awk
command-chmod
command-bash
command-echo
command-fish
command-nkf
command-ps
command-stdout
command-tee
command-which
```

## ネットワークしたい

```{toctree}
---
maxdepth: 1
---
command-arp
command-curl
command-dig
command-ping
command-rsync
command-ssh
command-ssh-keygen
command-tcpdump
command-wget
command-xargs
```

## 未分類

```{toctree}
---
maxdepth: 1
---
command-1password
command-exa
command-fd
command-find
command-grep
command-gzip
command-launchctl
command-mkcert
command-myst
command-pandoc
command-sd
command-sed
command-tar
command-texdoc
command-tig
command-uname
```
