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
ファイル形式は``JPEG``、``PNG``、``PDF``が使えます。
昔は``EPS``形式への変換が必要でしたが、最近はそんなことをしなくても大丈夫です。

画像の配置には[figure環境](./latex-figure.md)を使います。


## 画像のサイズを指定したい

```latex
\includegraphics[width=3cm]{図のファイル名}
\includegraphics[height=3cm]{図のファイル名}
\includegraphics[width=3cm,height=3cm,keepaspectratio]{図のファイル名}
\includegraphics[0.5\linewidth]{図のファイル名}
```

画像のサイズは``width``や``height``オプションを指定して拡大・縮小できます。
``width``と``height``の両方を指定すると縦横比が変わってしまうため、``keepaspectratio``をつけておくとよいです。

個人的には``\linewidth``のN倍という指定をよく使います。


## ドライバーを指定したい

```latex
\documentclass[dvipdfmx]{jsarticle} % pLaTeX
\documentclass[dvipdfmx, uplatex]{jsarticle} % upLaTeX
```

ドライバーは**ドキュメントクラスのオプション**で指定します。
(u)pLaTeXの場合は、ドライバーに``dvipdfmx``を必ず指定する必要があります。
LuaLaTeXの場合は自動判断してくれるため、逆に、何も指定してはいけません。

## リファレンス

- {command}`texdoc graphicx`
