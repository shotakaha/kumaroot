# 図版したい（`#figure` / `#figure.caption`）

```typst
#figure(
  image("image.jpg", width: 80%),
  caption: [図版のキャプション],
)
```

`#figure`要素で図版を挿入できます。
第一引数に挿入したい図版コンテンツを指定します。
`caption`オプションで図版のキャプションを指定します。

図版コンテンツは、画像（`#image`）だけでなく、表（`#table`）や数式（`#math`）、コードブロック（`#raw`）なども指定できます。
図版全体にラベルを設定して、本文中で参照できます。

:::{hint}

レポートや論文の場合、本文に関係のない図版は挿入してはいけません。
図版は、本文の内容を補足・説明するものであるべきです。
図版を挿入するときには、その図版が本当に必要かどうか、本文の文脈に沿っているか、など吟味が必要です。

また、図版のキャプションは必須です。
このとき、単に図版のタイトルだけ記述するのではなく、本文を読まなくても、この図版が何を示しているのかわかるように説明するとよいです。

:::

:::{seealso}

- [](./typst-image.md)
- [](./typst-table.md)
- [](./typst-math.md)
- [](./typst-raw.md)
- [](./typst-label.md)
- [](./typst-ref.md)

:::

## 図版を参照したい（`#label` / `#ref`）

```typst
#figure(
  image("image.jpg", width: 80%),
  caption: [図版のキャプション],
) <fig1>

この図は
#ref(<fig1>)
を参照してください。
```

相互参照の機能をつかって、本文中で図版を参照できます。
図版にラベル（`#label`）を設定して、`#ref`要素で参照します。
参照情報は、図版の要素名と番号の形式で表示されます。
図版の要素名は、`#page.lang`で設定した言語に

:::{seealso}

- [](./typst-label.md)
- [](./typst-ref.md)

:::

## 図版を設定したい（`#set figure`）

```typst
// figureの設定
#set figure(gap: 0em)

#show figure: block.with(
  width: 100%,
  inset: 0.5em,
  // stroke: 1tp,  // enable when debug
)
```

デフォルトだと図版と本文のアキが窮屈に感じたので、微調整したサンプルです。
まず、図版とキャプションのアキをリセット（`gap: 0em`に設定）したあと、コンテンツの余白（パディング）を`0.5em`に設定しています。

:::{hint}

図版の設定を調整するときは、
`stroke: 1pt`を有効にして、表示エリアを確認しながら調整するのがオススメです。

:::

:::{note}

```typst
#show figure: set block(
  width: 100%,
  inset: 0.5em,
  stroke: 1pt,
)
```

`block.with`の代わりに`set block`を使うと、この設定が子要素（`figure.caption`など）にも引き継がれてしまいます。

:::

## 図版のキャプションを設定したい（`#show figure.caption`）

```typst
// キャプションの設定
#show figure.caption: block.with(
  inset: 0.5em,
  width: 100%,
  // stroke: 1pt,  // enable when debug
)

// テキストを左寄せ
#show figure.caption: it => {
  align(left)[
    #it
  ]
}


#figure(
  [content],
  caption: [...]
)
```

図版のキャプション設定は`show`ルールで変更できます。
キャプションはデフォルトで図版に対して中央寄せで表示されるため、このサンプルでは、キャプション全体の幅を図版と同じにして、キャプションテキストを左寄せにしています。

また、前述の`figure`の設定に、この`caption`の設定を追加すると、結果的に図版と本文の間に`1em`のアキができます。

## プレースホルダーしたい

```typst
#let placeholder(width: 100%, height: 6cm, label: [placeholder]) = rect(
  width: width,
  height: height,
  fill: gray.lighten(80%),
  stroke: gray,
)[
  align(center + horizon )[
    text(size: 12pt, color: gray)[label]
  ]
]

// プレースホルダーを作成
#figure(
  placeholder(),
  caption: [図版のキャプション],
)

// 大きさなどを変更したプレースホルダーを作成
#figure(
  placeholder.with(width: 80%, height: 4cm, label: [幅80%のプレースホルダー]),
  caption: [図版のキャプション],
)
```

図版がまだ用意できないときは、プレースホルダーを挿入しておくと便利です。
上記のサンプルでは、`placeholder`関数を定義して、矩形とテキストを組み合わせたプレースホルダーを作成しています。
`with`メソッドで、プレースホルダーの大きさやラベルを変更した新しいプレースホルダーを作成できます。

## 複数の図版を並べたい

```typst
// +----------+----------+
// | image1   | image2   |
// | caption1 | caption2 |
// +----------+----------+
#columns(2, gutter: 0em)[
  #figure(
    [content],
    caption: [左図のキャプションです。],
  )<fig-left>

  #figure(
    [content],
    caption: [右図のキャプションです。],
  )<fig-right>
]
```

複数の図版を横に並べたい場合は、`#grid`関数で段組みしたところに、図版（`#figure`）を挿入します。
上記のサンプルでは、2列のグリッドを作成して、各列に図版を挿入しています。
グリッドの`gutter`オプションで、図版同士のスペースを調整できます。

## 複数の図版をまとめたい

```typst
// +---------+---------+
// | image1  | image2  |
// +---------+---------+
// |      caption      |
// +---------+---------+

#let images = columns(2, gutter: 1em)[
  [左図]
  #colbreak()
  [右図]
]

#figure(
  images,
  caption: [2つの図を説明する1つのキャプションです。]
)<fig-label>
```

複数の図版を横にならべて、キャプションを1つにまとめたい場合は、
あらかじめ`#grid`で段組みしたコンテンツブロックを`#figure`の第一引数に渡します。
上記のサンプルでは、2列のグリッドに図を並べて、
そのグリッド全体に対してキャプションを設定しています。

:::{note}

LaTeXで横並びの図を作成する場合、
[minipage](../latex/latex-minipage.md)のような外部パッケージが必要でした。

Typstでは標準機能だけで簡単に作ることができました。
角括弧が多くなり読みづらくなるのはさておき、
コンテンツブロック（`[...]`）の柔軟さと使い勝手のよさが、ようやくわかってきた気がします。

:::

## リファレンス

- [figure - Typst](https://typst.app/docs/reference/model/figure/)
