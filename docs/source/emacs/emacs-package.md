# パッケージ管理したい（`package`）

```emacs
(require 'package)
(setq package-archives
      '(("gnu" . "https://elpa.gnu.org/packages/")
        ("melpa" . "https://melpa.org/packages")))

;; Emacs27+では不要だが互換性のため書いてもOK
;; (package-initialize)
```

Emacs24からパッケージ管理システムがデフォルトで使えるようになりました。
拡張パッケージは、
公式（GNU ELPA）とコミュニティ（MELPA）から取得できます。

:::{note}

Emacs27以降では`package-initialize`が自動実行されるようになりました。
古めの記事には残っていることがありますが、現在は明示的に書く必要はありません。

:::

:::{note}

現在では、実質終了してしまったプロジェクトのようですが、
パッケージ管理が過渡期であったことには`Marmalade`という
（おいしそうな）リポジトリがありました。

:::

## パッケージを追加したい（`package-list-packages`）

```emacs
M-x package-list-packages
;; i -> インストールの予約
;; x -> インストールを実行
;; d -> 削除
```

`package-list-packages`コマンドで、Emacsの中からパッケージを追加できます。
取得したパッケージは`~/.emacs.d/elpa/`にインストールされます。

:::{note}

`package.el`はEmacsのパッケージ管理システムの基盤です。
現在は、その上に構築された`use-package`や`elpaca`を使って設定することが多いです。

:::
