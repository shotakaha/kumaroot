# 一時ファイルしたい（`mktemp`）

```console
$ mktemp
/var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tmp.AfnWksCOe2
```

`mktemp`で一時ファイルを作成できます。
ファイル名はランダムに生成されるため、他のスクリプトとの競合を避けることができます。
単体で使うより、シェルスクリプトに組み込むことで力を発揮します。
