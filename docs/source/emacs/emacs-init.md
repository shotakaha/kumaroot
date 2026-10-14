# 設定ファイルしたい（`~/.emacs.d/init.el`）

```emacs
;;; init.el --- package.el + use-package setup for Emacs 31 -*- lexical-binding: t -*-

;; --------------------------------
;; package.el + use-package (built-in)
;; --------------------------------
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; 初回起動時にパッケージ一覧を取得する
(unless package-archive-contents
  (package-refresh-contents))

(setq use-package-always-ensure t)

;; --------------------------------
;; custom-file
;; --------------------------------
(setq custom-file (expand-file-name "custom.el" user-emacs-directory))
(load custom-file 'noerror 'no-message)

;; early-init.elで大きくしたGCの閾値を、起動後に戻す
(add-hook 'emacs-startup-hook
          (lambda () (setq gc-cons-threshold (* 2 1000 1000))))

;; --------------------------------
;; 基本設定
;; --------------------------------
(use-package emacs
  :ensure nil
  :custom
  (inhibit-startup-screen t)
  (make-backup-files nil)
  (auto-save-default nil)
  (create-lockfiles nil)
  (tab-always-indent 'complete)
  :init
  (prefer-coding-system 'utf-8)
  (set-locale-environment "en_US.UTF-8")
  (show-paren-mode 1)
  :bind
  (("C-h" . delete-backward-char))
)

;; --------------------------------
;; 標準パッケージ
;; --------------------------------

;; savehist
(use-package savehist
  :ensure nil
  :init
  (savehist-mode 1)
)

;; recentf
(use-package recentf
  :ensure nil
  :init
  (recentf-mode 1)
  :custom
  (recentf-max-saved-items 200)
  (recentf-auto-cleanup 'mode)
  (recentf-autosave-interval 300) ; Emacs31から。5分ごとに履歴を自動保存
  ;; :bind -- consultでバインドを設定
  ;; (("C-x C-r" . recentf-open-files))
)

;; saveplace
(use-package saveplace
  :ensure nil
  :init
  (save-place-mode 1)
  :custom
  (save-place-autosave-interval 300) ; Emacs31から。5分ごとに位置を自動保存
)

;; which-key（Emacs30から標準搭載）
(use-package which-key
  :ensure nil
  :init
  (which-key-mode)
)

;; --------------------------------
;; 拡張パッケージ
;; --------------------------------

;; 検索ルール
;; orderless
(use-package orderless
  :custom
  (completion-styles '(orderless basic))
  (completion-category-defaults nil)
  (completion-category-overrides
    '((file (styles partial-completion)))
  )
)

;; UI強化
;; vertico
(use-package vertico
  :init
  (vertico-mode)
  :custom
  (vertico-cycle t)
)

;; marginalia
(use-package marginalia
  :init
  (marginalia-mode)
)

;; バッファー操作

;; consult
(use-package consult
  :bind
  (("C-x C-r" . consult-recent-file))
)

;; embark
(use-package embark
  :bind
  (("C-." . embark-act))
)

(use-package embark-consult
  :after (embark consult)
)

;; 入力補完

;; corfu
(use-package corfu
  :init
  (global-corfu-mode)
  :custom
  (corfu-cycle t)
  (corfu-auto t)
)

;;; init.el ends here
```

`init.el`は、Emacsの起動時に読み込まれる設定ファイルです。
上記は`package.el`と`use-package`（どちらもEmacs標準）を使ってパッケージを管理する、Emacs31向けの設定サンプルです。
初期設定としてオススメのパッケージも追加してあります。

```tree
~/.emacs.d/
|-- init.el
|-- early-init.el
|-- custom.el
```

:::{note}

正しくは`~/.emacs.el`もしくは`~/.emacs.d/init.el`が、起動時に読み込まれるファイルです。
設定内容が競合するため、どちらか片方のみ作成してください。
現在は後者を作成することが多いです。

:::

:::{note}

`custom.el`は、`M-x customize`などで自動生成される設定の保存先です。
`custom-file`で指定しておくと、`init.el`に自動生成のコードが混ざりません。

:::

## Emacs31での変更点

- `recentf-autosave-interval`と`save-place-autosave-interval`が追加されました。
  数値（秒）を指定すると、履歴や位置を定期的に自動保存します（デフォルトは`nil`で無効）。
  Lispから設定するときは`setq`ではなく`setopt`を使います（`use-package`の`:custom`ならそのまま使えます）。
- `lexical-binding`のクッキーがないファイルを読み込むと、警告が表示されるようになりました。
  `init.el`や`early-init.el`の1行目には`-*- lexical-binding: t -*-`を書いておきます。
