# 長さしたい（``setlength``）

```latex
\setlength{\長さ名}{単位付きの数}
```

用紙のサイズや、テキストエリアのサイズなど``\setlength``を使ってカスタマイズできます。
LaTeXで利用できる長さについては[Length in LaTeX - Overleaf](https://www.overleaf.com/learn/latex/Lengths_in_LaTeX)が参考になります。

:::{warning}

LaTeXで扱う長さを調べてみると、``\setlength``コマンドをを直接使うことはあまりオススメされていません。
基本はドキュメントクラスで用紙サイズを設定するか、``geometry``パッケージで設定するのが簡単でよい方法のようです。

とはいえ、公開されているパッケージでは``\setlength``で設定されている場合もあります。
ソースコードを読むときには知っておいたほうがよいでしょう。

:::

## 単位したい

| 単位 | 説明 |
|---|---|
| pt | ポイント。約1/72.27インチ。 }
| in | インチ。25.4mm。 |
| mm | ミリメートル |
| cm | センチメートル |
| ex | 小文字の``x``の高さ。使用するフォントに依存。 |
| em | 大文字の``M``の横幅。使用するフォントに依存。 |
| zw | 和文フォントの文字幅。Zenkaku Width。|
| zh | zwと同じ大きさ。使わないほうがよい（とどこかでみた）|
| truemm | ``geometry``パッケージで使える（真の？）mm |

LaTeXの長さの単位です。
和文の場合は``zw``を長さの基準にするとよいと思います。

:::{note}

(u)pLaTeXでは``数zw``をそのまま使えますが、LuaLaTeXでは``数\zw``と書きます。
以下ではLuaLaTeXを想定して``\zw``で書いてます。

:::

## 段落したい

```latex
\setlength{\linewidth}{40\zw}     % 1行の長さ
\setlength{\baselineskip}{1.5\zw} % 行送りの大きさ（＝行間の高さ）
\setlength{\parindent}{1\zw}      % 段落のインデント
\setlength{\parskip}{1\zw}        % 段落の間の高さ
```

## 段組したい

```latex
\setlength{\columnwidth}{20\zw} % 段の幅
\setlength{\columnsep}{1\zw}    % 段の間の長さ
```

## レイアウトしたい

```latex
\setlength{\paperwidth}{210mm}   % 用紙の幅
\setlength{\paperheight}{297mm}  % 用紙の高さ
\setlength{\textheight}{45\baselineskip}  % テキストエリアの高さ
\setlength{\textwidth}{1.2\linewidth}     % テキストエリアの長さ
```

## 余白したい

```latex
\setlength{\evensidemargin}{20mm}  % 偶数ページの余白
\setlength{\oddsidemargin}{20mm}   % 奇数ページの余白
\setlength{\topmargin}{20mm}       % 上マージン
```

## 画像したい

```latex
\includegraphics[width=0.8\textwidth]{画像ファイル名}
```

画像を挿入するときの横幅は``\textwidth``を基準にするとよいです。

:::{seealso}

``jlreq``では、これらのほとんどがドキュメントクラスオプションで設定できます。

```latex
\documentclass[paper=a4paper, head_space=20mm, line_length=40zw, number_of_lines=45, gutter=20mm]{jlreq}
```

:::
