# LuaLaTeXしたい

```bash
$ lualatex ファイル名
$ latexmk -lualatex ファイル名
```

``LuaLaTeX``エンジンを使ってPDFを作成したい場合は、
``lualatex``コマンドもしくは``latexmk``コマンドに``-lualatex``オプションをつけて実行します。

## オススメのドキュメントクラス

```latex
\documentclass{jlreq}
\documentclass{ltjsarticle}
```

``LuaLaTeX``を使う場合は、ドキュメントクラスに``jlreq``を使います。
昔からある``jsarticle``に相当するものを使いたい場合は``ltjsarticle``が使えます。

## ヘルプを確認したい

```bash
$ lualatex --help
```

- ``lualatex -h``は使えないので注意が必要です

## バージョンを確認したい

```bash
$ lualatex --version
This is LuaHBTeX, Version 1.15.0 (TeX Live 2022)
...(省略)...
```

## latexmkしたい

```bash
# ./latexmkrc
$pdf_mode = 4;
```

{file}`latexmkrc`は``$pdf_mode = 4;``に設定します。
