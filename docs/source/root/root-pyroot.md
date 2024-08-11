# PyROOTしたい（``$PYTHONPATH``）

```bash
export ROOTSYS=$(root-config --prefix)
export PYTHONPATH=$ROOTSYS/lib/root:$PYTHONPATH
```

PyROOTパッケージを使うと、PythonからROOTを操作できるようになります。
PyROOTパッケージはROOTをインストールしたパスにあります。
環境変数``$PYTHONPATH``にそのパスを追加する必要があります。

```python3
import ROOT
ROOT.__version__
# '6.32.02'

ROOT.__file__
# '/opt/homebrew/Cellar/root/6.32.02_1/lib/root/ROOT/__init__.py'
```

:::{note}

``$PYTHONPATH``だけを設定しても、付属の設定スクリプトを使って他の環境変数と一緒に設定してもOKです。

- [](./root-install-env.md)

:::


## （削除予定）MacPortsしたい

> この段落の内容は古くなっています。
> 10年くらいMacPortsは使っていないため、近いうちに削除します。

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
