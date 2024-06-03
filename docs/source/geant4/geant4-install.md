# インストールしたい（``geant4``）

```console
// 外部ツールを準備する
$ brew install --cask cmake
$ brew install --cask xquartz
$ brew install qt@5

// Geant4用ディレクトリを作成する
$ mkdir ~/repos/g4home

// ソースコードをダウンロードする
$ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.2.1/geant4-v11.2.1.zip
$ unzip geant4-v11.2.1.zip

// インストール先のディレクトリを作成する
$ mkdir 11.2.1  # Geant4のバージョンにした

// cmakeでビルド作業するディレクトリを作成する
$ mkdir build

// 現在のディレクトリ構成を確認する
$ ls ls
ls -1
11.2.1/
build/
geant4-v11.2.1/
geant4-v11.2.1.zip

// cmakeでビルドする
$ cd build
$ export G4HOME=~/repos/g4home
$ cmake -DMAKE_INSTALL_PREFIX=$G4HOME/g4install/install -DGEANT4_INSTALL_DATA=ON -DGEANT4_INSTALL_DATADIR=$G4HOME/g4install/data -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) ../geant4-v11.2.1/
$ ls
ビルドに必要なファイルが作成されていることを確認

// ビルドする
$ make -j8
$ make install

// ディレクトリ構成を確認
$ tree ~/repos/g4home -L 3
```

Geant4は自分でビルドしてインストールする必要があります。
インストール手順にはいくつかステップがあるので、それぞれを分割して整理しました。
各ステップを確認しながら順番に作業してください。

```{toctree}
---
maxdepth: 1
---
geant4-install-brew
geant4-install-mkdir
geant4-install-download
geant4-install-cmake-options
geant4-install-ccmake
geant4-install-cmake
geant4-install-make
```

## 環境変数を設定する

```console
// CMAKE_INSTALL_PREFIX は設定したパスに変更
$ source $CMAKE_INSTALL_PREFIX/bin/geant4.sh

// 上記の設定でインストールした場合
$ source ~/repos/g4home/g4install/install/bin/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（``$CMAKE_INSTALL_PREFIX/bin/``）の中に、設定スクリプト（``geant4.sh``）が用意されています。
これを読み込んでからアプリケーションをコンパイルしてください。

いつも使うような場合は、シェルの起動スクリプトに書いておくとよいです。

:::{caution}

残念ながらFish用の設定スクリプトはありません。

僕は、以下のようにGeant4を使う時だけZshに切り替えて作業することにしました。

```console
(fish) $ zsh
(zsh) $ source ~/repos/g4home/g4install/install/bin/geant4.sh
(zsh) $ cd ~/repos/sandbox/g4work/examples/basic/B1/
(zsh) $ mkdir build
(zsh) $ cd build
(zsh) $ cmake ..
(zsh) $ make
(zsh) $ ./exampleB1
```

一度ビルドしたアプリケーションはFishでも起動できました。

:::

## リビルドする

``Xcode``や``CMake``を更新すると、アプリケーションがビルドできなくなります。
そのときは、Geant4のリビルド＆インストールが必要です。

参考までに、CMakeを更新（3.29.2 -> 3.29.3）したあとで遭遇したコンパイルエラーをメモしておきます。

```console
$ cd examples/basic/B1/
$ cd build
$ cmake ..
CMake Warning at /Applications/CMake.app/Contents/share/cmake-3.29/Modules/Platform/Darwin-Initialize.cmake:308 (message):
  Ignoring CMAKE_OSX_SYSROOT value:

   /Library/Developer/CommandLineTools/SDKs/MacOSX14.2.sdk

  because the directory does not exist.
Call Stack (most recent call first):
  /Applications/CMake.app/Contents/share/cmake-3.29/Modules/CMakeSystemSpecificInitialize.cmake:34 (include)
  CMakeLists.txt:4 (project)

-- The C compiler identification is AppleClang 15.0.0.15000309
-- The CXX compiler identification is AppleClang 15.0.0.15000309
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - failed
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc - broken
CMake Error at /Applications/CMake.app/Contents/share/cmake-3.29/Modules/CMakeTestCCompiler.cmake:67 (message):
  The C compiler

    "/Library/Developer/CommandLineTools/usr/bin/cc"

  is not able to compile a simple test program.

  It fails with the following output:

    Change Dir: '/Users/shotakaha/repos/sandbox/g4work/examples/basic/B1/build/CMakeFiles/CMakeScratch/TryCompile-893kjO'

    Run Build Command(s): /Applications/CMake.app/Contents/bin/cmake -E env VERBOSE=1 /usr/bin/make -f Makefile cmTC_75b67/fast
    /Library/Developer/CommandLineTools/usr/bin/make  -f CMakeFiles/cmTC_75b67.dir/build.make CMakeFiles/cmTC_75b67.dir/build
    Building C object CMakeFiles/cmTC_75b67.dir/testCCompiler.c.o
    /Library/Developer/CommandLineTools/usr/bin/cc   -arch arm64 -mmacosx-version-min=13.6 -MD -MT CMakeFiles/cmTC_75b67.dir/testCCompiler.c.o -MF CMakeFiles/cmTC_75b67.dir/testCCompiler.c.o.d -o CMakeFiles/cmTC_75b67.dir/testCCompiler.c.o -c /Users/shotakaha/repos/sandbox/g4work/examples/basic/B1/build/CMakeFiles/CMakeScratch/TryCompile-893kjO/testCCompiler.c
    Linking C executable cmTC_75b67
    /Applications/CMake.app/Contents/bin/cmake -E cmake_link_script CMakeFiles/cmTC_75b67.dir/link.txt --verbose=1
    /Library/Developer/CommandLineTools/usr/bin/cc  -arch arm64 -mmacosx-version-min=13.6 -Wl,-search_paths_first -Wl,-headerpad_max_install_names CMakeFiles/cmTC_75b67.dir/testCCompiler.c.o -o cmTC_75b67
    ld: library 'System' not found
    clang: error: linker command failed with exit code 1 (use -v to see invocation)
    make[1]: *** [cmTC_75b67] Error 1
    make: *** [cmTC_75b67/fast] Error 2

  CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt:4 (project)

-- Configuring incomplete, errors occurred!
```

:::{note}

すでにビルド済みのアプリケーションの実行ファイルは実行できました。

:::
