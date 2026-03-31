# キーバインドしたい（`which-key`）

```emacs
(use-package which-key
  :config
  (which-key-mode)
)
```

`which-key`はEmacsのキーバインド入力を補助するパッケージです。
`C-x`などを入力した段階で、候補となるキーバインドを表示してくれます。
難解なキーバインドを覚えなくてよくなるので大変便利です。

:::{note}

Emacs v30からはEmacs本体の機能としてリリースされるようです。

:::

## リファレンス

- [justbur/emacs-which-key](https://github.com/justbur/emacs-which-key)
