# ビルドの準備する（``cmake``）

```console
// ビルド用ディレクトリで作業する
$ cd $G4HOME/g4install/build

// オプションを指定してcmakeする
$ cmake \
-DMAKE_INSTALL_PREFIX=$G4HOME/g4install/install \
-DGEANT4_INSTALL_DATA=ON \
-DGEANT4_INSTALL_DATADIR=$G4HOME/g4install/data \
-DGEANT4_USE_OPENGL_X11=ON \
-DGEANT4_USE_RAYTRACER_X11=ON \
-DGEANT4_USE_QT=ON \
-DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) \
../../geant4-v11.2.1/
```

前ページのように``ccmake``を使うと視覚的にオプションを設定できました。
しかし、設定項目に表示されないオプションがあったりして、痒いところに手が届かない面もあります。
そのようなときは、``cmake``コマンドをオプション付きで実行します。

:::{note}

[前のページのccmake](./geant4-install-ccmake.md)で設定できた場合、このページの内容はスキップしてOKです。

:::



## ディレクトリ構成

```console
$ tree g4home -L 3
g4home
└── g4install
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
    ├── data
    ├── geant4-v11.2.1
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
    ├── geant4-v11.2.1.zip
    └── install

23 directories, 35 files
```

``build``の中にファイルが生成されました。
このようなディレクトリ構成になっていたら、次に進んでください。
（ディレクトリ構成は前ページと同じです）


