# 全体スタイルを変更したい（`#set`）

```typst
#set page(
  paper: "presentation-16-9",
  margin: 10mm,
)

#set text(
  lang: "ja",
  font: ("Noto Sans CJK JP"),
)
```

`#set`ルールを使って、文書全体のスタイルを変更できます。
この設定は、ファイルの先頭に一度だけ設定するのが一般的です。

## フォント設定したい（`text`）

```typst
#set text(
  lang: "ja",
  size: 11pt,
  font: "Noto Sans CJK JP",
  line-spacing: 1.5,
  color: navy
)
```

`text`要素の設定で、本文のフォントや行間などを変更できます。

:::{seealso}

- [](./typst-text.md)

:::

## ページ設定したい（`page`）

```typst
#set page(
  paper: "a4"
  margin: (x: 2cm, y:3cm),
  header: rect[inset: 4pt][ヘッダー],
  footer: rect[inset: 4pt][フッター],
  number-align: center,
  numbering: "1 of 1",
  columns: 2
)
```

`page`キーの設定で、サイズや余白、ヘッダー／フッターなどを変更できます。

:::{note}

- [](./typst-page.md)

:::

## 段落したい（`par`）

```typst
#set par(
  justify: true,
  leading: 0.5cm
)
```

`par`キーで、段落の整形や字下げなどを変更できます。

:::{seealso}

- [](./typst-par.md)

:::

## 見出ししたい（`heading`）

```typst
#set heading(
  numbering: "I. ",
)
```

`heading`キーで見出しのスタイルを変更できます。

:::{seealso}

- [](./typst-heading.md)

:::

## 箇条書きしたい（`list`）

```typst
#set list(
  marker: "→",
  indent: 1.5em
)
```

`list`キーの設定で、箇条書きのスタイルを変更できます。

:::{seealso}

- [](./typst-list.md)
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

## 画像したい（`figure`）

```typst
#set figure(
    align: center,
    caption: above
)
```

`figure`キーで、図の配置やキャプションの位置などを変更できます。

## メタデータしたい（`document`）

```typst
#set document(
  title: "レポートのタイトル",
  author: ("著者1", "著者2"),
  date: datetime(year: 2025, month: 7, day: 13)
)
```

`document`キーで、ドキュメントのPDFに埋め込むメタデータを設定できます。

:::{seealso}

- [](./typst-document.md)

:::
