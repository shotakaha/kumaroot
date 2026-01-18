# 見出ししたい（`#heading`）

```typst
// 見出しレベルの表示設定
#set heading(
  numbering: "1.1.",
)

// 見出しに背景色を設定
#show heading: it => {
  block(
    fill: luma(90%),
    width: 100%,
    spacing: 1em,
  )[
    #it
  ]
}

// #heading(level, numbering, outlined)[content]
#heading[見出し1]  // デフォルトは(level: 1)
#heading(level: 2)[見出し2]
#heading(level: 3)[見出し3]
#heading(level: 4)[見出し4]  // 見出し4以降は見た目が同じ
```

[heading要素](https://typst.app/docs/reference/model/heading/)
で「見出し」をマークアップできます。

`numbering`オプションで見出し番号の表示設定、
`depth`オプションで、目次に含める見出しレベルを設定できます。
これらは`set`ルールで全体設定するとよいです。
また、表示方法は`show`ルールで変更できます。

`#heading`のオプションを使うと、
個別の見出しをより細かく設定できます。

:::{seealso}

- [](../latex/latex-section.md)

:::

## マークアップしたい（`=`）

```typst
= 見出し1
== 見出し2
=== 見出し3
==== 見出し4
```

見出しは`=`でマークアップできます。
`=`の数が見出しレベルに相当します。

:::{seealso}

Markdown記法では`#`に相当します。

:::

## レベルを変更したい（`level`）

```typst
#heading(level: 2)[見出し2]
```

`level`オプションで、見出しレベルを変更できます。

## 見出しを非表示にしたい（`outlined`）

```text
#heading(outlined: false)[隠したい見出し]
```

`outlined`オプションで、見出しを目次に追加するかどうかを変更できます。
`outlined: false`で非表示にできます。

:::{seealso}

`outlined: false`は
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

`#heading`には背景色を設定するオプションがありません。
そのため、`#show`ルールで変更します。

まず、`#show heading: set block(spacing: 1em)`で、すべての見出し要素をブロック要素に変換して、上下に`1em`のパディングを追加しています。

その後、`#show heading.where(level: ...)`で見出しレベルごとに個別設定しています。

:::{seealso}

- [](./typst-show.md)
- [](./typst-where.md)
- [](./typst-block.md)
- [](./typst-color.md)

:::
