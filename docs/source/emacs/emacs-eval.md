# S式を評価したい（`eval-last-sexp`）

```emacs-lisp
(use-package emacs
  :bind (
    ("C-c e" . eval-last-sexp)
    ("C-c r" . eval-region)
    ("C-c b" . eval-buffer)
    ("M-:" . eval-expression)
  )
)
```

EmacsのS式はファイルに保存しただけでは反映されません。
ファイル（や該当する行）を読み込んで「評価」する必要があります。
S式の評価をよく使う場合、上記サンプルのようにキーバインドを設定するとよいかもしれません。

```text
M-x eval-last-sexp
C-x C-e
```

`eval-last-sexp`でカーソル直前のS式を評価（＝実行）できます。
デフォルトで`C-x C-e`にバインドされています。
`init.el`に設定を追加した後、その行末で`C-x C-e`を実行すると、その設定行だけ即時反映できます。

## バッファーを評価したい（`eval-buffer`）

```text
M-x eval-buffer
```

`eval-buffer`でバッファー全体を評価できます。
`init.el`を大きく書き換えた時に、Emacsを再起動せずに設定全体をまとめて反映できます。

:::{note}

Emacsを再起動すれば`init.el`を再読み込みできます。
`eval-buffer`を使えば、再起動が不要です。

:::

## リージョンを評価したい（`eval-region`）

```text
M-x eval-region
```

`eval-region`で選択した範囲のS式をまとめて評価できます。
複数の設定ブロックだけをまとめて試すことができます。

## 関数を評価したい（`eval-defun`）

```text
M-x eval-defun
```

`eval-defun`で関数全体を評価できます。
関数を作成しているときに使います。

## ミニバッファーで評価したい（`eval-expression`）

```text
M-x eval-expression
M-:
```

`eval-expression`でミニバッファーにS式を入力して評価できます。
設定値を確認したり、簡易電卓の代わりに利用できます。
