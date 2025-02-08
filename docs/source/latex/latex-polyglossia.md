# 多言語対応したい（`polyglossia`）

```latex
% プリアンブル
\usepackage{polyglossia}
\setdefaultlanguage{japanese}
```

`polyglossia`パッケージで多言語対応できます。
このパッケージを使うことで言語ごとの組版ルールに対応できるようになります。
また、[fontspecパッケージ](./latex-fontspec.md)と統合されていて、
言語ごとにフォントを設定できます。

- 改行ルールやハイフネーション
- 句読点や引用符のスタイル
- 日付表記のローカライズ
- 自動生成される見出しのローカライズ（Chapter 1、第1章、など）
- 言語ごとのフォント設定

:::{note}

同様のパッケージに`babel`があります。
`babel`はレガシーLaTeXのころから利用されていたパッケージです。
`pdfLaTeX`の場合は`babel`、
`LuaLaTeX`や`XeLaTeX`の場合は`polyglossia`の利用が推奨されています。

:::

## 言語を追加したい（`\setotherlanguage`）

```latex
\usepackage{polyglossia}

\setdefaultlanguage{japanese}
\setotherlanguage{english}
\setotherlanguage{germany}
\setotherlanguage{french}

% 本文
ここは日本語の組版です。

\textenglish{ここは英語の組版です。}
\textgermany{ここはドイツ語の組版です。}
\textfrench{ここはフランス語の組版です。}
```

本文で使用する言語をプリアンブルで追加します。
`\setdefaultlanguage{言語名}`でメインの言語を設定し、
`\setotherlanguage{言語名}`で他の言語を追加できます。
**言語名**は`poliglossia`のドキュメントで確認してください（`$ texdoc polyglossia`）。

`\text言語名{}`で、本文中に言語の切り替えができます。

## フォントを設定したい

```latex
% プリアンブル
\newfontfamily\japanesefont{Noto Serif CJK JP}
\newfontfamily\englishfont{Times New Roman}
\newfontfamily\germanfont{フォント名}
\newfontfamily\frenchfont{フォント名}
```

`\newfontfamily\言語名font{フォント名}`で言語ごとのフォントを設定できます。

## RTL言語したい（`arabic`）

```latex
% 本文
\begin{arabic}
  アラビア語やヘブライ語
\end{araic}
```

`arabic`環境で、アラビア語やヘブライ語などの
RTL言語（右から左に書く言語）に対応できます。
