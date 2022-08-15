# Magitの使い方

[Magit](https://magit.vc/)はEmacsのGitインターフェースです。
Emacsを使ってGitするひとはぜひ使いましょう！


## インストール

```lisp
M-x package-install RET magit RET
```

## 設定
```lisp
(use-package magit
    :ensure t
    :bind (("C-x g" . magit-status)
            ("C-x M-g" . magit-dispatch-popup)
            )
    )
```

## 使い方

```{toctree}
emacs-magit-status
emacs-magit-dispatch
emacs-magit-stage
emacs-magit-commit
emacs-magit-push
```
