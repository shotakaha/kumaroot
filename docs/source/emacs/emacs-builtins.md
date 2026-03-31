# 基本設定したい（`emacs`）

```emacs
(use-package emacs
  :init    ;; 起動直後に実行
  (set-locale-environment "en_US.UTF-8")

  :config  ;; 初期化後に実行
  (fset 'yes-or-no-p 'y-or-n-p)

  :custom  ;; 基本はここ（setqの代わり）
  (inhibit-startup-screen t)
  (initial-scratch-message nil)
  (make-backup-files nil)
  (auto-save-default nil)
  (create-lockfiles nil)
  (tab-width 4)
  (indent-tabs-mode nil)
  (ring-bell-function 'ignore)

  :bind
  (("C-h" . delete-backward-char))
)
```

`(use-package emacs)`で、Emacsの基本設定（ビルトイン設定）を変更できます。

:::{note}

この「`emacs`」はパッケージ名ではなく、
`use-package`を使ってビルトイン設定を統一的に書けるようにする特殊な名前です。

:::
