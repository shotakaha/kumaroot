# tlmgr

LaTeXパッケージを管理するコマンドです。

## パッケージの更新を確認する

```bash
tlmgr update --list
```

## すべてのパッケージを更新する

```bash
sudo tlmgr update --all
```

## パッケージを追加する

```bash
tlmgr install パッケージ名
```

## パッケージを削除する

```bash
tlmgr remove パッケージ名
```

## 設定を確認する

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

``tlmgr option``コマンドで設定を確認できます。
各項目の括弧内にある文字列で個別に確認できます。

```console
$ tlmgr option repository
Default package repository (repository): http://mirror.ctan.org/systems/texlive/tlnet
```

ここに値を渡して、設定を書き換えることができます。

```console
$ tlmgr option repository リポジトリ名
（ためしてない）
```

## 関連コマンド

- [](command-texdoc.md)
