# バッファー補完したい（`vertico`）

```emacs
(use-package vertico
  :init
  (vertico-mode)
  (vertico-cycle)
)
```

`vertico`はミニバッファーの補完を強化するパッケージです。
`M-x`したときの候補が縦表示になり、
ミニバッファー補完がスクロール可能になります。

:::{note}

`vertico`は`anything.el`の流れを汲んだパッケージらしいです。
ただし、`anything.el`がすべてを管理する思想だったのに対し、
`vertico`は他のパッケージとうまく協働する思想らしいです。

検索に`orderless`、
補完の説明に`marginalia`
高機能コマンドに`consult`
と組み合わせて使います。

:::

## ループしたい（`vertico-cycle`）

```emacs
(setq vertico-cycle t)
```

`vertico-cycle`で候補選択をループにできます。

## 補完候補の数を変更したい（`vertico-count`）

```emacs
(setq vertico-count 15)
```

`vertico-count`で補完候補の表示数を変更できます。

## リファレンス

- [minad/vertico](https://github.com/minad/vertico)
