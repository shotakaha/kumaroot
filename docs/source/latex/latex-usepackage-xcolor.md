# 色を指定したい（`xcolor`）

```latex
\usepackage{graphicx, xcolor}
```

``xcolor``パッケージを``graphicx``パッケージと一緒に使います。
``\color``コマンドと``\textcolor``コマンドが使えます。

個人的は好みから、以下では``\textcolor``コマンドを使った例を紹介しています。

## グレースケールを使いたい

```latex
\textcolor[gray]{0.5}{グレースケールにしたい文字列}
```

## CMYKを使いたい

```latex
\textcolor[cmyk]{0.75,0,0.65,0}{CMYKにしたい文字列}
```

## HTMLの色コードを使いたい

```latex
\textcolor[HTML]{35A16B}{文字列}
```

## 色を定義したい（``definecolor``）

```latex
\definecolor{red}{HTML}{e5171f}
\definecolor{orange}{HTML}{ee7b1a}
\definecolor{yellow}{HTML}{d7c447}
\definecolor{green}{HTML}{019a66}
\definecolor{blue}{HTML}{0078ba}
\definecolor{indigo}{HTML}{522886}
\definecolor{purple}{HTML}{e44d93}
```

[メトロカラー](https://www.colordic.org/m)から選んでみました。
