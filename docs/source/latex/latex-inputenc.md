# UTF8を読み込みたい（``inputenc``）

```{note}
2018年4月から(u)pLaTeXもUTF8が標準になっているため、
この設定はもう必要ありません。
詳細はLaTeX Newsで確認できます（`texdoc ltnews28`）。
```

```latex
% プリアンブル
\usepackage[utf8]{inputenc}
```

(u)pLaTeXで入力``.tex``ファイルのエンコーディングを指定するパッケージです。
LuaLaTeXはUTF8を前提にしているので、このパッケージは不要です。
