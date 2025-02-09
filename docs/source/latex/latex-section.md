# 見出ししたい（`\section`）

```latex
\part{部}
\chapter{章}
\section{節}
\subsection{項}
\subsubsection{目}
\paragraph{段落}
\subparagraph{小段落}
```

見出しは、自分で**太字**などにせず、専用のコマンドを使います。
見出しには
部（`\part{}`）、
章（`\chapter{}`）、
節（`\section{}`）、
項（`\subsection{}`）、
目（`\subsubsection{}`）
段落（`\paragraph{}`）と
小段落（`\subparagraph{}`）
の階層があります。

それぞれの見出しと番号ラベルを整理しました。

| 見出し | コマンド名 | 番号ラベル | 表示形式 |
|---|---|---|---|
| 部 | `\part{}` | `\thepart` | ローマ数字（I、II、III、...） |
| 章 | `\chapter{}` | `\thechapter` | アラビア数字（1、2、3、...） |
| 節 | `\section{}` | `\thesection` | アラビア数字 |
| 項 | `\subsection{}` | `\thesubsection` | アラビア数字 |
| 目 | `\subsubsection{}` | `\thesubsubsection` | アラビア数字 |
| 段落 | `\paragraph{}` | `\theparagraph` | 番号なし／太字 |
| 小段落 | `\subparagraph{}` | `\thesubparagraph` | 番号なし／太字 |

`\part{}`と`\chapter{}`はbookやreportクラスで利用します。
articleクラスは`\section{}`から使うことが多いです。

## 見出しを変更したい（`\thesection`）

```latex
% 第I部 -> 第1部
\renewcommand{\thepart}{\arabic{part}}

% 1 -> 第1章
\renewcommand{\thesection}{第\arabic{section}章}
% 1.1 -> 第1.1節
\renewcommand{\thesubsection}{第\arabic{section}.\arabic{subsection}節}
% 1.1.1 -> 第1.1.項
\renewcommand{\thesubsubsection}{第\arabic{section}.\arabic{subsection}.\arabic{subsubsection}項}
```

`\the見出しレベル`を再定義して、見出しの書式を変更できます。
章番号のデフォルトはアラビア数字（`\arabic{section}`）ですが、
ローマ数字（`\roman{section}`）や
アルファベット（`\alph{section}`）などに変更できます。

[titlesecパッケージ](./latex-titlesec.md)を使って変更する方法もあります。
