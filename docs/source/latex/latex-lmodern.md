# 欧文フォントしたい（``lmodern``）

```latex
% (u)platex
% プリアンブル
\usepackage[T1]{fontenc}
\usepackage{lmodern}
```

`lmodern`は(u)pLaTeXの欧文フォントをLatin Modern系に設定するパッケージです。
[fontenc](latex-fontenc.md)パッケージと合わせて、かならず読み込んでおくとよいです。

セリフ体
:   Latin Modern Roman (lmr)

サンセリフ体
:   Latin Modern Sans Serif (lmss)

タイプライタ体
:   Latin Modern Typewrite Type (lmtt)

:::{note}

LuaLaTeXはLatin Modern系がデフォルトになっているので、読み込む必要はありません。

:::
