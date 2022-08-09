# latexmkを使いたい

LaTeX文書をコンパイルするプロセスを自動化するためのコマンドです。
LaTeX用のMakefileだと考えればよいと思います。

目次や参照をするために自動で2回コンパイルしたり、
変更のあったファイルのみ差分コンパイルしたりできます。

同じディレクトリに``latexmkrc``もしくは``.latexmkrc``を置くことで、コンパイル設定をプリセットできます

```tex
@default_files = ("00_sample", "01_sample", "02_sample");
$pdf_mode = 4;
```

## コンパイル対象ファイルを指定したい

```bash
@default_files = ("00_sample", "01_sample", "02_sample");
```

## エンジンを指定したい

```bash
$pdf_mode = 0;  # PDFを生成しない
$pdf_mode = 1;  # pdflatex
$pdf_mode = 2;  # ps2pdf
$pdf_mode = 3;  # dvipdf
$pdf_mode = 4;  # lualatex
$pdf_mode = 5;  # xelatex
```


## ヘルプを確認したい

```bash
$ latexmk -h
$ latexmk --help
```

## バージョンを確認したい

```bash
$ latexmk -v
$ latexmk --version
Latexmk, John Collins, 17 Mar. 2022. Version 4.77
```

## 中間ファイルを削除したい

```bash
$ latexmk -c
$ latexmk -C
```

- 中間ファイルには``.aux`` / ``.fdb_latexmk`` / ``.fls`` / ``.log`` / ``.out``などの拡張子があります。
- {command}`-c`オプションで``dvi`` / ``ps`` / ``pdf`` 以外の中間ファイルが削除できます
- {command}`-c`オプションですべての中間ファイルが削除できます
