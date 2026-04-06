# ウェブ構文したい（`web-mode`）

```emacs-lisp
(use-package web-mode
  :ensure t
  :mode (
    "\\.html?\\'"
    "\\.tsx\\'"
    "\\.jsx\\'"
    "\\.vue\\'"
  )
  :custom
  (web-mode-markup-indent-offset 2)
  (web-mode-code-indent-offset 2)
  (web-mode-css-indent-offset 2)

  :config
  (setq web-mode-enable-auto-indentation t)
  (setq web-mode-enable-auto-pairing t)

  :bind (
    ("C-c C-e" . web-mode-element-close)
    ("C-c C-w" . web-mode-element-wrap)
  )
)
```

`web-mode`はHTML・CSS・JS・テンプレート言語（Vue／JSX／PHPなど）を1つのモードで扱えるメジャーモードです。
標準の`html-mode`よりも高機能で、フロントエンド開発に向いています。

:::{note}

`web-mode`はウェブサイト開発で広く使われている定番パッケージです。
設定も簡単なので、はじめて使うひとはまず試してみるのがオススメです。開発体験が大きく向上します。

一方、Emacs29以降では`tree-sitter`ベースの構文解析モードが標準で追加されました。

最近では
`tsx-ts-mode`、
`js-ts-mode`、
`css-ts-mode`、
`html-ts-mode`
などの言語別のモードとLSP（`eglot`）を組み合わせる構成が主流になりつつあります。

:::
