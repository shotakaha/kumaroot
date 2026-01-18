# 図版したい（`#figure`）

```typst
#figure(
  image("image.jpg", width: 80%),
  caption: [図版のキャプション],
) <label>

〇〇については @label を参照してください。
```

`#figure`要素で図版を挿入できます。
第一引数に挿入したい図版コンテンツを指定します。
画像ファイルを指定する場合は`#image`要素を使います。

コンテンツブロックを指定できるので、`#rect`などの図形も挿入できます。
また、表（`#table`）やコードブロック（`#raw`）なども指定できます。

:::{note}

ラベル機能で`<図ラベル>`を設定できます。
設定した図ラベルは`@図ラベル`で
本文中で参照できます。

:::

## キャプションしたい（`#figure.caption`）

```typst
#figure(
  [コンテンツ],
  caption: [キャプション],
)
```

`caption`オプションで図版のキャプションを設定できます。

:::{note}

レポートや論文の場合、図版のキャプションは必須です。
このとき、単に図版のタイトルだけ記述するのではなく、本文を読まなくても、この図版が何を示しているのかわかるように説明するとよいです。

:::

```typst
#show figure.caption: it => {
  set align(left)
  it
}
```

キャプションはデフォルトで図版に対して中央寄せで表示されます。
左寄せにしたい場合は`show`ルールで変更します。

## 余白したい

```typst
// figure全体の設定
#set figure(gap: 0em)
#show figure: set block(
  inset: 0.5em,
  width: 100%,
  // stroke: 1tp,  // enable when debug
)

// figure.captionの設定
#show figure.caption: it => {
  block(
    inset: 0.5em,
    width: 100%
  )[
    #align(left)[
      #it
    ]
  ]
}

#figure(
  [content],
  caption: [...]
)
```

画像とキャプション周りの余白は`show`ルールで変更できます。
デフォルトだと、
画像と本文の間、
画像とキャプションの間の間隔が窮屈に感じたので、微調整したサンプルです。
最適な値は各自で探してください。

:::{note}

まず、図版とキャプションのアキをリセット（`gap: 0em`に設定）したあと、
コンテンツとキャプションそれぞれに`0.5em`のパディングを追加しています。

結果として、
図版とキャプションの間に`1em`のアキができます。

`stroke: 1pt`を有効にすると
それぞれの表示エリアを確認できます。

:::

## 図版を並べたい

```typst
#columns(2)[
  #figure(
    [content],
    caption: [左図のキャプションです。],
  )<fig-left>

  #colbreak()

  #figure(
    [content],
    caption: [右図のキャプションです。],
  )<fig-right>
]
```

図版を横に並べたい場合は
`#columns`関数で段組みしたところに、`#figure`を挿入します。

```typst
#figure(
  [#columns(2)[
    [左図]
    #colbreak()
    [右図]
  ]],
  caption: [2つの図を説明する1つのキャプションです。]
)<fig-label>
```

複数の図版を横にならべて、キャプションを1つにまとめたい場合は、
`#figure`の第一引数であるコンテンツブロックの中を`#columns`で段組みして
図版コンテンツ（`#image`など）を挿入します。

:::{note}

LaTeXで横並びの図を作成する場合、
[minipage](../latex/latex-minipage.md)のような外部パッケージが必要でした。

Typstでは標準機能だけで簡単に作ることができました。
角括弧が多くなり読みづらくなるのはさておき、
コンテンツブロック（`[...]`）の柔軟さと使い勝手のよさが、ようやくわかってきた気がします。

:::

## リファレンス

- [figure - Typst](https://typst.app/docs/reference/model/figure/)
