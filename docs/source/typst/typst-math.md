# 数式したい（`#math.equation`）

```typst
#set math.equation(numbering: "(1)")
#show math.equation: text.with(font: "Noto Sans Math")

// インライン表示
$a^(2) + b^(2) = c^(2)$

// ブロック表示
$ a^(2) + b^(2) = c^(2) $

// ブロック表示（オススメ）
$
a^(2) + b^(2) = c^(2)
$
```

デフォルトで[数式モジュール](https://typst.app/docs/reference/math/)が使えます。
数式モード／ブロックを``$``記号で表現するのはLaTeXと同じです。
``$``のあとに空白を追加すると数式ブロックになります。

:::{seealso}

- [](../latex/latex-amsmath.md)

:::

## 式番号したい（`#math.equation.numbering`）

```typst
#set math.equation(
  numbering: "(1)",
  number-align: end + horizon
)

#set math.equation(
  numbering: "(1)",
  number-align: left  + bottom
  )
```

`numbering`オプションで、式番号を設定できます。
ブロック表示の`#math.equation`に数式番号が自動採番されます。

`number-align`で数式番号を表示する位置を変更できます。
デフォルトは`end + horizon`です。
`right | left`もしくは`start | end` + `top | horizon | bottom`の組み合わせで指定します。

## 数式フォントしたい

```typst
#show math.equation: text.with("Noto Sans Math")
```

せっかくなので数式に適したフォントに変更しましょう。

## 時間微分したい（`dot` / `dot.double`）

```typst
// 時間微分
$dot(x)$

// 2階の時間微分
$dot.double(x)$
```

## ラグランジアン密度したい（`#math.cal`)

```typst
$cal(L)$
```

## 集合したい（`#math.bb`）

```typst
$bb(R)$ or $RR$  // 実数
$bb(C)$ or $CC$  // 複素数
$bb(N)$ or $NN$  // 自然数

$x in RR$  // xは実数
```

## 数式モードでテキストしたい

```typst
$N_("SK")^("obs")$
```

数式モードの中で、テキストを立体（ローマン体）で表示できます。

:::{seealso}

LaTeXでは次のように書きます。
``\text``みたいなコマンドが不要なことがわかります。

```latex
$N_{\text{SK}}^{\text{obs}}$
```

:::

## リファレンス

- [equation | Element | Typst](https://typst.app/docs/reference/math/equation/)
