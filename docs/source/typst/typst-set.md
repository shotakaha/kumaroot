# setしたい（`#set`）

```typst
// ページ全体の設定
#set page(
  paper: "presentation-16-9",
  margin: 10mm,
  numbering: "1 / 1",
)

// 本文の設定
#set text(
  lang: "ja",
  font: ("Noto Sans CJK JP"),
)

// 段落の設定
#set par(
  justify: true,
  leading: 0.5cm,
)

// 見出しの設定
#set heading(
  numbering: "1. ",
)

// 箇条書きの設定
#set list(
  marker: "→",
  indent: 1.5em,
)

#set document(
  title: "レポートのタイトル",
  author: ("著者1", "著者2"),
  date: datetime(year: 2025, month: 7, day: 13)
)
```

`#set`ルールで、関数や要素の設定を変更できます。
変更の影響範囲はスコープに依存します。
`#set`した場所から、同じスコープ内のすべての関数や要素に影響を与えます。

スコープは、関数の引数や`#let`ルールのブロック、`#show`ルールのブロックなどで区切られます。
スコープの外側にある関数や要素には影響を与えません。

:::{seealso}

- [](./typst-page.md)
- [](./typst-text.md)
- [](./typst-par.md)
- [](./typst-heading.md)
- [](./typst-list.md)
- [](./typst-quote.md)
- [](./typst-note.md)
- [](./typst-table.md)
- [](./typst-document.md)

:::

## 引用したい（`quote`）

```typst
#set quote(
    border: none,
    fill: lightgray
)
```

`quote`キーで、引用ブロックのレイアウトや装飾を変更できます。

## 脚注したい（`note`）

```typst
#set note(
    size: 8pt,
    color: gray
)
```

`note`キーで、脚注を変更できます。

## 表したい（`table`）

```typst
#set table(
    stroke: lightgray,
    spacing: (x: 0.5em, y: 0.2em)
)

#set table.cell(
    align: center,
    stroke: none
)
```

`table`キーで表全体の枠線、罫線、余白などを変更できます。
`table.cell`キーでセルの設定を変更できます。
