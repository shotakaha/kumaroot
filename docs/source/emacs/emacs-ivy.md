# ミニバッファーしたい（`ivy` / `counsel` / `swiper`）

```emacs
(use-package ivy
  :ensure t
  :init
  (ivy-mode 1)
  :custom
  (ivy-use-virtual-buffers t)
  (enable-recursive-minibuffers t)
)

(use-package counsel
  :ensure t
  :after ivy
  :config
  (counsel-mode 1)
  ;; counsel-mode で以下のバインドも設定される
  ;; :bind
  ;; (("M-x" . counsel-M-x)
  ;; ("C-x C-f" . counsel-find-file))
)

(use-package swiper
  :ensure t
  :after ivy
  :bind
  ("C-s" . swiper)
)
```

`ivy`はミニバッファーを拡張する補完UIです。
単体で使うより`counsel` / `swiper`とセットで使うのが一般的です。

:::{seealso}

- `ido` + `ido-vertical-mode`
- `vertico` + `orderless`

:::
