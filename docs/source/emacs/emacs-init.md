# 設定ファイルしたい（`~/.emacs.d/init.el`）

```emacs
;;; init.el --- straight + use-package minimal setup

;; --------------------------------
;; straight.el bootstrap
;; --------------------------------
(defvar bootstrap-version)
(let ((bootstrap-file
       (expand-file-name
        "straight/repos/straight.el/bootstrap.el"
        user-emacs-directory))
      (bootstrap-version 6))
  (unless (file-exists-p bootstrap-file)
    (with-current-buffer
        (url-retrieve-synchronously
         "https://raw.githubusercontent.com/radian-software/straight.el/develop/install.el"
         'silent 'inhibit-cookies)
      (goto-char (point-max))
      (eval-print-last-sexp)))
  (load bootstrap-file nil 'nomessage))

;; --------------------------------
;; straight + use-package
;; --------------------------------
(straight-use-package 'use-package)
(setq straight-use-package-by-default t)
(setq straight-vc-git-default-clone-depth 1)

;; --------------------------------
;; 基本設定
;; --------------------------------
(use-package emacs
  :custom
  (inhibit-startup-screen t)
)

;; --------------------------------
;; パッケージ例
;; --------------------------------

;; which-key
(use-package which-key
  :config
  (which-key-mode 1))

;; vertico
(use-package vertico
  :init
  (vertico-mode))

;; orderless
(use-package orderless
  :custom
  (completion-styles '(orderless)))

;; consult
(use-package consult)

;; marginalia
(use-package marginalia
  :init
  (marginalia-mode))

;;; init.el ends here
```

`init.el`は、Emacsの起動時に読み込まれる設定ファイルです。
上記は`straight`と`use-package`を使ってパッケージを管理する設定サンプルです。
初期設定としてオススメのパッケージも追加してあります。

```tree
~/.emacs.d/
|-- init.el
|-- early-init.el
|-- custom/
|--
```

:::{note}

正しくは`~/.emacs.el`もしくは`~/.emacs.d/init.el`が、起動時に読み込まれるファイルです。
設定内容が競合するため、どちらか片方のみ作成してください。
現在は後者を作成することが多いです。

:::

## early-initしたい（`~/.emacs.d/early-init.el`）

```emacs
;; early-init.el --- early settings

;; パッケージの自動初期化を無効化
(setq package-enable-at-startup nil)

;; GCを一時的に大きくする
(setq gc-cons-threshold (* 50 1000 1000))
;; init.elで大きさを戻す
;; (setq gc-cons-threshold (* 2 1000 1000))

;; UIを非表示
(menu-bar-mode -1)
(tool-bar-mode -1)
(scroll-bar-mode -1)

;; フレーム設定
(setq frame-inhibit-implied-resize t)
```

`early-init.el`は、起動直後（通常の`init.el`よりも前）に読み込まれる設定ファイルです。
Emacs27以降に導入された機能で、初期化の挙動を制御して、起動を速くできます。

上記のサンプルでは、パッケージの自動初期化を無効にしたり、
ガベージコレクション（GC）のサイズを一時的に大きくしたりして、
高速に起動できるようにしています。

:::{note}

このファイルは軽く書くのが基本です。
重たい処理やパッケージの設定は書きません。

:::

## XDG準拠したい（`~/.config/emacs/init.el`）

```bash
export XDG_CONFIG_HOME="HOME/.config"
```

`XDG_CONFIG_HOME`が設定されていると
`~/.config/emacs/`にある設定が読み込まれるようになります。

:::{note}

最近のモダンなツールは設定ファイルを`~/.config/{ツール名}`に配置する傾向があります。
上記の環境変数を設定すれば、Emacsでも利用できます。
ただし、まだまだ`~/.emacs.d/`を使うほうが一般的なようです。
`~/.emacs.el`のときと同じですが、`~/.emacs.d/`と`~/.config/emacs/`も併用できません。

:::
