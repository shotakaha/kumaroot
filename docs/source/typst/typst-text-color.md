# 文字色したい（``#text(fill: 色)``）

```text
#text(fill: gray)[灰色]のテキスト
#text(red)[赤色]のテキスト
```

[#textのfill要素](https://typst.app/docs/reference/text/text/)で文字色を設定できます。
色名（色クラス）であることを自動で判断してくれるためか、``fill: ``は省略できます。

全体の文字色や変更したい場合は、ファイルの最初の方で``#setルール``しておきます。

```text
#set text(gray)

本文の色が灰色になります。
黒より読みやすい気がします。
```

見出しや強調表示の色も変更できます。

```text
#set heading: text(navy)
#set strong: text(red)

= 紺色の見出し

強調したい単語は#strong[強調は赤色]で表示します。
```

正規表現を使って、色を変更する箇所を指定できます。
数字を青色にしたい場合は次のように書きます。

```text
#set regex("\d"): text(blue)
```

:::{seealso}

- [](../latex/latex-usepackage-xcolor.md)

:::
