# 透かししたい（`draftwatermark`）

```latex
% プリアンブル
\usepackage[オプション]{draftwatermark}
```

`draftwatermark`は、文書の背景に透かしを出力するパッケージです。
**DRAFT**や
**CONFIDENTIAL**などの文字を指定したページに表示できます。

パッケージオプションもしくは
`\DraftwatermarkOptions`で設定を変更できます。

## 全ページしたい（`firstpageonly=false`）

```latex
\usepackage[firstpageonly=false]{draftwatermark}
```

デフォルトは`firstpageonly=true`になっていて、
最初のページにだけ透かしが表示されるようになっています。
`firstpageonly=false`に変更することで、全ページに表示できます。
この設定は`\DraftwatermarkOptions`では設定できません。

## 脱稿したい（`stamp=false`）

```latex
\usepackage{draftwatermark}
\DraftwatermarkOptions{
    stamp=false,
}
```

デフォルトは`stamp=true`になっていて、
透かしが表示されるようになっています。
`stamp=false`に変更することで、透かしを非表示にできます。
完成版を脱稿する際は、このオプションを使うとよいです。

## テキストを変更したい（`text`）

```latex
\usepackage{draftwatermark}
\DrafrwatermarkOptions{
    text=DRAFT,
    fontsize=0.25\paperwidth,
    scale=1,
    angle=45,
    color={[gray]{0.8}},
}
```

`text`オプションで透かし文字を変更できます。
また、出力するサイズや角度、文字色なども変更できます。
