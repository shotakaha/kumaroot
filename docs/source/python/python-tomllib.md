# TOMLしたい（`tomllib`）

```python
import tomllib
from pathlib import Path

fname = Path("設定ファイル.toml")
with fname.open("rb") as f:
    config = tomllib.load(f)
```

`tomllib`はPython3.11で標準モジュールに追加された読み込み専用のTOMLパーサーです。
TOML形式のファイルを読み込み、辞書型に変換します。

:::{note}

`tomllib`は読み込み専用のため、TOMLファイルを書き出す機能はありません。
書き出したい場合は、[tomli-w](https://github.com/hukkin/tomli-w)のような
サードパーティ製パッケージを使う必要があります。

:::

## キー／バリューしたい

```toml
integer = 1
string = "two"
number = 3.0
```

```python
{
    "integer": 1,
    "string": "two",
    "number": 3.0,
}
```

## リストしたい

```toml
integers = [1, 2, 3]
strings = ["one", "two", "three"]
mixed = [1, "two", 3.0]
```

```python
{
    "integers": [1, 2, 3],
    "strings": ["one", "two", "three"],
    "mixed": [1, "two", 3.0],
}
```

## テーブルしたい（`[table]`）

```toml
[owner]
name = "Tom"
age = 36
```

```python
{
    "owner": {
        "name": "Tom",
        "age": 36,
    }
}
```

`[table]`のようにセクション名を書くと、キー／バリューをまとめたテーブル（辞書）になります。

## インライン・テーブルしたい（`{ key = value }`）

```toml
point = { x = 1, y = 2 }
```

```python
{
    "point": {"x": 1, "y": 2}
}
```

`{ key = value, ... }`のように1行で書くテーブルを、インライン・テーブルと呼びます。
`[table]`と違い、複数行に分けて書くことはできません。

## 配列テーブルしたい（`[[table]]`）

```toml
[[record]]
run_id = 1
distance = 10.0

[[record]]
run_id = 2
distance = 20.0
```

```python
{"record":
    [
        {"run_id": 1, "distance": 10.0},
        {"run_id": 2, "distance": 20.0},
    ]
}
```

## リファレンス

- [tomllib](https://docs.python.org/3/library/tomllib.html)
- [TOML v1.0.0](https://toml.io/ja/v1.0.0)
