# A0ポスターしたい

```latex
\documentclass[paper=a0, jafontsize=32pt, twocolumn]{jlreq}

%% プリアンブル
\usepackage[haranoaji]{luatexja-preset}

%% 余白の設定
%% jlreqのオプションでも設定できますが、
%% geometryパッケージを使う方が、あとで修正しやすいです
\usepackage{geometry}
\geometry{
    left=50truemm,
    right=50truemm,
    top=25truemm,
    bottom=25truemm,
}

%% ヘッダー／フッターにロゴを入れたい場合は
%% ここをカスタマイズしてください
%\usepackage{fancyhdr}
%\pagestyle{fancy}

%% ポスターのレイアウトを考えるときに使います
\usepackage{mwe}
% \usepackage{blindtext}
% \usepackage{graphicx}
\usepackage{bxjalipsum}

%% 追加しとくとよいパッケージ
\usepackage{enumitem}
\usepackage{tcolorbox}

%% ポスター情報
\title{ポスターのタイトル}
\author{ポスターの発表者}
\date{ポスターの発表日}

\begin{abstract}
ポスターの概要
\end{abstract}

%% 本文
\begin{document}

\section{概要}

\section{まとめ}

\end{document}
```
