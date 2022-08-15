# Magitの使い方

[Magit](https://magit.vc/)はEmacsのGitインターフェースです。
Emacsを使ってGitするひとはぜひ使いましょう！


## インストール

```lisp
(use-package magit
    :ensure t
    :bind (("C-x g" . magit-status)
            ("C-x M-g" . magit-dispatch-popup)
            )
    )
```

```{toctree}
emacs-magit-status
emacs-magit-dispatch
emacs-magit-stage
emacs-magit-commit
emacs-magit-push
```
