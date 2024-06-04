# ビルドする（``make`` / ``make install``）

```console
// ビルド用ディレクトリで作業する
$ cd ~/geant4/build

// プロセッサの数を指定する
(~/geant4/build/) $ make -j8
# ビルドがはじまる
# 実行したマシンのスペックによるが、30分以上かかると思う
```

ビルド用ディレクトリで``make``コマンドを実行します。
複数のプロセッサを持ったCPUを使っている場合は、``-j 利用するプロセッサー数``オプションを使うことで、
並列処理により、ビルド時間を短縮できます。

``GEANT4_INSTALL_DATA=ON``にした場合は、Geant4用データのダウンロードがはじまるため、
ネットワークに接続した状態で実行する必要があります。

```console
// インストールする
(~/geant4/build/) $ make install
Install the project...
-- Install configuration: "Release"
-- Installing: ~/geant4/11.2.1/share/Geant4/data/...省略...
-- Installing: ~/geant4/11.2.1/lib/libG4*.dylib
-- Installing: ~/geant4/11.2.1/include/Geant4/...省略...
-- Installing: ~/geant4/11.2.1/bin/geant4.sh
-- Installing: ~/geant4/11.2.1/bin/geant4.csh
-- Installing: ~/geant4/11.2.1/bin/geant4-config
-- Installing: ~/geant4/11.2.1/share/Geant4/examples/...省略...
```

ビルドできたら``make install``コマンドを実行します。
``CMAKE_INSTALL_PREFIX``で指定したディレクトリにGeant4がインストール（コピー）されます。

## アンインストールしたい

```console
// ビルド用ディレクトリで作業する
// インストール時に使ったMakefileが残っていることが前提
$ cd ~/geant4/build/
(~/geant4/build/) $ make uninstall
```

ビルド時に使った``Makefile``が残っていれば、``make uninstall``でアンインストールできます。
``Makefile``が残っていない場合は、``CMAKE_INSTALL_PREFIX``で指定したディレクトリを削除します。

:::{note}

デフォルトで``CMAKE_INSTALL_PREFIX=/usr/local/``になっていますが、
これだと削除しにくいため、必ず設定することをオススメします。

``/usr/local/``にインストールした場合は、もう一度Makefileを作れば、アンストールできると思います（未確認）。

:::

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
