# 段組したい（`columns`）

```typst
ここは段組の前のスペースです。

#columns(2, gutter: 1em)[  // 2段組
段組の内容1
段組の内容2

#colbreak()

段組の内容3
段組の内容4
]

ここは段組の後のスペースです。
```

`columns(n)`関数で、段数を指定して段組できます。
`gutter`オプションで、段間のスペースを調整できます。
段組の途中で改段したいときは、`#colbreak()`を使います。

## 複数の図版を並べたい

```typst
#let image1 = #image("image1.png")
#let image2 = #image("image2.png")

#figure(
  #columns(2, gutter: 1em)[
    #image1
    #colbreak()
    #image2
  ],
  caption: "複数の図版を並べる例",
)
```

複数の図を1つの図版としてまとめたい場合、
`#figure`関数の中で、`columns`関数で段組します。
