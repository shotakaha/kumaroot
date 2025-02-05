# 結合したい（`latexpand`）

```console
$ latexpand --version
latexpand version v1.7.2.

$ latexpand [オプション] ファイル.tex > expanded.tex
$ latexpand --keep-comments ファイル.tex > expanded.tex

// 結合したファイルをPDFに出力
$ latexmk expanded.tex
```

`latexpand`で、`\include{}`や`\input{}`などした内容を
ひとつのファイルに結合し、コメントを削除できます。
`--keep-comments`オプションでコメントを残せます。
