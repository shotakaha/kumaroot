# コンパイルしたい（`cmake`）

```console
$ cmake [options] <path-to-source>
$ cmake [options] -S <path-to-source> -B <path-to-build>
$ cmake --build <path-to-build> --parallel
$ cmake --install <path-to-build>
```

CMakeは、C++やCなどのプログラムを **ビルドするための設定を自動化** するツールです。
`CMakeLists.txt`に記述されたビルド情報を元に、
`make`や`ninja`などのビルドツールに応じた設定ファイル（`Makefile`や`ninja.build`）を
自動で生成してくれます。

また、クロスプラットフォーム対応しているため、
Linux、macOS、Windowsなどさまざまな環境で利用できます。

:::{note}

これまでのビルド＆インストールで
`./configure`していた部分で
`cmake`します。

```console
./configure
make
make install
```

:::

## インストールしたい

```console
$ brew install cmake
$ brew install cmake-docs

$ cmake --version
cmake version 3.29.6

$ ccmake --version
ccmake version 3.29.6
```

CMakeはHomebrewでインストールできます。
オフラインでドキュメントを確認したい場合は、
`cmake-docs`も追加します。

## ビルド構成したい

```console
$ mkdir <path-to-build>
$ cd <path-to-build>
$ cmake ..
```

`cmake`では「**out-of-source build**」が **推奨** されています。
ソースコードとビルド環境を分離することで、
ソースディレクトリ（やリポジトリ）を汚さずにすみます。
また、ビルド環境を完全に削除しやすくなります。

通常は`build`のようなビルド用ディレクトリを作成して`cmake ..`で
ビルド構成ファイルを生成（=configure）します。
必要なファイルはすべて`build`ディレクトリの中に生成されます。

```console
$ cmake -S source -B build
```

`-S`と`-B`オプションを使って、ビルド対象を明示できます。
ビルド作業をスクリプト化する場合には、
これらのオプションを使った方が可読性があがります。

## ビルドしたい（`--build`）

```console
$ cmake --build <path-to-build>
```

`cmake --build`で、ビルド構成ファイルにしたがってビルドします。

```console
$ cmake --build <path-to-build> --parallel <n>
```

`--parallel`オプションで並列ビルドできます。
数値を指定して並列ジョブ数を変更できます。

## インストールしたい（`--install`）

```console
$ cmake --install <path-to-build>
```

`cmake --install`でシステムにインストールできます。
インストール先は`CMAKE_INSTALL_PREFIX`です。

```console
$ cmake --install <path-to-build> --prefix <path-to-install-binary>
```

`--prefix`オプションで、インストール先を一時的に変更できます。

:::{note}

```console
$ cmake -DCMAKE_INSTALL_PREFIX=path-to-install -S source -B build
```

インストール先は、ビルド構成時のオプションで設定します。
デフォルトは`/usr/local/`です。

:::

## オプション設定したい（`-Dオプション名`）

```console
$ cmake -Dオプション名 -S source -B build

// インストール先を変更
$ cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local/bin -S source -B build
```

`-Dオプション名=値`でビルドオオプショを変更できます。
オプションは、CMakeの組み込みオプションもあれば、
ユーザー定義されたオプションもあります。

## 複数オプションしたい（`--preset` / `CMakePresets.json`）

```console
$ cmake --preset=プリセット名 -S source -B build
```

複数のオプションを設定する場合は、`CMakePresets.json`を作成し、
`--preset`オプションでプリセット名を指定するとよいです。

```json
{
    "name": "プリセット名",
    "displayName": "表示名",
    "description": "ビルド内容の説明",
    "generator": "Ninja",
    "binaryDir": "${sourceDir}/build",
    "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug",
        "CMAKE_INSTALL_PREFIX": "${sourceDir}/install",
        "...": "..."
    }
}
```

`Release`用と`Debug`用のように、
ビルドタイプごとにプリセットを作成しておくのも便利です。

## ビルドタイプしたい（`-DCMAKE_BUILD_TYPE`）

```console
$ cmake -DCMAKE_BUILD_TYPE=Debug ..
$ cmake -DCMAKE_BUILD_TYPE=Release ..
$ cmake -DCMAKE_BUILD_TYPE=MinSizeRel ..
$ cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
```

