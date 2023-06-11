# LuaLaTeXしたい（``lualatex``）

```bash
$ lualatex ファイル名
$ latexmk -lualatex ファイル名
```

``LuaLaTeX``エンジンを使ってPDFを作成したい場合は、
``lualatex``コマンドもしくは``latexmk``コマンドに``-lualatex``オプションをつけて実行します。

## ドキュメントクラス

```latex
\documentclass{jlreq}
\documentclass{ltjsarticle}
```

``LuaLaTeX``を使う場合は、ドキュメントクラスに``jlreq``を使います。
昔からある``jsarticle``に相当するものを使いたい場合は``ltjsarticle``が使えます。

## latexmkrc

```text
$pdf_mode = 4;
@default_files = ("ファイル1", "ファイル2");
# ライブプレビューに関する設定
$preview_continuous_mode = 1;
$pvc_timeout = 1;
$pvc_timeout_mins = 10;  # 30min; default
$sleep_time = 60;  # 60s
# $out_dir = "outd";
# $aux_dir = "auxd";
```
