```{eval-rst}
.. index::
    pair: レイアウトしたい; LaTeX
```

# レイアウトしたい（``geometry``）

```latex
% プリアンブル
\usepackage{geometry}
\geometry{
  paperwidth=210mm,
  paperheight=297mm,
  left=25mm,
  right=25mm,
  top=25mm,
  bottom=25mm,
  margin=25mm,
  textwidth=160mm,
  textheight=240mm,
  headheight=15pt,
  headsep=10mm,
  footskip=15mm
}
```

`geometry`パッケージでレイアウトをカスタマイズできます。
`\geometry`コマンドはプリアンブルに書きます。
LaTeXの標準マクロでレイアウトを調整するのはとても大変なので、迷わずこのパッケージを使いましょう。

:::{hint}

``layout``パッケージでレイアウトを確認できます。

```latex
\usepackage{layout}

% ドキュメント内
\newpage
\layouts
```

:::

## A4サイズにしたい

```latex
\geometry{
    paper=a4paper,
}
```

`paper`で規定のサイズを設定できます。

```latex
\geometry{
    paperwidth=210mm,
    paperheight=297mm,
}

\geometry{
    papersize={210mm, 297mm},
}
```

また、用紙サイズ（幅と高さ）を単位込みで直接指定できます。

## 印刷サイズを変えたい

```latex
\geometry{
    paper=a4paper,
    layout=a5paper,
}
```

A4用紙にA5サイズのレイアウトを表示する方法です。

## テキストエリアしたい

```latex
\geometry{
    text={160mm, 240mm},
}

\geometry{
    textwidth=160mm,
    textheight=240mm,
}
```

## ヘッダーしたい（``headheight``）

```latex
\geometry{
    headheight=3cm,
    headsep=1cm,
    includehead=true,
}
```

``headheight``でヘッダーエリアの高さを設定できます。
ヘッダーエリアとテキストエリアの間の距離を``headsep``で設定できます。

## 一部だけレイアウトしたい（``\newgeometry``）

```latex
\newgeometry{
...
}
\restoregeometry
```

文書の途中でレイアウトを変更する場合は``\newgeometry``を使います。
これまでの設定は無視されるので、すべて再設定する必要があります。
``\restoregeometry``元のレイアウトに戻せます。

## リファレンス

- {command}`texdoc geometry`
