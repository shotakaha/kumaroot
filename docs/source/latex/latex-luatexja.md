# 和文フォントしたい（``luatexja``）

```latex
\usepackage{luatexja}
```

LuaLaTeXの場合、``luatexja``パッケージを読み込むだけで和文フォントが使えます。
ドキュメントクラスは``article``などの欧文用クラスでも大丈夫です。
テンプレートが配布されている海外の学会などで、一部（や一時的に）日本語を使いたい場合に役に立ちます。

```latex
% compiler: LuaLaTeX
\documentclass{article}
\usepackage{luatexja}
```
