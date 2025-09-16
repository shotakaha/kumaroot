# 見出ししたい（`#heading`）

```typst
// #heading(level, numbering, outlined)[content]
#heading[見出し1]  // デフォルトは(level: 1)
#heading(level: 2)[見出し2]
#heading(level: 3)[見出し3]
#heading(level: 4)[見出し4]  // 見出し4以降は見た目が同じ
```

[heading要素](https://typst.app/docs/reference/model/heading/)
で見出しを表示できます。

```typst
// Typst記法
= 見出し1
== 見出し2
=== 見出し3
==== 見出し4
```

Typst記法では`=`を使います。

:::{note}

Markdown記法では`#`です。

:::

:::{seealso}

- [](../latex/latex-section.md)

:::

## レベル表示を変更したい（`numbering`）

```typst
#set heading(numbering: "1.")
#set heading(numbering: "【1.1.1】")
```

[heading要素のnumberingオプション](https://typst.app/docs/reference/model/heading/)で、見出しの番号表示をカスタマイズできます。

`numbering`オプションで、レベル表示を変更できます。

## 見出しを非表示にしたい（`outlined`）

```text
#heading(outlined: false)[隠したい見出し]
```

`outlined: false`オプションで、見出しを目次から非表示にできます。
LaTeXの``\section*``に相当します。

## 見出しをカスタマイズしたい

```typst
// 基本設定
#set heading(numbering: "1.")

// 全体設定
#show heading: set block(spacing: 2em)

// 個別設定
#show heading.where(level: 1): block.with(fill: luma(150), inset: 12pt)
#show heading.where(level: 2): block.with(fill: luma(100), inset: 12pt)
#show heading.where(level: 3): block.with(fill: luma(50), inset: 12pt)
```

`#set heading(..options)`で基本設定をします。
その後、`#show heading`で個別設定できます。

:::{seealso}

`#show`ルールの詳細はこちらを参照してください。

- [](./typst-show.md)

:::
