# latexmkを使いたい

LaTeXファイルをコンパイルするプロセスを自動化するためのコマンドです。
LaTeX版makeだと考えればよく、
目次や参照をするために自動でコンパイルを繰り返したり、
変更のあったファイルのみ差分コンパイルしたりできます。

設定ファイルは``latexmkrc``（もしくは``.latexmkrc``）です。


## 設定ファイル

```tex
@default_files = ("00_sample", "01_sample", "02_sample");
$pdf_mode = 4;
```

### コンパイル対象ファイルを指定したい

```bash
@default_files = ("00_sample", "01_sample", "02_sample");
```

コンパイル対象のファイルは複数指定できます。

### エンジンを指定したい

```bash
$pdf_mode = 0;  # PDFを生成しない
$pdf_mode = 1;  # pdflatex
$pdf_mode = 2;  # ps2pdf
$pdf_mode = 3;  # dvipdf
$pdf_mode = 4;  # lualatex
$pdf_mode = 5;  # xelatex
```

LuaLaTeXを使う場合は``$pdf_mode=4``にします。

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

## コンパイルしたファイルを別ディレクトリに作成したい

```bash
latexmk -outdir="out"
```

## 中間ファイルを別ディレクトリに作成したい

```bash
latexmk -auxdir="aux"
```

- ``latexmk -c``するときには``-auxdir="aux"``が必要です
- もちろん{command}`rm -r aux/`でも削除できます


## 中間ファイルを削除したい

```bash
$ latexmk -c
$ latexmk -C
```

- 中間ファイルには``.aux`` / ``.fdb_latexmk`` / ``.fls`` / ``.log`` / ``.out``などの拡張子があります。
- {command}`-c`オプションで``dvi`` / ``ps`` / ``pdf`` 以外の中間ファイルが削除できます
- {command}`-C`オプションですべての中間ファイルが削除できます

## リファレンス

- {command}`texdoc latexmk`
