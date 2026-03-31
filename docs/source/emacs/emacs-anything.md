# anythingしたい（`anything`）

```emacs
(require 'anything)
(require 'anything-config)
(global-set-key (kbd "M-x") 'anything-M-x)
```

```emacs
(use-package anything
  :ensure t
  :config
  (require 'anything-config)
  :bind
  (("M-x" . anything-M-x)
   ("C-x b" . anything)
  )
)
```

`anything`は、2010年ころのEmacs環境で使われていた「なんでもできる」UI拡張パッケージです。
バッファーの情報を一箇所に集約することで、
コマンド検索、ファイル検索、バッファー切り替えなどすべてを統一的に操作できます。

`anything`は、Emacsにおけるコマンドパレット思想の原点です。
現在は、後継として
`helm` ->
[ivy](./emacs-ivy.md) ->
[vertico](./emacs-vertico.md)
へと発展しています。

:::{note}

学生の時に、Emacs操作を一番助けてくれた印象深いパッケージです。
`anything`開発者のるびきち（rubikitch）さんの本やブログにもお世話になりました。

:::
