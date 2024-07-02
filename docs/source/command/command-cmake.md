# cmakeしたい

```console
$ brew install --cask cmake
$ brew install cmake-docs

$ cmake --version
cmake version 3.29.6

$ ccmake --version
ccmake version 3.29.6
```

CMakeはクロスプラットフォーム対応したビルドツールです。
``cmake``で使っているプラットフォームに対応したMakefileを生成できます。
設定ファイルは``CMakeLists.txt``に記述します。

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
