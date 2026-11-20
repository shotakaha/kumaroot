# ビルド構成オプションしたい（`cmake -D`）

```console
$ cmake -S source -B build -DCMAKE_INSTALL_PREFIX=install -DCMAKE_PREFIX_PATH=$(brew --prefix qt) -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON
```

`cmake -D`（`cmake --define`）オプションでビルド構成オプションを指定できます。
Geant4にはたくさんのビルド構成オプションがあります。
その中から、有効（`ON`）にしておくとよいオプションをいくつか紹介します。

以下の例では、`-S source -B build`を省略しています。
実際に実行するときは、`~/geant4/v11.X.Y/`で`-S source -B build`を付けてください。

## インストールしたい（`CMAKE_INSTALL_PREFIX`）

```console
$ cmake -DCMAKE_INSTALL_PREFIX=install
```

`CMAKE_INSTALL_PREFIX`は、`cmake --install`したときに、ビルドした実行ファイルやライブラリなどをインストールするパスを指定するオプションです。
デフォルトは`/usr/local/`になっています。

システムの管理者権限がない場合、`/usr/local/`にインストールできない場合があります。
また、個人用に環境を構築する場合や複数のバージョンを使い分けたい場合もあります。
そのような場合は、インストール先を変更しましょう。

:::{note}

このドキュメントで紹介している方法では、`$HOME/geant4/{versions}/install`にインストールするように設定を変更しています。

:::

## 依存ライブラリしたい（`CMAKE_PREFIX_PATH`）

```console
$ cmake -DCMAKE_PREFIX_PATH="/path/to/dependencies;/path/to/other/dependencies"
```

`CMAKE_PREFIX_PATH`は依存ライブラリの検索パスを指定するオプションです。
複数のパスを指定する場合は、`;`（セミコロン）で区切ります。
`;`はシェルで特別な意味を持つので、パス全体を引用符（`"`）で囲んでください。

## マルチスレッド対応したい（`GEANT4_BUILD_MULTITHREADED`）

```console
$ cmake -DGEANT4_BUILD_MULTITHREADED=ON
```

`GEANT4_BUILD_MULTITHREADED`はマルチスレッドを有効にするオプションです。
デフォルトで有効（`ON`）になっています。

## データセットしたい（`GEANT4_INSTALL_DATA`）

```console
$ cmake -DGEANT4_INSTALL_DATA=ON
```

`GEANT4_INSTALL_DATA`は、Geant4のシミュレーションに必要なデータセットのダウンロードを有効にするオプションです。
デフォルトは無効（`OFF`）になっています。
このドキュメントでは、データセットをインストールするために`ON`を指定しています。

データセットのインストール先は、`GEANT4_INSTALL_DATADIR`で決まります。
デフォルトは`${CMAKE_INSTALL_DATADIR}/data`で、
通常は`share/Geant4/data`になります。

## 付属サンプルしたい（`GEANT4_INSTALL_EXAMPLES`）

```console
$ cmake -DGEANT4_INSTALL_EXAMPLES=ON
```

`GEANT4_INSTALL_EXAMPLES`は付属サンプルをインストールするオプションです。
デフォルトで有効（`ON`）になっています。
サンプルコードは`share/Geant4/examples`にインストールされます。
具体的な使い方は「[](geant4-examples)」を参照してください。

## Qtしたい（`GEANT4_USE_QT`）

```console
$ brew install qt
$ cmake -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt)
```

`GEANT4_USE_QT`はQtを有効にするオプションです。
デフォルトは無効（`OFF`）になっています。

このオプションを有効にする場合は、まずQtをインストールして、`CMAKE_PREFIX_PATH`にQtのインストール先を指定します。

Qtのバージョンは、Geant4のバージョンによってデフォルトが異なります。
v11.4以降のデフォルトはQt6です。
Qt5を使う場合は、`-DGEANT4_USE_QT_QT5=ON`を指定します。
また、v11.4より前のデフォルトはQt5です。
Qt6を使う場合は、`-DGEANT4_USE_QT_QT6=ON`を指定します。

:::{note}

v11.0からQt6はサポートされているようですが、v11.2.1ではQt6でビルドに失敗しました。
もしビルドできない場合は、ビルドできるバージョンを使いましょう。

:::


## OpenGLしたい（`GEANT4_USE_OPENGL_X11`）

```console
$ cmake -DGEANT4_USE_OPENGL_X11=ON
```

`GEANT4_USE_OPENGL_X11`はOpenGLを有効にするオプションです。
デフォルトで無効（`OFF`）になっています。

