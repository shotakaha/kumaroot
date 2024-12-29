# マイクロタイポグラフィしたい（``microtype``）

```latex
\usepackage{microtype}
```

マイクロタイポグラフィを実現するためのパッケージです。
和文フォントには適用されないオプションがあります。

「[マイクロタイポグラフィ](https://en.wikipedia.org/wiki/Microtypography)」は、
視覚的な妨害を最小限に抑えながら、文書の外観と読みやすさを向上させる技術のことだそうです。
ユーザーが気が付かないレベルで、文字や単語、行間、余白を調整してくれるみたいです。
（調整に気が付かないことが理想的のようです）

```latex
\documentclass[a4paper]{article}
\usepackage[protrusion=true, expansion=false]{microtype}
\usepackage{luatexja}
\usepackage{luatexja-fontspec}
\setmainfont{Times New Roman}  % 欧文フォント
\setmainjfont{Noto Serif CJK JP}  % 日本語フォント
```



## リファレンス

- {command}`texdoc microtype`
