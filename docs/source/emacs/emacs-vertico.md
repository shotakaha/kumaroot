# ミニバッファー操作したい（`vertico`）

```emacs
(use-package vertico
  :init
  (vertico-mode)
  (vertico-cycle)
)
```

`vertico`はミニバッファー操作を拡張するパッケージです。
ミニバッファーの内容が縦表示になり、補完候補がスクロール可能になります。
`C-n` / `C-p`で移動できたり、
`C-v` / `M-v`でスクロール移動できたりするのが地味に助かります。

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
