# スライドしたい（`beamer`）

```latex
\documentclass[t]{beamer}
\usepackage{luatexja}

\title{発表タイトル}

\begin{document}

\begin{frame}
  \frametitle{スライドのタイトル}
\end{frame}

\end{document}
```

`beamer`クラスでスライド形式の文書を作成できます。
LaTeXの知識があれば、かなり強力なスライド作成ツールとして活用できます。
ドキュメントがすごく充実しているので、何回も目を通すことをオススメします（`texdoc beamer`）

[luatexjaパッケージ](./latex-luatexja.md)で日本語を扱えるようになります。

:::{caution}

`beamer`は非常に多機能なクラスで、カスタマイズ性も高いですが、
沼にハマる可能性も秘めています。
用法・容量を守って使うことを心がけるとよいです。

急ぎのスライド作成にはWYSIWYGなツールが圧倒的に便利であることは、
忘れないようにしてください。

:::

## テーマしたい（`\usetheme`）

## スライドしたい（`frame`）

```latex
% 目次を生成するために section を設定
\section{タイトル}
\begin{frame}
  \frametitle{タイトル}
  \framesubtitle{サブタイトル}

  スライドの本文

\end{frame}
```

`frame`環境で1枚のスライドを作成できます。

## 段組したい（`columns`）
