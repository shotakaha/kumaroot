# シェルしたい（`eshell`）

```emacs
(use-package eshell
  :ensure: nil
  :custom
  (eshell-history-size 10000)
  (eshell-hist-ignoredups t)
  (eshell-cmpl-cycle-completions t)
)
```

`eshell`はEmacs標準のEmacs Lispで実装されたシェルです。
外部シェルに依存せず、Emacsコマンドとシームレスに連携できます。
軽いコマンド実行には向いていますが、ヘビーな作業には向いていません。
