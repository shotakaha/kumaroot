# シェルしたい（`vterm`）

```emacs
(use-package vterm
  :ensure t
  :commands vterm
  :bind
   (("C-c t" . vterm)
    ("C-c T" . vterm-other-window))
  :custom
  (vterm-shell "/opt/homebrew/bin/fish")
  (vterm-max-scrollback 10000)
)

;; vtermを複数使うための拡張（オプション）
(use-package multi-vterm
  :ensure t
  :after vterm
  :bind (("C-c m" . multi-vterm))
)
```

`vterm`は、Emacs内で「本物のターミナル」を動かせる高性能ターミナルです。
BashやZshをEmacsのミニバッファーとして扱えるのが便利です。
