# パス操作したい（`pathlib`）

```python
from pathlib import Path
```

パス操作をするための標準モジュールです。
`Python3`で新しく追加されました（はず）。
`pathlib.Path`オブジェクトを使うことで、
`os.path`モジュールと同じことが、
よりオブジェクトっぽく操作できます。

## ファイルを開きたい

```python
p = Path("ファイル名")
with p.open("r") as f:
    # ファイル操作
```

`Path.open`メソッドでファイルを操作できます。
`with ... as`構文と合わせて、これまでの`open`関数と同じことができます。

```python
# これまでの開き方
p = Path("ファイル名")
with open(p, "r") as f:
    # ファイル操作
```

## ファイル名のリストを取得したい

```python
p = Path("ディレクトリ名")
fnames = sorted(p.glob("*.csv"))
```

ディレクトリ内にあるファイルの拡張子などを指定して、ファイル名のリストを取得できます。
`Path.glob(パターン)`だとジェネレーターが返ってくるので、
`sorted`して、ファイル名の順番に並べたリスト型に変換しています。

## ディレクトリを作成したい

```python
p = Path(write_to)
p.mkdir()
```

`mkdir`でディレクトリを作成できます。
すでにディレクトリが存在している場合は``FileExistsError``となります。
上書きを防止したい場合は、{command}`try ... except:`でこのエラーをキャッチすればOKです。

## パスを連結したい

```python
fname = Path("../data", "data.csv")

dname = Path("../data/")
fname = data_dir / "data.csv"
```

複数の引数を指定すると、それらを連結した`Path`オブジェクトが生成できます。
`Path`オブジェクトは`/`を使って連結できます。
`Path`オブジェクトはファイルが存在しなくても作成できます。

## パスを取得したい

```python
# ホームディレクトリ
Path.home()

# カレントディレクトリ
Path.cwd()
```

ホームディレクトリとカレントディレクトリを取得する``Path``のクラスメソッドがあります。
``Path.home()``と``Path.cwd()``でそれぞれのディレクトリ名を``Path``オブジェクトとして取得できます。

## リファレンス

- [pathlib - docs.python.org](https://docs.python.org/ja/3/library/pathlib.html)
