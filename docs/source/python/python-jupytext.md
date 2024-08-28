# JupyTextしたい（``jupytext``）

```console
$ pipx install jupytext
```

`pipx`で`jupytext`をインストールしました。

## ノートブックを変換したい（``--to`` / ``--output``）

```console
$ jupytext --to script ノートブック名.ipynb
$ jupytext --to md ノートブック名.ipynb
$ jupytext --to myst ノートブック名.ipynb
$ jupytext --to md --output 出力ファイル名.md ノートブック名.ipynb
```

``--to``オプションで出力先の形式を指定します。
``ipynb``、``markdown``、``script``の文字列や、
ファイルの拡張子（``md``、``Rmd``、``jl``、``py``、``R``、...など）を指定します。

``-o / --output``オプションで出力先のファイル名を指定します。
デフォルトは入力ファイル名と同じです（拡張子は変更されます）。


