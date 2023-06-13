# 表紙したい（``\maketitle``）

```latex

\title{すごい文書}
\author{すごい著者}
\date{2022年8月1日}

\begin{document}
\maketitle
\end{document}
```

プリアンブルにタイトル（``\title``）、著者（``\author``）、日付（``\date``）を書き、本文の``\maketitle``で表示できます。
3つの順番は適当で構いません。

:::{hint}

表紙をカスタムできる``titling``パッケージがあります。
自分でも使ったらページを作成します。

:::

## タイトルを2行にしたい

区切りたい箇所に``\\``を使います。

```latex
\title{すごい長いタイトル \\ 本当に長いタイトルなのです}
```

タイトルが長い場合、``\\``で途中で改行できます。

## 複数の著者名を表示したい

```latex
\author{すごい著者 \and これまたすごい著者}
```

著者名の間に``\and``を使います。

## 所属を表示したい

```latex
%% 脚注に表示される記号を数字に変更する
\makeatletter
\renewcommand{\@fnsymbol}[1]{\@arabic{#1}}
\makeatother

\author{
    すごい著者 \thanks{すごい大学} \and
    これまたすごい著者 \thanks{すごい研究所}
}
```

``\thanks``コマンドで所属を設定するのが一般的です。
所属は脚注に表示されます。
その際、デフォルトは記号（*、†、‡、など）で表示されます。
これを数字（1、2、3、…）に変更しておきます。

:::{note}

```latex
\makeatletter
\let\@fnsymbol\@arabic
\makeatother
```

``\let``でも同様の結果を得られますが、より安全な（？）``\renewcommand``を使っています。

:::

:::{caution}

> なお、\@fnsymbolは内部コマンドであるため、直接使用することは推奨されません。
> 代わりに、適切な文脚注パッケージ（例：footmiscパッケージ）を使用することをおすすめします。
> これにより、脚注のスタイルを簡単にカスタマイズすることができます。

ChatGPTに聞いたら``fontmisc``パッケージを教えてくれました

:::

## 作成日を表示したい

LaTeXファイルをコンパイルした日を自動挿入したい場合は``\today``を使います。

```latex
\date{\today}
```
