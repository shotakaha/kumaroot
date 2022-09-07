# pathlib

```python
from pathlib import Path
```

## ファイル名のリストを取得したい

```python
p = Path("ディレクトリ名")
fnames = sorted(p.glob("*.csv"))
```

指定したディレクトリにあるデータファイルの一覧をリスト型で取得しています。
``p.glob``だとジェネレーターが返ってきて、使いづらいので``sorted``して、ファイル名の順番に並べたリストにしています。

## ファイルが存在する場合は〇〇したい

```python
if p.exists():
    error = "File already exists."
    ic(error)
```

## ファイルが存在しない場合は〇〇したい

```python
if not p.exists():
    error = "No file found."
    ic(error)
```
