# vimしたい（`evil`）

```emacs-lisp
(use-package evil
  :ensure t
  :init
  (evil-mode 1)
  :custom
  (evil-want-integration t)
  (evil-want-keybinding nil)
  (evil-default-state 'normal)
)
```

`evil`はEmacsでvim操作ができるようになる拡張パッケージです。
僕は、vimのステータス切り替えが好きなので導入しています。