- `site-start.el`が`early-init.el`より前に読み込まれるようになりました。
- `~/.emacs.d/user-lisp/`に置いたLispファイルが、自動でコンパイルされて`load-path`に追加されるようになりました。
- `package-refresh-contents`が、対話的に実行したときは非同期になりました。
- `which-key`はEmacs30から標準搭載です。`:ensure nil`を付けて標準パッケージとして扱います。

:::{note}

Emacs31の変更点は`NEWS`（`C-h n`）で確認できます。
上記はEmacs 31.1の`NEWS`から、このサンプルに関係するものを抜粋しています。

:::

## Emacs30以前では

```emacs
;;; init.el --- package.el + use-package setup (Emacs 30 and earlier) -*- lexical-binding: t -*-

;; --------------------------------
;; package.el + use-package (built-in)
;; --------------------------------
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; 初回起動時にパッケージ一覧を取得する
(unless package-archive-contents
  (package-refresh-contents))

(setq use-package-always-ensure t)

;; --------------------------------
;; custom-file
;; --------------------------------
(setq custom-file (expand-file-name "custom.el" user-emacs-directory))
(load custom-file 'noerror 'no-message)

;; early-init.elで大きくしたGCの閾値を、起動後に戻す
(add-hook 'emacs-startup-hook
          (lambda () (setq gc-cons-threshold (* 2 1000 1000))))

;; --------------------------------
;; 基本設定
;; --------------------------------
(use-package emacs
  :ensure nil
  :custom
  (inhibit-startup-screen t)
  (make-backup-files nil)
  (auto-save-default nil)
  (create-lockfiles nil)
  (tab-always-indent 'complete)
  :init
  (prefer-coding-system 'utf-8)
  (set-locale-environment "en_US.UTF-8")
  (show-paren-mode 1)
  :bind
  (("C-h" . delete-backward-char))
)

;; --------------------------------
;; 標準パッケージ
;; --------------------------------

;; savehist
(use-package savehist
  :ensure nil
  :init
  (savehist-mode 1)
)

;; recentf
(use-package recentf
  :ensure nil
  :init
  (recentf-mode 1)
  :custom
  (recentf-max-saved-items 200)
  (recentf-auto-cleanup 'mode)
  ;; :bind -- consultでバインドを設定
  ;; (("C-x C-r" . recentf-open-files))
)

;; saveplace
(use-package saveplace
  :ensure nil
  :init
  (save-place-mode 1)
)

;; --------------------------------
;; 拡張パッケージ
;; --------------------------------

;; 検索ルール
;; orderless
(use-package orderless
  :custom
  (completion-styles '(orderless basic))
  (completion-category-defaults nil)
  (completion-category-overrides
    '((file (styles partial-completion)))
  )
)

;; UI強化
;; vertico
(use-package vertico
  :init
  (vertico-mode)
  :custom
  (vertico-cycle t)
)

;; marginalia
(use-package marginalia
  :init
  (marginalia-mode)
)

;; which-key
(use-package which-key
  :init
  (which-key-mode)
)

;; バッファー操作

;; consult
(use-package consult
  :bind
  (("C-x C-r" . consult-recent-file))
)

;; embark
(use-package embark
  :bind
  (("C-." . embark-act))
)

(use-package embark-consult
  :after (embark consult)
)

;; 入力補完

;; corfu
(use-package corfu
  :init
  (global-corfu-mode)
  :custom
  (corfu-cycle t)
  (corfu-auto t)
)

;;; init.el ends here
```

Emacs31向けのサンプルとの違いは次のとおりです。

- `recentf-autosave-interval`と`save-place-autosave-interval`は、Emacs31より前には存在しません。
- `which-key`は、Emacs29以前では標準搭載されていないため、`:ensure nil`を付けずに`use-package`でインストールします。
  Emacs30では標準搭載なので、Emacs31向けのサンプルと同じ書き方もできます。
- `use-package`は、Emacs29から標準搭載です。Emacs28以前では別途インストールが必要です。

## early-initしたい（`~/.emacs.d/early-init.el`）

```emacs
;;; early-init.el --- early settings -*- lexical-binding: t -*-

;; パッケージの自動初期化を無効化
(setq package-enable-at-startup nil)

;; GCを一時的に大きくする
(setq gc-cons-threshold (* 50 1000 1000))
;; init.elの`emacs-startup-hook`で大きさを戻す

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
export XDG_CONFIG_HOME="$HOME/.config"
```

`XDG_CONFIG_HOME`が設定されていると
`~/.config/emacs/`にある設定が読み込まれるようになります。

:::{note}

最近のモダンなツールは設定ファイルを`~/.config/{ツール名}`に配置する傾向があります。
上記の環境変数を設定すれば、Emacsでも利用できます。
ただし、まだまだ`~/.emacs.d/`を使うほうが一般的なようです。
`~/.emacs.el`のときと同じですが、`~/.emacs.d/`と`~/.config/emacs/`も併用できません。

:::
