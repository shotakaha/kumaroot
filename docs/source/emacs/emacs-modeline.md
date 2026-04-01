# モードラインしたい（`mode-line-format`）

```emacs-lisp
(use-package emacs
  :custom
  (line-number-mode t)
  (column-number-mode t)
  (size-indication-mode t)
  (display-time-mode t)
  :config
  (setq-default mode-line-format
    '(
        "%e "
        mode-line-buffer-identification
        " | "
        mode-line-position
        " | "
        mode-line-modes
    )
  )
)
```

「モードライン」はEmacsのフレーム下に表示される情報バーのことです。
その表示内容をON/OFFできます。
また`mode-line-format`を設定することで、好みの表示内容に書き換えることができます。
