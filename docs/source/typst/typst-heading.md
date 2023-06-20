# 見出ししたい（``#heading``）

```text
= 見出し1
== 見出し2
=== [見出し3]
```

``=``を使って見出しをマークアップします。
上記は、次の``#heading``関数に相当します。

```text
#heading[見出し1]  // デフォルトは(level: 1)
#heading(level: 2)[見出し2]
#heading(level: 3)[見出し3]
#heading(level: 4)[見出し4]  // 見出し4以降は見た目が同じ
```

## 見出しを隠したい

```text
#heading(outlined: false)[隠したい見出し]
```

``outlined: false``にした見出しは目次（``#outline()``）から隠すことができます。
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

[heading要素のnumberingオプション](https://typst.app/docs/reference/meta/heading/)で、見出しの番号表示をカスタマイズできます。
また、``#showルール``を使って、見出しのレベルに応じて表示を変更できます。

:::{seealso}

- [](../latex/latex-section.md)

:::
