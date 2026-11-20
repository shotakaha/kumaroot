# UTF8を読み込みたい（`inputenc`）

```{note}
2018年4月から、pdfTeXを使うLaTeXの標準の入力エンコーディングがUTF-8になりました。
(u)pLaTeXも、UTF-8の入力として動作することを確認しています。
そのため、この設定はもう必要ありません。
詳細はLaTeX Newsで確認できます（`texdoc ltnews28`）。
```

```latex
% プリアンブル
\usepackage[utf8]{inputenc}
```

`inputenc`は、入力ファイルのエンコーディングを指定するパッケージです。
LuaLaTeXはUTF8を前提にしているので、このパッケージは不要です。
