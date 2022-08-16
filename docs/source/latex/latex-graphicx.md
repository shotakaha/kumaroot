# graphicx

```latex
\documentclass[ドライバ名]{ドキュメントクラス名}

\usepackage{graphicx}

\begin{document}
...本文...
\includegraphics[図のオプション]{図のファイル名}
...本文...
\end{document}
```

図を挿入するのに必要不可欠なパッケージです。
(u)pLaTeXの場合は、ドライバー名に``dvipdfmx``を必ず指定する必要があります。
LuaLaTeXの場合は自動判断してくれるため、逆に、何も指定してはいけません。

画像のファイル形式は``JPEG``、``PNG``、``PDF``が使えます。
昔は``EPS``形式への変換が必要でしたが、最近はそんなことをしなくても大丈夫です。

## 画像のサイズを指定したい

```latex
\includegraphics[width=3cm]{図のファイル名}
\includegraphics[height=3cm]{図のファイル名}
\includegraphics[width=3cm,height=3cm,keepaspectratio]{図のファイル名}
\includegraphics[totalheight=3cm]{図のファイル名}
```

- ``width``や``height``のみを指定して拡大・縮小できます
- ``width``と``height``の両方を指定すると縦横比が変わってしまうので``keepaspectratio``をつけるとよいです。
- 画像を回転させた場合は``totalheight``を使ったほうが便利です

## リファレンス

- {command}`texdoc graphicx`
