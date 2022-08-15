# ドキュメントクラスを設定する（``documentclass``）

日本語用のドキュメントクラスには次の3種類があります。
これから新しく作成する場合は``jlreq``を使うのがよさそうです。

- ``js``系
- ``ltjs``系
- ``jlreq``

```latex
\documentclass[uplatex, a4paper, 12pt, papersize, dvipdfmx]{jsarticle}
\documentclass[uplatex, a4paper, 12pt, papersize, dvipdfmx]{jsreport}
\documentclass[uplatex, a4paper, 12pt, papersize, dvipdfmx]{jsbook}
```

``pLaTeX/upLaTeX``の場合、``jsarticle``系のドキュメントクラスを使用する場合が多いです。
ドキュメントクラスのオプションには用紙サイズ（``[a4paper, papersize]``）、欧文フォントサイズ（``[12pt]``）、ドライバ（``[dvipdfmx]``）などを指定します。

```latex
\documentclass{jlreq}
\documentclass[report]{jlreq}
\documentclass[book]{jlreq}
```
