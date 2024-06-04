# ビルドしたい（``cmake``）

```console
// プロジェクト内に移動する
$ cd $G4WORK/プロジェクト

// ビルド用ディレクトリを作成する
(プロジェクト) $ mkdir build
(プロジェクト)$ cd build

// ビルド準備する
(プ/build) $ cmake ..

// ビルドする
(プ/build) $ make -j8   # 必要ならば make install する
```

Geant4本体と同じようにアプリケーションも[CMake](https://cmake.org/)でビルド準備します。
自作アプリケーションも、付属サンプルのように``CMakeLists.txt``が必要です。

ここでも``cmake``の作法（out-of-source）にしたがい、ビルド用ディレクトリで作業します。
ディレクトリ名は任意ですが、分かりやすく``build``としました。
ビルド作業はすべてこのディレクトリで行います。

まずはじめに``CMakeLists.txt``から、``Makefile``などビルドに必要なファイルを生成します。
ビルド用ディレクトリに対して``CMakeLists.txt``は親ディレクトリにあるので``cmake ..``を実行しています。

そして``Makefile``から実行ファイルを生成します。
``Makefile``はビルド用ディレクトリの中にあるので``make -j8``を実行しています。
プロセッサ数のオプション（``-jN``）は指定した方がよいです。

実行ファイルは現在のディレクトリ（``build``）に生成されます。
プロジェクトの中でアプリケーションを実行するのがよいと思うので、ここで完了です。
もし、システム全体で使いたい場合は``make install``します。

```console
// アプリケーションを実行
$ ./実行ファイル名    # 対話モード
$ ./実行ファイル名 マクロ.mac    # バッチモード
```

アプリケーションの実行方法は「対話モード」と「バッチモード」の2種類あります。
引数なしで実行すると対話モード、
引数にマクロファイル（``.mac``）を指定するとバッチモードになります。

マクロは、対話モードで使用するコマンドをまとめたようなファイルです。
対話モードで起動するときも、同じディレクトリにある
``init_vis.mac``と``vis.mac``が読み込まれるようです。

## 環境変数のエラー

```console
$ cmake ..
CMake Error at CMakeLists.txt:13 (find_package):
  By not providing "FindGeant4.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Geant4", but
  CMake did not find one.

  Could not find a package configuration file provided by "Geant4" with any
  of the following names:

    Geant4Config.cmake
    geant4-config.cmake

  Add the installation prefix of "Geant4" to CMAKE_PREFIX_PATH or set
  "Geant4_DIR" to a directory containing one of the above files.  If "Geant4"
  provides a separate development package or SDK, be sure it has been
  installed.

-- Configuring incomplete, errors occurred!
```

Geant4に関する環境変数の設定を忘れて``cmake``するとエラーになります。
インストール先（``$G4HOME/g4install/install``）の中にある設定スクリプト（``bin/geant4.sh``）を、その場で読み込んでからビルドしなおしてください。

```console
// bash/zshの場合
$ source $G4HOME/g4install/install/geant4.sh

// csh/tcshの場合
$ source $G4HOME/g4install/install/geant4.csh
```
