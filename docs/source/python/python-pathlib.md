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

ディレクトリを作成するだけなら``mkdir()``でできます。
しかし、たいていの場合、上書きするのを防止したいことが多いので、```try ... except:``を使っています。