`CMAKE_BUILD_TYPE`オプションで、ビルドタイプを変更できます。
ビルドタイプの値は次の4種類があります。

1. `Debug`: 最適化なし、デバッグ情報あり
2. `Release`: 最適化あり、デバッグ情報なし
3. `RelWithDebugInfo`: 最適化あり、デバッグ情報あり
4. `MinSizeRel`: 最適化あり（サイズ最小化に特化）

:::{note}

カスタムなビルドタイプを使用可能ですが、一般的ではないようです。
特別な理由がなければ、標準的な値を使い分けるのがベストです。

:::

```console
$ cmake -DCMAKE_BUILD_TYPE=Debug -S ./source -B ./build-debug
$ cmake --build ./build
```

```console
$ cmake -DCMAKE_BUILD_TYPE=Release -S ./source -B./build-release
$ cmake --build ./build
```

## ジェネレーターしたい（`-G`）

```console
$ cmake -G "Unix Makefiles"
$ cmake -G "Ninja"
$ cmake -G "Xcode"
```

`-G`オプションで、ビルドツールを変更できます。
設定できる値には次のような値があります。

1. `Unix Makefiles`: 標準的なMakefileを生成
2. `Ninja`: `build.ninja`を生成
3. `Ninja Multi-Config`: `build-<Config>.ninja`を生成
4. `Xcode`: Xcodeプロジェクトファイルを生成

:::{note}

ジェネレーターを変更しても、生成されるビルド結果は同じです。

:::

```console
$ cmake -G "Unix Makefiles" -Dオプション -S ./source -B ./build
$ cmake --build ./build
```

```console
$ cmake -G "Ninja" -Dオプション -S ./source -B ./build
$ cmake --build ./build
```



## ビルドの設定（`CMakeLists.txt`）

```cmake
cmake_minimum_required(VERSION 3.16...3.27)
project(プロジェクト名)

add_executable(名前 名前.cc ${sources} ${headers})
target_link_libraries(名前 ライブラリ)
```

ビルドの設定は`CMakeLists.txt`に記述します。
このファイルは、`CMake言語`（もしくはCMake構文）で記述します。

## 変数したい（`set`）

```cmake
set(変数名 値)
```

