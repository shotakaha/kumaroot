# 索引したい（`makeindex`）

```console
$ lualatex ファイル名.tex
$ makeindex ファイル名.idx
```

`makeindex`コマンドで**索引**をタイプセットできます。
索引ありのLaTeXファイルをコンパイルすると、索引ファイル（`.idx`）が生成されます。
この`.idx`ファイルを使って、索引を生成します。

## 自動処理したい（`$makeindex=1`）

```unixconfig
$makeindex = 1;
```

[latexmkrc](./latex-latexmkrc.md)に`$makeindex=1`と書いておくと、
索引ファイル（`.idx`）が存在する場合に`makeindex`を自動実行します。

## カスタマイズしたい

```unixconfig
$makeindex = "makeindex -s スタイル.ist";
$makeindex = "splitindex";
$makeindex = "xindy -L japanese -C utf8 -M スタイル.xdy";
```

`$makeindex`のコマンドをカスタマイズできます。
`makeindex`をオプション付きで実行したり、
`splitindex`や`xindy`などのコマンドを実行したりできます。
