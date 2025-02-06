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

`tabularray`はこれまでの表組みに関するパッケージの機能が統合されたパッケージです。
新しくドキュメントを作成する場合は、このパッケージを読み込んでおけば万事解決です。

| 環境／パッケージ | 特徴 |
|---|---|
| `tabular` | LaTeX標準の表組み環境 |
| `array` | `tabular`を拡張。数式環境で利用できる |
| `tabularx` | `tabular`を拡張。可変幅列（`X`）を利用できる |
| `booktabs` | 表組みの罫線を改善 |
| `longtable` | `tabular`を拡張。ページをまたぐ表を作成できる |
| `tabulararray` | `tabular`の完全上位互換 |

また`\UseTblrLibrary{}`で、さまざまな外部パッケージへの対応を追加できます。

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

## 改行したい

```latex
\begin{tblr}{Q[l,t] Q[c,m] Q[r,b]}
\toprule
Left & {Center \\ C } & {Right \\ R}\\
\midrule
{L \\ Left} & {Center \\ C } & R\\
\bottomrule
\end{tblr}
```

`{ \\ }`で表のセル内で改行できます。
`Q[左右揃え,上下揃え]`で整列する方向を指定できます。

```latex
\begin{tblr}{
    colspec={Q[l]Q[c]Q[r]},
    rowspec={Q[t]Q[m]Q[b]},
}
...
\end{tblr}
```

`Q[左右揃え,上下揃え]`は`colspec`と`rowspec`オプションでもそれぞれ指定できます。
こちらのオプションを使ったほうが、可読性が高いかもしれません。

## 可変幅したい（`X`）

## セル操作したい

## 交互の背景色したい

## ページをまたぎたい（`longtblr`）

```latex
% 表の末尾に表示する内容
\DefTblrTemplate{contfoot-text}{テンプレート名}{次ページに続く}
\SetTblrTemplate{contfoot-text}{テンプレート名}
% 表の先頭に表示する内容
\DefTblrTemplate{conthead-text}{テンプレート名}{（続き）}
\SetTblrTemplate{conthead-text}{テンプレート名}

\begin{longtblr}[
    % オプション
    caption = {表のキャプション},  % 本文に表示される説明
    entry = {短いキャプション},    % listoftablesに表示される説明
    label = {tblr:ラベル},
    ]{
        colspec = {XXX},  % 3列／可変幅
        width = 0.85\linewidth,
        rowhead = 1,  % すべてのページに表示するheaderの行数
        rowfoot = 1,  % すべてのページに表示するfooterの行数
        row{odd} = {gray9},    % 奇数行の背景色
        row{even} = {brown9},  % 偶数行の背景色
        row{1} = {purple7},    % headerの背景色
        row{Z} = {bulue7},     % footerの背景色
    }
    \toprule
    Head1 & Head2 * Head3\\
    \midrule
    Alpha & Beta & Gamma\\
    \midrule
    Alpha & Beta & Gamma\\
    \midrule
    .......
    Foot1 & Foot2 & Foot3\\
    \bottomrule
\end{longtblr}
```

`longtblr`環境でページをまたぐような長い表を作成できます。
header行やfooter行の指定、ページをまたぐときの案内表示などもカスタマイズできます。

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
