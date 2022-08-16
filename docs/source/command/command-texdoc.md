# texdoc

LaTeXのコマンドやパッケージのドキュメントを検索するコマンドです

## ドキュメントを開く

```bash
texdoc パッケージ名
```

## 検索結果を表示する

```bash
texdoc -l パッケージ名
texdoc --list パッケージ名
```

試しに{command}`texdoc -l jlreq``した結果は以下のようになりました。
全部で13個のファイルがヒットしています。

一番最後の出力で聞かれているように、番号を入力するとそのファイルが開きます。
PDFはビューワー、HTMLはブラウザで開くことができ、
テキストファイルはそのままターミナルに出力されます。

空欄のまま``RET``を押すと最初のドキュメントが開いてしまうので、
何も表示しない場合は``n``を入力して閉じるようにしています
（表示されている番号以外の文字ならなんでもよいです）。

```bash
texdoc -l jlreq
 1 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq-ja.pdf
   = [ja] Package documentation
 2 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq.pdf
   = Package documentation
 3 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq-ja.html
 4 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq.html
 5 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/README-ja.md
   = [ja] Readme
 6 /usr/local/texlive/2022/texmf-dist/doc/platex/jlreq-deluxe/jlreq-deluxe.pdf
   = [ja] Package documentation
 7 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq-trimmarks-ja.html
 8 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq-trimmarks.html
 9 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq-trimmarks-ja.md
10 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/jlreq-trimmarks.md
11 /usr/local/texlive/2022/texmf-dist/doc/latex/jlreq/README.md
   = Readme
12 /usr/local/texlive/2022/texmf-dist/doc/platex/jlreq-deluxe/README-ja.md
   = Readme (Japanese)
13 /usr/local/texlive/2022/texmf-dist/doc/platex/jlreq-deluxe/README.md
   = Readme (English)
Enter number of file to view, RET to view 1, anything else to skip:
```
