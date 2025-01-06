# フォントしたい

```latex
\usepackage{luatexja-fontspec}

% 欧文フォントの設定
\setmainfont{KiwiMaru-Regular}
\setsansfont{ReggaeOne-Regular}
\setmonofont{HackGen35Console-Regular}

% 和文フォントの設定
\setmainjfont{KiwiMaru-Regular}
\setsansjfont{ReggaeOne-Regular}
\setmonojfont{HackGen35Console-Regular}
```

LuaLaTeXでは、任意のフォントを簡単に埋め込むことができます。
(u)pLaTeXは、地獄（だった？）のでオススメしません。

:::{hint}

最近のTeXLiveでは、欧文フォントは**Latin Modern**、和文フォントは**原の味**がデフォルトになっているため、わざわざフォントを変える必要はないと思います。

:::

```{toctree}
---
maxdepth: 1
---
latex-font-family
latex-font-series
latex-font-shape
latex-font-size
latex-fonts-more
latex-japanese
```

```{toctree}
---
maxdepth: 1
caption: LuaLaTeXしたい
---
latex-luatexja
latex-luatexja-preset
latex-luatexja-fontspec
latex-luatexja-otf
latex-luatexja-ruby
```

```{toctree}
---
maxdepth: 1
caption: (u)pLaTeX
---
latex-kanji-config-udpmap-sys
latex-otf
```
