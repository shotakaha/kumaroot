# ``jlreq``クラスを使いたい

```latex
\documentclass{jlreq}  % articleに相当
\documentclass[report]{jlreq}  % reportに相当
\documentclass[book]{jlreq}  % bookに相当
```

``jlreq``はLuaLaTeX、(u)pLaTeXに対応しているドキュメントクラスです。
これから新しく文書を作成する場合は、迷わず使うとよいと思います。

JLReqはW3Cワーキンググループで議論されている「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」です。
``jlreq``パッケージはこの要件の実装を試みたクラスファイルです。



## フォントサイズを変更したい

```latex
\documentclass[fontsize=10pt]{jlreq}    % 欧文フォント
\documentclass[jafontsize=10pt]{jlreq}  % 和文フォント
\documentclass[jafontscale=1]           % 和文/欧文のフォントサイズ比

\documentclass[jafontsize=12Q, jafontscale=0.92]{jlreq}     % LaTeX美文書作成入門（改訂第8版）
```

欧文フォントと和文フォントのサイズをそれぞれ、
もしくはサイズ比を指定できます。
``fontsize``と``jafontsize``の両方が指定されている場合、
``jafontscale``は無視されます。
フォントサイズに小数点を使うことができます。

```{note}
LaTeXで使う``pt``はDTPソフトのポイントサイズと異なります。
DTPポイントで指定する場合は``bp``（big point）を使います。
```

## 1行あたりの文字数を指定したい

```latex
\documentclass[line_length=40zw]{jlreq}  % 全角40文字（デフォルト）
\documentclass[line_length=28zw]{jlreq}  % 全角28文字
```

## 1ページあたりの行数を指定したい

```latex
\documentclass[number_of_lines=30]{jlreq}  % 30行（デフォルト）
\documentclass[number_of_lines=27]{jlreq}  % 27行
```

## レポートを作成したい

```latex
\documentclass[report]{jlreq}
```

トップレベルが章（``\chapter``）の文書ができます。
**片面印刷を想定**して、左右ページのデザインは同じです。

## 書籍を作成したい

```latex
\documentclass[book]{jlreq}
```

トップレベルが章（``\chapter``）の文書ができます。
**両面印刷を想定**して、左右ページのデザインが異なっています。

## 余白を調整したい

```latex
\documentclass[head_space=25.4mm]{jlreq}    % 天の空き
\documentclass[foot_space=25.4mm]{jlreq}    % 地の空き
\documentclass[gutter=25.4mm]{jlreq}        % ノドの空き
\documentclass[headfoot_sidemargin=0pt]{jlreq}  % 柱やノンブルの左右の空き
```

**ノド**
:   ページを綴じる側の余白です。左右ページが同じデザインの場合、横組なら左マージン、縦組なら右マージンです。

**ノンブル**
:   各ページに振るページ番号です。

**柱**
:   各ページの上か下に出力する章や節の名前です。

## 二段組にしたい

```latex
\documentclass[twocolumn, column_gap=2zw]{jlreq}  % 二段組
```

二段組したときの段間（``column_gap``）を指定できます。

## ぶら下げ組にしたい

```latex
\documentclass[hanging_puctuation]{jlreq}
```

## リファレンス

- {command}`jlreq`
