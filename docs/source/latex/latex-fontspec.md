# 欧文フォントしたい（`fontspec`）

```latex
% lualatex
% プリアンブル
\usepackage{fontspec}
\setmainfont{Source Serif Pro}
\setsansfont{Source Sans Pro}
\setmonofont{Source Code Pro}
```

`fontspec`でUnicode対応のフォントを自由に設定できます。
手持ちのフォントを有効活用できます。

:::{note}

TeXLive2020以降では、デフォルトが
欧文フォントは**Latin Modern系（lmodern）**、
和文フォントは**原ノ味系（haranoaji）**が
なっています。

:::

## 本文フォントしたい（`\setmainfont`）

```latex
% プリアンブル
\setmainfont{フォント名}[詳細設定]

\setmainfont{HiraginoSans}[
    BoldFeature={HiraginoSans-W8},
    ItalicFeature={HiraginoSans-W7},
    BoldItalicFeatures={HiraginoSans-W9},
    SlantedFeature{HiraginoSans-W6},
    SmallCapsFeature={...},
    UprightFeature={HiraginoSans-W5},
]
```

`\setmainfont{}`で欧文の本文フォントを変更できます。
セリフ体のフォントを設定することが多いです。
シリーズ（ウェイト）は軽めにするとよいです。

## 見出しフォントしたい（`\setsansfont`）

```latex
% プリアンブル
\setsansfont{フォント名}[フォント詳細]
```

`\setsansfont{}`で欧文の見出しフォントを変更できます。
サンセリフ体のフォントを設定することが多いです。
シリーズ（ウェイト）は重めにするとよいです。

## 等幅フォントしたい（`\setmonofont`）

```latex
% プリアンブル
\setmonofont{フォント名}[フォント詳細]
```

`\setmonofont{}`で欧文の等幅フォントを変更できます。
モノスペース体のフォントを設定することが多いです。
シリーズ（ウェイト）は軽めがよいと思います。

## 強調したい（`\strong`）

```latex
% 本文
fontspecパッケージを追加すると
\strong{strong}で\strong{強調}できます。
```

`\strong{}`で**太字で強調**できます。

## 数式フォントしたい（`no-math`）

```latex
% プリアンブル
\usepackage[no-math]{fontspec}
\usepackage{unicode-math}
```

`no-math`オプションで、`fontspec`による数式フォントの変更を無効にできます。
[unicode-mathパッケージ](./latex-unicode-math.md)などで、数式フォントを別に設定する場合は、このオプションを設定しておくとよいかもしれません。

## 依存パッケージ

```console
$ kpsewhich fontspec.sty | xargs cat | rg RequirePackage
\RequirePackage{xparse}
// LuaTeXの場合
\RequirePackage{luaotfload}
\RequirePackage{fontspec-luatex}
// XeTeXの場合
\RequirePackage{fontspec-xetex}
```
