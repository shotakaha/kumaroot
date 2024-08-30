# TOMLしたい（`tomllib`）

```python
import tomllib

fname = Path("設定ファイル.toml")
with fname.open("rb") as f:
    config = tomllib.load(f)
```

`tomllib`はPython3.11で標準モジュールに追加された読み込み専用のTOMLパーサーです。
TOML形式のファイルを読み込み、辞書型に変換します。

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

## インライン・テーブルしたい

```toml
[[record]]
run_id = 1
distance = 10.0}

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
