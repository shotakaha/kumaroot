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

## 自由場のラグランジアンしたい

:::{note}

標準の`math.equation`モジュールで作成できました

:::

- スカラー場（スピン0、質量$m$）のラグランジアン（Klein-Gordon Lagrangian）

```typst
$
cal(L) = frac(1, 2) partial_(mu) phi partial^(mu) phi - frac(1, 2) ( frac(m c, hbar))^(2) phi^(2)
$
```

- スピノル場（スピン1/2、質量$m$）のラグランジアン（Dirac Lagrangian）

```typst
$
cal(L) = i ( hbar c) overline(psi) gamma^(mu) partial_(mu) psi - (m c^(2)) overline(psi) psi
$
```

- ベクトル場（スピン1、質量$m$）のラグランジアン（Proca Lagrangian）

```typst
$
cal(L) = - frac(1, 16 pi) F^(mu nu) F_(mu nu) + frac(1, 8 pi) (frac(m c, hbar))^(2) A^(nu) A_(nu)
$
```

## リファレンス

- [physica - Typst Universe](https://typst.app/universe/package/physica/)
- [Leedehai/typst-physics - GitHub](https://github.com/Leedehai/typst-physics)
