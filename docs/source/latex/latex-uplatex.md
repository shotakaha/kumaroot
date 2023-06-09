# (u)pLaTeXしたい

```bash
$ ptex2pdf -l -u ファイル名  # upLaTeX
$ ptex2pdf -l ファイル名     # pLaTeX
```

``(u)pLaTeX``を使ってPDFを作成する場合は``ptex2pdf``コマンドを使います。
``upLaTeX``のタイプセットは``-l -u``オプション、
``pLaTeX``のタイプセットは``-l``オプションをつけて実行します。

## ドキュメントクラス

```latex
\documentclass{jlreq}
\documentclass[dvipdfmx]{jsarticle}    % pLaTeX
\documentclass[uplatex, dvipdfmx]{jsarticle}     % upLaTeX
```

``(u)pLaTeX``を使う場合も、ドキュメントクラスに``jlreq``が使えます。
昔からある``jsarticle``系も使えます。

## latexmkrc

```text
#$pdf_mode = 4;
#@default_files = ("ファイル1", "ファイル2");
# ライブプレビューに関する設定
#$preview_continuous_mode = 1;
#$pvc_timeout = 1;
#$pvc_timeout_mins = 10;  # 30min; default
3$sleep_time = 60;  # 60s
# $out_dir = "outd";
# $aux_dir = "auxd";
```
