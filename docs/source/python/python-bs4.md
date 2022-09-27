# BeautifulSoup

```bash
$ pip3 install beautifulsoup4
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

## タグで検索したい

```python
tag = soup.タグ名
tag = soup.find("タグ名")
tag = soup.select_one("タグ名")
tags = soup.find_all("タグ名")
tags = soup.select("タグ名")
```

``soup.タグ名``や``soup.find("タグ名")``だと、最初のタグを拾うことができます。
すべてのタグを拾いたい場合は``soup.find_all("タグ名")``を使います。
返り値は``bs4.element.ResultSet``型のオブジェクトですが、リストのように扱うことができます。

## 属性で検索したい

```python
tag = soup.find("タグ名", "属性と値")
tags = soup.select("タグ名[属性と値]")
tag = soup.find("a", href="検索したいURL")
```

## クラス名で検索したい

```python
tag = soup.find("タグ名", class_="クラス名")
tags = soup.select("CSSセレクタ")
```

## タイトルを取得したい

```python
soup.title       # "<title>記事のタイトル</title>"
soup.title.text  # "記事のタイトル"
soup.title.name  # "title" = タグ名
```

## リンクのURLを取得したい

```python
soup.a.get("href")
soup.find("a").get("href")
[tag.get("href") for tag in soup.find_all("a")]
```

``<a href="URL" class="...">``のような``a``タグの属性値``href``を拾うことができます。
複数の``a``タグのURLを拾いたい場合は、リスト内包表記を使います。

## バージョンを確認したい

```python
import bs4
bs4.__version__
```

## リファレンス

- [BeautifulSoup4 Documentation](https://www.crummy.com/software/BeautifulSoup/)
