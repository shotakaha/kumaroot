# Magitの使い方

```emacs
(use-package magit
  :ensure t
  :bind (("C-x g" . magit-status)
         ("C-x M-g" . magit-dispatch))
  :custom
  (magit-auto-revert-mode nil)    ;; 自動更新をOFF
)
```

[Magit](https://magit.vc/)はEmacsのGitインターフェースです。
Git操作が楽しくなるので、Emacsを使ってGitするひとはぜひ使いましょう！

## 使い方

```{toctree}
emacs-magit-status
emacs-magit-dispatch
emacs-magit-stage
emacs-magit-commit
emacs-magit-push
```
