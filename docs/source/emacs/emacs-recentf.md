# 履歴保存したい（`recentf`）

```emacs
;; recentf
(use-package recentf
  :init
  (recentf-mode 1)
  :custom
  (recentf-max-saved-items 200)
  (recentf-auto-cleanup 'mode)
  :bind
  (("C-x C-r" . recentf-open-files))
)
```

`recentf`は最近開いたファイルの履歴を保存する標準パッケージです。
`consult`なども内部的に利用するため有効にしておくとよいです。

:::{note}

`consult`を使っている場合は、
キーバインドは`consult-recent-file`にアサインするとよいです。

```emacs
:bind (
    ("C-x C-r". consult-recent-file)
)
```

:::
