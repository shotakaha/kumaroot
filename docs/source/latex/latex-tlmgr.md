# パッケージ管理したい（`tlmgr`）

```console
$ tlmgr --version
tlmgr revision 73493 (2025-01-17 23:28:29 +0100)
tlmgr using installation: /usr/local/texlive/2024
TeX Live (https://tug.org/texlive) version 2024
```

`tlmgr`コマンドでLaTeX関係のパッケージを管理できます。
パッケージは[CTAN（Comprehensive TeX Archive Network）](https://www.ctan.org/)のリポジトリで公開されています。

詳しくは[tlmgrコマンドの使い方](../command/command-tlmgr.md)に整理しました。
パッケージのドキュメント／マニュアルを確認する方法は[texdocの使い方](../command/command-texdoc.md)に整理しました。

## 更新したい（`tlmgr update --list`）

```console
$ tlmgr update --list
$ sudo tlmgr update --all
```

`tlmgr update --list`でパッケージ更新の有無を確認できます。
`tlmgr update --all`でパッケージを更新します。
`--all`実行時には管理者権限が必要です。

## 強制再インストールしたい（`--reinstall-forcibly-removed`）

```console
$ sudo tlmgr update --all --reinstall-forcibly-removed
```

更新したときに`skipping forcibly removed package`と表示されることがあります。
これは、パッケージの更新が失敗していたり、途中でキャンセルしたりして、中途半端な状態となってしまったためだと思われます。
意図的に削除したパッケージでなければ`--reinstall-forcibly-removed`オプションで解決できます。
