# アノテーションしたい（`marginalia`）

```emacs-lisp
(use-package marginalia
  :ensure t
  :init
  (marginalia-mode 1)
  :custom
  (marginalia-align 'right)
)
```

`marginalia`は、ミニバッファーに表示される奉還候補に
アノテーション（補足説明）を追加する拡張パッケージです。

`M-x`したり、`M-x find-file`したりして表示された候補に対して、
コマンドの説明、
ファイルのサイズや種類、
バッファーの状態
などが右側に表示されるようになります。

:::{note}

`marginalia`単体では真価を発揮できません。
[vertico](./emacs-vertico.md) +
`consult`と一緒に使うのが一般的です。


:::
