# タイプセットしたい（``latexmk``）

```bash
$ latexmk    # LaTeX用makeコマンド
$ lualatex ファイル名        # LuaLaTeX
$ ptex2pdf -l -u ファイル名  # upLaTeX
$ ptex2pdf -l ファイル名     # pLaTeX
```

LaTeX文書（=``.tex``ファイル）をコンパイルしてPDFなどを生成することをタイプセットと呼びます。


```{toctree}
---
maxdepth: 1
---
latex-latexmk
latex-lualatex
latex-uplatex
```
