# UXを統一したい（`consult`）

```emacs-lisp
(use-package consult
  :ensure t
  :bind (
    ("C-c f" . consult-find)    ;; find-file / project-find-file を改善
    ("C-c g" . consult-ripgrep) ;; grep / rgrep / lgrep を改善
    ("C-c i" . consult-imenu)   ;; imenu を改善
    ("C-s" . consult-line)      ;; isearch-forward / occur を改善
    ("C-x b" . consult-buffer)  ;; switch-to-buffer を改善
    ("M-y" . consult-yank-pop)  ;; yank-pop を改善
    ("M-x" . consult-M-x)       ;; M-x を改善
  )
  :init
  (setq register-preview-delay 0.5)
  (setq register-preview-function #'consult-register-format)
  :config
  (advice-add #'register-preview :override #'consult-register-window)
)
```

`consult`は、Emacsの「選択・検索・コマンド実行」をミニバッファーで統一的に扱えるようにする拡張パッケージです。
ファイル選択、
バッファー切り替え、
コマンド実行、
バッファー内検索、
grep検索
などが「絞り込み可能な一覧」として操作できるようになります。

:::{seealso}

`consult`単体ではUIは完成しません。
`vertico` + `orderless` + `marginalia`と一緒に使うのが一般的です。

- [vertico](./emacs-vertico.md)
- [orderless](./emacs-orderless.md)
- [marginalia](./emacs-marginalia.md)

:::
