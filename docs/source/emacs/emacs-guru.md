# 修行したい（`guru-mode`）

```emacs-lisp
(use-package guru-mode
  :ensure t
  :init
  (guru-global-mode 1)
  :custom
  (guru-warn-only t)
)
```

`guru-mode`は、Emacsのキーバインドを矯正するためのツールです。
矢印キーを使ったり、便利なキーを使ったりすると、標準的なキーバインドを教えてくれます。
正しくない／甘いキー操作をしたときに動かないのはストレスなので、
`guru-warn-only`を有効にして警告までに留めておくことをオススメします。
