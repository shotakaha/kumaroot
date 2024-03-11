# B2したい（``examples/basic/B2``）

![](./fig/exampleB2.png)

B2の題材は飛跡検出器です。
外部磁場を与え、粒子が曲がる様子を観察できます。

## ビルドしたい（``cmake``）

```console
$ cd examples/basic/B2/B2a
(B2a) $ mkdir build
(B2a) $ cd build
(B2a/build) $ cmake ..
(B2a/build) $ make -j8
(B2a/build) $ ./exampleB2a
```

``examples/basic/B2/``の中には``B2a``と``B2b``のディレクトリがあります。
シミュレーションできることは同じなので、どちらをビルドしてもOKです。
マクロファイルが用意されているので、適当に実行して遊んでみます。
