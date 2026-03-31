# パッケージ管理したい（`straight`）

```emacs
;; straight.el bootstrap
(defvar bootstrap-version)
(let ((bootstrap-file
       (expand-file-name "straight/repos/straight.el/bootstrap.el" user-emacs-directory))
      (bootstrap-version 6))
  (unless (file-exists-p bootstrap-file)
    (with-current-buffer
        (url-retrieve-synchronously
         "https://raw.githubusercontent.com/radian-software/straight.el/develop/install.el"
         'silent 'inhibit-cookies)
      (goto-char (point-max))
      (eval-print-last-sexp)))
  (load bootstrap-file nil 'nomessage))

;; use-package を straight 経由で使う
(straight-use-package 'use-package)
(setq straight-use-package-by-default t)
(setq straight-vc-git-default-clone-depth 1)

;; add package below
(use-package which-key
  :config
  (which-key-mode))
```

`straight`はEmacsの次世代パッケージ管理ツールのひとつです。
[package.el](./emacs-package.md)はELPA（やMELPA）から取得しますが、
`straight`はGitHubからクローンして取得します。
取得するバージョンを指定できるため、パッケージ環境の再現性を高くできます。

単体で利用することもできますが、`use-package`と組み合わせることで、
パッケージの管理と設定を強化できます。

## バージョンをロックしたい（`straight-freeze-versions`）

```emacs
M-x straight-freeze-versions
```
