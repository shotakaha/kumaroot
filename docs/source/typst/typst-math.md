# 数式したい

```typst
// 数式モード（インライン表示）
ピラゴラスの定理$a^(2) + b^(2) = c^(2)$は・・・

// 数式ブロック
ピタゴラスの定理$ a^(2) + b^(2) = c^(2) $は・・・
```

デフォルトで[数式モジュール](https://typst.app/docs/reference/math/)が使えます。
数式モード／ブロックを``$``記号で表現するのはLaTeXと同じです。
``$``のあとに空白を追加すると数式ブロックになります。

:::{seealso}

- [](../latex/latex-amsmath.md)

:::

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
