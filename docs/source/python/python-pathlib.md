# pathlib

```python
from pathlib import Path
```

## ファイル名のリストを取得したい

特定のディレクトリにあるファイル名をリストで取得

```python
p = Path("ディレクトリ名")
fnames = sorted(p.glob("*.csv"))
```

## ファイルが存在する場合は〇〇したい



## ファイルが存在しない場合は〇〇したい
