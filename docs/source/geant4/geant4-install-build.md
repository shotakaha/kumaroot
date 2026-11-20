# ビルド＆インストールしたい（`cmake --build` / `cmake --install`）

```console
// ステップ1：バージョンごとの作業ディレクトリに移動する
$ cd ~/geant4/v11.4.3/

// ステップ2：ビルドする（--parallelで並列処理する）
$ cmake --build build --parallel

// ステップ3：インストールする
$ cmake --install build
```

`cmake --build`でビルドを実行します。
`--parallel`オプションを指定すると、並列処理でビルドできます。

`cmake --install`でインストールを実行します。
インストール先は、構成時に指定した`CMAKE_INSTALL_PREFIX`（`install/`）です。

## ディレクトリ構成

```console
$ tree ~/geant4/v11.4.3 -L 1
v11.4.3/
├── build/
├── install/
└── source/
```

`install/`の中に、実行ファイル、ヘッダー、ライブラリ、データセットなどが格納されます。
このディレクトリ構成になっていたら、インストール完了です。
