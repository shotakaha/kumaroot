# 索引したい（`makeindex`）

```console
$ lualatex ファイル名.tex
$ makeindex ファイル名.idx
```

`makeindex`コマンドで**索引**をタイプセットできます。
索引ありのLaTeXファイルをコンパイルすると`.idx`ファイルが生成されます。
この`.idx`ファイルを使って、索引を生成します。
