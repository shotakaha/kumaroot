# ビルド＆インストールしたい（`cmake --build` / `cmake --install`）

```console
$ cd ~/geant4/v11.X.Y/
$ cmake --build build --parallel
```

`cmake --build`でビルドを実行します。
`--parallel`オプションを指定すると、マルチスレッドでビルドできます。

```console
$ cmake --install build
```

`cmake --install`でインストールを実行します。

## ビルド＆インストールしたい（`make` / `make install`）

```console
$ cd ~/geant4/build
$ make -j8
$ make install
$ make uninstall
```

`make`コマンドで、従来どおりのビルドを実行できます。
`cmake`でビルド構成を指定した場合は、ビルド用ディレクトリに`Makefile`が生成されます。
`build`ディレクトリに移動して、`make`コマンドを実行します。
`-j`オプションを指定すると、マルチスレッドでビルドできます。


## ディレクトリ構成

```console
$ tree ~/geant4/ -L 2
geant4/
├── 11.2.1
│   ├── bin
│   ├── include
│   ├── lib
│   └── share
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
│   ├── install_manifest.txt
│   ├── source
│   └── source_package_extras.cmake
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
└── geant4-v11.2.1.zip

25 directories, 36 files

```

``~/geant4/11.2.1/``のディレクトリが追加されました。
この中にGeant4のデータを含むファイル一式が格納されています。
このディレクトリ構成になっていたら、インストール完了です。
