# 基本的な文書の構造

LaTeX文書の基本的な構造は以下の通りです。

## 構成要素

エンジン
:   文書をタイプセット（コンパイル）するときのコンパイラーです。
    さまざまなバリエーションがあります。
    このサイトでは和文LaTeXできる``pLaTeX`` / ``upLaTeX`` / ``LuaLaTeX``を使います。

ドキュメントクラス
:   文書のスタイルを指定します。
    欧文用のクラスや和文用のクラスがあります。
    学会や出版社によってはオリジナルのドキュメントクラスが用意されていることもあります。
    自分で作ることもできます。

プリアンブル
:   パッケージの追加や設定を行う部分です。
    自前のマクロもここに書けばOKです。
    **本文以外** の部分を書く場所だと考えておけばよいと思います。

本文
:   文章を書く部分です。
    セクションや図といった文書構造をLaTeXの**環境／コマンド**を使ってマークアップします。

タイプセット
:   LaTeX文書を元に、ページ配置や文字の埋め込みをする操作です。
    使用するエンジンごとにコマンド（``platex / uplatex / lualatex``など）があります。
    この手間が必要なため、WordなどのWYSIWYGなエディタと比べるとLaTeXはとっかかりにくいのかもしれません。

## サンプル

具体的な形のサンプルを用意してみました。

```latex
%% ドキュメントクラスの指定
\documentclass[uplatex, dvipdfmx,12pt]{jsarticle}

%% プリアンブル
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{fixltx2e}
\usepackage{graphicx}
...

%% ハイパーリンクのカスタマイズ
\usepackage{hyperref}
\usepackage{pxjahyper}
\hypersetup{setpagesize=false}
\hypersetup{colorlinks=true}
\hypersetup{linkcolor=blue}

%% 書籍情報の設定
\author{Shota TAKAHASHI}
\date{2016-01-14 Monday}
\title{第一回打ち合わせ}

%% 本文
\begin{document}

   \maketitle
   \tableofcontents

   \section{登山計画}

       \subsection{頂上：アインシュタイン方程式を理解する}

       \begin{itemize}
           \item デ 15. アインシュタインの重力の法則
           \item デ 24. 物質の存在によるアインシュタイン方程式の変更
           \item デ 25. 物質のエネルギー・運動量テンソル
           \item 杉 10. アインシュタイン方程式
       \end{itemize}

       \subsection{頂上からの眺め：アインシュタイン方程式で分かる物理}

       \begin{itemize}
           \item デ 33. 重力波
           \item デ 19. ブラック・ホール
           \item デ 18. シュヴァルツシルトの解
           \item 杉 11. 球対称時空
           \item 杉 12. 一般相対性理論の検証
       \end{itemize}

\end{document}
```
