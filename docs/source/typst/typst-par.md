# 段落したい（``#par``）

```typst
#par(オプション)[コンテキスト]
```

```typst
#set par(
    leading: 0.65em,
    justify: false,
    linebreaks: auto,
    first-line-indent: 0pt,
    hanging-indent: 0pt,
)
```

[par要素](https://typst.app/docs/reference/model/par/)で段落の設定ができます。
行間の大きさや、両端揃えの設定ができます。

:::{seealso}

- [](../latex/latex-linebreak.md)
- [](../latex/latex-usepackage-geometry.md)

:::

## 行間したい（``leading``）

```typst
#set par(leading: 0.8em)
```

``leading``オプションで行間を変更できます。
デフォルトは``0.65em``ですが、和文ドキュメントだと少し窮屈に感じたため、少し広げて使っています。

## 両端揃えしたい（``justify``）

```typst
#set par(justify: true)
```

``justify``オプションで両端揃えに変更できます。
和文ドキュメントは有効にしておいて問題ないと思います。

## インデントしたい（``first-line-indent``）

```typst
#set par(first-line-indent: 1em)
```

`first-line-indent`で段落の最初の行にインデントを設定できます。
デフォルトは``0pt``です。
一文字分だけインデントを挿入したい場合は、フォントサイズに応じた長さである``1em``を設定すればよいです。

## ぶらさげインデントしたい（``hanging-indent``）

```typst
#set par(hanging-indent: 1em)
```

``hangint-indent``オプションで、段落にぶら下げインデントを設定できます。
デフォルトは``0pt``です。

:::{note}

ぶら下げインデントを使うべきときは、よく分かっていません。

:::
