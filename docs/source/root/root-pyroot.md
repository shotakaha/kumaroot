# PyROOTしたい（``import ROOT``）

```python3
>>> import ROOT
>>> ROOT.__version__
'6.32.02'

>>> ROOT.__file__
'/opt/homebrew/Cellar/root/6.32.02_1/lib/root/ROOT/__init__.py'
```

``import ROOT``でPyROOTパッケージを読み込むと、PythonからROOTを操作できるようになります。
PyROOTパッケージはROOTをインストールしたパスにあります。

## パス設定（``$PYTHONPATH``）

```bash
export ROOTSYS=$(root-config --prefix)
export PYTHONPATH=$ROOTSYS/lib/root:$PYTHONPATH
```

[環境変数の設定](./root-install-env.md)で``PYTHONPATH``も設定されるはずですが、
使用しているPython環境によっては、パスが認識されない場合があります。
その場合は、環境変数``$PYTHONPATH``にパスを追加するとよいはずです。

:::{note}

``virtualenv``や``Poetry``などで仮想環境上に構築している場合、
``jupyter-lab``を``pipx``でインストールした場合、
VS Code上のJupyter（``ipykernel``）を使っている場合などで、
うまくimportできない場合は、まず``PYTHONPATH``の設定を確認してみるとよいと思います。

:::

## 仮想環境したい（`uv venv`）

```console
// PyROOTがビルドされたPythonのバージョンを確認
$ root-config --python-version
3.14.5

// uv venvで仮想環境を作成
$ uv venv --python 3.14 --system-site-packages

// PyROOTの動作確認
$ uv run python3 -c "import ROOT; print(ROOT.__version__)"

// ROOT Notebookを使う場合
$ uv pip install jupyter
$ uv pip install metakernel    # ROOT C++ kernelに必要
$ uv run root --notebook
```

プロジェクトでPyROOTを使う場合は、
仮想環境からシステムパッケージを参照できるようにするのが簡単です。
このサンプルは`uv venv`を使ったときのコマンド例です。

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
