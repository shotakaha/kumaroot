# モードラインしたい（`doom-modeline`）

```emacs-lisp
(use-package doom-modeline
  :ensure t
  :init
  (doom-modeline-mode 1)
  :custom
  (doom-modeline-height 25)
  (doom-modeline-icon t)
  (doom-modeline-minor-modes nil)
)
```

`doom-modeline`はモードライン表示を拡張するパッケージです。
多彩な変数があり、自由にカスタマイズできます。
