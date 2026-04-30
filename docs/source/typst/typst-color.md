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

## 読みやすい黒にしたい

```typst
#rgb("#222222")
#rgb(34, 34, 34)
#cmyk(0%, 0%, 0%, 87%)
#luma(13%)
```

白地に黒いテキストを配置する場合、純黒（`#000000`）よりも、少し明るい黒の方が読みやすいそうです。
上記のサンプルでは、`#222222`や`#cmyk(0%, 0%, 0%, 87%)`など、少し明るい黒を指定しています。

:::{note}

「オフブラック」や「ソフトブラック」と呼ばれるようです。

:::

## リッチブラックしたい（`cmyk`）

```typst
#let text-black = #cmyk(0%, 0%, 0%, 87%)
#let rich-black = #cmyk(60%, 40%, 40%, 100%)
```

印刷時の黒は、RGBで指定するよりもCMYKで指定する方が推奨されます。
「リッチブラック」は、CMYKで指定する黒の中でも、とくに濃い黒のことを指します。

印刷する紙やインクの種類によって、リッチブラックの定義は変わるそうです。
上記のサンプルでは、標準的と言われる`#cmyk(60%, 40%, 40%, 100%)`で指定しています。

:::{note}

すべての黒をリッチブラックにするのは、インクの使用量が増えるため、あまり推奨されません。
リッチブラックは、タイトルや見出しなど、強調したい部分のみに使用するのがオススメです。
本文テキストは、通常の黒で十分です。

:::

## RGBからCMYKに変換したい

```typst
#let rgb2cmyk(r, g, b) = {
  let r = r / 255
  let g = g / 255
  let b = b / 255

  let k = 1 - calc.max(r, g, b)
  if k == 1 {
    return (0%, 0%, 0%, 100%)
  }

  let c = (1 - r - k) / (1 - k)
  let m = (1 - g - k) / (1 - k)
  let y = (1 - b - k) / (1 - k)

  // return: (c, m, y, k)
  (c * 100%, m * 100%, y * 100%, k * 100%)
}

// Usage
#let (c, m, y, k) = rgb2cmyk(87, 127, 230)
#cmyk(c, m, y, k)
```

RGBとCMYKは、異なる色空間であるため、直接的な変換はできません。
RGBからCMYKへの変換は、一般的には近似的な方法で行われます。
Typstに、RGBからCMYKへの変換メソッドはないため、自分で計算する必要があります。

## CMYKからRGBに変換したい

```typst
#let cmyk2rgb(c, m, y, k) = {
  let c = c / 100
  let m = m / 100
  let y = y / 100
  let k = k / 100

  let r = 255 * (1 - c) * (1 - k)
  let g = 255 * (1 - m) * (1 - k)
  let b = 255 * (1 - y) * (1 - k)

    (r, g, b)
}
```

CMYKからRGBへの変換も、同様に近似的な方法で行われます。
Typstに、CMYKからRGBへの変換メソッドはないため、自分で計算する必要があります。

## リファレンス

- [color - Typst Reference](https://typst.app/docs/reference/visualize/color/)
