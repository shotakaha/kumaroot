# 色を変更したい（`#rgb` / `#cmyk` / `#luma`）

```typst
rgb()    // RGBで指定
cmyk()   // CMYKで指定
luma()   // グレイスケールを指定
```

## RGBしたい（`rgb`）

```typst
rgb("#b1f2eb")  // カラーコード
rgb(87, 127, 230)  // RGB
rgb(87, 127, 230, 50%)  // RGB + Alpha

#let color = rgb(87, 127, 230, 50%)

// 成分
color.components()
// 色空間
color.space()

// 濃淡
color.lighten(50%)
color.darken(50%)

// 補色
color.negate()

// 透明度
color.transparentize(50%)
color.opacify(-50%)
```

## リファレンス

- [color - Typst Reference](https://typst.app/docs/reference/visualize/color/)
