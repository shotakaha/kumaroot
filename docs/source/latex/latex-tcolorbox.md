# 枠したい（`tcolorbox`）

```latex
% プリアンブル
\usepackage[オプション]{tcolorbox}

% 本文
\begin{tcolorbox}[オプション]
  枠の中のコンテンツ
\end{tcolorbox}

% コンテンツ幅
\tcbox[オプション]{コンテンツ}
```

`tcolorbox`環境で、ページ幅いっぱいの枠を別行立てで作成できます。

`\tcbox{}`コマンドは、コンテンツ幅に応じた枠を作成します。

## インライン枠したい（`on line`）

```latex
\tcbox[on line, size=fbox]{テキスト}

% ラベル風
\tcbox[on line, size=tight]{\colorbox{Black!20}{ラベル} テキスト}
```

`on line`オプションで、インライン表示できます。
ただし、このままだと上下にはみ出して表示されます。
`size=fbox`もしくは`size=small`オプションで行の高さに収めることができます。
