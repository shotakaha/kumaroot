# 一時ファイルしたい（`mktemp`）

```console
$ mktemp
/var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tmp.AfnWksCOe2

$ mktemp --tmpdir=.
tmp.EBOCpr7uXX
```

`mktemp`で一時ファイルを作成できます。
ファイルは`$TMPDIR`に作成されます。
`--tmpdir`オプションでファイルの生成先を変更できます。

ファイル名がランダムに生成されるので、他のスクリプトとの競合を避けることができます。
単体で使うより、シェルスクリプトに組み込むことで力を発揮します。

## ファイル名したい

```console
$ mktemp -t example
/var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/example.QaYKwbG8BA


$ mktemp example-XXXXXX
example-uJrVLB
```

`-t`オプションで、ファイル名のprefixを変更できます。
デフォルトは`tmp`になっています。

また、引数にファイル名のテンプレートを指定できます。
`XXXXX`の部分が`X`の数だけランダムな文字に置換されます。

:::{note}

`x`（小文字）ではダメでした。
また、`X`のあとに文字列があってもダメでした。
なので、`example-XXX.txt`のように拡張子をつけることはできません。

:::

## ディレクトリしたい（`-d` / `--directory`）

```console
$ mktemp --directory
/var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tmp.t6ZigUBJUV

$ mktemp --directory --tmpdir=.
./tmp.yuE8DXF3Hx
```

`--directory`オプションで一時的なディレクトリを作成できます。
`--tmpdir`オプションと組み合わせて、任意のディレクトリの中に作成できます。
