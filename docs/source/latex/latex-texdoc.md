# ドキュメントを確認したい（`texdoc`）

```console
$ texdoc --version
Texdoc 4.1 (2024-03-10)

$ texdoc パッケージ名
```

`texdoc`はLaTeXパッケージやTeX関係のツールのドキュメント（主にPDF）を開くコマンドです。
ウェブ検索などしても使い方がでわからない場合は、このドキュメントを読んでみるとよいです。
このコマンドで開かれるPDFは、開発者（もしくは開発グループ）が作成した一次ソースです。

## コマンドの使い方を確認したい

```console
$ texdoc tlmgr
$ texdoc kpsewhich
$ texdoc latexmk
$ texdoc texdoc  # texdoc自身
```

`tlmgr`や`kpsewhich`などのコマンドの使い方も`texdoc`で確認できます。
`texdoc`自身の使い方も確認できます。

## ドキュメントクラスを確認したい

```console
$ texdoc article
$ texdoc jlreq
$ texdoc jsclasses  # jsarticleやjsbook
```

`article`や`jlreq`などのドキュメントクラスの使い方も確認できます。
`jsarticle`と`jsbook`は`jsclasses`で確認できます。

## パッケージを確認したい

```console
$ texdoc minipage
$ texdoc graphicx
$ texdoc tikz-feynman
$ texdoc feynmp-auto
$ texdoc minted
$ texdoc luatexja
```

LaTeXのパッケージやコマンドの使い方を確認できます。
