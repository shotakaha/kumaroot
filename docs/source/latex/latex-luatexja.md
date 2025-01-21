# 和文フォントしたい（``luatexja``）

```latex
\usepackage{luatexja}
```

LuaLaTeXの場合、`luatexja`パッケージを読み込むだけで和文フォントが使えます。
原の味フォント（`haranoaji`）が設定されます。

```latex
% compiler: LuaLaTeX
\documentclass{article}
\usepackage{luatexja}
```

ドキュメントクラスは`article`などの欧文用クラスでも大丈夫です。
テンプレートが配布されている海外の学会などで、一部（や一時的に）日本語を使いたい場合に役に立ちます。

:::{caution}

欧文用クラスの場合、`Contents`や`Abstract`、`Appendix`などのように
コマンドや環境で表示される内容が英語のまま出力されます。
局所的にカスタマイズすることはできますが、
日本語の文書を作成する場合は、素直に和文クラスを選ぶとよいです。

:::

```{toctree}
---
maxdepth: 1
---
latex-luatexja-preset
latex-luatexja-fontspec
latex-luatexja-otf
latex-luatexja-ruby
```
