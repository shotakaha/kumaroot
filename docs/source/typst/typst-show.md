# showしたい（`#show`）

```typst
// 見出しレベルのフォントサイズ
#let sizes = (1.5em, 1.4em, 1.3em, 1.2em, 1.1em, 1em,)
for (i, size) in sizes.enumerate() [
  #show heading.where(level: i + 1): set text(size: size)
]
#show heading: set text(
  font: ("Harano Aji Gothic", "Noto Sans CJK JP", "Yu Gothic Medium"),
  weight: "bold",
  fill: luma(20%),
)
#show heading: set block(
  above: 1em,
  below: 1em,
)
```

`#show`ルールで要素の表示方法をカスタマイズできます。

見た目を装飾する場合、`show 要素名: set 装飾`の形で適用するのが基本です。
上記のサンプルでは、
見出しレベルごとにフォントサイズを変更し、
テキスト装飾を設定し、
見出しの上下にスペースを追加しています。

```typst
#show heading: set block(above: 1em, below: 1em)
#show heading: set text(size: 1.5em, weight: "bold")
#show heading: set block(above: 2em, fill: luma(20%))
```

`#show`ルールは、複数回適用することもできます。
ルールは上から順番に重ね書きされます。
同じオプションを複数回指定した場合は、後から指定した方が優先されます。

:::{note}

`show`ルールは指定した要素を**変換する**操作です。
上記のサンプルでは
`heading.where(level: 1)` = `text`の変換に、
`heading` = `text` + `block`の組み合わせが追加されているイメージです。

:::

## クロージャーしたい（`#show ...: it => {...}`）

```typst
// ハイパーリンクの文字を太字に変更
#show link: set text(weight: "bold")

// ハイパーリンクに下線を追加
#show link: it => {
  underline[#it]
}
```

`#show 要素: it => {装飾}[#it]`の形で、要素をクロージャーして装飾することもできます。
要素の構造全体を書き換え、複数の装飾を組み合わせることができるのが特徴です。
こちらの形式は、毎回新しい関数を定義しているイメージです。

:::{caution}

`#show 要素: set 装飾`の形は（後勝ちなことを利用して）ユーザーが後から上書きできるのに対して、
`#show 要素: it => {装飾}[#it]`の形は、ユーザーが上書きできません。

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

## 文字列を置換したい

```typst
#show "文字列": "置換文字列"

#show "pi0": $pi^(0)$
#show "pi+": $pi^(+)$
#show "pi-": $pi^(-)$
```

`#show "文字列": "置換文字列"`の形で、特定の文字列を別の文字列に置換できます。
上記サンプルではπ中間子の文字列を数式に置換しています。

:::{note}

`#show`ルールの基本が**変換操作**であることが分かります。
文字列を置換して表示するように、要素を置き換えて表示しています。

:::

:::{seealso}

- [](../latex/latex-newcommand.md)

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