## VTKしたい（`GEANT4_USE_VTK`）

```console
$ cmake -DGEANT4_USE_VTK=ON
```

`GEANT4_USE_VTK`はVTKを有効にするオプションです。
デフォルトで無効（`OFF`）になっています。

## GDMLしたい（`GEANT4_USE_GDML`）

```console
$ cmake -DGEANT4_USE_GDML=ON
```

`GEANT4_USE_GDML`はGDMLを有効にするオプションです。
デフォルトで無効（`OFF`）になっています。

## HDF5したい（`GEANT4_USE_HDF5`）

```console
$ cmake -DGEANT4_USE_HDF5=ON
```

`GEANT4_USE_HDF5`はHDF5を有効にするオプションです。
デフォルトで無効（`OFF`）になっています。


## 利用可能なビルドオプションの一覧

[Geant4 Build Options](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#geant4buildo)を参考にしました。
使いそうなオプションや、知っておくとよさそうなオプションを整理しました。

| オプション名 | デフォルト値 | 推奨値 | 説明 |
|---|---|---|---|
| CMAKE_INSTALL_PREFIX |  ``/usr/local/`` | ``$HOME/geant4/バージョン番号/install`` | Geant4をインストールするパス |
| CMAKE_PREFIX_PATH | | ``$(brew --prefix qt)`` | Geant4のビルドに必要な外部パッケージのパス。``;``（セミコロン）で複数のパスを指定できる |
| CMAKE_INSTALL_BINDIR | ``bin`` | | 実行ファイルがインストールされるパス |
| CMAKE_INSTALL_INCLUDEDIR | ``include`` | | ヘッダーファイルがインストールされるパス |
| CMAKE_INSTALL_LIBDIR | ``lib``（環境により``lib64``） | | ライブラリがインストールされるパス |
| CMAKE_INSTALL_DATAROOTDIR | ``share`` | | 読み取り専用のデータがインストールされるパス |
| GEANT4_INSTALL_DATA |  ``OFF`` | ``ON`` | インストール時にGeant4のデータセットのダウンロードを有効にするフラグ |
| GEANT4_INSTALL_DATADIR | ``${CMAKE_INSTALL_DATADIR}/data`` | | データセットをインストールするパス |
| GEANT4_INSTALL_EXAMPLES | ``ON`` | | 付属サンプルをインストールするフラグ |
| GEANT4_INSTALL_PACKAGE_CACHE | ``OFF`` | | 必要なパッケージのビルド時の場所を記録するファイルをインストールするフラグ |
| GEANT4_USE_SYSTEM_CLHEP | ``OFF`` | ``OFF`` | システムのCLHEPライブラリを使うフラグ。最近のGeant4はCLHEP同梱なのでOFFでOK |
| GEANT4_USE_SYSTEM_EXPAT | ``ON`` | | システムのExpatを有効にするフラグ |
| GEANT4_USE_SYSTEM_ZLIB | ``OFF`` | | システムのzlibを有効にするフラグ |
| GEANT4_USE_GDML | ``OFF`` | | GDMLを有効にするフラグ |
| GEANT4_USE_INVENTOR_QT | ``OFF`` | | OpenInventorQtを有効にするフラグ |
| GEANT4_USE_OPENGL_X11 | ``OFF`` | ``ON`` | X11（XQuartz） OpenGLを有効にするフラグ |
| GEANT4_USE_QT | ``OFF`` | ``ON`` | Qtを有効にするフラグ |
| GEANT4_USE_QT_QT5 | ``OFF`` | | v11.4以降。Qt5を使うフラグ（`GEANT4_USE_QT`がONのときのみ有効） |
| GEANT4_USE_QT_QT6 | ``OFF``（v11.4以降は``ON``） | | v11.4より前。Qt6を使うフラグ（`GEANT4_USE_QT`がONのときのみ有効） |
| GEANT4_USE_RAYTRACER_X11 | ``OFF`` | | RayTracerを有効にするフラグ |
| GEANT4_USE_VTK | ``OFF`` | | VTKを有効にするフラグ |
| GEANT4_USE_XM | ``OFF`` | | Motifを有効にするフラグ |
| GEANT4_USE_SMARTSTACK | ``OFF`` | | G4SmartStackを有効にするフラグ |
| GEANT4_USE_FREETYPE | ``OFF`` | | Freetypeフォントを有効にするフラグ |
| GEANT4_USE_HDF5 | ``OFF`` | | HDF5形式を有効にするフラグ |
