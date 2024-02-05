# 文字色したい（``#text(fill: 色)``）

```typst
#text(fill: gray)[灰色]のテキスト
#text(red)[赤色]のテキスト
```

[#textのfill要素](https://typst.app/docs/reference/text/text/)で文字色を設定できます。
色名（色クラス）であることを自動で判断してくれるのか``fill: ``は省略できます。

## 全体設定したい

```typst
#set text(gray)

本文の色が灰色になります。
黒より読みやすい気がします。
```

``#set``ルールを使って、ドキュメント全体の地の文の文字色を一括設定できます。

## 部分的に変更したい

```typst
#set strong: text(red)

強調したい単語を#strong[強調は赤色]で表示します。
```

``#set コマンド名``ルールで部分的に文字色を変更できます。

## 数値の色を変更したい

```typst
#set regex("\d"): text(blue)
```

``#set regex``で正規表現を使って、色を変更する箇所を指定できます。
上記サンプルでは数字を青色に変更しています。

:::{seealso}

- [](../latex/latex-usepackage-xcolor.md)

:::
