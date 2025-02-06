# 表組みしたい（`booktabs`）

```latex
% プリアンブル
\usepackage{booktabs}

% 本文
\begin{tabular}{lccr}
\toprule
Alpha & Beta & Gamma & Delta \\
\midrule
Epsilon & Zeta & Eta & Theta \\
\midrule
Iota & Kappa & Lambda & Mu \\
\bottomrule
\end{tabular}
```

`booktabs`は表の見た目をよくするパッケージです。
**縦線と二重線は絶対に使わない** という方針で設計されています。

主なコマンドは
`\toprule`、
`\midrule`、
`\bottomrule`の3種類です。

これまで表の区切り線（横罫線）に使っていた`\hline`を置き換える形で使用できます。
また、これらのコマンドは`longtable`パッケージと同時に使えます。

:::{note}

作者によると、イギリスではlineのことをruleと呼ぶため、
この慣習にならってコマンド名をつけているそうです。

:::
