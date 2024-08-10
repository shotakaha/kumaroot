# PyROOTしたい（ROOT + Python）

PyROOTモジュールを使うと、PythonからROOTを操作できるようになります。
HomebrewでROOTをインストールした場合、システムのPythonライブラリにインストールされます。
``virtualenvs`` や ``Poetry`` などで仮想環境を構築している場合、別途インストールが必要です。
PyROOT自体はPyPIで公開されていませんが ``uproot`` パッケージでインストールできます。

```console
$ poetry add uproot
```

## MacPortsしたい

``MacPorts`` でインストールする場合は、Pythonの {command}`variants` を指定します。
``ROOT6`` では ``+python27`` がデフォルトで **ON** になっています。
``ROOT5`` では忘れずに指定する必要があります。

また、このとき ``variants`` に指定するバージョンは、自分が使うPythonのバージョンに合わせる必要があります。
ミスマッチだと、動作せず、クラッシュします。

:::{note}

Python2.7のころには、よりPythonicな書き方で使うことを目指した `rootpy`パッケージがありました。
Python3にも対応していたと思いますが、数年前に開発停止しているようです。

- [rootpy](https://github.com/rootpy/rootpy/)

:::
