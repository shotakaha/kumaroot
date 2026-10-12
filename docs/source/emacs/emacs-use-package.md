# パッケージ管理したい（`use-package`）

```emacs
(require 'package)

;; MELPAリポジトリを追加
;;GNU ELPAとNonGNU ELPAは標準で登録済み
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)

(setq use-package-always-ensure t        ;; 未インストールのパッケージを自動でインストール
      use-package-expand-minimally t     ;; 展開後のコードを簡素にする
      use-package-compute-statistics t   ;; 起動時間の統計をとる（M-x use-package-report）
)
```

`use-package`は、Emacsのパッケージ管理を強化するためのパッケージです。
パッケージ設定を宣言的に書くことができ、パッケージの遅延読み込みや、キーバインドの設定、フックの追加など、設定ファイルを見通しよく整理できます。
また、`package.el`と連携して、パッケージのインストールも自動化できます。
Emacs23のころに登場し、Emacs29から標準で同梱されるようになりました。

:::{note}
**Emacs28以前**では`use-package`が同梱されていないため、先にインストールする必要があります。
また、`package-archives`に`gnu`の登録が必要な場合があります。

```emacs
;; リポジトリを追加
(setq package-archives
      '(("gnu" . "https://elpa.gnu.org/packages/")
        ("melpa" . "https://melpa.org/packages/"))
)

;; use-packageをインストール
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package)
)

;; use-packageを読み込む
(eval-when-compile
  (require 'use-package)
)
```
:::

## パッケージを読み込みたい

```emacs
;; before
(require 'foo)

;; after
(use-package foo)
```

これまで`require`していたパッケージを、`use-package`に置き換えるだけです。
`use-package-always-ensure`が`t`なので、未インストールのパッケージは自動でインストールされます。

```emacs
(use-package dired
  :ensure nil
)
```

Emacs本体に同梱されているパッケージは、`:ensure nil`でインストールを省略できます。


## パッケージ設定したい（`:custom` / `:init` / `:config`）

```emacs
;; これまで
(require 'foo)
(setq foo-option t)

;; 置き換え
(use-package foo
  :custom
  (foo-option t)
  :init
  (message "before loading foo")
  :config
  (message "after loading foo")
  (foo-mode 1)
)
```

`:custom`、`:init`、`:config`オプションで、パッケージの設定を宣言的に管理できます。
変数の設定は`:custom`に、モードの有効化や関数の呼び出しは`:init`や`:config`に書く、と使い分けます。

`:custom`オプションは、パッケージの変数を設定します。
内部的に`customize-set-variable`を使用しています。

`:init`オプションは、パッケージを**読み込む前**に実行されます。
`:config`オプションは、パッケージを**読み込んだ後**に実行されます。


:::{note}
デフォルトで遅延読み込みが有効になっています。
後述する`:hook`や`:bind`を使うと、パッケージは必要になるまで読み込まれません。
`:config`の設定も、パッケージが読み込まれるまで実行されません。
起動時に必ず実行したい設定は、`:init`に書く必要があります。
:::

## フックしたい（`:hook`）

```emacs
;; これまで
(add-hook 'foo-mode-hook #'my-func)

;; 置き換え
(use-package foo
  :hook
  (foo-mode . my-func)
)
```

`:hook`オプションで、モードが有効になったときに実行する関数を設定できます。
これは`add-hook`の置き換えです。

フック名には、自動的に`-hook`が付きます。
`foo-mode`と書くと`foo-mode-hook`に登録されます。

## キーバインドしたい（`:bind`）

```emacs
;; これまで
(global-set-key (kbd "C-c f") #'foo-function)

;; 置き換え
(use-package foo
  :bind
  ("C-c f" . foo-function)
)
```

`:bind`オプションで、キーバインドを設定できます。
これは`global-set-key`と`kbd`関数の置き換えです。
コマンドが初めて呼ばれたときにパッケージを読み込みます。

## リポジトリ指定したい（`:vc`）

```emacs
(use-package some-package
  :vc (:url "https://github.com/user/repo"
       :rev :newest
       :branch "main"
      )
)
```

`:vc`オプションで、パッケージをGitリポジトリから直接インストールできます。
Emacs30で追加された機能です。
MELPAなどに登録されていないパッケージや、開発中のバージョンを使いたいときに便利です。

`:rev`には、`:newest`（最新のコミット）のほか、タグやコミットを文字列で指定できます。

:::{note}
Emacs29以前では、リポジドリ指定する場合は`straight.el`パッケージを使います。
`straight.el`は`package.el`とは別のパッケージ管理ツールで、`use-package`との連携設定が必要です。

```emacs
(use-package some-package
  :straight (some-package
             :type git
             :host github
             :repo "user/repo"
             :branch "main"
            )
)
```
:::

## オススメのパッケージを設定したい

```emacs
(use-package emacs
  :bind
    (
      ("C-h" . backward-delete-char)   ;; C-hでバックスペース
      ("C-c h" . help-command)         ;; C-c hでヘルプ
      ("C-x C-b" . ibuffer)            ;; C-x C-bでibuffer
    )  
)

(use-package which-key
  :config
  (which-key-mode)
)

(use-package vertico
  :init
  (vertico-mode)
)

(use-package orderless
  :custom
  (completion-styles '(orderless basic))
  (completion-category-defaults nil)
  (completion-category-overrides '((file (styles basic partial-completion))))
)

(use-package marginalia
  :init
  (marginalia-mode)
)

(use-package consult
  :bind
  (("C-s" . consult-line)
   ("C-x b" . consult-buffer))
)

(use-package magit
  :bind ("C-x g" . magit-status)
)
```

- `which-key`：押したキーの続きの候補を表示します。Emacs30から標準で同梱されています。
- `vertico`：ミニバッファの候補を縦に表示します。
- `orderless`：スペース区切りで、順不同に絞り込めます。ファイルパスの補完は、`partial-completion`で従来の挙動を残しています。
- `marginalia`：候補に説明などの注釈を表示します。
- `consult`：行や、バッファの検索を強化します。`C-s`は標準の`isearch`を置き換えます。
- `magit`：Gitの操作ができます。
