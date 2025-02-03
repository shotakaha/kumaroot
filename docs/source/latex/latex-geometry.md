```{eval-rst}
.. index::
    pair: レイアウトしたい; LaTeX
```

# レイアウトしたい（`geometry`）

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

% 行間を設定
\renewcommand{\baselinestretch}{1.5}
```

`geometry`パッケージでレイアウトをカスタマイズできます。
`\geometry`コマンドはプリアンブルに書きます。
LaTeXの標準マクロでレイアウトを調整するのはとても大変なので、迷わずこのパッケージを使いましょう。
ただし、行間の設定はできないため、`\baselinestretch`を`\renewcommand`する必要があります。

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

`paper=用紙サイズ名`で規定のサイズを設定できます。
用紙サイズ名は
`a0paper` - `a6paper`、
`b0paper` - `b6paper`、
`c0paper` - `c6paper`などから選択できます。
JISのB版は`b0j` - `b6j`を使います。

## スライドしたい（`papersize`）

```latex
% 解像度: $dpi dpi
% 1 bp = 1/72inch
% $px = $L / 72 * $dpi * bp

\geometry{
    papersize={160mm,90mm},
}
```

`papersize={横寸, 縦寸}`で用紙サイズを直接指定できます。

:::{note}

`paper=screen`というプレゼンテーション用のオプションがありますが、
W225mm x H180mmという設定値になっています。
アスペクト比が5:4という現在のスクリーン環境では
使いづらい値なので、直接指定するほうがよいです。

:::

## 印刷サイズしたい（`layout`）

```latex
\geometry{
    paper=a4paper,    % 用紙サイズ
    layout=a5paper,   % 印刷サイズ
}
```

A4用紙にA5サイズのレイアウトを表示する方法です。

## テキストエリアしたい（`text`）

```latex
\geometry{
    text={160mm, 240mm},
}

\geometry{
    textwidth=160mm,
    textheight=240mm,
}
```

## ヘッダーしたい（`headheight`）

```latex
\geometry{
    headheight=3cm,
    headsep=1cm,
    includehead=true,
}
```

`headheight`でヘッダーの高さを設定できます。
`headsep`と`footskip`で、ヘッダー／フッターとテキストエリアの間のアキを設定できます。

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
