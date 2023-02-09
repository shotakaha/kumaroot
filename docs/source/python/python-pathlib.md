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
with p.open() as f:
    # ファイル操作
```

`Path.open`メソッドでファイルを操作できます。
`with ... as`構文と合わせて、これまでの`open`関数と同じことができます。

```python
# これまでの開き方
p = Path("ファイル名")
with open(p) as f:
    # ファイル操作
```

## ファイル名のリストを取得したい

```python
p = Path("ディレクトリ名")
fnames = sorted(p.glob("*.csv"))
```

指定したディレクトリにあるデータファイルの一覧をリスト型で取得しています。
`Path.glob(パターン)`だとジェネレーターが返ってきて、
使いづらいので`sorted`して、ファイル名の順番に並べたリストにしています。

## ディレクトリを作成したい

```python
p = Path(args.saved)
try:
    p.mkdir()
    info = f"Created new directory : {p}"
    ic(info)
except FileExistsError as e:
    warning = f"Directory already exists : {p}"
    ic(warning)
    if not args.append:
        ic(e)
        sys.exit()
    warning = "Append data to existing files."
    ic(warning)
```

ディレクトリを作成するだけなら`mkdir()`でできます。
しかし、たいていの場合、上書きするのを防止したいことが多いので{command}`try ... except:`を使っています。

## パスを連結したい

```python
fname = Path("../data", "data.csv")

dname = Path("../data/")
fname = data_dir / "data.csv"
```

複数の引数を指定すると、それらを連結した`Path`オブジェクトが生成できます。
`Path`オブジェクトは`/`を使って連結できます。
`Path`オブジェクトはファイルが存在しなくても作成できます。

## リファレンス

- [pathlib - docs.python.org](https://docs.python.org/ja/3/library/pathlib.html)
