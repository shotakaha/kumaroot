# URL操作したい（`urllib.parse`）

```python
from urllib.parse import urlparse, urlsplit

o = urlparse("https://example.com/path1/path2/path3.html?key1=value1&key2=value2#frag1)
# o = urlsplit("https://example.com/path1/path2/path3.html?key1=value1&key2=value2#frag1)
print(f"{o.scheme=}")  # https
print(f"{o.netloc=}")  # example.com
print(f"{o.path=}")    # /path1/path2/path3.html
print(f"{o.query=}")    # key1=value1&key2=value2
print(f"{o.fragment=}")    # frag1
```

`urllib.parse`は標準モジュールです。
`urlparse`や`urlsplit`、`parse_qs`といったURLやクエリを抽出するメソッドを持っています。
URLにアクセスすることなく、文字列操作できるのが便利です。

## クエリを取り出したい（`parse_qs` / `parse_qsl`）

```python
from urllib.parse import urlparse, parse_qs
o = urlparse("https://example.com/path1/path2/path3.html?key1=value1&key2=value2#frag1)

parse_qs(o.query)    # {"key1": ["value1"], "key2": ["value2"]}
parse_qsl(o.query)   # [("key1", "value1"), ("key2", "value2")]
```

`parse_qs`でクエリを辞書型、
`parse_qsl`でクエリをリスト型に変換できます。

```python
# 辞書型（parse_qs）
response = requests.get(url="https://httpbin.org/get", params=parse_qs(o.query))

# リスト型（parse_qsl）
response = requests.get(url="https://httpbin.org/get", params=parse_qsl(o.query))
```

どちらの結果も[requests](./python-requests.md)の`params`に直接渡すことができます。

## クエリを文字列にしたい（`urlencode`）

```python
from urllib.parse import urlencode

q1 = {"key1": "value1", "key2": "value2"}
q2 = [("key1", "value1"), ("key2": "value2")]

urlencode(q1)  # key1=value1&key2=value2
urlencode(q2)  # key1=value1&key2=value2
```

`urlencode`で、辞書型／リスト型になっているクエリを文字列に変換できます。
`parse_qs` / `parse_qsl`で取得したオブジェクトも復元できます。
