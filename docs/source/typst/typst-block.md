# ブロック要素したい（`block`）

```typst
#block(
    fill: luma(230),
    inset: 8pt,
    outset: 8pt,
    radius: 4pt
)[
    #lorem(30)
]
```

`block`要素は、HTMLのブロック要素に相当する機能です。
自作テンプレートを作成して、あとからカスタマイズ可能にしたい場合に便利です。

## 背景色したい（`fill`）

```typst
#block(fill: none)
```

`fill`オプションでブロック要素の背景色を変更できます。

:::{note}

[text要素](./typst-text.md)の`fill`オプションは文字色、
`block`要素は背景色を変更できます。

:::

## 枠線したい（`stroke`）

```typst
#block(stroke: (:))
```

## 余白したい

```typst
#block(inset: (:))
#block(outset: (:))
#block(above: auto)
#block(below: auto)
#block(spacing: 1.2em)
```

## リファレンス

- [block](https://typst.app/docs/reference/layout/block/)
