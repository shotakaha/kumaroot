# ビルド構成したい（`cmake`）

```console
// オプションを指定してcmakeする
$ cd ~/geant4/v11.2.1
(~/geant4/v11.2.1/) $ cmake \
-G "Unix Makefiles" \
-S source \
-B build \
-DCMAKE_INSTALL_PREFIX=install \
-DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) \
-DGEANT4_INSTALL_DATA=ON \
-DGEANT4_USE_OPENGL_X11=ON \
-DGEANT4_USE_QT=ON
```

`cmake`を使ってビルドに必要なファイルを生成します。
Geant4のビルドオプションは
`-Dオプション名=設定値`で変更できます。

```console
(~/geant4/v11.2.1/) $ less build/CMakeCache.txt
```

`cmake`を実行すると、ビルド用ディレクトリに`CMakeCache.txt`が生成されます。
このファイルを確認して、オプションが設定できているか確認できます。

## ビルドツールを設定する（`-G`）

```console
$ cmake -G "Unix Makefiles"
$ cmake -G "Ninja"
```

`-G`オプションでジェネレーター（＝ビルドツール）を変更できます。
多くの場合、デフォルトは`make`（＝`Unix Makefiles`）です。

## インストール先を設定する（`-DCMAKE_INSTALL_PREFIX`）

```console
// 絶対パスで指定
$ cmake -DCMAKE_INSTALL_PREFIX=$HOME/geant4/v11.2.1/install

// 相対パスで指定
$ cmake -DCMAKE_INSTALL_PREFIX=install
```

`CMAKE_INSTALL_PREFIX`オプションで、Geant4本体のインストール先のパスを変更できます。
絶対パス、もしくは`cmake`を実行したパスからの相対パスを指定できます。

## ライブラリを追加する（`-DCMAKE_PREFIX_PATH`）

```console
// macOSの設定
$ cmake -DCMAKE_PREFIX_PATH=/opt/homebrew/opt/qt@5

// 汎用的な設定
$ cmake -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5)
```

`CMAKE_PREFIX_PATH`で、ビルドに必要なライブラリのパスを追加できます。
Qtを使う場合、ローカルにインストールされているQtのパスを指定する必要があります。

:::{note}

HomebrewでインストールしたQtのパスは、プラットフォームによって違うことがあります。
`/opt/homebrew/opt/qt@5`のようなベタ書きではなく、
`brew --prefix qt@5`で取得するほうが汎用的です。

```console
// macOS (x86_64)
$ brew --prefix qt@5
/usr/local/qt@5

// macOS (M2 Apple)
$ brew --prefix qt@5
/opt/homebrew/opt/qt@5

// WSL2 (Ubuntu)
$ brew --prefix qt@5
/home/linuxbrew/.linuxbrew/opt/qt@5
```

:::

## オプションを再利用したい（`CMakePresets.json`）

```console
$ cmake \
-S source \
-B build \
-DCMAKE_INSTALL_PREFIX=install \
--preset=geant4-build
```

`CMakePresets.json`を使うと、オプション入力時のタイポを防ぐことができます。

```json
{
    "name": "geant4-build",
    "displayName": "Geant4 Build",
    "description": "Build Geant4 with OpenGL and Qt",
    "generator": "Unix Makefiles",
    "binaryDir": "${sourceDir}/build",
    "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Release",
        "GEANT4_INSTALL_DATA": "ON",
        "GEANT4_USE_OPENGL_X11": "ON",
        "GEANT4_USE_QT": "ON"
    }
}
```

## ビルドオプションを確認する

