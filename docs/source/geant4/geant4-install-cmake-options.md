# ビルドオプションを確認する

| オプション名 | デフォルト値 | 推奨値 | 説明 |
|---|---|---|---|
| CMAKE_INSTALL_PREFIX |  ``/usr/local/`` | ``$HOME/geant4/``| Geant4をインストールするパス |
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

[Geant4 Build Options](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#geant4buildo)を参考に、
使いそうなオプションや、知っておくとよさそうなオプション設定のデフォルト値を整理しました。

:::{note}

可視化ツールにQt5を使う場合、Qt5がインストールされているパスを``CMAKE_PREFIX_PATH``で指定する必要があります。
該当するパスを直接指定してもよいのですが、``brew --prefix パッケージ名``コマンドを使うことで、
パソコンのシステム構成に依存しにくいように汎用化しています。

```console
// macOS (x86_64)
$ brew --prefix qt@5
/usr/local/qt@5

// macOS (M2 Apple)
$ brew --prefix qt@5
/opt/homebrew/opt/qt@5
```

:::
