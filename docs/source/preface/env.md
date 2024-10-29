# ドキュメント環境

DokuWikiの引っ越し先をあれこれ検討した結果、いちから作り直すことにして、
[GitHub](https://github.com/shotakaha/kumaroot)でソースを管理、
[Sphinx](https://www.sphinx-doc.org/ja/master/)で文書を作成、
[Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)で公開することにしました。

## ローカルの開発環境

このドキュメントをビルドしているローカル環境です。

> 2023/05/22時点

## macOS環境

```console
$ neofetch
                    'c.
                 ,xNMM.          --------------------------------------
               .OMMMMo           OS: macOS 13.2.1 22D68 arm64
               OMMM0,            Host: Mac14,2
     .;loddo:' loolloddol;.      Kernel: 22.3.0
   cKMMMMMMMMMMNWMMMMMMMMMM0:    Uptime: 7 days, 4 hours, 58 mins
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.    Packages: 118 (brew)
 XMMMMMMMMMMMMMMMMMMMMMMMX.      Shell: fish 3.6.1
;MMMMMMMMMMMMMMMMMMMMMMMM:       Resolution: 1440x2560, 1710x1112
:MMMMMMMMMMMMMMMMMMMMMMMM:       DE: Aqua
.MMMMMMMMMMMMMMMMMMMMMMMMX.      WM: Quartz Compositor
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.    WM Theme: Orange (Light)
 .XMMMMMMMMMMMMMMMMMMMMMMMMMMk   Terminal: Apple_Terminal
  .XMMMMMMMMMMMMMMMMMMMMMMMMK.   Terminal Font: SFMono-Regular
    kMMMMMMMMMMMMMMMMMMMMMMd     CPU: Apple M2
     ;KMMMMMMMWXXWMMMMMMMk.      GPU: Apple M2
       .cooc,.    .,coo:.        Memory: 3942MiB / 24576MiB
```

## Homebrew環境

```console
$ brew --version
Homebrew 4.0.18
Homebrew/homebrew-core (git revision ceb6f460128; last commit 2023-02-20)
```

macOS上のツール（ソフトウェアやフォント）は[Homebrew](https://brew.sh/)で管理しています。

## シェル環境

```console
$ brew info fish
==> fish: stable 3.6.1 (bottled), HEAD
User-friendly command-line shell for UNIX-like operating systems
https://fishshell.com
/opt/homebrew/Cellar/fish/3.6.1 (1,487 files, 15.4MB) *
  Poured from bottle using the formulae.brew.sh API on 2023-03-27 at 09:55:26
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/fish.rb
License: GPL-2.0-only
```

```console
$ fish --version
fish, version 3.6.1
```

## Git環境

```console
$ brew info git
==> git: stable 2.40.1 (bottled), HEAD
Distributed revision control system
https://git-scm.com
/opt/homebrew/Cellar/git/2.40.1 (1,635 files, 48.9MB) *
  Poured from bottle using the formulae.brew.sh API on 2023-04-26 at 09:24:33
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/git.rb
License: GPL-2.0-only
```

```console
$ git --version
git version 2.40.1
```

```console
$ git lfs --version
git-lfs/3.3.0 (GitHub; darwin arm64; go 1.19.3)
```

## Python環境

```console
$ brew info python@3.11
==> python@3.11: stable 3.11.3 (bottled)
Interpreted, interactive, object-oriented programming language
https://www.python.org/
/opt/homebrew/Cellar/python@3.11/3.11.3 (3,273 files, 64.7MB) *
  Poured from bottle using the formulae.brew.sh API on 2023-04-09 at 15:50:14
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/python@3.11.rb
License: Python-2.0
```

```console
$ brew info pipx
==> pipx: stable 1.2.0 (bottled), HEAD
Execute binaries from Python packages in isolated environments
https://pypa.github.io/pipx
/opt/homebrew/Cellar/pipx/1.2.0 (936 files, 11.7MB) *
  Poured from bottle using the formulae.brew.sh API on 2023-05-27 at 09:53:30
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/pipx.rb
License: MIT
```

```console
$ which python3
/opt/homebrew/bin/python3

$ python3 --version
Python 3.11.3
```

```console
$ which pipx
/opt/homebrew/bin/pipx

$ pipx --version
1.2.0
```

```console
$ which poetry
~/.local/bin/poetry

$ poetry --version
Poetry (version 1.5.0)
```

```console
$ poetry env info

Virtualenv
Python:         3.11.3
Implementation: CPython
Path:           ~/repos/github.com/shotakaha/kumaroot/.venv
Executable:     ~/repos/github.com/shotakaha/kumaroot/.venv/bin/python
Valid:          True

System
Platform:   darwin
OS:         posix
Python:     3.11.3
Path:       /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11
Executable: /opt/homebrew/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/bin/python3.11
```

Python環境はプロジェクトごとに[Poetry](https://python-poetry.org/)で管理しています。

## Hugo環境

```console
$ brew info hugo
==> hugo: stable 0.111.3 (bottled), HEAD
Configurable static site generator
https://gohugo.io/
/opt/homebrew/Cellar/hugo/0.111.3 (48 files, 56.4MB) *
  Poured from bottle using the formulae.brew.sh API on 2023-03-25 at 14:03:17
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/hugo.rb
License: Apache-2.0
```

```console
$ hugo version
hugo v0.111.3+extended darwin/arm64 BuildDate=unknown
```

## Node環境

```console
$ brew info node
==> node: stable 20.1.0 (bottled), HEAD
Platform built on V8 to build network applications
https://nodejs.org/
/opt/homebrew/Cellar/node/20.1.0 (2,260 files, 57.3MB) *
  Poured from bottle using the formulae.brew.sh API on 2023-05-05 at 22:03:03
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/node.rb
License: MIT
```

```console
$ node --version
v20.1.0
```

```console
$ npm --version
9.6.4
```

## ROOT環境

```console
$ brew info root
==> root: stable 6.26.06 (bottled), HEAD
Object oriented framework for large scale data analysis
https://root.cern.ch/
/opt/homebrew/Cellar/root/6.26.06_2 (6,415 files, 534.9MB) *
  Poured from bottle using the formulae.brew.sh API on 2023-02-25 at 20:40:16
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/root.rb
License: LGPL-2.1-or-later
```

```console
$ root --version
ROOT Version: 6.26/06
Built for macosxarm64 on Jul 28 2022, 18:08:51
From tags/v6-26-06@v6-26-06
```

## LaTeX環境

``Homebrew``を使ってMacTeXをインストールしています。

```console
$ brew info --cask mactex
==> mactex: 2023.0314
https://www.tug.org/mactex/
/opt/homebrew/Caskroom/mactex/2023.0314 (5.1GB)
From: https://github.com/Homebrew/homebrew-cask/blob/HEAD/Casks/mactex.rb
==> Name
MacTeX
==> Description
Full TeX Live distribution with GUI applications
==> Artifacts
mactex-20230314.pkg (Pkg)
```

```console
$ tlmgr --version
tlmgr revision 66798 (2023-04-08 02:15:21 +0200)
tlmgr using installation: /usr/local/texlive/2023
TeX Live (https://tug.org/texlive) version 2023
```

```console
$ lualatex --version
This is LuaHBTeX, Version 1.17.0 (TeX Live 2023)
Development id: 7581
```

## Docker環境

```console
$ brew info --cask docker
==> docker: 4.19.0,106363 (auto_updates)
https://www.docker.com/products/docker-desktop
/opt/homebrew/Caskroom/docker/4.17.0,99724 (120B)
From: https://github.com/Homebrew/homebrew-cask/blob/HEAD/Casks/docker.rb
==> Names
Docker Desktop
Docker Community Edition
Docker CE
==> Description
App to build and share containerized applications and microservices
==> Artifacts
Docker.app (App)
Docker.app/Contents/Resources/bin/docker-compose -> /usr/local/bin/docker-compose (Binary)
Docker.app/Contents/Resources/bin/docker-compose-v1/docker-compose -> /usr/local/bin/docker-compose-v1 (Binary)
Docker.app/Contents/Resources/bin/docker-credential-desktop -> /usr/local/bin/docker-credential-desktop (Binary)
Docker.app/Contents/Resources/bin/docker-credential-ecr-login -> /usr/local/bin/docker-credential-ecr-login (Binary)
Docker.app/Contents/Resources/bin/docker-credential-osxkeychain -> /usr/local/bin/docker-credential-osxkeychain (Binary)
Docker.app/Contents/Resources/bin/docker-index -> /usr/local/bin/docker-index (Binary)
Docker.app/Contents/Resources/bin/hub-tool -> /usr/local/bin/hub-tool (Binary)
Docker.app/Contents/Resources/bin/kubectl -> /usr/local/bin/kubectl.docker (Binary)
Docker.app/Contents/Resources/etc/docker-compose.bash-completion -> /opt/homebrew/etc/bash_completion.d/docker-compose (Binary)
Docker.app/Contents/Resources/etc/docker.zsh-completion -> /opt/homebrew/share/zsh/site-functions/_docker (Binary)
Docker.app/Contents/Resources/etc/docker-compose.zsh-completion -> /opt/homebrew/share/zsh/site-functions/_docker_compose (Binary)
Docker.app/Contents/Resources/etc/docker.fish-completion -> /opt/homebrew/share/fish/vendor_completions.d/docker.fish (Binary)
Docker.app/Contents/Resources/etc/docker-compose.fish-completion -> /opt/homebrew/share/fish/vendor_completions.d/docker-compose.fish (Binary)
Docker.app/Contents/Resources/bin/com.docker.vpnkit -> /usr/local/bin/vpnkit (Binary)
Docker.app/Contents/Resources/bin/com.docker.cli -> /usr/local/bin/com.docker.cli (Binary)
Docker.app/Contents/Resources/etc/docker.bash-completion -> /opt/homebrew/etc/bash_completion.d/docker (Binary)
Docker.app/Contents/Resources/bin/docker -> /usr/local/bin/docker (Binary)
```

```console
$ docker --version
Docker version 23.0.5, build bc4487a
```
