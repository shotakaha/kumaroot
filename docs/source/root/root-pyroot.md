# PyROOTしたい（`import ROOT`）

```python3
>>> import ROOT
>>> ROOT.__version__
'6.40.00'

>>> ROOT.__file__
'/opt/homebrew/Cellar/root/6.40.00/lib/root/ROOT/__init__.py'
```

`PyROOT`は、PythonからROOTを操作できるパッケージです。
`import ROOT`でパッケージを読み込み、
バージョンやライブラリのパスを確認しています。

## パス設定したい（`$PYTHONPATH`）

```bash
export ROOTSYS=$(root-config --prefix)
export PYTHONPATH=$ROOTSYS/lib/root:$PYTHONPATH
```

`ROOTSYS`と`PYTHONPATH`を適切に設定します。
[環境変数の設定](./root-install-env.md)で設定されるはずですが、使用しているPython環境によっては、このPATHが認識されない場合があります。
その場合は、`$PYTHONPATH`の値がどうなっているかを確認し、必要に応じてパスを追加してください。

:::{note}

`virtualenv`や`uv`などで仮想環境上に構築している場合、
`jupyter-lab`を`pipx`でインストールした場合、
VS Code上のJupyter（`ipykernel`）を使っている場合などで、
うまくimportできない場合は、まず`PYTHONPATH`の設定を確認してみるとよいと思います。

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

このサンプルは`uv venv`を使ったときのコマンド例です。
プロジェクトごとに仮想環境を作成する場合、
`--system-site-packages`オプションで、仮想環境からシステムパッケージを参照できるようにします。
