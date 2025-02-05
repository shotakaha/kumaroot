# 差分したい（`latexdiff`）

```console
$ latexdiff --version
This is LATEXDIFF 1.3.4 (Algorithm::Diff 1.15 so, Perl v5.34.1)

$ latexdiff [オプション] old.tex new.tex > diff.tex
```

`latexdiff`コマンドで2つのLaTeXファイルの差分を抽出できます。
差分は標準出力（stdout）に表示されるため、
ファイルにリダイレクトして保存できます。

```console
$ latexdiff-vc --version
This is LATEXDIFF-VC 1.3.4

$ latexdiff-vc old.tex new.tex > diff.tex
$ latexdiff-vc --git -r file1.tex > diff.tex
$ latexdiff-vc --git -r rev1 file1.tex > diff.tex
$ latexdiff-vc --git -r rev1 -r rev2 file1.tex > diff.tex
```

バージョン管理システム（VCS）を使っている場合は、
`latexdiff-vc`で過去のリビジョンと差分を抽出できます。
Gitを使っている場合は`--git`オプションをつけます。
