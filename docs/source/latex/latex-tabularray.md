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

## 格子組したい（`hlines` / `vlines`）

```latex
\begin{tblr}{
    hlines,
    vlines
    }
Alpha & Beta & Gamma & Delta \\
Epsilon & Zeta & Eta & Theta \\
Iota & Kappa & Lambda & Mu \\
\end{tblr}
```

`hlines`で横罫線、`vlines`で縦罫線を表示します。
両方を指定すると格子組できます。

`hlines={1pt, solid}`、
`vlines={red3, dashed}`でそれぞれの罫線の太さや、
スタイル、色などを変更できます。

## 依存パッケージ

```console
$ kpsewhich tabularray.sty | xargs cat | rg RequirePackage
\RequirePackage{expl3}
  \@ifpackageloaded{xcolor}{\RequirePackage{ninecolors}}{}
    \RequirePackage { amsmath }
    \RequirePackage { booktabs }
    \RequirePackage { etoolbox }
    \RequirePackage{ diagbox }
    \RequirePackage { functional }
    \RequirePackage { nameref }
    \RequirePackage { siunitx }
    \RequirePackage { varwidth }
    \RequirePackage { zref-user }
```

`\UseTblrLibrary{}`で設定できるパッケージ名を確認できます。
