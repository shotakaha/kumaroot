# LuaLaTeXを使いたい

``LuaLaTeX``を使う場合は、ドキュメントの基本設定を次のようにします。

```latex
\documentclass{jlreq}

\usepackage{graphicx}
\usepackage{hyperref}

\title{ドキュメントのタイトル}
\author{著者}
\date{\today}

\begin{document}

\maketitle

\end{document}
```

## ヘルプを確認したい

```bash
$ lualatex --help
```

- ``lualatex -h``は使えないので注意が必要です

## バージョンを確認したい

```bash
$ lualatex --version
This is LuaHBTeX, Version 1.15.0 (TeX Live 2022)
...(省略)...
```

## PDFを作成したい

```bash
$ lualatex main.tex
This is LuaHBTeX, Version 1.15.0 (TeX Live 2022)
...(省略)...
Output written on main.pdf (2 pages, 72580 bytes).
Transcript written on main.log.
```

- {command}`lualatex`コマンド1発でPDFを作成できます
