# 色を指定したい（`xcolor`）

```latex
\usepackage{xcolor}
\usepackage{graphicx}
```

`xcolor`で文字色や背景色を変更できます。
`graphicx`パッケージと一緒に使うことが多いです。

## 文字色したい（`\textcolor`）

```latex
\textcolor{文字色}{テキスト}

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
個人的な好みから、以下では`\textcolor`コマンドを使います。

## 背景色したい（`\colorbox`）

```latex
% \colorbox{背景色}{テキスト}
\colorbox{yellow}{背景が黄色の文字}

% \fcolorbox{枠色}{背景色}{テキスト}
\fcolorbox{red}{cyan}{枠が赤、背景がシアンの文字}
```

`\colorbox`コマンドや`\fcolorbox`コマンドで背景色を変更できます。

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
