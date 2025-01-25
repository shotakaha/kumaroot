# ヒラギノしたい（`HiraginoProN`）

```latex
\usepackage[hiragino-pron]{luatexja-preset}
```

macOSに入っているヒラギノフォント用の設定です。
プリセットのひとつとして呼び出せるようになっています。

:::{note}

ヒラギノフォントのプリセットとして、
`hiragino-pro`と`hiragino-pron`があります。
ProはJIS文字に対応したフォントせっと、
ProNはUnicodeに対応したフォントセットらしいので、
ProNを使っておけば問題ないと思います。

:::

```latex
\usepackage{luatexja-fontspec}
% 欧文フォント
\setmainfont{HiraginoSans-W2}
\setsansfont{HiraginoSans-W9}
\setmonofont{HiraginoSans-W5}

% 和文フォント
\setmainjfont{HiraginoSans-W2}
\setsansjfont{HiraginoSans-W9}
\setmonojfont{HiraginoSans-W5}
```

ポスターを作成する場合は、
ウェイトが豊富なヒラギノ角ゴシック（`Hiragino Sans`）を使って設定するとよいです。
