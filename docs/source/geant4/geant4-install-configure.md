# ビルド構成したい（`cmake`）

```console
$ cd ~/geant4/v11.X.Y/
// 1行でまとめて指定する
$ cmake -G Ninja -S source -B build -DCMAKE_INSTALL_PREFIX=install -DCMAKE_PREFIX_PATH=$(brew --prefix qt) -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON
```

同じ内容を、ステップに分けて指定することもできます。
ビルドディレクトリのキャッシュ（`CMakeCache.txt`）に値が追記されます。
そのため、結果は1行で指定した場合と同じです。

```console
// ステップ1：ビルドシステムとソース／ビルドディレクトリを指定する
$ cmake -G Ninja -S source -B build

// ステップ2：インストール先を指定する
$ cmake -S source -B build -DCMAKE_INSTALL_PREFIX=install

// ステップ3：Qt・OpenGL・データセットを指定する
$ cmake -S source -B build -DCMAKE_PREFIX_PATH=$(brew --prefix qt) -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON
```

:::{note}

ステップ2以降も`-S source`を付けてください。
付けないと、カレントディレクトリがソースとして扱われます。
その場合、`CMakeLists.txt`が見つからずに失敗します。

:::

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
どちらも同じソースを、同じオプションでビルドした場合の結果（バイナリなど）は同じになります。
一般に`Ninja`のほうが`Make`より高速にビルドできるらしいです。

## 分割ビルドしたい（`cmake -S -B`）

```console
$ cmake -S source -B build
```

`-S / --source`オプションでソースコードのディレクトリを指定します。
`-B / --build`オプションでビルド用のディレクトリを指定できます。
`cmake`では、ソースコードとビルド用のディレクトリを分けて管理することが推奨されています。

## ビルドオプションしたい（`cmake -D`）

```console
$ cmake -S source -B build -DCMAKE_INSTALL_PREFIX=install -DCMAKE_PREFIX_PATH=$(brew --prefix qt) -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_QT=ON
```

`-D / --define`オプションでビルドオプションを指定できます。
`-Dオプション名=値`の形式で記述します。

`-DCMAKE_INSTALL_PREFIX`はインストール先のディレクトリ（`CMAKE_INSTALL_PREFIX`）を指定するオプションです。
作業ディレクトリ（`~/geant4/v11.X.Y/`）の中に`install`ディレクトリを作成します。
そして、そこにインストールするようにしています。

`-DCMAKE_PREFIX_PATH`は依存ライブラリの検索パス（`CMAKE_PREFIX_PATH`）を指定します。
Qtを使う場合は、`brew --prefix qt`でQtのインストール先を取得します。
そのパスを`CMAKE_PREFIX_PATH`に指定する必要があります。

`-DGEANT4_INSTALL_DATA=ON`はGeant4のデータをインストールするオプション（`GEANT4_INSTALL_DATA`）を有効にしています。
`-DGEANT4_USE_OPENGL_X11=ON`はOpenGLを使うオプション（`GEANT4_USE_OPENGL_X11`）を有効にしています。
`-DGEANT4_USE_QT=ON`はQtを使うオプション（`GEANT4_USE_QT`）を有効にしています。

:::{seealso}

- [](geant4-install-configure-options)

:::


## プリセットしたい（`CMakePresets.json`）

```console
$ cmake -S source -B build --preset=geant4
```

`CMakePresets.json`にビルドオプションをまとめることで、オプション設定を再利用できます。
ファイルとして残すことで、ビルドオプションの設定を他の人と共有することもできます。
また、オプション設定時のタイポを防ぐことができます。

```json
{
    "version": 3,
    "configurePresets": [
        {
            "name": "geant4",
            "displayName": "Geant4 Build",
            "description": "Build Geant4 with OpenGL and Qt",
            "generator": "Ninja",
            "binaryDir": "${sourceDir}/../build",
            "cacheVariables": {
                "CMAKE_BUILD_TYPE": "Release",
                "CMAKE_INSTALL_PREFIX": "${sourceDir}/../install",
                "GEANT4_INSTALL_DATA": "ON",
                "GEANT4_USE_OPENGL_X11": "ON",
                "GEANT4_USE_QT": "ON"
            }
        }
    ]
}
```

## ディレクトリ構成

```console
$ tree ~/geant4/v11.X.Y -L 2
geant4/v11.X.Y
├── build
│   ├── BuildProducts
│   ├── CMakeCPackOptions.cmake
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   ├── CPackConfig.cmake
│   ├── CPackSourceConfig.cmake
│   ├── Externals
│   ├── G4EXPATShim.cmake
│   ├── G4FreetypeShim.cmake
│   ├── G4HDF5Shim.cmake
│   ├── G4ModuleAdjacencyList.txt
│   ├── G4ModuleInterfaceMap.csv
│   ├── G4MotifShim.cmake
│   ├── G4X11Shim.cmake
│   ├── Geant4Config.cmake
│   ├── Geant4ConfigVersion.cmake
│   ├── Geant4LibraryDepends.cmake
│   ├── Geant4PackageCache.cmake
│   ├── InstallTreeFiles
│   ├── LICENSE.txt
│   ├── Makefile
│   ├── Modules
│   ├── README.txt
│   ├── UseGeant4.cmake
│   ├── UseGeant4_internal.cmake
│   ├── _source_extras
│   ├── cmake_install.cmake
│   ├── cmake_uninstall.cmake
│   ├── cmake_uninstall.cmake.in
│   ├── cxx_filesystem
│   ├── data
│   ├── geant4-config
│   ├── geant4_module_check.py
│   ├── geant4_validate_sources.cmake
│   ├── geant4make.csh
│   ├── geant4make.sh
│   ├── source
│   └── source_package_extras.cmake
├── source
│   ├── CHANGELOG -> ReleaseNotes
│   ├── CITATION.cff
│   ├── CMakeLists.txt
│   ├── CONTRIBUTING.rst
│   ├── LICENSE
│   ├── README.rst
│   ├── ReleaseNotes
│   ├── cmake
│   ├── config
│   ├── environments
│   ├── examples
│   ├── packaging
│   └── source
```

`source/CMakeLists.txt`の内容をもとに、`build/CMakeCache.txt`が生成されました。
このようなディレクトリ構成になっていたら、次に進んでください。
