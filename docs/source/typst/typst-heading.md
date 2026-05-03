# 見出ししたい（`#heading`）

```typst
// 簡易マークアップ
= 見出し1
== 見出し2
=== 見出し3
==== 見出し4

// 関数でのマークアップ
#heading[見出し1]  // デフォルトは(level: 1)
#heading(level: 2)[見出し2]
#heading(level: 3)[見出し3]
#heading(level: 4)[見出し4]  // 見出し4以降は見た目が同じ
```

`heading`関数で見出しをマークアップできます。
また`=`を使った簡易マークアップも利用できます。

## 見出しレベルを変更したい（`level`）

```typst
#heading(level: 2)[見出し2]
```

`level`オプションで、見出しレベルを変更できます。
簡易マークアップでは、`=`の数でレベルを指定します。

## 見出しを非表示にしたい（`outlined`）

```text
#heading(outlined: false)[隠したい見出し]
```

`outlined`オプションで、見出しを目次に追加するかどうかを変更できます。
`outlined: false`で非表示にできます。

:::{seealso}

`outlined: false`は
LaTeXの`\section*`に相当します。

:::

## 見出し番号したい（`numbering`）

```typst
#heading(numbering: "1.")[算用数字]       // -> 1. 見出し1
#heading(numbering: "a.")[アルファベット]  // -> a. 見出し2
```

`numbering`オプションで、見出し番号の表示方法を変更できます。
デフォルトは`none`で、見出し番号は表示されません。

```typst
// 全体設定
#set heading(numbering: "1.")
```

`#set heading`ルールで、ドキュメント全体の見出し設定を変更できます。
通常はこの方法で、見出し番号を表示するのがオススメです。

```typst
#set heading(numbering: "1.")  // -> 1., 1.1., 1.1.1.,

// ローマ数字
#set heading(numbering: "I.")  // -> I., I.I., I.I.I.,
#set heading(numbering: "i.")  // -> i., i.i., i.i.i.,

// アルファベット
#set heading(numbering: "A.")  // -> A., A.B., A.B.C.,
#set heading(numbering: "a.")  // -> a., a.b., a.b.c.,
```

見出しレベルの番号はアルファベットやローマ数字に変更できます。

```typst
#set heading(numbering: "あ.")  // -> あ., あ.い., あ.い.う.,
#set heading(numbering: "ア.")  // -> ア., ア.イ., ア.イ.ウ.,
#set heading(numbering: "い.")  // -> い., い.ろ., い.ろ.は.,
#set heading(numbering: "イ.")  // -> イ., イ.ロ., イ.ロ.ハ.,
```

五十音やいろは順も利用できます。
ただし、見出しレベルが深くなるとわかりにくくなるので、あまりオススメしません。

```typst
#set heading(numbering: "1.1")   // -> 1 , 1.1 , 1.1.1 ,
#set heading(numbering: "1.1.")  // -> 1., 1.1., 1.1.1.,
#set heading(numbering: "1.1)"   // -> 1), 1.1), 1.1.1),
```

番号の区切り文字も変更できます。
その場合、`1.)` ではなく`1.1.)`のように、レベル2まで番号を指定する必要があります。

:::{seealso}

- [](../latex/latex-section.md)

:::

## 見出しを装飾したい（`#show heading:`）

```typst
// 基本設定
#set heading(numbering: "1.")

#show heading: set text(weight: "bold")
#show heading: set block(
  width: 100%,  // 見出しを行幅に広げる
  above: 1em,  // 見出しの上にスペースを追加
  below: 1em,  // 見出しの下にスペースを追加
  // stroke: luma(50%) + 2pt,  // ボーダーを追加
  // fill: luma(90%),  // 背景色を追加
)
```

`#show heading`ルールで、見出しの装飾を設定できます。
見出しの装飾は、`set block`で`block`要素に変換して、スペースや背景色を追加するのが簡単です。

上記のサンプルでは、すべての見出しを対象に、
フォントを太字（`weight: "bold"`）にし、
上（`above: 1em`）と下（`below: 1em`）にスペースを追加しています。
デフォルトでは見出しの周りが窮屈なので、こうしています。

また、コメントアウトしている部分を有効にすることで、ボーダーや背景色を追加できます。
このあたりはお好みです。いろいろ試してみてください。

:::{note}

`inset: 1em`オプションでパディングを追加すると、見出し文字列の周囲にもスペースが追加されてしまします。
`above`と`below`でスペースを追加するか、
`inset: (top: 1em, bottom: 1em)`で上下のパディングのみ追加するのがよさそうです。

どちらも見た目は同じになりますが、微妙に違うようです。
それぞれの違いは、`fill: red`などで背景色を追加してみるとわかりやすいと思います。

:::

## 見出しのサイズを揃えたい

```typst
// 基準サイズを指定 -> 1.2倍
#show: heading: set text(size: 10pt)
#show: heading: set text(size: 1.2em)
```

デフォルトでは見出しレベルごとにフォントサイズが異なります。
これはウェブページでは一般的ですが、
印刷物では同じサイズにしたいこともあると思います。

:::{note}

`#show: heading: set text(size: 1.2em)`だけでは、
`レベルごとのサイズ * 1.2`になるだけで、すべての見出しのサイズが揃うわけではありません。
`#show heading: set text(size: 10pt)`のように、絶対サイズで基準サイズの指定が必要です。

:::

:::{caution}

```typst
#show: heading: set text(size: 1.2em)
#show: heading: set text(size: 10pt)
```

`#show`ルールは上から順番に重ね書きされるため、同じオプションを設定する場合は、定義する順番に注意が必要がです。
上記の順番で定義すると、すべての見出しレベルが`10pt`になります。

:::

## 見出しレベルごとに装飾したい

```typst
#show heading.where(level: 1): set text(size: 1.5em, weight: "bold")
#show heading.where(level: 2): set text(size: 1.3em, weight: "bold")
#show heading.where(level: 3): set text(size: 1.1em, weight: "bold")
```

`#show heading.where(level: n)`で、見出しレベルごとに装飾を設定できます。
上記のサンプルでは、レベル1から3までの見出しに対して、サイズと太字を設定しています。
レベル4以降は、デフォルトのままにしています。

:::{seealso}

- [](./typst-show.md)
- [](./typst-where.md)
- [](./typst-block.md)
- [](./typst-color.md)

:::

## 見出しで改ページしたい

```typst
#show heading.where(level: 1): it => { pagebreak(weak: true) + it }
```

見出しごとに改ページすることもできます。
上記のサンプルでは、レベル1の見出しに対して改ページ（`pagebreak`）を適用しています。
`weak: true`を指定することで、改ページが連続しないようにしています。
スライド資料を作成するときに便利です。
