# ビルドしたい（``cmake``）

```console
$ brew install --cask cmake
```

Geant4アプリケーションのビルドには[CMake](https://cmake.org/)を使います。
Homebreを使ってCaskをインストールしておきます。

```console
$ cd プロジェクト
$ mkdir build && cd build
$ cmake ..         # CMakeList.txtがあるディレクトリを指定する
$ cmake --build .  # Makefileがあるディレクトリを指定する
$ ./実行ファイル名 マクロ名
```

Geant4付属のサンプルのように、適切な``CMakeLists.txt``が用意されたプロジェクトで、上記の手順で``cmake``コマンドを使って実行ファイルをビルドできます。

ポイントは``cmake``の作法にしたがい、ビルド用のディレクトリを作成する点です。
ディレクトリ名は任意ですが、分かりやすく``build``としました。
ビルド作業はすべてこのディレクトリで行います。

まずはじめに``CMakeLists.txt``から、``Makefile``などビルドに必要なファイルを生成します。
ビルド用ディレクトリに対して``CMakeLists.txt``は親ディレクトリにあるので``cmake ..``を実行しています。

そして``Makefile``から実行ファイルを生成します。
``Makefile``はビルド用ディレクトリの中にあるので``cmake --build .``を実行しています。

:::{hint}

``Makefile``を使ったビルドなので、``make``でも代用できます。
なんとなく``cmake``で揃えたかったので、このように整理しました。

:::

