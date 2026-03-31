# パッケージ管理したい（`use-package`）

```emacs
(require 'package)

(setq package-archives
      '(("gnu" . "https://elpa.gnu.org/packages/")
        ("melpa" . "https://melpa.org/packages/"))
)

(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package)
)

(eval-when-compile
  (require 'use-package)
)

(setq use-package-always-ensure t
      use-package-expand-minimally t
      use-package-compute-statistics t
)

```

`use-package`はパッケージ管理を強化するパッケージです。
Emacs24から利用がはじまり、Emacs27あたりから、標準的なパッケージとして使われています。

## パッケージを読み込みたい

```emacs
;; before
(require 'foo)

;; after
(use-package foo)
```

これまで`require`していたパッケージを、`use-package`に置き換えるだけです。

## 変数を設定したい（`:custom` / `:init` / `:config`)

```emacs
;; これまで
(require 'foo)
(setq foo-option t)

;; 置き換え
(use-package foo
  :custom
  (foo-custom t)
  :init
  (message "before loading foo")
  (setq foo-before t)
  :config
  (message "after loading foo")
  (setq foo-after t)
)
```

`:custom`オプションで、パッケージ設定を宣言的に変更できます。
これは内部的に`custom-set-variable`を使用しています。

これまでのように`setq`を使って設定することもできます。
`:init`オプションは、パッケージを読み込む前、
`:config`オプションは、パッケージを読み込んだ後に実行されます。

:::{note}

`:init`や`:config`では、任意のElispコードを使って自由に設定できます。
しかし、よほどのElisp上級者でない限り、`:custom`で設定変更することをオススメします。

:::

## フックしたい（`:hook`）

```emacs
(require 'foo)
(add-hook 'foo-mode-hook #'function)

(use-package foo
  :hook
  (foo-mode . func)
)
```

`:hook`オプションで、パッケージを読み込んだときのフックを設定できます。
これは`add-hook`の置き換えです。

## キーバインドしたい（`:bind`）

```emacs
(require 'foo)
(global-set-key (kbd "C-key bind") 'foo-function)

(use-package foo
  :bind
  ("C-key bind" . foo-function)
)
```

`:bind`オプションで、パッケージごとにキーバインドを設定できます。
これは`global-set-key`と`kbd`関数の置き換えです。

## よく使うパッケージしたい

```emacs
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
  (completion-category-overrides nil)
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
