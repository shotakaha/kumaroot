# ビルドしたい（``cmake``）

```console
// プロジェクト内に移動する
$ cd $G4WORK/プロジェクト

// ビルド用ディレクトリを作成する
(プロジェクト) $ mkdir build
(プロジェクト)$ cd build

// ビルド準備する
(プ/build) $ cmake ..

// ビルドする
(プ/build) $ make -j8   # 必要ならば make install する
```

Geant4本体と同じようにアプリケーションも[CMake](https://cmake.org/)でビルド準備します。
自作アプリケーションも、付属サンプルのように``CMakeLists.txt``が必要です。

ここでも``cmake``の作法（out-of-source）にしたがい、ビルド用ディレクトリで作業します。
ディレクトリ名は任意ですが、分かりやすく``build``としました。
ビルド作業はすべてこのディレクトリで行います。

まずはじめに``CMakeLists.txt``から、``Makefile``などビルドに必要なファイルを生成します。
ビルド用ディレクトリに対して``CMakeLists.txt``は親ディレクトリにあるので``cmake ..``を実行しています。

そして``Makefile``から実行ファイルを生成します。
``Makefile``はビルド用ディレクトリの中にあるので``make -j8``を実行しています。
プロセッサ数のオプション（``-jN``）は指定した方がよいです。

実行ファイルは現在のディレクトリ（``build``）に生成されます。
プロジェクトの中でアプリケーションを実行するのがよいと思うので、ここで完了です。
もし、システム全体で使いたい場合は``make install``します。

```console
// アプリケーションを実行
$ ./実行ファイル名    # 対話モード
$ ./実行ファイル名 マクロ.mac    # バッチモード
```

アプリケーションの実行方法は「対話モード」と「バッチモード」の2種類あります。
引数なしで実行すると対話モード、
引数にマクロファイル（``.mac``）を指定するとバッチモードになります。

マクロは、対話モードで使用するコマンドをまとめたようなファイルです。
対話モードで起動するときも、同じディレクトリにある
``init_vis.mac``と``vis.mac``が読み込まれるようです。

## CMakeLists.txtしたい

``exampleB1``のCMakeLists.txtをサンプルに、
何をしているのか分割しながら確認します。

```cmake
#----------------------------------------------------------------------------
# Setup the project
cmake_minimum_required(VERSION 3.16...3.21)
project(B1)
```

プロジェクト全体の設定です。
``cmake_minimum_required``でCMakeのバージョンを指定しています。

:::{note}

``CMake 3.29.6`` を使ってビルドしましたが、エラーはでませんでした。
上限値の制限はゆるいみたいです。

:::

```cmake
#----------------------------------------------------------------------------
# Find Geant4 package, activating all available UI and Vis drivers by default
# You can set WITH_GEANT4_UIVIS to OFF via the command line or ccmake/cmake-gui
# to build a batch mode only executable
#
option(WITH_GEANT4_UIVIS "Build example with Geant4 UI and Vis drivers" ON)
if(WITH_GEANT4_UIVIS)
  find_package(Geant4 REQUIRED ui_all vis_all)
else()
  find_package(Geant4 REQUIRED)
endif()
```

``find_package``コマンドで、Geant4の設定を取得しています。
``WITH_GEANT4_UIVIS``オプションは可視化オプションです。
デフォルトは``ON``になっていて、すべての可視化オプション（``ui_all`` / ``vis_all``）が有効になります。
``OFF``にすると無効にできます。

```cmake
#----------------------------------------------------------------------------
# Setup Geant4 include directories and compile definitions
# Setup include directory for this project
#
include(${Geant4_USE_FILE})
include_directories(${PROJECT_SOURCE_DIR}/include)
```

Geant4アプリのビルドに必要なディレクトリを設定しています。
``Geant4_USE_FILE``は``find_package(Geant4)``したときに設定されます。
他にも設定される変数がありますが、``$HOME/geant4/11.2.1/lib/cmake/Geant4/Geant4Config.cmake``の頭にあるコメントと、中の処理を直接確認するのがよいと思います。

```cmake
#----------------------------------------------------------------------------
# Locate sources and headers for this project
# NB: headers are included so they will show up in IDEs
#
file(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.cc)
file(GLOB headers ${PROJECT_SOURCE_DIR}/include/*.hh)
```

Geant4アプリのビルドに必要なファイルを取得しています。
``${sources}``にソースファイルの一覧、
``${headers}``にヘッダーファイルの一覧、
を代入しています。

```cmake
#----------------------------------------------------------------------------
# Add the executable, and link it to the Geant4 libraries
#
add_executable(exampleB1 exampleB1.cc ${sources} ${headers})
target_link_libraries(exampleB1 ${Geant4_LIBRARIES})
```

実行ファイルを作るときの設定です。
``add_executable``で、実行ファイルの作成に必要なファイルを指定しています。
``target_link_libraries``でビルド時にリンクさせるライブラリを指定しています。

Geant4以外の外部ライブラリを使う場合は、ここに設定を追加すればOKです。

```cmake
#----------------------------------------------------------------------------
# Copy all scripts to the build directory, i.e. the directory in which we
# build B1. This is so that we can run the executable directly because it
# relies on these scripts being in the current working directory.
#
set(EXAMPLEB1_SCRIPTS
  exampleB1.in
  exampleB1.out
  init_vis.mac
  run1.mac
  run2.mac
  vis.mac
  tsg_offscreen.mac
  )

foreach(_script ${EXAMPLEB1_SCRIPTS})
  configure_file(
    ${PROJECT_SOURCE_DIR}/${_script}
    ${PROJECT_BINARY_DIR}/${_script}
    COPYONLY
    )
endforeach()
```

これはGeant4のexamples固有の設定です。
アプリの実行に必要なファイルをコピーしています。

:::{note}

ファイルが存在しない場合は、エラーになります。
汎用的な設定ではないと思うので、自分のアプリに不要な場合は、
この部分は真似しなくてもよいと思います。

:::

```cmake
#----------------------------------------------------------------------------
# For internal Geant4 use - but has no effect if you build this
# example standalone
#
add_custom_target(B1 DEPENDS exampleB1)
```

（ここはわかってない）

```cmake
#----------------------------------------------------------------------------
# Install the executable to 'bin' directory under CMAKE_INSTALL_PREFIX
#
install(TARGETS exampleB1 DESTINATION bin)
```

実行ファイルのインストール先の設定です。
``プロジェクト/bin/exampleB1``にインストールされます。
