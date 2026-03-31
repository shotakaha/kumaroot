# Emacsクライアントしたい（`emacsclient`）

```console
// デーモンを起動
emacs --daemon

// 別セッションからデーモンに接続
// ターミナル内で開く
emacsclient -nw ファイル名

// GUIで開く
emacsclient ファイル名

```

`emacsclient`で、既存のEmacsデーモン（常駐プロセス）に接続してファイルを開くことができます。
複数のターミナルから起動した`emacsclient`から同じEmacsセッションを共有できます。

:::{note}

`vim`に対する`Emacs`のデメリットとして起動が遅いことが挙げられます。
それはきっと、Emacsをきちんと使ったことがない人の戯言です。
デーモン運用で起動コストを省略すれば、Emacsの真価を体感できるはずです。

:::

## デーモン設定したい（`server-start`）

```emacs
(use-package server
  :ensure nil
  :custom
  (setq server-kill-new-buffers t)
  :config
  (unless (server-running-p)
    (server-start)
  )
)
```

`server-start`でEmacsデーモンを起動できます。
設定ファイル（`init.el`）の必須設定のひとつです。
