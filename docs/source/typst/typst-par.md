# 段落したい（``#par``）

```typst
// ページ全体で設定
#set par(
  leading: 0.65em,
  spacing: 1.2em,
  justify: false,
  linebreaks: auto,
  first-line-indent: (amount: 0pt, all: false),
  hanging-indent: 0pt,
)
```

[par要素](https://typst.app/docs/reference/model/par/)で段落の設定ができます。
行間の大きさや、両端揃えの設定ができます。

```typst
// 個別設定
#par(leading: 1em)[
  行間を広くしたい段落
]

#par(justify: true)[
  両端揃えにしたい段落
]
```

`#par`を直接呼び出して、本文中で段落ごとに設定することもできます。

:::{seealso}

- [](../latex/latex-linebreak.md)
- [](../latex/latex-geometry.md)

:::

## 行間したい（`leading`）

```typst
#par(leading: 0.65em)  // デフォルト

// 全体設定
#set par(leading: 1em)

// 個別設定
#par(leading: 1em)
```

`leading`オプションで行間を変更できます。
デフォルトは`0.65em`です。
和文ドキュメントだと少し窮屈に感じるので、少し広げて使うとよいと思います。

## 両端揃えしたい（`justify`）

```typst
#par(justify: false)  // デフォルト

// 全体設定
#set par(justify: true)

// 個別設定
#par(justify: true)
```

`justify`オプションで両端揃えに変更できます。
デフォルトは`false`で、左揃えになっています。
和文ドキュメントは有効にしておいて問題ないと思います。

## インデントしたい（`first-line-indent`）

```typst
#par(first-line-indent: 0pt)    // デフォルト

// 全体設定
#set par(first-line-indent: 1em)

// 個別設定
#par(first-line-indent: 1em)
```

`first-line-indent`で段落の最初の行にインデントを設定できます。
デフォルトは`0pt`です。
和文では、段落の最初の行を1文字下げるのが一般的です。
フォントサイズの相対比で指定できる`1em`を設定するとよいです。

:::{note}

紙面では1字下げますが、ウェブ媒体では下げないことも多いです。

:::

## ぶらさげインデントしたい（``hanging-indent``）

```typst
#par(hanging-indent: 0pt)    // デフォルト

// 全体設定
#set par(hanging-indent: 1em)

// 個別設定
#par(hanging-indent: 1em)
```

`hangint-indent`オプションで、段落にぶら下げインデントを設定できます。
デフォルトは`0pt`です。

:::{note}

ぶら下げインデントを使うべきときは、よく分かっていません。

:::
