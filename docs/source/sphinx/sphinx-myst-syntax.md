# ロールとディレクティブ

> {sub-ref}`today` | {sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read


``reST``記法で（よく）使うロールとディレクティブの
``MyST``記法での書き方についてメモしておきます。

## 目次（``toctree``）

````
```{toctree}
---
maxdepth: 2
---
ファイル名1
ファイル名2
```
````

## コードブロック（``code-block``）

````
```{code-block} python
---
linenos: true
---
コード
コード
コード
```
````

## リンクと参照

``reST``記法だといろいろなロールを使い分ける必要があるが、
``MyST``記法は、基本的にMarkdownのリンクを作成すればよいです。

```md
[外部サイトのタイトル](外部URL)
[ページのタイトル](内部のファイルへの相対パス)
```

- ``:doc:``、``:download:``、``:any:``などのロールは意識しなくても大丈夫です
- ``ページのタイトル``を空欄にすると、ページのタイトルが自動で表示される
