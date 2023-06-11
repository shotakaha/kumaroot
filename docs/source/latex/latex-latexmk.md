# タイプセットしたい（``latexmk``）

```console
$ latexmk
$ latexmk [オプション] ファイル名  # .texはあってもなくてもよい
```

LaTeX文書のタイプセット（＝コンパイル）を自動化するコマンドです。
目次や参照をするために自動でコンパイルを繰り返したり、
変更のあったファイルのみ差分コンパイルしたりできます。
ファイル名を指定しない場合でも、よしなにやってくれます。

## 設定ファイルしたい（``latexmkrc``）

:::{literalinclude} ../_static/latex/templates/latexmkrc
:::

LaTeX文書を作成する場合は、繰り返しコンパイルすることが多いです。
コマンドラインのオプションを毎回指定するのは面倒なので{file}``latexmkrc``を作成しておきましょう。

## エンジンを指定したい

```console
$ latexmk -lualatex ファイル名
```

```{toctree}
---
maxdepth: 1
---
latex-lualatex
latex-uplatex
```

## シェルエスケープしたい

```console
$ latexmk -shell-escape
```

コードをシンタックスハイライトする``minted``パッケージなど、外部スクリプトを呼び出すパッケージを使う場合、``-shell-escape``オプションが必要です。

## ライブプレビューしたい

```console
$ latexmk -pvc
```

``-pvc``オプションでPDF出力をライブプレビューできます。
これで編集作業が捗ります。

```text
## latexmkrc
$preview_continuous_mode = 1;
$pvc_timeout = 1;
$pvc_timeout_mins = 10;  # 30min; default
$sleep_time = 60; # in sec
```

{file}`latexmkrc`で設定する場合は``$preview_continuous_mode = 1``に設定します。
ライブプレビューをしたまま忘れてしまうことがあるので、一定時間更新がなかった場合に自動で終了するように``$pvc_timeout = 1``と``$pvc_timeout_mins = 分``も設定しておくとよいと思います。

文書を大量に作成していて、頻繁に更新しているフェーズは``$sleep_time = 秒``を長めに設定しておくとよいです。
こまめに保存している最中に、ムダにコンパイルされる回数を減らすことができます。

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
