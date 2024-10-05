# パス操作したい（`pathlib`）

```python
from pathlib import Path
```

パス操作をするための標準モジュールです。
`Python3`で新しく追加されました（はず）。
`pathlib.Path`オブジェクトを使うことで、
`os.path`モジュールと同じことが、
よりオブジェクトっぽく操作できます。

## ファイル名のリストを取得したい

```python
p = Path("ディレクトリ名")
fnames = sorted(p.glob("*.csv"))
```

ディレクトリ内にあるファイルの拡張子などを指定して、ファイル名のリストを取得できます。
`Path.glob(パターン)`だとジェネレーターが返ってくるので、
`sorted`して、ファイル名の順番に並べたリスト型に変換しています。

## ファイルを開きたい（`open`）

```python
# ファイルを開いて、データを読み込む
p = Path("入力ファイル名")
with p.open("r") as f:
    lines = f.read()

# ファイルを開いて、データを書き込む
o = Path("出力ファイル名")
with o.open("w") as f:
    f.write(lines)
```

`open`メソッドでファイル（のポインター）を取得できます。
また、コンテキストマネージャー（`with ... as`構文）と組み合わせて、
ファイル操作ができます。

:::{note}

読み込む／書き込むデータがテキストデータとわかっている場合は、
より簡便な`read_text`、`write_text`メソッドがあります。

:::

```python
# これまでの開き方
p = Path("ファイル名")
with open(p, "r") as f:
    # ファイル操作
```

Pathオブジェクトは、従来の`open`関数の引数に直接渡すことができます。

## ファイルから読み込みたい（`read_text` / `read_bytes`）

```python
p = Path("ファイル名")
p.read_text(encoding="utf-8")  # mode="r"
p.read_bytes()    # mode="rb"
```

`reat_text`メソッドで、ファイルからテキストデータを読み込めます。
エンコーディングはデフォルトでUTF-8ですが、`encoding`オプションで変更できます。
バイナリーデータを読み込む場合は`read_bytes`を使います。
これらのメソッドの内部処理では
コンテキストマネージャーを使っています。

```python
with p.open(mode="r", encoding="utf-8") as f:
    lines = f.read()
```

`open`メソッドを使って、コンテキストマネージャーを明示的に書いたサンプルです。
テキストデータの場合は`mode="r"`、
バイナリデータの場合は`mode="rb"`に設定します。

## ファイルに書き込みたい（`write_text` / `write_bytes`）

```python
p = Path("ファイル名")
p.write_text("テキストデータ", encoding="utf-8")  # mode="w"
p.write_bytes("バイナリーデータ")   # mode="wb"
```

`write_text`メソッドで、ファイルにテキストデータを書き込めます。
`encoding`オプションでエンコーディングを変更できます。
デフォルトはシステムのエンコーディングです（Linux／macOSだと`utf-8`）。
`errors`オプションでエンコーディングエラーが発生した場合の処理方法を設定できます。
デフォルトは`strict`で`UnicodeEncodeError`の例外が発生します。

`newline`オプションで改行コードを変更できます。
デフォルトは`None`でシステムの改行コードが指定されます。

バイナリーデータを書き込む場合は`write_bytes`を使います。
これらのメソッドの内部処理では
受け取ったデータの型チェックと、
コンテキストマネージャーを使っています。

```python
# with...as構文
with p.open(mode="w", encoding="utf-8") as f:
    f.write("テキストデータ")
```

`open`メソッドを使って、コンテキストマネージャーを明示的に書いたサンプルです。
テキストデータの場合は`mode="w"`、
バイナリデータの場合は`mode="wb"`に設定します。

## ディレクトリを作成したい（`mkdir`）

```python
p = Path("ディレクトリ名")
p.mkdir()
```

`mkdir` メソッドでディレクトリを作成できます。
すでにディレクトリが存在している場合は``FileExistsError``となります。

```python
p = Path("ディレクトリ名")
try:
    p.mkdir()
except FileExistsError as e:
    print("ディレクトリはすでに存在します")
```

上書きを防止したい場合は、、`try ... except:`でこのエラーをキャッチすればOKです。

```python
p = Path("ディレクトリ名/サブディレクトリ名/ファイル名.csv")
# 親ディレクトリのPathオブジェクトを取得
# p.parent => Path("ディレクトリ名/サブディレクトリ名")
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("テキストデータ")
```

中間ディレクトリも含めて作成することもできます。
ディレクトリを必ず作成したい場合は、``parents=True``と``exist_ok=True``オプションを設定します。

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
