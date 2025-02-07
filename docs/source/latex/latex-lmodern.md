# Latin Modernしたい（`lmodern`）

```latex
% (u)platex
% プリアンブル
\usepackage[T1]{fontenc}
\usepackage{lmodern}
```

`lmodern`で、(u)pLaTeXの欧文フォントをLatin Modern系に設定するパッケージです。
[fontenc](latex-fontenc.md)パッケージと合わせて、かならず読み込んでおくとよいです。

:::{note}

LuaLaTeXはLatin Modern系がデフォルトになっているので、読み込む必要はありません。

:::

| ファミリー | シリーズ | シェープ | フォント名 |
|---|---|---|---|
| `lmr` | m | n | LMRoman10-Regular |
| `lmr` | m | it | LMRoman10-Italic |
| `lmr` | m | sl | LMRomanSlant10-Regular |
| `lmr` | b | n | LMRomanDemi10-Regular |
| `lmr` | bx | n | LMRoman10-Bold |
| `lmss` | m | n | LMSans10-Regular |
| `lmss` | b, bx | n | LMSans10-Bold |
| `lmtt` | m | n | LMMono10-Regular |
| `lmtt` | m | it | LMMono10-Italic |
