# 見出ししたい（`#heading`）

```typst
= 見出し1
== 見出し2
=== 見出し3
==== 見出し4
```

Typst記法では`=`で見出しレベルを指定できます。

:::{seealso}

Markdown記法では`#`に相当します。

:::

```typst
// #heading(level, numbering, outlined)[content]
#heading[見出し1]  // デフォルトは(level: 1)
#heading(level: 2)[見出し2]
#heading(level: 3)[見出し3]
#heading(level: 4)[見出し4]  // 見出し4以降は見た目が同じ
```

[heading要素](https://typst.app/docs/reference/model/heading/)を使うと、見出しをより細かく設定できます。

:::{seealso}

- [](../latex/latex-section.md)

:::

## レベルを変更したい（`level`）

```typst
#heading(level: 2)[見出し2]
```

`level`オプションで、見出しレベルを変更できます。

## レベル表示を変更したい（`numbering`）

```typst
#set heading(numbering: "1.")
#set heading(numbering: "【1.1.1】")
```

`numbering`オプションで、見出しレベルの表示方法を変更できます。

## 見出しを非表示にしたい（`outlined`）

```text
#heading(outlined: false)[隠したい見出し]
```

`outlined`オプションで、見出しを目次に追加するかどうかを変更できます。
`outlined: false`で非表示にできます。

:::{seealso}

LaTeXの`\section*`に相当します。

:::

## 背景色したい

```typst
// 基本設定
#set heading(numbering: "1.")

// 全体設定
#show heading: set block(spacing: 1em)

// 個別設定
#show heading.where(level: 1): block.with(fill: luma(150), inset: 12pt)
#show heading.where(level: 2): block.with(fill: luma(100), inset: 12pt)
#show heading.where(level: 3): block.with(fill: luma(50), inset: 12pt)
```

見出しに背景色を追加して、視覚的に分かりやすくしてみます。
まず、`#set heading(..options)`で基本設定をします。
その後、`#show heading`で見出しレベルごとに個別設定します。

:::{note}

```typst
#show heading: set block(spacing: 1em)
```

見出しをカスタマイズする際は、[ブロック要素](./typst-block.md)にしておくとよいです。

:::

:::{seealso}

- [](./typst-show.md)

:::
