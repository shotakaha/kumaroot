# フォントサイズしたい（``fontsize`` / ``jafontsize``）

```latex
\documentclass[fontsize=10pt]{jlreq}    % 欧文フォント
\documentclass[jafontsize=10pt]{jlreq}  % 和文フォント
\documentclass[jafontscale=1]           % 和文/欧文のフォントサイズ比

\documentclass[jafontsize=12Q, jafontscale=0.92]{jlreq}     % LaTeX美文書作成入門（改訂第8版）
```

``jlreq``は欧文フォントのサイズ（``fontsize=フォントサイズ``）と和文フォントのサイズ（``jafontsize=フォントサイズ``）をそれぞれ指定できます。フォントサイズに小数点を使うことができます。

また、そのサイズ比（``jafontscale``）でも指定できます。
``fontsize``と``jafontsize``の両方が指定されている場合には、``jafontscale``は無視されます。

```{note}
LaTeXで使う``pt``はDTPソフトのポイントサイズと異なります。
DTPポイントで指定する場合は``bp``（big point）を使います。
```

## フォントサイズしたい（``10pt``）

```latex
\documentclass[10pt]{ltjsarticle}  % 10pt（デフォルト）
\documentclass[uplatex, dvipdfmx, 12pt]{jsarticle}  % 12pt
```

``jsclasses``系はフォントサイズを直接指定します。
フォントサイズは定められた整数値から選択する必要があります。
