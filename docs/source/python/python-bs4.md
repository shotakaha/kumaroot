# BeautifulSoup

```python
from bs4 import BeautifulSoup
```

## ウェブページをスクレイプしたい

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com/"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
```

ウェブページの取得は[requests](python-requests.md)を使います。
その内容をパース（＝スクレイプ）するために``BeautifulSoup``を使います。

## タグを取得したい

```python
tag = soup.タグ名
tag = soup.find("タグ名")
tags = soup.find_all("タグ名")
```

``soup.タグ名``や``soup.find("タグ名")``だと、最初のタグを拾うことができます。
すべてのタグを拾いたい場合は``soup.find_all("タグ名")``を使います。
返り値は``bs4.element.ResultSet``型のオブジェクトですが、リストのように扱うことができます。

## バージョンを確認したい

```python
import bs4
bs4.__version__
```
