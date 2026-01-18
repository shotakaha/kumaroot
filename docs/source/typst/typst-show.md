# 要素のスタイルを変更したい（`#show`）

```typst
// ハイパーリンクの文字を太字に変更
#show link: set text(weight: "bold")
// ハイパーリンクに下線を追加
#show link: it => {
  underline[#it]
}
```

`#show`ルールで、さまざまな要素の表示方法を自由にカスタマイズできます。
同じ要素に対して、何度も使うことができます。

## 見出ししたい（`#show heading.where`）

```typst
// 見出し番号の表示設定
#set heading(
  numbering: "1.1."
)
// すべての見出しに背景色を追加
#show heading: it => {
  block(
    fill: luma(90%),
    width: 100%,
    inset: 1em
  )[
    #it
  ]
}
// 見出しレベルごとにフォントサイズを変更
// #show heading.where(level: 見出しレベル): set 要素(オプション)
#show heading.where(level: 1): set text(size: 42pt, weight: "bold")
#show heading.where(level: 2): set text(size: 32pt, weight: "semibold")
#show heading.where(level: 3): set text(size: 22pt, weight: "semibold")
```

見出しのテキストを変更するサンプルです。
`heading.where`で変更したい見出しのレベルを指定します。
続けて`set text`でテキスト要素のオプションを指定します。

```typst
#show heading.where(level: 1): it => block.with(fill: luma(150), inset:12pt)[#it]

// #show heading.where(level: 見出しレベル): it => (装飾)[#it.body]
#show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(2em)
    set text(size: 22pt, weight: bold)
    block[#it.body]
    v(1em)
}
```

より複雑な設定のサンプルです。
`it => {ブロック}`関数を使うことで、複数の要素を指定できます。
見出しテキストは`[#it.body]`で取得できます。

:::{seealso}

- [](./typst-heading.md)

:::

## コードブロックを装飾したい

```typst
// テーマ設定
#set raw(theme: "github.Themes")

// テーマを使用せずフォントだけ変更したい場合
// #show raw: set text(font: ("Roboto Mono", "Noto Sans CJK JP"))

// ブロック要素の装飾
#show raw.where(block: true): set block(
    fill: rgb("#f6f8fa"),    // 背景色
    inset: 10pt,              // 余白（パディング）
    radius: 4pt,              // 角丸
    width: 100%,              // 幅
)

// インライン要素の装飾
#show raw.where(block: false): set box(
    fill: rgb("#fff3cd"),    // ハイライト色
    inset: (x: 3pt, y: 1pt),   // 余白（パディング）
    outset: (y: 3pt),          // 余白（マージン）
    radius: 2pt,               // 角丸
)
```

コードブロック（`raw`要素）を変更するサンプルです。
`#set raw(theme: "テーマ名")`で表示スタイルを簡単に変更できます。
`#show raw.where(block: true or false)`でブロック要素とインライン要素を判別し、それぞれの表示方法を設定しています。

## 強調テキストを変更したい

```typst
#show strong: set text(fill: red, weight: "bold")
```

強調テキスト（`strong`要素）を変更するサンプルです。

## リスト表示を変更したい

```typst
#show list.item: set text(fill: blue)
```

リストのアイテム（`list.item`要素）を変更するサンプルです。

## 文字列を置換したい

```typst
#show "文字列": "置換文字列"

#show "pi0": $pi^(0)$
#show "pi+": $pi^(+)$
#show "pi-": $pi^(-)$
```

Typstは文字列が簡単に置換できます。
上記サンプルではπ中間子の文字列を数式に置換しています。

:::{seealso}

- [](../latex/latex-newcommand.md)

:::

## 図版したい（`figure` / `figure.caption`）

```typst
#set figure(gap: 0em)
#show figure: set block(
  inset: 0.5em,
  width: 100%,
  // stroke: 1pt,  // enable when debug
)
#show figure.caption: it => {
  block(
    inset: 0.5em,
    width: 100%,
  )[
    #align(left)[
      #it
    ]
  ]
}
```

:::{seealso}

- [](./typst-figure.md)

:::

## 実践的な使い方

```typst
// setでベーススタイルを設定
#set text(font: "フォント名", size: "サイズ")
#set par(justify: true)
#set page(margin: 2.5cm)

// showで特定要素をカスタマイズ
#show heading: set block(..options)
#show heading.where(level: 1): set block(..options)
#show raw: it=> set text(..options)
#show raw.where(block: true): set block(..options)
#show raw.where(block: false): set box(..options)
```

ドキュメント全体に関する基本設定は`#set`で設定し、
個別要素は`#show`で変更するのが推奨されています。