[set](https://cmake.org/cmake/help/latest/command/set.html)コマンドで変数を定義できます。

## メッセージしたい（`message`）

```cmake
message(ログレベル "メッセージ")
message(STATUS "G4LIB=${G4LIB}")
```

[message](https://cmake.org/cmake/help/latest/command/message.html)コマンドを使ってログを出力できます。
ログレベルは``STATUS``のほかに、``DEBUG``、``NOTICE``、``WARNING``、``FATAL_ERROR``などがあります。
``${変数名}``で、CMake内で定義した変数の値を参照できます。

## CMakeのバージョンしたい（`cmake_minimum_required`）

```cmake
cmake_minimum_required(VERSION 最小値)
cmake_minimum_required(VERSION 最小値...最大値)
```

[cmake_minimum_required](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html)コマンドで、CMakeのバージョンの最小値／最大値を指定できます。

## プロジェクト名したい（`project`）

```cmake
project(プロジェクト名)
```

```cmake
project(プロジェクト名
  VERSION 11.2.1
  DESCRIPTION "プロジェクトの説明"
  HOMEPAGE_URL "https://example.com"
)

message("Project Name: ${PROJECT_NAME}")
message("Version: ${PROJECT_VERSION}")
message("  Major: ${PROJECT_VERSION_MAJOR}")
message("  Minor: ${PROJECT_VERSION_MINOR}")
message("  Patch: ${PROJECT_VERSION_PATCH}")
message("Description: ${PROJECT_DESCRIPTION}")
message("Homepage URL: ${PROJECT_HOMEPAGE_URL}")
```

## ライブラリを使いたい（`find_package`）

```cmake
find_package(パッケージ名 REQUIRED)
```

[find_package](https://cmake.org/cmake/help/latest/command/find_package.html)コマンドで、インストール済みのライブラリ情報を取得できます。

:::{note}

ライブラリをどのように作成するかは調べていません。

:::

## 外部リポジトリを使いたい（`FetchContent`）

```cmake
include(FetchContent)
FetchContent_Declare(
    名前
    GIT_REPOSITORY "URL"
    GIT_TAG "タグ名"
)
FetchContent_MakeAvailable(名前)
```

[FetchContent](https://cmake.org/cmake/help/latest/module/FetchContent.html)モジュールで、外部リポジトリにあるライブラリを取得できます。
取得したファイルは``build/_deps/``にキャッシュされます。

具体的な使い方は、CMakeに対応したライブラリのREADMEなどに書いてあると思うので、個別に確認してください。

## ビルド用ディレクトリを強制したい

```cmake
if(${CMAKE_CURRENT_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_BINARY_DIR})
  message(STATUS "This package requires an out-of-source build.")
  message(STATUS "Please remove these files from ${CMAKE_CURRENT_BINARY_DIR} first:")
  message(STATUS "CMakeCache.txt")
  message(STATUS "CMakeFiles")
  message(STATUS "Once these files are removed, create a separate directory")
  message(STATUS "and run CMake from there")
  message(FATAL_ERROR "in-source build detected")
endif()
```

Out-of-source build を強制するための設定です。
`CMakeLists.txt`の冒頭に記述しておくとよいです。

## 組み込み変数したい

```cmake
get_cmake_property(_vars VARIABLES)
foreach(v ${_vars})
  message(STATUS "${v} = ${${v}}")
endforeach()
```

組み込み関数の`get_cmake_property`を使って、
プロジェクト内のすべての変数（`VARIABLES`）を出力できます。

`VARIABLES`の他に、
`CACHE_VARIABLES`、
`COMMANDS`、
`MODULES`のプロパティ名を指定できます。

### プロジェクト情報したい

- `PROJECT_NAME`: `project()`で定義したプロジェクト名
- `PROJECT_SOURCE_DIR`: プロジェクトのルートソースディレクトリ
- `PROJECT_BINARY_DIR`: プロジェクトのルートビルドディレクトリ
- `CMAKE_PROJECT_NAME`: 最初に読み込まれたプロジェクトの名前
- `CMAKE_SOURCE_DIR`: 最上位の`CMakeLists.txt`があるディレクトリ
- `CMAKE_BINARY_DIR`: 最上位のビルドディレクトリ

### バージョン情報したい

- `PROJECT_VERSION`: `project()`で定義したバージョン番号
- `PROJECT_VERSION_MAJOR`: メジャーバージョン
- `PROJECT_VERSION_MINOR`: マイナーバージョン
- `PROJECT_VERSION_PATCH`: パッチバージョン

### CMake実行環境したい

- `CMAKE_VERSION`: 実行中のCMakeのバージョン
- `CMAKE_COMMAND`: `cmake`コマンドのパス
- `CMAKE_ROOT`: CMakeのモジュールファイルがあるディレクトリ

### パスを確認したい

- `CMAKE_CURRENT_SOURCE_DIR`: 現在処理している`CMakeLists.txt`のあるディレクトリ
- `CMAKE_CURRENT_BINARY_DIR`: 現在のビルド出力ディレクトリ
- `CMAKE_CURRENT_LIST_FILE`: 現在処理中のファイル名
- `CMAKE_CURRENT_LIST_DIR`: 現在処理中のファイルがあるディレクトリ名

### ビルド環境を確認したい

- `CMAKE_BUILD_TYPE`: ビルドタイプの種類
- `CMAKE_INSTALL_PREFIX`: インストール先のパス
- `CMAKE_RUNTIME_OUTPUT_DIRECTORY`: 実行ファイルの出力先
- `CMAKE_LIBRARY_OUTPUT_DIRECTORY`: ライブラリの出力先
- `CMAKE_SYSTEM_NAME`: ターゲットOSの名前
- `CMAKE_HOST_SYSTEM_NAME`: ビルドを実行するマシンのOS名
- `CMAKE_GENERATOR`: ビルドシステムの種類
- `CMAKE_CACHEFILE_DIR`: `CMakeCache.txt`のディレクトリ名

### コンパイラを確認したい

- `CMAKE_C_COMPILER`: 使用するCコンパイラのパス
- `CMAKE_C_FLAGS`: Cコンパイル時のフラグ
- `CMAKE_CXX_COMPILER`: 使用するC++コンパイラのパス
- `CMAKE_CXX_FLAGS`: C++コンパイル時のフラグ


## VS Code したい

次の2つの拡張をVS Codeに追加してください。

- [C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [CMake Tools extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
