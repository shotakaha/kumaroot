# ビルド構成したい（`cmake`）

```console
$ cd ~/geant4/v11.X.Y/
$ cmake -G Ninja -S source -B build -DCMAKE_INSTALL_PREFIX=install -DCMAKE_PREFIX_PATH=(brew --prefix qt) -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON
```

`cmake`でビルド構成を指定します。

```console
(~/geant4/v11.X.Y/) $ less build/CMakeCache.txt
```

`cmake`を実行すると、ビルド用ディレクトリに`CMakeCache.txt`が生成されます。
このファイルを確認して、オプションが設定できているか確認できます。

## ビルドシステムしたい（`cmake -G`）

```console
$ cmake -G Ninja
```

`-G / --generator`オプションでビルドシステムを指定できます。
デフォルトは`Unix Makefiles`です。
どちらも同じソースを、同じオプションでビルドした場合の結果（バイナリなど）は同じになりますが、一般に`Ninja`のほうが`Make`より高速にビルドできるらしいです。

## 分割ビルドしたい（`cmake -S -B`）

```console
$ cmake -S source -B build
```

`-S / --source`オプションでソースコードのディレクトリを指定し、`-B / --build`オプションでビルド用のディレクトリを指定できます。
`cmake`では、ソースコードとビルド用のディレクトリを分けて管理することが推奨されています。

## ビルドオプションしたい（`cmake -D`）

```console
$ cmake -DCMAKE_INSTALL_PREFIX=install -DCMAKE_PREFIX_PATH=(brew --prefix qt) -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON
```

`-D / --define`オプションでビルドオプションを指定できます。
`-Dオプション名=値`の形式で記述します。

`-DCMAKE_INSTALL_PREFIX`はインストール先のディレクトリ（`CMAKE_INSTALL_PREFIX`）を指定するオプションです。
作業ディレクトリ（`~/geant4/v11.X.Y/`）の中に`install`ディレクトリを作成し、そこにインストールするようにしています。

`-DCMAKE_PREFIX_PATH`は依存ライブラリの検索パス（`CMAKE_PREFIX_PATH`）を指定します。
Qtを使う場合は、`brew --prefix qt`でQtのインストール先を取得し、指定する必要があります。

`-DGEANT4_INSTALL_DATA=ON`はGeant4のデータをインストールするオプション（`GEANT4_INSTALL_DATA`）を有効にしています。
`-DGEANT4_USE_OPENGL_X11=ON`はOpenGLを使うオプション（`GEANT4_USE_OPENGL_X11`）を有効にしています。
`-DGEANT4_USE_QT=ON`はQtを使うオプション（`GEANT4_USE_QT`）を有効にしています。

### 利用可能なビルドオプションを確認する

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

## プリセットしたい（`CMakePresets.json`）

```console
$ cmake -S source -B build --preset=geant4
```

`CMakePresets.json`にビルドオプションをまとめることで、オプション設定を再利用できます。
ファイルとして残すことで、ビルドオプションの設定を他の人と共有することもできます。
また、オプション設定時のタイポを防ぐことができます。

```json
{
    "name": "geant4",
    "displayName": "Geant4 Build",
    "description": "Build Geant4 with OpenGL and Qt",
    "generator": "Ninja",
    "binaryDir": "${sourceDir}/build",
    "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Release",
        "GEANT4_INSTALL_DATA": "ON",
        "GEANT4_USE_OPENGL_X11": "ON",
        "GEANT4_USE_QT": "ON"
    }
}
```

## ディレクトリ構成

```console
$ tree ~/geant4/v11.X.Y -L 2
geant4/v11.X.Y
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
