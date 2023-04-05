# タイトルしたい（``html_title``）

```python
html_title = "ウェブサイトのタイトル"
```

HTMLドキュメントの``<title>``を設定できます。
この値は、それぞれのページ内の``<title>``タグにも追加され、サイドバーの上にも表示されます。
デフォルト値は ``{<project>} v{<revision>} document`` です。

## 短いタイトルしたい（``html_short_title``）

```python
html_title = "ウェブサイトの正式タイトル（長め）"
html_short_title = "ウェブサイトの省略タイトル（略称など）"
```

短いタイトルを追加できます。
定義されていない場合は``html_title``の値が使われます。

:::{note}

テーマによっては、サイドバー表示に反映されないかもしれません。
とりあえず[sphinx_book_theme](./sphinx-html-book.md)では表示されなかったので、調べたいと思っています。

:::
