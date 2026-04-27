# showしたい（`#show`）

```typst
#show heading: it => {
  block(
    fill: luma(90%),
    width: 100%,
    above: 1em,
    below: 1em,
  )[
    text(size: 24pt, weight: "bold")[
      #it
    ]
 ]
}
```

`#show`ルールで、要素の表示方法をカスタマイズできます。
上記のサンプルでは、すべての見出しを`block`要素に変換して、背景色と上下のスペースを追加し、テキスト要素のサイズとウェイトを変更しています。

```typst
// ハイパーリンクの文字を太字に変更
#show link: set text(weight: "bold")

// ハイパーリンクに下線を追加
#show link: it => {
  underline[#it]
}
```

`#show 要素: set 装飾`の形で、要素を装飾することもできます。
上記のサンプルでは、ハイパーリンク（`link`要素）を太字に変更したり、下線を追加したりしています。

:::{note}

`set`だけでも要素の装飾を変更できますが、
`it => {装飾}[#it]`の形だと、複数の要素を組み合わせることができます。
どちらも便利なので、使い分けてみるのがよいですが、
まずは
`#show 要素: it => {装飾}[#it]`の形の無名関数を使う方法をマスターすることをオススメします。

:::

:::{hint}

`it => {装飾}[#it]`の`it`は、変更したい要素を指す変数です。
`it`は「それ（it）」を指す変数で特別な意味はありません。
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
