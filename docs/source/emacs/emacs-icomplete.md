# バッファー補完したい（`icomplete`）

```emacs
(use-package icomplete
  :init
  (icomplete-mode 1)
)
```

`icomplete`はミニバッファー補完を拡張する標準パッケージです。
軽量でシンプルに補完機能を強化したい場合に便利です。

:::{note}

現在では
[vertico](./emacs-vertico.md) +
[orderless](./emacs-orderless.md) +
[consult](./emacs-consult.md)
のようなモダンな補完構構を使うことが一般的です。

これらを使用する場合、`icomplete`は不要です。
同時に有効化すると競合する可能性があります。

:::
