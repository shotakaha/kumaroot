# ビルドする（``make`` / ``make install``）

```console
// ビルド用ディレクトリで作業する
$ cd $G4HOME/g4install/build/

// プロセッサの数を指定する
$ make -j8
# ビルドがはじまる
# 実行したマシンのスペックによるが、30分以上かかると思う

// インストールする
$ make install
Install the project...
-- Install configuration: "Release"
-- Installing: /usr/local/share/Geant4/data/...省略...
-- Installing: /usr/local/lib/libG4*.dylib
-- Installing: /usr/local/include/Geant4/...省略...
-- Installing: /usr/local/bin/geant4.sh
-- Installing: /usr/local/bin/geant4.csh
-- Installing: /usr/local/bin/geant4-config
-- Installing: /usr/local/share/Geant4/examples/...省略...
```

ビルド用ディレクトリで``make``コマンドを実行します。
複数のプロセッサを持ったCPUを使っている場合は、``-j 利用するプロセッサー数``オプションを使いましょう。
並列処理により、ビルド時間を短縮できます。

``GEANT4_INSTALL_DATA=ON``にした場合は、Geant4用データのダウンロードがはじまるため、ネットワークに接続した状態で実行する必要があります。
（ネットワークに接続してない場合にどうなるかは未確認）

ビルドが終わったら``make install``コマンドを実行します。
``CMAKE_INSTALL_PREFIX``で指定したディレクトリにGeant4がインストール（コピー）されます。

:::{note}

デフォルトで``CMAKE_INSTALL_PREFIX=/usr/local/``になっています。
この場合は、管理者パスワードの入力が必要かもしれません。

:::

## アンインストールしたい

```console
// ビルド用ディレクトリで作業する
// インストール時に使ったMakefileが残っていることが前提
$ cd $G4HOME/g4install/build
$ make uninstall
```


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
    │   ├── install_manifest.txt
    │   ├── source
    │   └── source_package_extras.cmake
    ├── data
    │   ├── G4ABLA3.3
    │   ├── G4EMLOW8.5
    │   ├── G4ENSDFSTATE2.3
    │   ├── G4INCL1.2
    │   ├── G4NDL4.7
    │   ├── G4PARTICLEXS4.0
    │   ├── G4PII1.3
    │   ├── G4SAIDDATA2.0
    │   ├── PhotonEvaporation5.7
    │   ├── RadioactiveDecay5.6
    │   └── RealSurface2.2
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
        ├── bin
        ├── include
        ├── lib
        └── share

38 directories, 36 files
```

``install``と``data``のディレクトリにファイルが追加されました。
このようなディレクトリ構成になっていたら、インストール完了です。
アプリケーション開発のときはシェルに環境変数を設定すると使えるようになります。
