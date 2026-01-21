# グラフしたい（`simple-plot`）

```typst
#import "@preview/simple-plot:0.2.0": plot

#align(center)[
#plot(
  xmin: -1.2,
  xmax:  1.2,
  ymin: -1.2,
  ymax:  1.2,
  width: 10,
  height: 10,
  axis-x-pos: 0,
  axis-y-pos: 0,
  show-grid: true,

  // 上半円
  (
    fn: x => calc.sqrt(1 - x*x),
    domain: (-1, 1),
    stroke: blue + 1.5pt,
  ),

  // 下半円
  (
    fn: x => -calc.sqrt(1 - x*x),
    domain: (-1, 1),
    stroke: blue + 1.5pt,
  ),
)
]
```

`simple-plot`で、簡単なグラフを描画できます。
本文中の数式をグラフにしたい場合などに利用できます。

:::{note}

`simpleplot`（ハイフンなし）という同じような名前のパッケージもあるようなので注意してください。

:::

## リファレンス

- [simple-plot | Typst Universe](https://typst.app/universe/package/simple-plot)
