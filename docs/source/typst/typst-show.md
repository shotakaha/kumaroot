# showしたい（`#show`）

```typst
// シグネチャ
#show TARGET: RULES

// 文字列の置換
#show "文字列": "置換文字列"

// スタイル変更
#show SELECTOR: set ELEMENT(..options)

// 自由変形
#show SELECTOR: it => {...}[#it]
```

`#show`ルールで、要素の表示方法をカスタマイズできます。
文字列の置換から完全なカスタマイズまで、幅広い表現が可能です。

:::{note}

`show`ルールの本質は「指定した要素を**変換する**」操作です。

:::

## 文字列を置換したい

```typst
#show "TY": "Typst"
```

`#show "文字列": "置換文字列"`の形で、特定の文字列を別の文字列に置換できます。
上記サンプルでは、`TY`という文字列を`Typst`に置換しています。

```typst
#show "pi0": $pi^(0)$
#show "pi+": $pi^(+)$
#show "pi-": $pi^(-)$
```

文字列を数式に置換することもできます。
上記サンプルではπ中間子の記号を数式に置換しています。

## スタイルを変更したい（`#show 要素: set 装飾`）

```typst
#show heading: set block(
  above: 1em,
  below: 1em,
  // fill: luma(20%),
)
```

`#show 要素: set 装飾`の形で、要素のスタイルを変更できます。
Typstではスタイルを追加・変更するための基本的な形式です。

上記のサンプルでは、すべての見出しを対象に、上と下にスペースを追加しています。
具体的には、`heading`要素を`block`要素に変換して「スタイル」を追加しています。
`heading`要素の構造自体には変更を加えていないため、見出しのレベルや文字列などはそのまま保持されます。

```typst
#show heading: set text(size: 1.5em, weight: "bold")
#show heading: set block(
  above: 1em,
  below: 1em,
)
```

指定した要素の構造を変更しないため、複数回`#show`ルールを定義して、装飾を重ね書きすることもできます。

## 自由変形したい（`#show 要素: it => {...}[#it]`）

```typst
// 見出しを太字にする
#show heading: set text(weight: "bold")
#show heading: set block(
  width: 100%,
  above: 1em,
  below: 1em,
)

// クロージャ形式
#show heading: it => {
  block(
    above: 1em,
    below: 1em,
  )[
    #text(weight: "bold")[
      #it
    ]
  ]
}
```

`#show 要素: it => {装飾}[#it]`の形で、
要素の構造全体を書き換えることができます。
この形式は、指定した要素に適用する変換関数を定義するイメージです。
変換関数の中で、複数の装飾やラップ処理を組み合わせることができいます。
`it`を元にした新しい構造が生成されます。

:::{caution}

`#show 要素: set 装飾`の形で書かれたルールは、ユーザーが後から上書きできます。
一方で、`#show 要素: it => {装飾}[#it]`の形は、ユーザーが上書きできません。

:::

:::{hint}

`it => {装飾}[#it]`の`it`は、指定した要素を指す変数です。
`#show link: it => {...}`の例ではれば、`it` = `link`を指しています。
そのため`link`オブジェクトが持つプロパティにアクセスできます。

Typstにおける`it`は「それ（it）」を指す変数で特別な意味はありません。
`body`や`content`など、利用シーンに応じてわかりやすい名前をつけることもできます。

:::

:::{seealso}

- [](./typst-set.md)
- [](./typst-heading.md)
- [](./typst-raw.md)
- [](./typst-figure.md)

:::


:::{seealso}

- [](../latex/latex-newcommand.md)

:::

## ページの設定

```typst
#set page(
  paper: "a4",  // 用紙サイズ
  fill: white,  //  背景色
)
```

## テキストの設定

```typst
#set text(
  font: "Noto Serif CJK JP",  // フォント
  lang: "ja",  // 言語
  size: 12pt,
  fill: rgb(0, 0, 0),  // 文字色
)
```

## 段落の設定

```typst
#set par(
  justify: true,   // 両端揃え
  leading: 1.5em,  // 行間
  spacing: 0.5em,  // 段落間
)
```

## 見出しの設定

```typst
#show heading: set text(
  font: "Noto Serif CJK JP",
  weight: "bold",
)

#show heading: set block(
  above: 1em,
  below: 1em,
)
```

## 目次の設定

```typst
#set outline(indent: 1em)
#show outline.entry: set block(
  spacing: 1em,
)
```

## リストの設定

```typst
#set list(
  spacing: 1em,
  indent: 1em,
  body-indent: 0.5em,
  // marker: ([•], [‣], [–]),
)
```

```typst
#set enum(
  spacing: 1em,
  indent: 1em,
  body-indent: 0.5em,
  // numbering: "1. ",
)
```

```typst
#set term(
  spacing: 1em,
  indent: 1em,
  body-indent: 0.5em,
  // separator: ": ",
)
```

## 数式の設定

```typst
#show math.equation: set text(
  font: "Fira Math",
)
```

## 表の設定

```typst
#set table(
  stroke: (x, y) => {
    let thick: 2pt
    let thin: 0.5pt
    (
      top: if y == 0 or y == 1 { thick } else { thin },
      bottom: thick,
      left: none,
      right: none,
    )
  },
  inset: 1em,
)

#show table.header: set text(
  weight: bold,
)
```

## コードブロックの設定

```typst
#show raw: set text(
  font: "Fira Code",
)

#show raw.where(block: true): set block(
  width: 100%,
  fill: luma(95%),
  inset: 1em,
  radius: 1em,
  stroke: luma(50%) + 0.5pt,
)

#show raw.where(block: false): set text(
  fill: olive,
)
```

## 図版の設定

```typst
#show figure: set block(
  width: 100%,
  above: 1em,
  below: 1em,
)

#show figure.caption: set text(
  fill: luma(50%),
)
```

## インライン要素の設定

```typst
#show strong: set text(
  fill: red,
)
```

```typst
#show emph: set text(
  fill: red,
)
```

```typst
#show highlight: set text(
  fill: yellow,
)
```

## リンクの設定

```typst
#show link: set text(
  fill: blue,
)
```

## 脚注の設定

```typst
#show footnote.entry: set text(
    size: 0.8em,
    fill: luma(50%),
)
```

## 引用文献の設定

```typst
#show bibliography.entry: set text(
  size: 0.8em,
  fill: luma(50%),
)
```

```typst
#show cite: set text(
  size: 0.8em,
  fill: luma(50%),
)
```

## 引用の設定

```typst
#show quote: set block(
  width: 100%,
  above: 1em,
  below: 1em,
  fill: luma(95%),
  inset: 1em,
  stroke: luma(50%) + 0.5pt,
)
```
