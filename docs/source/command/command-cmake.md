# cmakeしたい

```console
$ brew install --cask cmake

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

### ライブラリを使いたい（``find_package``）

```cmake
find_package(パッケージ名 REQUIRED)
```

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

``FetchContent``モジュールで、外部リポジトリを取得できます。
取得したファイルは``build/_deps/``にキャッシュされます。

## VS Code したい

次の2つの拡張をVS Codeに追加してください。

- [C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [CMake Tools extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
