# 構文チェックしたい（`flymake`）

```emacs-lisp
(use-package flymake
  :hook (prog-mode . flymake-mode)
  :bind (
    ("M-n" . flymake-goto-next-error)
    ("M-p" . flymake-goto-prev-error)
    ("C-c d" . flymake-show-buffer-diagnostics)
  )
)
```

`flymake`は、構文チェックの結果を表示する標準パッケージです。
コードのエラーや警告をリアルタイムで表示してくれます。

上記の設定サンプルでは
フック（`:hook`）を設定し、プログラミングモード（`prog-mode`）で有効になるようにすると便利です。
また、
`M-n`キーで次のエラー（`flymake-goto-next-error`）、
`M-p`キーで前のエラー（`flymake-goto-prev-error`）
に移動できるようにキーバインドを設定しています。

```text
M-x flymake-show-buffer-diagnostics
```

`flymake-show-buffer-diagnostics`コマンドで一覧表示できます。

:::{note}

`flymake`単体には構文チェック機能はありません。
LSP（Language Server Protocol）や言語別リンターなどの外部ツールの設定も必要です。

Emacs29+では`eglot`を設定すると、自動で`flaymake`が有効になります。

```emacs-lisp
(use-package eglot
  :hook (prog-mode . eglot-ensure)
)
```

:::
