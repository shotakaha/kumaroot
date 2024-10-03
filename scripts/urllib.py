# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,mystmd//md:myst,scripts//py:light
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

# # URL操作したい
#
# - `URL`の構成要素
#   - `scheme://netloc/path;parameters?query#fragment`

TEST_URL = (
    "https://example.com/path1/path2/path3.html?key1=value1&key2=value2#fragment1"
)

# # urlparse
#
# - `urlparse`でURLをパースできる
# - `urlparse` -> `ParseResult`が返ってくる
# - `ParseResult`はnamed tupleみたいなオブジェクト
# - URLにアクセスせずにURLを操作できる

# +
from urllib.parse import urlparse

p = urlparse(url=TEST_URL)
print(f"{p=}")
print(f"{p.scheme=}")
print(f"{p.netloc=}")
print(f"{p.path=}")
print(f"{p.params=}")
print(f"{p.query=}")
print(f"{p.fragment=}")
# -

# `allow_fragments=False`にすると、フラグメントはクエリに含まれる

p = urlparse(url=TEST_URL, allow_fragments=False)
# print(f"{p=}")
print(f"{p.query=}")
print(f"{p.fragment=}")

# # urlsplit
#
# - `urlsplit`でURLを分割できる
# - `urlsplit` -> `SplitResult`オブジェクト
# - `SplitResult`も named tuple みたいなオブジェクト

# +
from urllib.parse import urlsplit

s = urlsplit(url=TEST_URL)
print(f"{s=}")
print(f"{s.scheme=}")
print(f"{s.netloc=}")
print(f"{s.path=}")
print(f"{s.query=}")
print(f"{s.fragment=}")
# -

# # urldefrag
#
# - `urldefrag`でフラグメントを抽出できる
# - `urldefrag` -> `DefragResult`オブジェクト
# - `DefragResult`もnamed tupleみたいなオブジェクト
# - フラグメントを抽出するだけなので、あまり使い所がわからない

# +
from urllib.parse import urldefrag

d = urldefrag(url=TEST_URL)
print(f"{d=}")
# -

# # parse_qs
#
# - `parse_qs`でクエリを辞書型に変換できる
# - `parse_qsl`でクエリをリスト型に変換できる

# +
from urllib.parse import parse_qs, parse_qsl

p = urlparse(url=TEST_URL)
s = urlsplit(url=TEST_URL)
# -

parse_qs(p.query)

parse_qs(s.query)

parse_qsl(p.query)

# # urlencode

# - `urlencode`で辞書型／リスト型のクエリを文字列に戻すことができる

# +
from urllib.parse import urlencode

q = {"key1": "value1", "key2": "value2", "key3": "value3"}

urlencode(query=q)

# +
from urllib.parse import urlencode

q = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]

urlencode(query=q)
# -

# `parse_qs` / `parse_qsl`したオブジェクトを復元できる

q = parse_qs(p.query)
print(f"{q=}")
urlencode(q, doseq=True)

q = parse_qsl(p.query)
print(f"{q=}")
urlencode(q, doseq=True)

# # Requestsを組み合わせる
#
# - `parse_qs` / `parse_qsl`で得られたオブジェクトは、`requests.get`の`params`オプションにそのまま渡すことができる

# +
import requests

response = requests.get(url="https://httpbin.org/get", params=parse_qs(s.query))
response.url
# -

response = requests.get(url="https://httpbin.org/get", params=parse_qsl(s.query))
response.url
