# サイズしたい（`\LARGE`）

```latex
\tiny  % 5pt
\scriptsize   % 7pt
\footnotesize  % 8pt
\small  % 9pt
\normalsize  % 10pt
\large  % 12pt
\Large  % 14.4pt
\LARGE  % 17.28pt
\huge  % 20.74pt
\Huge  % 24.88pt
```

本文中で局所的に文字サイズを切り替えることができます。
欧文フォントで``cm``（Computer Modern）を使っている場合、``\fontsize``コマンドでは任意のサイズに指定できません。
``fix-cm``パッケージを読み込むか、[lmodernパッケージ](latex-lmodern.md)を読み込んで``lm``（Latin Modern）に変更するとよいです。

```latex
\usepackage{fix-cm}

\fontsize{サイズ}{ベースラインスキップ}\selectfont
このフォントが変更されます。

\normalsize
デフォルトのフォントサイズ（10pt）に戻ります。
```
