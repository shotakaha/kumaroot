# 長さしたい（``\setlength``）

```latex
\setlength{\長さ名}{単位付きの数}
```

`\setlength`で用紙のサイズや、テキストエリアのサイズなどをカスタマイズできます。
このコマンドは本文エリア（`\begin{document}...\end{document}）で定義します。

:::{warning}

LaTeXで扱う長さを調べてみると、``\setlength``コマンドをを直接使うことはあまりオススメされていません。
基本はドキュメントクラスで用紙サイズを設定するか、``geometry``パッケージで設定するのが簡単でよい方法のようです。

とはいえ、公開されているパッケージでは``\setlength``で設定されている場合もあります。
ソースコードを読むときには知っておいたほうがよいでしょう。

:::

## 単位したい

LaTeXで利用できる長さについては[Length in LaTeX - Overleaf](https://www.overleaf.com/learn/latex/Lengths_in_LaTeX)が参考になります。

| 単位 | 説明 |
|---|---|
| `pt` | ポイント。約1/72.27インチ。 }
| `in` | インチ。25.4mm。 |
| `mm` | ミリメートル |
| `cm` | センチメートル |
| `ex` | 小文字の``x``の高さ。使用するフォントに依存。 |
| `em` | 大文字の``M``の横幅。使用するフォントに依存。 |
| `zw` | 和文フォントの文字幅。Zenkaku Width。LuaLaTeXでは`\zw`。|
| `zh` | zwと同じ大きさ。使わないほうがよい（とどこかでみた）|
| `truemm` | ``geometry``パッケージで使える（真の？）mm |

LaTeXの長さの単位です。
和文の場合は``zw``を長さの基準にするとよいと思います。

:::{note}

(u)pLaTeXでは``数zw``をそのまま使えますが、LuaLaTeXでは``数\zw``と書きます。
以下ではLuaLaTeXを想定して``\zw``で書いてます。

:::

## 行間したい（`\baselineskip`）

```latex
% 行送り（行間+文字の高さ）を設定
\setlength{\baselineskip}{1.5em}

% 数式の行間
\setlength{\abovedisplayskip}{1.5em}  % 数式の上側のアキ
\setlength{\belowdisplayskip}{1.5em}  % 数式の下側のアキ
```

## 段落したい（`\parindent` / `\parskip`）

```latex
% 段落のインデントを設定
\setlength{\parindent}{1\zw}

% 段落間のアキを設定
\setlength{\parskip}{2em}
```

## 段組したい（`\columnwidth` / `\columnsep`）

```latex
\setlength{\columnwidth}{20\zw} % 段の幅
\setlength{\columnsep}{1\zw}    % 段の間の長さ
```

## レイアウトしたい（`\paperwidth` / `\paperheight`）

```latex
\setlength{\paperwidth}{210mm}   % 用紙の幅
\setlength{\paperheight}{297mm}  % 用紙の高さ
\setlength{\textheight}{45\baselineskip}  % テキストエリアの高さ
\setlength{\textwidth}{1.2\linewidth}     % テキストエリアの長さ
```

`\paperwidth`と`\paperheight`でページサイズを変更できます。

また`\textheight`と`\textwidth`でテキスト領域を変更できます。
`mm`のような単位の他に、`\baselineskip`（行送り＝行間+文字の高さ）などでも指定できます。

## 余白したい

```latex
\setlength{\evensidemargin}{20mm}  % 偶数ページの余白
\setlength{\oddsidemargin}{20mm}   % 奇数ページの余白
\setlength{\topmargin}{20mm}       % 上マージン
```

## ヘッダー／フッターしたい（`\headsep` / `\footskip`）

```latex
\setlength{\headheight}{20mm}  % ヘッダーの高さ
\setlength{\headsep}{1.5em}    % ヘッダーと本文のアキ
\setlength{\footskip}{1.5em}   % フッターと本文のアキ
```

## 箇条書きしたい（`\itemsep` / `\labelsep`）

```latex
\setlength{\itemsep}{1\zw}  % 項目間のアキ
\setlength{\parsep}{1\zw}   % 項目間の段落のアキ
\setlength{\labelsep}{1\zw}  % ラベルと項目のアキ
\setlength{\leftmargin}{1\zw}  % リストの左側のアキ
```

## 画像したい

```latex
\includegraphics[width=0.8\textwidth]{画像ファイル名}
```

画像を挿入するときの横幅は`\textwidth`（もしくは`\linewidth`）を基準にするとよいです。

:::{hint}

`\textwidth`はページ内のテキストエリアの幅、
`\linewidth`は環境内のテキスト幅です。

:::

:::{seealso}

``jlreq``では、これらのほとんどがドキュメントクラスオプションで設定できます。

```latex
\documentclass[paper=a4paper, head_space=20mm, line_length=40zw, number_of_lines=45, gutter=20mm]{jlreq}
```

:::
