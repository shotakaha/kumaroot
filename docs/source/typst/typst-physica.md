# 物理記号したい（`physica`）

```typ
#import "@preview/physica:0.9.8": *
```

`physica`パッケージを使って、物理記号を簡単に記述できるようになります。
数式モード（`$...$`）で使います。

:::{seealso}

- [](../latex/latex-physics.md)

:::

## ベクトルしたい

```typst
$va(a)$  // ベクトルを矢印で表現
$vb(a)$  // ベクトルを太字で表現
$vu(a)$  // 単位ベクトル（^）
```

## 微分したい（`dv`）

```typst
$dv(x, t)$        // dx/dt
$dv(x, t, n)$     // d^{n}x/dt^{n}

$dv(, t)$         // d     /dt
$dv(x, t, n)$     // d^{n} /dt^{n}
```

## 偏微分したい（`pdv`）

```typst
$pdv(U, x)$
$pdv(U, x, [n])$
$pdv(U, x, y)$
```

## リファレンス

- [physica - Typst Universe](https://typst.app/universe/package/physica/)
- [Leedehai/typst-physics - GitHub](https://github.com/Leedehai/typst-physics)
