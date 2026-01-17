# ブロック要素したい（`block`）

```typst
#block(
  fill: luma(230),
  inset: 8pt,
  outset: 8pt,
  radius: 4pt,
  stroke: 1pt,
)[
  #lorem(30)
]
```

`block`要素は、コンテンツをブロック化する機能です。
ブロック化することで、枠線、背景色、余白などを設定できるようになります。

自作テンプレートを作成する際に、とりあえず使っておくとよいです。
あとからカスタマイズ可能にしたい場合にも便利です。

:::{seealso}

HTMLのブロック要素（`div`など）に相当する機能です。

:::

## 大きさしたい（`width` / `height`）

```typst
#block(
  width: 90%,
)
```

`width`オプションで、ブロック要素の横幅を変更できます。

## 背景色したい（`fill`）

```typst
#block(fill: none)
```

`fill`オプションで、ブロック要素の背景色を変更できます。

:::{note}

[text要素](./typst-text.md)の`fill`オプションは文字色、
`block`要素は背景色を変更できます。

:::

## 枠線したい（`stroke`）

```typst
#block(stroke: (:))
```

`stroke`オプションで、ブロック要素の枠線を変更できます。

## 角丸したい（`radius`）

```typst
#block(
  stroke: 1pt,
  radius: 1em,
)
```

`radius`オプションで、ブロック要素の枠線の角の丸みを変更できます。

:::{note}

`stroke`オプションによる枠線表示と併用しないと、変更がわかりません。

:::

## 余白したい（`inset` / `outset` / `spacing`）

```typst
#block(inset: (:))
```

`inset`オプションで、ブロック要素の内側の余白（＝パディング）を変更できます。

```typst
#block(outset: (:))
```

`outset`オプションで、ブロック要素の外側の余白（＝マージン）を変更できます。

```typst
#block(spacing: 1.2em)
```

`spacing`オプションで、ブロック要素の上下の余白を変更できます。

```typst
#block(above: auto)
#block(below: auto)
```

`above`、`below`オプションで片側ずつ変更できます。

:::{note}

余白のサイズを調整する際は、一時的に`stroke`オプションを有効にして、枠線を表示させるとスムーズに調整できます。

:::

## リファレンス

- [block - Typst](https://typst.app/docs/reference/layout/block/)
