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
