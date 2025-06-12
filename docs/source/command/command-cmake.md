# cmakeしたい

```console
$ brew install --cask cmake
$ brew install cmake-docs

$ cmake --version
cmake version 3.29.6

$ ccmake --version
ccmake version 3.29.6
```

CMakeは、C++やCなどのプログラムを **ビルドするための設定を自動化** するファイルです。
必要な設定は`CMakeLists.txt`に記述します。

クロスプラットフォーム対応しており、
`Makefile`などのビルド用ファイルを、プラットフォームに対応した形式で生成できます。

## ビルドしたい

```console
// ビルド用ディレクトリを作成
$ mkdir build
$ cd build

// cmakeを実行
$ cmake ..

// makeを実行
$ make
```

`cmake`ではビルド用ディレクトリを作成することが **推奨** されています。
ビルド用ディレクトリを使うことで、ソースディレクトリを汚さずにすみます。
また、`rm -rf build/`でビルド環境を完全に削除できます。

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

### デバッグ用ビルドしたい

デバッグ用、リリース用にそれぞれビルド用ディレクトリを作成することで、
2つのビルド結果を同時に持つことができます。

```console
$ mkdir build-debug
$ cd build-debug
$ cmake -DCMAKE_BUILD_TYPE=Debug ..
$ make
```

### リリース用ビルドしたい

```console
$ mkdir build-release
$ cd build-release
$ cmake -DCMAKE_BUILD_TYPE=Release ..
$ make
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

## CMakeListsの設定

### 基本設定

```cmake
cmake_minimum_required(VERSION 3.16...3.27)
project(プロジェクト名)

add_executable(名前 名前.cc ${sources} ${headers})
target_link_libraries(名前 ライブラリ)
```

### CMakeのバージョンしたい

```cmake
cmake_minimum_required(VERSION 最小値)
cmake_minimum_required(VERSION 最小値...最大値)
```

[cmake_minimum_required](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html)コマンドで、CMakeのバージョンの最小値／最大値を指定できます。

### 変数したい

```cmake
set(変数名 値)
```

[set](https://cmake.org/cmake/help/latest/command/set.html)コマンドで変数を定義できます。

### デバッグしたい

```cmake
message(ログレベル "メッセージ")
message(STATUS "G4LIB=${G4LIB}")
```

[message](https://cmake.org/cmake/help/latest/command/message.html)コマンドを使ってログを出力できます。
ログレベルは``STATUS``のほかに、``DEBUG``、``NOTICE``、``WARNING``、``FATAL_ERROR``などがあります。
``${変数名}``で、CMake内で定義した変数の値を参照できます。

### ライブラリを使いたい（``find_package``）

```cmake
find_package(パッケージ名 REQUIRED)
```

[find_package](https://cmake.org/cmake/help/latest/command/find_package.html)コマンドで、インストール済みのライブラリ情報を取得できます。

:::{note}

ライブラリをどのように作成するかは調べていません。

:::

### 外部リポジトリを使いたい（``FetchContent``）

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

## VS Code したい

次の2つの拡張をVS Codeに追加してください。

- [C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [CMake Tools extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
