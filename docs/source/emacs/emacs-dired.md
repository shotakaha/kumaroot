# ディレクトリ操作したい（`dired` / `dired-x` / `wdired`）

```emacs
(use-package dired
  :ensure nil
  :bind (("C-x C-j" . dired-jump))
  :custom
  (dired-listing-switches "-alh")
  (dired-dwim-target t)
  :config
  (setq dired-recursive-copies 'always
        dired-recursive-deletes 'always)
  (put 'dired-find-alternate-file 'disabled nil)
  (define-key dired-mode-map (kbd "a") 'dired-find-alternate-file))

(use-package dired-x
  :ensure nil
  :after dired
  :custom
  (dired-omit-mode t)
  (dired-omit-files "^\\.DS_Store\\|^\\.git$"))

(use-package wdired
  :ensure nil
  :after dired)
```

`dired`は、ディレクトリ操作ができる標準パッケージです。
ファイルの一覧を表示し、コピー・削除・リネームなどの操作ができます。
`dired-x`と`wdired`はそれを拡張する標準パッケージです。

Emacsでは、ディレクトリ／ファイル一覧も「バッファー」として表示されます。
とくに`wdired`では、その強みを活かして、バッファー内のテキストを編集する感覚でファイルをリネームできます。

:::{note}

VS Codeに移行して一番不便に感じていると言っても過言ではないのが
`wdired`相当のプラグイン拡張がないことです。

:::
