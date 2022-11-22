# 色を指定したい（`xcolor`）

```latex
\usepackage{graphicx, xcolor}
```

``xcolor``パッケージを``graphicx``パッケージと一緒に使います。
``{\color[色空間]{色調} 文字列}``コマンドと
``\textcolor[色空間]{色調}{文字列}``コマンドが使えます。

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
