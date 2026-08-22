# パッケージ管理したい（`tlmgr`）

```console
$ tlmgr update --list
$ sudo tlmgr update --all
$ sudo tlmgr update --self
$ sudo tlmgr install パッケージ名
$ sudo tlmgr remove パッケージ名
```

`tlmgr`は、LaTeXのパッケージ管理コマンドです。

## インストールしたい（`mactex`）

```console
$ brew install --cask mactex
$ tlmgr --version
tlmgr revision 79639 (2026-07-10 18:45:34 +0200)
tlmgr using installation: /usr/local/texlive/2026
TeX Live (https://tug.org/texlive) version 2026
```

`tlmgr`はHomebrewでインストールできます。
フォーミュラ名は`mactex`です。

:::{note}

`mactex`は、macOS用のTeX Liveディストリビューションです。
サイズがかなり大きいため、インストールに時間がかかります。

:::

## パッケージを探したい（`tlmgr search`）

```console
$ tlmgr search --file "ファイル名"
$ tlmgr search --file "siunitx.sty"
luatexja:
    texmf-dist/tex/luatex/luatexja/patches/lltjp-siunitx.sty
...
siunitx:
    texmf-dist/tex/latex/siunitx/siunitx.sty
```

`search`コマンドで、パッケージを検索できます。
`--file`オプションをつけると、ファイル名（`.sty`や`.cls`など）からそれを含むパッケージを逆引きできます。
`\usepackage{}`で指定するパッケージ名がわからないときに便利です。

## パッケージの詳細を確認したい（`tlmgr info`）

```console
$ tlmgr info パッケージ名
$ tlmgr info siunitx
package:     siunitx
category:    Package
shortdesc:   A comprehensive (SI) units package
installed:   Yes
revision:    79011
sizes:       src: 801k, doc: 881k, run: 661k
cat-version: 3.5.5
cat-license: lppl1.3c
```

`info`コマンドで、パッケージの詳細情報を確認できます。
インストール済みかどうか（`installed`）、バージョン（`cat-version`）、ライセンス（`cat-license`）などがわかります。

## パッケージを追加したい（`tlmgr install`）

```console
$ sudo tlmgr install パッケージ名
```

`install`コマンドでパッケージを追加できます。
インストール先がシステム領域なので、`sudo`が必要です。

## パッケージを削除したい（`tlmgr remove`）

```console
$ sudo tlmgr remove パッケージ名
```

`remove`コマンドでパッケージを削除できます。

## パッケージの更新を確認したい（`tlmgr update`）

```console
$ tlmgr update --list
tlmgr: package repository ... (verified)
tlmgr: no updates available
```

`update --list`で、更新可能なパッケージがあるかを確認できます。
このコマンド自体はパッケージを更新しません。

## すべてのパッケージを更新したい（`tlmgr update --all`）

```console
$ sudo tlmgr update --all
```

`--all`オプションをつけると、更新可能なパッケージをすべて更新できます。
インストール先がシステム領域なので、`sudo`が必要です。

## 設定を確認したい（`tlmgr option`）

```console
$ tlmgr option
Number of backups to keep (autobackup): 1
Directory for backups (backupdir): tlpkg/backups
Generate formats at installation or update (formats): 1
Install documentation files (docfiles): 1
Install source files (srcfiles): 1
Default package repository (repository): http://mirror.ctan.org/systems/texlive/tlnet
Run postinst code blobs (postcode): 1
Destination for symlinks for binaries (sys_bin): /usr/local/bin
Destination for symlinks for info docs (sys_info): /usr/local/share/info
Destination for symlinks for man pages (sys_man): /usr/local/share/man
```

`tlmgr option`コマンドで設定を確認できます。
各項目の括弧内にある文字列（キー）で個別に確認できます。

```console
$ tlmgr option repository
Default package repository (repository): http://mirror.ctan.org/systems/texlive/tlnet
```

`tlmgr option キー 値`で、設定を書き換えることができます。
たとえば、パッケージリポジトリのミラーを変更したいときに使います。

```console
$ tlmgr option repository https://mirror.ctan.org/systems/texlive/tlnet
```

## 関連コマンド

- [](command-texdoc.md)
