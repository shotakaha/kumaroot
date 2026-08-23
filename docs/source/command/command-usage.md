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
command-exa
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
command-tree
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
command-zed
command-vim
command-helix
```

## ドキュメントしたい

```{toctree}
---
maxdepth: 1
---
command-myst
command-pandoc
command-texdoc
command-jsdoc
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
command-brew
command-apt
command-dnf
command-asdf
command-mise
command-npm
command-gem
command-pip
command-uv
command-cmake
command-spack
command-tlmgr
command-task
command-docker
command-ghq
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
command-nushell
command-chmod
command-stat
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
command-curl
command-httpie
command-xh
command-wget
command-dig
command-ping
command-gping
command-tcpdump
command-arp
command-ssh
command-ssh-keygen
command-rsync
command-openssl
command-gpg
command-shasum
command-goaccess
```

## バージョン管理したい

```{toctree}
---
maxdepth: 1
---
command-tig
command-glab
command-gitlab
command-dvc
```

## 圧縮・展開したい

```{toctree}
---
maxdepth: 1
---
command-tar
command-gzip
command-zcat
```

## システム管理・その他したい

```{toctree}
---
maxdepth: 1
---
command-uname
command-launchctl
command-systemctl
command-zellij
command-1password
command-mkcert
command-mysql
command-fc-list
command-expect
command-ansible
command-wp-cli
command-clang-format
```
