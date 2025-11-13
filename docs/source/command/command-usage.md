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
command-pwd
command-ls
command-lsd
command-open
command-mdfind
command-date
command-df
command-du
command-mktemp
command-pbcopy
command-pwgen
command-screen
command-crontab
```

## ファイル検索・テキスト処理したい

```{toctree}
---
maxdepth: 1
---
command-bat
command-find
command-fd
command-grep
command-ripgrep
command-sed
command-sd
command-awk
command-jq
command-nkf
command-tldr
command-zoxide
```

## エディターしたい

```{toctree}
---
maxdepth: 1
---
command-code
command-emacs
command-helix
command-vim
command-zed
command-myst
command-clang-format
```

## エージェントしたい

```{toctree}
---
maxdepth: 1
---
command-claude
command-specify
command-opencode
command-ollama
command-lmstudio
```

## 環境構築したい

```{toctree}
---
maxdepth: 1
---
command-apt
command-asdf
command-brew
command-cmake
command-docker
command-gem
command-mise
command-npm
command-spack
command-task
command-tlmgr
command-ghq
command-poetry
command-rye
command-softwareupdate
command-xcode
command-arduino-cli
```

## シェルしたい

```{toctree}
---
maxdepth: 1
---
command-bash
command-fish
command-chmod
command-ps
command-which
command-echo
command-stdout
command-tee
command-xargs
```

## ネットワークしたい

```{toctree}
---
maxdepth: 1
---
command-arp
command-curl
command-dig
command-goaccess
command-gping
command-gpg
command-httpie
command-openssl
command-ping
command-rsync
command-ssh
command-ssh-keygen
command-tcpdump
command-wget
command-xh
```

## Git・バージョン管理したい

```{toctree}
---
maxdepth: 1
---
command-tig
command-glab
command-gitlab
```

## 圧縮・アーカイブしたい

```{toctree}
---
maxdepth: 1
---
command-tar
command-gzip
```

## システム管理・その他したい

```{toctree}
---
maxdepth: 1
---
command-uname
command-launchctl
command-systemctl
command-mysql
command-zellij
command-1password
command-mkcert
command-pandoc
command-texdoc
command-fc-list
command-expect
command-jsdoc
command-wp-cli
command-ansible
```

## 未分類

```{toctree}
---
maxdepth: 1
---
command-exa
```
