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
```

`\setmainfont{}`で欧文の本文フォントを変更できます。
セリフ体のフォントを設定することが多いです。
シリーズ（ウェイト）は軽めにするとよいです。

## 見出しフォントしたい（`\setsansfont`）

```latex
% プリアンブル
\setsansfont{フォント名}
```

`\setsansfont{}`で欧文の見出しフォントを変更できます。
サンセリフ体のフォントを設定することが多いです。
シリーズ（ウェイト）は重めにするとよいです。

## 等幅フォントしたい（`\setmonofont`）

```latex
% プリアンブル
\setmonofont{フォント名}
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
