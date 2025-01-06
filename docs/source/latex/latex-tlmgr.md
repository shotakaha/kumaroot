# パッケージを更新したい（`tlmgr`）

```console
$ tlmgr update --list
$ sudo tlmgr update --all
```

`tlmgr`はLaTeXのパッケージを管理するコマンドです。
パッケージは[CTAN（Comprehensive TeX Archive Network）](https://www.ctan.org/)のリポジトリで公開されています。
詳しくは[tlmgrコマンドの使い方](../command/command-tlmgr.md)を参照してください。
パッケージの詳細を確認する方法は[texdocの使い方](../command/command-texdoc.md)を参照してください。

## パッケージを強制的に再インストールしたい

```console
$ sudo tlmgr update --all --reinstall-forcibly-removed
```

更新したときに`skipping forcibly removed package`と表示されることがあります。
これは、パッケージの更新が失敗していたり、途中でキャンセルしたりして、中途半端な状態となってしまったためだと思われます。
意図的に削除したパッケージでなければ`--reinstall-forcibly-removed`オプションで解決できます。
