# 図表したい（`#figure`）

```typst
#figure(
  image("image.jpg", width: 80%),
  caption: [図のキャプション],
) <label>

〇〇については @label を参照してください。
```

`#figure`要素で図表を挿入できます。
第一引数に挿入したい図表コンテンツを指定します。
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

`caption`オプションで図表のキャプションを設定できます。

:::{note}

レポートや論文の場合、図表のキャプションは必須です。
このとき、単に図のタイトルだけ記述するのではなく、本文を読まなくても、この図が何を示しているのかわかるように説明するとよいです。

:::

```typst
#show figure.caption: it => {
  set align(left)
  it.body
}
```

キャプションはデフォルトで図に対して中央寄せで表示されます。
`show`ルールで左寄せに変更できます。

## 余白したい

```typst
// figure全体の設定
#show figure: set block(spacing: 2em, width: 90%)

// figure.captionの設定
#show figure.caption: it => {
  block(inset: 1em)[
    #set align(left)
    #it.body
  ]
}

#figure(
  [content],
  gap: 0em,
  caption: [...]
)
```

画像とキャプション周りの余白は`show`ルールで変更できます。
デフォルトだと、
画像と本文の間、
画像とキャプションの間の間隔が窮屈に感じたので、微調整したサンプルです。
最適な値は各自で探してください。

:::{note}

キャプションに`1em`のパディングを追加したので、画像とキャプション間の間隔（`#figure.gap`）は`0em`に変更しています。

:::

:::{caution}

このように`#figure.caption`を変更すると、キャプションの先頭の「図番号」が表示されない点は注意してください。

ちょっと確認したところ、
「図」という文字列は`#it.supplement`で取得できました。
`#it.numbering`で図番号を取得できるかと思ったのですが、すべて「`1`」になってしまって、お手上げ状態です。

:::

## 画像を並べたい

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

画像を横に並べる場合は`#columns`関数でN段組にしたところに、`#figure`を設定すればOKです。

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

複数の図に対して、キャプションを1つにまとめたい場合は、`#figure`の第一引数であるコンテンツブロックの中を`#columns`で段組にして画像コンテンツ（`#image`など）を配置すればOKです。

:::{note}

LaTeXで横並びの図を作成する場合、
[minipage](../latex/latex-minipage.md)のような外部パッケージが必要でした。

Typstでは標準だだだけで簡単に作ることができました。
角括弧が多くなり読みづらくなるのはさておき、
コンテンツブロック（`[...]`）の柔軟さと使い勝手のよさが、ようやくわかってきた気がします。

:::

## リファレンス

- [figure - Typst](https://typst.app/docs/reference/model/figure/)
