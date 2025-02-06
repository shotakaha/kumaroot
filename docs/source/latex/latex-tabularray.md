# 表組したい（`tabularray`）

```latex
% プリアンブル
\usepackage{tabularray}
\UseTblrLibrary{booktabs}

% 本文
\begin{tblr}{lccr}
\toprule
Alpha & Beta & Gamma & Delta \\
\midrule
Epsilon & Zeta & Eta & Theta \\
\midrule
Iota & Kappa & Lambda & Mu \\
\bottomrule
\end{tblr}
```

`tabularray`パッケージで表を作成できます。
このパッケージは、`array`や`tabularx`、`booktabs`、`longtable`などの機能が統合されたパッケージだそうです。
また`\UseTblrLibrary{}`で、さまざまなパッケージ拡張を追加できます。
