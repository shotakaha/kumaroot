# マクロしたい（`root macro.C`）

```console
$ root macro.C

// マクロを実行後に終了
$ root -q macro.C

// マクロをバッチモードで実行
$ root -b macro.C
```

`root`コマンドの引数にマクロ（`macro.C`）を指定できます。
マクロの拡張子は`.C`とするのが慣習です。
ファイル名とマクロ内の関数名は同じにする必要があります。

## マクロを読み込みたい（`.L`）

```console
$ root

root [0] .L macro.C
root [1] macro_function()
```

ROOTのインタープリター上で、`.L`コマンドを使ってマクロを読み込むこともできます。
マクロを読み込んだ後は、マクロ内の任意の関数を呼び出すことができます。
