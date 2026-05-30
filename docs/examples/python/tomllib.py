# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# # TOMLしたい（`tomllib`）
#
# - `tomllib`はPython3.11で追加されたTOMLパーサー
# - https://docs.python.org/3/library/tomllib.html
# - https://toml.io/en/

import tomllib

# +
s = """
integer = 1
string = "two"
number = 3.0
"""

tomllib.loads(s)
# -

# リスト

# +
s = """
integers = [1, 2, 3]
colors = [ "red", "yellow", "green" ]
nested_arrays_of_ints = [ [ 1, 2 ], [3, 4, 5] ]
nested_mixed_array = [ [ 1, 2 ], ["a", "b", "c"] ]
string_array = [ "all", 'strings', '''are the same''', '''type''' ]
numbers = [ 0.1, 0.2, 0.5, 1, 2, 5 ]
"""

tomllib.loads(s)
# -

# テーブル

# +
s = """
# Top-level table begins.
name = "Fido"
breed = "pug"

# Top-level table ends.
[owner]
name = "Regina Dogman"
member_since = 1999-08-04

[table-1]
key1 = "some string"
key2 = 123

[table-2]
key1 = "another string"
key2 = 456
"""

tomllib.loads(s)
# -

# インライン・テーブル
#
# - テーブルとインライン・テーブルは互換性がある
# - どちらで書いてもよい

# +
s = """
# インライン・テーブル
name = { first = "Tom", last = "Preston-Werner" }
point = { x = 1, y = 2 }

# テーブル
[animal]
type.name = "pug"
"""

tomllib.loads(s)
# -

# テーブルの中の配列
#
# ```python
# {"key": [
#     {"k1": "v1"},
#     {"k2": "v2"}
#     ]
# }
# ```

# +
s = """
[[products]]
name = "Hammer"
sku = 738594937

[[products]]  # empty table within the array

[[products]]
name = "Nail"
sku = 284758393

color = "gray"
"""

tomllib.loads(s)
