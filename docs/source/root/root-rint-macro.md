# マクロしたい

```console
$ root マクロ名.C
$ root -b マクロ名.C
```

ROOTコマンドはマクロとしてファイルにまとめることができます。
引数にマクロ名を指定して、


## マクロを読み込みたい（``.L``）

```console
$ root

root [0] .L マクロ.C
root [1] macro_function()
```

`.L`でRINTにマクロを読み込めます。
