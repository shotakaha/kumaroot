# スタイルを変更したい（`#set`）

```typst
#set スタイルキー(オプション: 値, ...)

#set text(font: "Noto Sans CJK JP")
#set page(margin: 2.5cm)
```

`#set`コマンドを使って、Typstドキュメント全体のスタイルを変更できます。
それぞれのカテゴリに分かれたスタイルキーに対して、
オプションと値のペアを与えて設定します。
この設定は、ファイルの先頭に一度だけ設定するのが一般的です。

## 本文したい（`text`）

```typst
#set text(
    size: 11pt,
    font: "Noto Sans CJK JP",
    line-spacing: 1.5,
    color: navy
)
```

`text`キーの設定で、本文のフォントや行間などを変更できます。

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

## 段落したい（`par`）

```typst
#set par(
    justify: true,
    leading: 0.5cm
)
```

`par`キーで、段落の整形や字下げなどを変更できます。

## 見出ししたい（`heading`）

```typst
#set heading(
    numbering: "I. ",
    font: "Noto Serif",
)
```

`heading`キーで見出しのスタイルを変更できます。

## 箇条書きしたい（`list`）

```typst
#set list(
    marker: "→",
    indent: 1.5em
)
```

`list`キーの設定で、箇条書きのスタイルを変更できます。

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

## 数式モードしたい（`math`）

```typst
#set math(
    font: "Cambria Math",
    size: 12pt
)
```

`math`キーの設定で、数式フォントなどを変更できます。

## メタデータしたい（`document`）

```typst
#set document(
    title: "レポートのタイトル",
    author: ["著者1", "著者2],
    date: "2025-07-13"
)
```

`document`キーで、ドキュメントのPDFに埋め込むメタデータを設定できます。
