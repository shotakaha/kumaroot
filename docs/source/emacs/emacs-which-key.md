# キーバインドしたい（`which-key`）

```emacs
(use-package which-key
  :init
  (which-key-mode)
  :custom
  (which-key-idle-delay 0.5)  ;; キーバインド候補が表示されるまでの待機時間（秒）; デフォルトは 1.0 秒
)
```

`which-key`はEmacsのキーバインド入力を補助するパッケージです。
`C-x`などを入力して少し待つと、続けて入力できるキーバインドの候補が表示されます。
キーバインドを正確に覚えていなくても、候補から探せるので便利です。

:::{note}
Emacs30からEmacs本体に標準で同梱されるようになりました。
Emacs29以前では`use-package`（または`package.el`など）でインストールが必要です。
:::

## リファレンス

- [justbur/emacs-which-key](https://github.com/justbur/emacs-which-key)
