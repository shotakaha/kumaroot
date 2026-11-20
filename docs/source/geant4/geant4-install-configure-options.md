# ビルド構成オプションしたい（`cmake -D`）

```console
$ cmake -DCMAKE_INSTALL_PREFIX=install -DCMAKE_PREFIX_PATH=(brew --prefix qt) -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON
```

`cmake -D`（`cmake --define`）オプションでビルド構成オプションを指定できます。
Geant4にはたくさんのビルド構成オプションがあります。
その中から有効（`ON`）にしておくとよいオプションをいくつか紹介します。

## インストールしたい（`CMAKE_INSTALL_PREFIX`）

```console
$ cmake -DCMAKE_INSTALL_PREFIX=install
```

`CMAKE_INSTALL_PREFIX`は、`cmake --install`したときに、ビルドした実行ファイルやライブラリなどをインストールするパスを指定するオプションです。
デフォルトは`/usr/local/`になっています。

システムの管理者権限がなく`/usr/local/`にインストールできない場合、
個人用に環境を構築する場合、複数のバージョンを使い分ける場合などは、インストール先を変更するとよいです。

:::{note}

このドキュメントで紹介している方法では`$HOME/geant4/{versions}/install`にインストールするように設定を変更しています。

:::

## 依存ライブラリしたい（`CMAKE_PREFIX_PATH`）

```console
$ cmake -DCMAKE_PREFIX_PATH=/path/to/dependencies;/path/to/other/dependencies
```

`CMAKE_PREFIX_PATH`は依存ライブラリの検索パスを指定するオプションです。
複数のパスを指定する場合は、`;`（セミコロン）で区切ります。

## マルチスレッド対応したい（`GEANT4_USE_MULTITHREADING`）

```console
$ cmake -DGEANT4_USE_MULTITHREADING=ON
```

`GEANT4_USE_MULTITHREADING`はマルチスレッドを有効にするオプションです。
デフォルトで有効（`ON`）になっています。

## データセットしたい（`GEANT4_INSTALL_DATA`）

```console
$ cmake -DGEANT4_INSTALL_DATA=ON
```

`GEANT4_INSTALL_DATA`は、Geant4のシミュレーションに必要はデータセットのダウンロードを有効にするオプションです。
デフォルトで有効（`ON`）になっています。
データセットは`CMAKE_INSTALL_DATADIR`でダウンロードされます。
デフォルトは`share/Geant4/data`になっています。

## 付属サンプルしたい（`GEANT4_INSTALL_EXAMPLES`）

```console
$ cmake -DGEANT4_INSTALL_EXAMPLES=ON
```

`GEANT4_INSTALL_EXAMPLES`は付属サンプルのダウンロードを有効にするオプションです。
デフォルトで有効（`ON`）になっています。
サンプルコードは`share/Geant4/examples`にダウンロードされます。
具体的な使い方は「[](geant4-examples)」を参照してください。

## Qtしたい（`GEANT4_USE_QT`）

```console
$ brew install qt
$ cmake -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt)
```

`GEANT4_USE_QT`はQtを有効にするオプションです。
デフォルトは無効（`OFF`）になっています。
このオプションを有効にする場合、Qtをインストールして、`CMAKE_PREFIX_PATH`にQtのインストール先を指定する必要があります。

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
