# 用紙サイズしたい

```latex
\documentclass[paper=a4]{jlreq}  % A4サイズ（デフォルト）
\documentclass[paper=a5]{jlreq}  % A5サイズ
\documentclass[paper=b4]{jlreq}  % B4サイズ
\documentclass[paper=b5]{jlreq}  % B5サイズ
```

``jlreq``は``paper=用紙サイズ``で指定します。
A判（JIS/ISO）は``a0 - a10``、B判（JIS）は``b0 - b10``、C判（ISO）は``c2 - c8``から選択できます
``paper={横mm, 縦mm}``でサイズを直接指定することもできます

```latex
% LuaLaTeX
\documentclass[a4paper]{ltjsarticle}  % A4サイズ
\documentclass[a5paper]{ltjsarticle}  % A5サイズ
% (u)pLaTeX
\documentclass[uplatex, dvipdfmx, b4paper, papersize]{jsarticle}  % B4サイズ
\documentclass[uplatex, dvipdfmx, b5paper, papersize]{jsarticle}  % B5サイズ
```

``jsclasses``系は``a4paper``や``b5paper``など用紙サイズのオプションを直接指定します。
``papersize``オプションを同時に指定して、ドライバー（``dvipdfmx``）にPDFのページサイズを伝える必要があります。

## よく使う用紙サイズ

よく使う用紙サイズもメモしておきます。
A判はISO規格とJIS規格でサイズが同じですが、B判は異なります（JIS規格のほうが大きい）。
レター判は使ったことがありませんが、欧文ドキュメントのデフォルトなので載せておきます。

| 名称 | 寸法 | メモ |
|---|---|---|
| A4判 | 210mm $\times$ 297mm | 和文デフォルト |
| A5判 | 148mm $\times$ 210mm | |
| B4判 | 257mm $\times$ 364mm | |
| B5判 | 182mm $\times$ 257mm | |
| レター判 | 8.5in. $\times$ 11in. | 欧文デフォルト |

より柔軟に用紙サイズを設定したい場合は[geometryパッケージ](./latex-geometry.md)を使います。
