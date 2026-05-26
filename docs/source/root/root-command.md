# ファイルを確認したい（`rootls`）

```console
$ rootls filename.root

$ rootls -l filename.root
```

`rootls`コマンドで、ROOTファイルの内容を確認できます。
`-l`オプションで、ファイルの内容を詳細に表示できます。
`ls`コマンドに相当するコマンドです。

```console
$ root filename.root

root[0] .ls
```

ROOTインタープリターでファイルを開き、
`.ls`コマンドを実行することに相当します。

## ファイルをブラウズしたい（`rootbrowse`）

```console
$ rootbrowse filename.root
```

`rootbrowse`コマンドで、ROOTファイルを直接`TBrowser`で開くことができます。

```console
$ root filename.root

root[0] TBrowser b;
```

ROOTインタープリターでファイルを開き、
`TBrowser`を起動することに相当します。
