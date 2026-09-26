# 物理したい（`physics-patch`）

```latex
\usepackage{siunitx}
\usepackage{physics-patch}
\AtBeginDocument{\RenewCommandCopy\qty\SI}
```

`physics-patch`は、[physics](./latex-physics.md)パッケージを改良・拡張したパッケージです。
`physics`パッケージのコマンドをそのまま使えるようにしつつ、いくつかの機能を追加しています。

改良されたコマンドは`PT`（Physics Patch）という接頭辞を付けて使えるようになっています。
