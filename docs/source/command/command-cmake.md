# コンパイルしたい（`cmake`）

```console
$ cmake [options] <path-to-source>
$ cmake [options] -S <path-to-source> -B <path-to-build>
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

## ビルドしたい

```console
// ビルド用ディレクトリを作成
$ mkdir build
$ cd build

// cmakeを実行（CMakeLists.txtがあるディレクトリを指定）
$ cmake [オプション] ..
$ cmake --build ..
$ cmake --install ..  # CMAKE_INSTALL_PREFIXにインストール
```

`cmake`では「**out-of-source build**」が **推奨** されており、
ビルド用ディレクトリを作成する必要があります。
ソースコードとビルド環境を分離することで、
ソースディレクトリ（やリポジトリ）を汚さずにすみます。
また、`rm -rf build/`でビルド環境を完全に削除できます。

```console
$ cmake [オプション] -S ./source -B ./build
$ cmake --build ./build
$ cmake --install ./build  # CMAKE_INSTALL_PREFIXにインストール
```

ソースとビルド同じ階層にする場合は`-S`と`-B`オプションを使用します。

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

## オプション設定したい（`CMakePresets.json`）

```console
$ cmake --preset=プリセット名 ..
```

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

`CMakePresets.json`に
ジェネレーターやオプションの設定を保存できます。
`cmake`時に`--preset`オプションでプリセット名を指定します。

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