[Geant4 Build Options](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#geant4buildo)を参考に、
使いそうなオプションや、知っておくとよさそうなオプション設定のデフォルト値を整理しました。

| オプション名 | デフォルト値 | 推奨値 | 説明 |
|---|---|---|---|
| CMAKE_INSTALL_PREFIX |  ``/usr/local/`` | ``$HOME/geant4/バージョン番号/install`` | Geant4をインストールするパス |
| CMAKE_PREFIX_PATH | | ``$(brew --prefix qt@5)`` | Geant4のビルドに必要な外部パッケージのパス。``;``（セミコロン）で複数のパスを指定できる |
| CMAKE_INSTALL_BINDIR | ``bin`` | | 実行ファイルがインストールされるパス |
| CMAKE_INSTALL_INCLUDEDIR | ``include`` | | ヘッダーファイルがインストールされるパス |
| CMAKE_INSTALL_LIBDIR | ``lib(+?SUFFIX))`` | | ライブラリがルがインストールされるパス |
| CMAKE_INSTALL_DATAROOTDIRR | ``share`` | | 読み取り専用のデータセットがルがインストールされるパス |
| GEANT4_INSTALL_DATA |  ``ON`` | ``ON`` | インストール時にGeant4のデータセットのダウンロードを有効にするフラグ |
| GEANT4_INSTALL_DATADIR | ``CMAKE_INSTALL_DATAROOTDIR`` | | データセットをインストールするパス |
| GEANT4_INSTALL_EXAMPLES | ``ON`` | | サンプルプロジェクトを有効にするフラグ |
| GEANT4_INSTALL_PACKAGE_CACHE | ``ON`` | | サンプルプロジェクトを有効にするフラグ |
| GEANT4_USE_SYSTEM_CLHEP | ``OFF`` | ``OFF`` | システムのCLHEPライブラリを有効にするフラグ。RayTracerを有効にするフラグ。最近のGeant4はCLHEP同梱なのでOFFでOK |
| GEANT4_USE_SYSTEM_EXPAT | ``ON`` | | システムのExpatを有効にするフラグ。|
| GEANT4_USE_SYSTEM_ZLIB | ``OFF`` | | システムのzlibを有効にするフラグ。|
| GEANT4_USE_GDML | ``OFF`` | | GDMLを有効にするフラグ |
| GEANT4_USE_INVENTOR_QT | ``OFF`` | | OpenInventorQtを有効にするフラグ |
| GEANT4_USE_OPENGL_X11 | ``OFF`` | ``ON`` | X11（XQuartz） OpenGLを有効にするフラグ |
| GEANT4_USE_QT | ``OFF`` | ``ON`` | Qt5を有効にするフラグ |
| GEANT4_USE_QT6 | ``OFF`` | | Qt6を有効にするフラグ |
| GEANT4_USE_RAYTRACER_X11 | ``OFF`` | | RayTracerを有効にするフラグ |
| GEANT4_USE_VTK | ``OFF`` | | VTKを有効にするフラグ。|
| GEANT4_USE_XM | ``OFF`` | | Motifを有効にするフラグ。|
| GEANT4_USE_SMARTSTACK | ``OFF`` | | G4SmartStackを有効にするフラグ。|
| GEANT4_USE_FREETYPE | ``OFF`` | | Freetypeフォントを有効にするフラグ。|
| GEANT4_USE_HDF5 | ``OFF`` | | HDF5形式を有効にするフラグ。|

## ディレクトリ構成

```console
$ tree ~/geant4/v11.2.1 -L 2
geant4/v11.2.1
├── build
│   ├── BuildProducts
│   ├── CMakeCPackOptions.cmake
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   ├── CPackConfig.cmake
│   ├── CPackSourceConfig.cmake
│   ├── Externals
│   ├── G4EXPATShim.cmake
│   ├── G4FreetypeShim.cmake
│   ├── G4HDF5Shim.cmake
│   ├── G4ModuleAdjacencyList.txt
│   ├── G4ModuleInterfaceMap.csv
│   ├── G4MotifShim.cmake
│   ├── G4X11Shim.cmake
│   ├── Geant4Config.cmake
│   ├── Geant4ConfigVersion.cmake
│   ├── Geant4LibraryDepends.cmake
│   ├── Geant4PackageCache.cmake
│   ├── InstallTreeFiles
│   ├── LICENSE.txt
│   ├── Makefile
│   ├── Modules
│   ├── README.txt
│   ├── UseGeant4.cmake
│   ├── UseGeant4_internal.cmake
│   ├── _source_extras
│   ├── cmake_install.cmake
│   ├── cmake_uninstall.cmake
│   ├── cmake_uninstall.cmake.in
│   ├── cxx_filesystem
│   ├── data
│   ├── geant4-config
│   ├── geant4_module_check.py
│   ├── geant4_validate_sources.cmake
│   ├── geant4make.csh
│   ├── geant4make.sh
│   ├── source
│   └── source_package_extras.cmake
├── source
│   ├── CHANGELOG -> ReleaseNotes
│   ├── CITATION.cff
│   ├── CMakeLists.txt
│   ├── CONTRIBUTING.rst
│   ├── LICENSE
│   ├── README.rst
│   ├── ReleaseNotes
│   ├── cmake
│   ├── config
│   ├── environments
│   ├── examples
│   ├── packaging
│   └── source
```

`source/CMakeLists.txt`の内容をもとに、
`build/CMakeCache.txt`が生成されました。
このようなディレクトリ構成になっていたら、次に進んでください。
