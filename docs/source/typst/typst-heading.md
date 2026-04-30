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

## 見出しを設定したい（`#set heading`）

```typst
// 見出しの設定
#set heading(
  depth: 3,
  numbering: "1.1.1",
)
```

`#set`ルールで、ドキュメント全体の見出し設定を変更できます。
`depth`オプションで、目次に含める見出しレベルを設定できます。
デフォルトは`1`です。
`numbering`オプションで、見出し番号の表示方法を変更できます。
デフォルトは`none`です。レベルに応じて`1.1.`、`1.1.1.`のように表示されます。

:::{seealso}

- [](../latex/latex-section.md)

:::

## 見出しを装飾したい（`#show heading:`）

```typst
// 基本設定
#set heading(numbering: "1.")

// 共通の装飾を設定
#show heading: block.with(
  fill: luma(90%),  // 背景色を追加
  inset: 1em,       // 内側のスペースを追加
  above: 1em,  // 見出しの上にスペースを追加
  below: 1em,  // 見出しの下にスペースを追加
)

// レベルごとの装飾を追加
#show heading.where(level: 1): block.with(fill: luma(150), inset: 1em)
#show heading.where(level: 2): block.with(fill: luma(100), inset: 1em)
#show heading.where(level: 3): block.with(fill: luma(50), inset: 1em)
```

見出しの装飾は`#show`ルールで設定できます。
全体の共通設定と、レベルごとの個別設定を組み合わせて設定するのがオススメです。
基本的には`block`要素に変換して、スペースや背景色を追加するのが簡単です。

上記のサンプルでは、すべて見出しを`block`要素に変換して、上下にスペースを追加しています。
デフォルトでは見出しの上下は窮屈なので、これは必須の設定だと思います。
また、レベルごとに背景色を変えて、見出しの階層が分かりやすくなるようにしています。
このあたりはお好みです。いろいろ試してみてください。

```typst
// 共通の装飾を定義
#let h = block.with(
  fill: luma(90%),  // 背景色を追加
  inset: 1em,       // 内側のスペースを追加
  above: 1em,  // 見出しの上にスペースを追加
  below: 1em,  // 見出しの下にスペースを追加
)

// レベルごとの装飾を再定義
#let h1 = h.with(fill: luma(150))
#let h2 = h.with(fill: luma(100))
#let h3 = h.with(fill: luma(50))

// レベルごとの装飾を適用
#show heading.where(level: 1): h1
#show heading.where(level: 2): h2
#show heading.where(level: 3): h3
```

冒頭のサンプルが設定を「追加」する方法だったのに対して、こちらは設定を「上書き」する方法です。
こちらの方が、設定しやすいかもしれません。

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
