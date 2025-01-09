```{eval-rst}
.. index::
    pair: ビルドしたい; LaTeX
```

# タイプセットしたい（`latexmk`）

```console
$ latexmk [オプション] ファイル名  # .texはあってもなくてもよい
$ latexmk  # ファイル名がなくてもよい（ときもある）
```

`latexmk`はLaTeX版Makefileのようなもので、
文書のタイプセット（＝コンパイル）を自動化できるコマンドです。

目次や参照が更新されたときに複数回コンパイルしたり、
変更のあったファイルのみを差分コンパイルしたり、
だんだん煩わしくなってくる作業を簡単化できます。
ファイル名を指定しない場合でも、よしなにやってくれます。

:::{note}

`latexmk`は1990年代に開発され、2008年にTeX Liveに同梱されそうです。
2010年ころにエディターとの統合や設定例の普及により、
現在のように広く利用されるようになりました。

:::


## シェルエスケープしたい（``-shell-escape``）

```console
$ latexmk -shell-escape
```

コードをシンタックスハイライトする``minted``パッケージなど、外部スクリプトを呼び出すパッケージを使う場合、``-shell-escape``オプションが必要です。

## エラーを無視したい

```console
$ latexmk -f -interaction=nonstopmode
```

```{eval-rst}
.. index::
    pair: プレビューしたい; LaTeX
```
## ライブプレビューしたい（``-pvc``）

```console
$ latexmk -pvc
```

``-pvc``オプションでPDF出力をライブプレビューできます。
これで編集作業が捗ります。

## 設定ファイルを指定したい

```bash
$ latexmk -r latexmkjarc
```

設定ファイルのデフォルトは{file}`latexmkrc`もしくは{file}`.latexmkrc`ですが、``-r``オプションで変更できます。

## 中間ファイルを削除したい（``-c / -C``）

```console
$ latexmk -c
$ latexmk -C  # 中間ファイルをすべて削除する
```

コンパイルすると``.aux`` / ``.fdb_latexmk`` / ``.fls`` / ``.log`` / ``.out``などの拡張子の中間ファイルが作成されます。
`-c`オプションをつけると、コンパイル後にそれらの中間ファイルを削除できます。
`-C`オプションで``dvi`` / ``ps`` / ``pdf``も含めたすべての中間ファイルを削除できます。





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
