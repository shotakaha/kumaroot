# 色を指定したい（`xcolor`）

```latex
\usepackage{xcolor}
\usepackage{graphicx}
```

`xcolor`で文字色や背景色を変更できます。
`graphicx`パッケージと一緒に使うことが多いです。

## カラーパレットしたい

```latex
\usepackage{xcolor}  % 19色
\usepackage[dvipsnames]{xcolor}  % +68色
\usepackage[svgnames]{xcolor}    % +151色
\usepackage[x11names]{xcolor}    % +289色
\usepackage[dvipsnames,svgnames,x11names]{xcolor}
```

オプションで、利用できる色を増やすことができます。
オプションは`dvipsnames`、`svgnames`、`x11names`の3つあります。
すべてを指定することもできます。
それぞれのオプションで増える色名は`xcolor`のドキュメントで確認できます。

基本色は使いにくい色もあるので`dvipsnames`オプションは有効にするとよいと思います。
`dvipsnames`を有効にすると、大文字ではじまる色名が利用可能になります。
以下に、基本色の代替となりそうな色名をリストしてみました。

| 基本色 | `dvipsnames`色 |
|---|---|
| `red` | `Red` / `OrangeRed` |
| `green` | `Green` / `ForestGreen` |
| `blue` | `Blue` / `RoyalBlue` |
| `cyan` | `Cyan` / `ProcessBlue` |
| `magenta` | `Magenta` / `WildStrawberry` |
| `yellow` | `Yellow` / `Goldenrod` |
| `lime` | `LimeGreen` |

## 文字色したい（`\textcolor`）

```latex
% 本文
{\color{文字色} テキスト}
\textcolor{文字色}{テキスト}
\textcolor{文字色!透過度}{テキスト}

\textcolor{red}{赤色のテキスト}
\textcolor{green}{緑色のテキスト}
\textcolor{blue}{青色のテキスト}
\textcolor{cyan}{シアン色のテキスト}
\textcolor{magenta}{マゼンタ色のテキスト}
\textcolor{yellow}{黄色のテキスト}
\textcolor{black}{黒色のテキスト}
\textcolor{white}{白色のテキスト}
```

`\color`コマンドや`\textcolor`コマンドで文字色を変更できます。
`色名!10`ようにして透過度を設定できます。
個人的な好みから、以下では`\textcolor`コマンドを使います。

## 背景色したい（`\pagecolor`）

```latex
% 本文
\pagecolor{SpringGreen!20}
\section{背景色あり}

\newpage
\newpage
\newpage

\pagecolor{White}
\section{背景色なし（白）}
```

`\pagecolor{}`でページの背景色を変更できます。
色指定に透明度を追加すると雰囲気がよくなることが多いです。

このコマンドより後のすべてのページの背景色に適用されます。
元に戻す場合、再度、コマンドの実行が必要です。

## 背景色したい（`\colorbox`）

```latex
% \colorbox{背景色}{テキスト}
\colorbox{Yellow}{背景が黄色の文字}
```

`\colorbox`コマンドで文字の背景色を変更できます。

```latex
% \fcolorbox{枠色}{背景色}{テキスト}
\fcolorbox{Red}{Red!10}{枠が赤、背景が赤10パーセントの文字}
```

`\fcolorbox`コマンドで枠線付きにできます。

## グレースケールを使いたい

```latex
% \textcolor[色空間]{文字色}{テキスト}
\textcolor[gray]{0.5}{グレースケールにしたい文字列}
```

`\textcolor`の`gray`オプションでグレースケールにできます。

## CMYKを使いたい

```latex
\textcolor[cmyk]{0.75,0,0.65,0}{CMYKにしたい文字列}
```

## HTMLの色コードを使いたい

```latex
\textcolor[HTML]{35A16B}{文字列}
```

`\textcolor`の`HTML`オプションでHTMLの色コードを使用できます。

## 色を定義したい（`\definecolor`）

```latex
\definecolor{red}{HTML}{e5171f}     % 御堂筋線
\definecolor{orange}{HTML}{f39700}  % 銀座線
\definecolor{yellow}{HTML}{d7c447}  % 有楽町線
\definecolor{green}{HTML}{009944}   % 千代田線
\definecolor{blue}{HTML}{0078ba}    % 四つ橋線
\definecolor{indigo}{HTML}{522886}  % 谷町線
\definecolor{purple}{HTML}{9b7cb6}  % 半蔵門線
```

`\definecolor`でカスタムカラーを定義できます。
既存の色名は上書きされます。
上記は[メトロカラー](https://www.colordic.org/m)から選んでみました。
