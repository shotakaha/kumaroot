# 差分したい（`latexdiff`）

```console
$ latexdiff --version
This is LATEXDIFF 1.3.4 (Algorithm::Diff 1.15 so, Perl v5.34.1)

$ latexdiff [オプション] old.tex new.tex > diff.tex
$ latexdiff --flatten old.tex new.tex > diff.tex
```

`latexdiff`コマンドで2つのLaTeXファイルの差分を抽出できます。
差分は標準出力（stdout）に表示されるため、
ファイルにリダイレクトして保存できます。

`--flatten`オプションで、
文書内の`\include{}`や`\input{}`を展開して、
差分を取得できます。

```console
$ latexdiff-vc --version
This is LATEXDIFF-VC 1.3.4

$ latexdiff-vc --flatten old.tex new.tex > diff.tex
$ latexdiff-vc --git --flatten -r ファイル.tex > diff.tex
$ latexdiff-vc --git --flatten -r rev1 ファイル.tex > diff.tex
$ latexdiff-vc --git --flatten -r rev1 -r rev2 ファイル.tex > diff.tex

// 差分をPDFに変換
$ latexmk diff.tex
```

バージョン管理システム（VCS）を使っている場合は、
`latexdiff-vc`で過去のリビジョンと差分を抽出できます。
Gitを使っている場合は`--git`オプションをつけます。
