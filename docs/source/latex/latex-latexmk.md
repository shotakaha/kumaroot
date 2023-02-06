# タイプセットしたい（``latexmk``）

```bash
$ latexmk
$ latexmk [オプション] ファイル名  # .texはあってもなくてもよい
```

LaTeX文書のタイプセット（＝コンパイル）を自動化するコマンドです。
目次や参照をするために自動でコンパイルを繰り返したり、
変更のあったファイルのみ差分コンパイルしたりできます。
ファイル名を指定しない場合でも、よしなにやってくれます。

```{toctree}
---
maxdepth: 1
---
latex-lualatex
latex-uplatex
```

## エンジンを指定したい

```bash
$ latexmk -lualatex ファイル名
```

## シェルエスケープしたい

```bash
$ latexmk -shell-escape
```

コードをシンタックスハイライトする``minted``パッケージなど、外部スクリプトを呼び出すパッケージを使う場合、``-shell-escape``オプションが必要です。

## ライブプレビューしたい

```bash
$ latexmk -pvc
```

PDF出力をライブプレビューできると編集作業が捗ります。
そんなときは``-pvc``オプションを使いましょう。

## 出力ファイルを別ディレクトリに作成したい

```bash
latexmk -outdir="outd"
```

出力ファイルを保存するディレクトリを指定できます。
``-auxdir``と一緒に使えます。

## 中間ファイルを別ディレクトリに作成したい

```bash
$ latexmk -auxdir="aux"
$ latexmk -c -auxdir="aux"  # 中間ファイルを削除する
```

中間ファイルを保存するディレクトリを指定できます。
中間ファイルを削除する場合も、{command}`-auxdir="aux"`が必要です。
もちろん{command}`rm -r aux/`で直接削除できます。

## 中間ファイルを削除したい

```bash
$ latexmk -c
$ latexmk -C  # 中間ファイルをすべて削除する
```

コンパイルすると``.aux`` / ``.fdb_latexmk`` / ``.fls`` / ``.log`` / ``.out``などの拡張子の中間ファイルが作成されます。
`-c`オプションをつけると、コンパイル後にそれらの中間ファイルを削除できます。
`-C`オプションで``dvi`` / ``ps`` / ``pdf``も含めたすべての中間ファイルを削除できます。

## エラーを無視したい

```bash
$ latexmk -f -interaction=nonstopmode
```

## 設定ファイルを指定したい

```bash
$ latexmk -r latexmkjarc
```

設定ファイルのデフォルトは{file}`latexmkrc`もしくは{file}`.latexmkrc`ですが、``-r``オプションで変更できます。


## ヘルプを確認したい

```bash
$ latexmk -h
$ latexmk --help
$ texdoc latexmk
```

シェルでの実行オプションを確認したい場合は`-h / --help` で十分です。
もっと詳細を確認したい場合は``texdoc``してPDFを確認するのが一番です。

## バージョンを確認したい

```bash
$ latexmk -v
$ latexmk --version
Latexmk, John Collins, 17 Mar. 2022. Version 4.77
```

## リファレンス

- {command}`texdoc latexmk`
