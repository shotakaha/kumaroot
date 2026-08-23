# ドキュメント環境

DokuWikiの引っ越し先をあれこれ検討した結果、いちから作り直すことにして、
[GitHub](https://github.com/shotakaha/kumaroot)でソースを管理、
[Sphinx](https://www.sphinx-doc.org/ja/master/)で文書を作成、
[Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)で公開することにしました。

## ローカルの開発環境

このドキュメントをビルドしているローカル環境です。

> 2026/08/23時点

## macOS環境

```console
$ fastfetch
                     ..'          shotakaha@orca
                 ,xNMM.           --------------
               .OMMMMo            OS: macOS Tahoe 26.5.2 (25F84) arm64
               lMM"               Host: MacBook Air (M2, 2022)
     .;loddo:.  .olloddol;.       Kernel: Darwin 25.5.0
   cKMMMMMMMMMMNWMMMMMMMMMM0:     Uptime: 2 hours, 14 mins
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.     Packages: 362 (brew), 136 (brew-cask)
 XMMMMMMMMMMMMMMMMMMMMMMMX.       Shell: fish 4.8.1
;MMMMMMMMMMMMMMMMMMMMMMMM:        CPU: Apple M2 (4+4) @ 3.50 GHz
:MMMMMMMMMMMMMMMMMMMMMMMM:        GPU: Apple M2 (10) @ 1.40 GHz [Integrated]
.MMMMMMMMMMMMMMMMMMMMMMMMX.       Memory: 18.54 GiB / 24.00 GiB (77%)
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.     Disk (/): 902.21 GiB / 926.35 GiB (97%) - apfs [Read-only]
 'XMMMMMMMMMMMMMMMMMMMMMMMMMMk
  'XMMMMMMMMMMMMMMMMMMMMMMMMK.
    kMMMMMMMMMMMMMMMMMMMMMMd
     ;KMMMMMMMWXXWMMMMMMMk.
       "cooc*"    "*coo'"
```

`neofetch`は開発が止まってしまったので、後継の[fastfetch](https://github.com/fastfetch-cli/fastfetch)を使っています。

## Homebrew環境

```console
$ brew --version
Homebrew 6.0.18-160-gc142e82
Homebrew/homebrew-cask (git revision 34fe3b2409d; last commit 2026-08-23)
```

macOS上のツール（ソフトウェアやフォント）は[Homebrew](https://brew.sh/)で管理しています。

## シェル環境

```console
$ brew info fish
==> fish: stable 4.8.1 (bottled), HEAD
User-friendly command-line shell for UNIX-like operating systems
https://fishshell.com
Installed (on request)
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/f/fish.rb
License: GPL-2.0-only
```

```console
$ fish --version
fish, version 4.8.1
```

## Git環境

```console
$ brew info git
==> git: stable 2.55.0 (bottled), HEAD
Distributed revision control system
https://git-scm.com
Installed (on request)
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/g/git.rb
License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND MIT
```

```console
$ git --version
git version 2.55.0
```

```console
$ git lfs --version
git-lfs/3.7.1 (GitHub; darwin arm64; go 1.25.3)
```

## Python環境

```console
$ brew info python@3.12
==> python@3.12: stable 3.12.14 (bottled)
Interpreted, interactive, object-oriented programming language
https://www.python.org/
Installed (on request)
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/p/python@3.12.rb
License: Python-2.0
```

```console
$ brew info pipx
==> pipx: stable 1.16.7 (bottled), HEAD
Execute binaries from Python packages in isolated environments
https://pipx.pypa.io
Installed (on request)
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/p/pipx.rb
License: MIT
```

```console
$ which python3
/opt/homebrew/bin/python3

$ python3 --version
Python 3.12.7
```

```console
$ which pipx
/opt/homebrew/bin/pipx

$ pipx --version
1.16.7
```

```console
$ which poetry
~/.local/bin/poetry

$ poetry --version
Poetry (version 2.4.1)
```

```console
$ poetry env info

Virtualenv
Python:         3.12.7
Implementation: CPython
Path:           ~/repos/github.com/shotakaha/kumaroot/.venv
Executable:     ~/repos/github.com/shotakaha/kumaroot/.venv/bin/python
Valid:          True

Base
Platform:   darwin
OS:         posix
Python:     3.12.7
Path:       ~/.local/share/uv/python/cpython-3.12-macos-aarch64-none
Executable: ~/.local/share/uv/python/cpython-3.12-macos-aarch64-none/bin/python3.12
```

Python環境はプロジェクトごとに[Poetry](https://python-poetry.org/)で管理しています。

## Hugo環境

```console
$ brew info hugo
==> hugo: stable 0.165.0 (bottled), HEAD
Configurable static site generator
https://gohugo.io/
Installed (on request)
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/h/hugo.rb
License: Apache-2.0
```

```console
$ hugo version
hugo v0.165.0+extended+withdeploy darwin/arm64 BuildDate=2026-08-12T14:26:28Z VendorInfo=Homebrew
```

## Node環境

```console
$ brew info node
==> node: stable 26.7.0 (bottled), HEAD
Open-source, cross-platform JavaScript runtime environment
https://nodejs.org/
Aliases: node.js, node@26, nodejs, npm
Installed (on request)
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/n/node.rb
License: MIT
```

```console
$ node --version
v26.7.0
```

```console
$ npm --version
11.19.0
```

## ROOT環境

```console
$ brew info root
==> root: stable 6.40.02 (bottled), HEAD
Analyzing petabytes of data, scientifically
https://root.cern
Old Names: root6
Installed (on request)
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/r/root.rb
License: LGPL-2.1-or-later
```

```console
$ root --version
ROOT Version: 6.40.02
Built for macosxarm64 on Jun 10 2026, 09:29:53
From tags/6-40-02@6-40-02
```

## LaTeX環境

``Homebrew``を使ってMacTeXをインストールしています。

```console
$ brew info --cask mactex
==> mactex (MacTeX): 2026.0324
Full TeX Live distribution with GUI applications
https://www.tug.org/mactex/
Installed (as dependency)
/opt/homebrew/Caskroom/mactex/2026.0324 (6.9GB)
From: https://github.com/Homebrew/homebrew-cask/blob/HEAD/Casks/m/mactex.rb
==> Artifacts
mactex-20260324.pkg (Pkg)
```

```console
$ tlmgr --version
tlmgr revision 79639 (2026-07-10 18:45:34 +0200)
tlmgr using installation: /usr/local/texlive/2026
TeX Live (https://tug.org/texlive) version 2026
```

```console
$ lualatex --version
This is LuaHBTeX, Version 1.24.0 (TeX Live 2026)
Development id: 7724
```

## Docker環境

```console
$ brew info --cask docker-desktop
==> docker-desktop (Docker Desktop, Docker Community Edition, Docker CE): 4.87.0,236836 (auto_updates)
App to build and share containerised applications and microservices
https://www.docker.com/products/docker-desktop
Installed (on request)
/opt/homebrew/Caskroom/docker-desktop/4.87.0,236836 (2.3GB)
From: https://github.com/Homebrew/homebrew-cask/blob/HEAD/Casks/d/docker-desktop.rb
==> Artifacts
Docker.app (App)
/Applications/Docker.app/Contents/Resources/bin/docker-credential-osxkeychain -> /usr/local/bin/docker-credential-osxkeychain (Binary)
/Applications/Docker.app/Contents/Resources/bin/kubectl -> /usr/local/bin/kubectl.docker (Binary)
/Applications/Docker.app/Contents/Resources/cli-plugins/docker-compose -> /usr/local/cli-plugins/docker-compose (Binary)
/Applications/Docker.app/Contents/Resources/bin/docker -> /usr/local/bin/docker (Binary)
```

```console
$ docker --version
Docker version 29.7.2, build a7dcaa6
```

``Homebrew``のCask名が``docker``から``docker-desktop``に変わりました。
