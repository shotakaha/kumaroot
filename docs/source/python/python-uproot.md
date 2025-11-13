# uprootしたい（`uproot`）

```python
import uproot

with uproot.open("path/to/dataset.root") as f:
    # データ処理
```

`uproot`パッケージでROOT形式のファイルを読み込むことができます。
C++に依存せず、Pure Python + Numpyで書かれています。
ROOTファイルをPythonで処理したい場合に便利です。

## インストールしたい（`uproot`）

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install uproot awkward
```

## リファレンス

- [uproot](https://uproot.readthedocs.io/en/latest/)
