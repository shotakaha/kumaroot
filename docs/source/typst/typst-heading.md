# 見出ししたい（``#heading``）

```typst
#set heading(numbering: "1.")
#show heading: set block(spacing: 2em)
```

``heading``関数で見出しを表示できます。
デフォルトだと上下のマージンが窮屈に感じたため、``spacing``オプションを変更しています。

```typst
= 見出し1
== 見出し2
=== 見出し3
==== 見出し4

#heading[見出し1]  // デフォルトは(level: 1)
#heading(level: 2)[見出し2]
#heading(level: 3)[見出し3]
#heading(level: 4)[見出し4]  // 見出し4以降は見た目が同じ
```

## 見出しを隠したい（``outlined``）

```text
#heading(outlined: false)[隠したい見出し]
```

``outlined``オプションを使って、目次から見出しを非表示にできます。
LaTeXの``\section*``に相当します。

## 見出しをカスタマイズしたい

```rust
#set heading(
    numbering: "【1.1.1】",
)

#show heading.where(level: 1): block.with(
  fill: luma(150),
  inset: 12pt,
)

#show heading.where(level: 2): block.with(
  fill: luma(100),
  inset: 12pt,
)

#show heading.where(level: 3): block.with(
  fill: luma(50),
  inset: 12pt,
)
```

[heading要素のnumberingオプション](https://typst.app/docs/reference/model/heading/)で、見出しの番号表示をカスタマイズできます。
また、``#showルール``を使って、見出しのレベルに応じて表示を変更できます。

:::{seealso}

- [](../latex/latex-section.md)

:::
