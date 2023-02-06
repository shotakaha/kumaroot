# 画像を挿入したい（``graphicx``）

```latex
\usepackage{graphicx}

\begin{document}
...本文...
\includegraphics[図のオプション]{図のファイル名}
...本文...
\end{document}
```

画像を挿入する場合は``graphicx``パッケージを使います。
また、文字列の変形もできるようになります。

画像ファイルは``JPEG``、``PNG``、``PDF``形式が使えます。
昔は``EPS``形式への変換が必要でしたが、最近はそんなことをしなくても大丈夫です。
画像の配置には[figure環境](./latex-figure.md)を使います。

## 画像のサイズを指定したい

```latex
\includegraphics[width=3cm]{図のファイル名}
\includegraphics[height=3cm]{図のファイル名}
\includegraphics[width=0.8\linewidth]{図のファイル名}
```

画像のサイズは``width``や``height``オプションを指定して拡大・縮小できます。
個人的には行幅（``\linewidth``）を基準にした相対値で指定します。

## 画像のアスペクト比を維持したい

```latex
\includegraphics[width=3cm,height=3cm,keepaspectratio]{図のファイル名}
```

``width``と``height``の両方を指定すると縦横比が変わってしまいます。
アスペクト比を維持したい場合は``keepaspectratio``を追加します。

## ドライバーを指定したい

```latex
\documentclass[dvipdfmx]{jsarticle} % pLaTeX
\documentclass[dvipdfmx, uplatex]{jsarticle} % upLaTeX
```

ドライバーは**ドキュメントクラスのオプション**で指定します。
(u)pLaTeXの場合は、ドライバーに``dvipdfmx``を必ず指定する必要があります。
LuaLaTeXの場合は自動判断してくれるため、逆に、何も指定してはいけません。

## 色空間を変換したい

パソコンで作成した画像の色空間は``RGB``となっています。
これを印刷物にする場合、色空間を``CMYK``に変換する必要があります。
変換はAdobe PhotoshopやAdobe Illustratorなどを使うとよいです。

## 画像ディレクトリを指定したい

```latex
\graphicspath{{images/}}
\graphicspath{{images/} {figures/}}
```

LaTeXで文書を作成していると、画像ファイルをひとつのディレクトリにまとめて管理することが多いと思います。
``\graphicspath``で画像ディレクトリのパスを指定しおくと、``\includgraphics``するときにちょっとだけ楽になります。

## リファレンス

- {command}`texdoc graphicx`
