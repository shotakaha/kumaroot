# エラー対処

## No "FindGeant4.cmake"

アプリケーションをはじめてビルドしたときにエラーが発生しました。
これは、Geant4関連の変数が設定されていないため、CMakeが``find_package``できないために生じるエラーです。

### エラーの内容

```console
$ cmake ..
-- The C compiler identification is AppleClang 15.0.0.15000309
-- The CXX compiler identification is AppleClang 15.0.0.15000309
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at CMakeLists.txt:14 (find_package):
  By not providing "FindGeant4.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Geant4", but
  CMake did not find one.

  Could not find a package configuration file provided by "Geant4" with any
  of the following names:

    Geant4Config.cmake
    geant4-config.cmake

  Add the installation prefix of "Geant4" to CMAKE_PREFIX_PATH or set
  "Geant4_DIR" to a directory containing one of the above files.  If "Geant4"
  provides a separate development package or SDK, be sure it has been
  installed.

-- Configuring incomplete, errors occurred!
```

### 対処方法

```console
$ source $HOME/geant4/11.2.1/bin/geant4.sh
```

``$CMAKE_INSTALL_PREFIX/bin/geant4.sh``にある設定用スクリプトを読み込ませると解決できます。
Geant4をよく使う場合は、``.zshrc``に追記することをオススメします。

:::{note}

すでに``cmake``したことがあり、ビルド用ディレクトリに``CMakeCache.txt``のキャッシュがある場合は、環境変数を読み込まなくても``make -j8``でビルドできます（たぶん）。
CMakeでクリーン＆リビルドするとエラーになります。

:::

## C compiler - broken

macOSのコマンドラインツールのバージョンが変わってしまったために発生したエラーのようです。
エラーメッセージを読んで、``CMAKE_OSX_SYSROOT``に設定されているSDKツールのバージョンと、現在のシステムに存在するSDKのバージョンを確認したら異なっていました。

```diff
- /Library/Developer/CommandLineTools/SDKs/MacOSX14.2.sdk   # Geant4インストール時に指定されたバージョン（自動）
+ /Library/Developer/CommandLineTools/SDKs/MacOSX14.4.sdk   # 現在のシステムに存在するバージョン
```

OSの更新か、Xcodeの更新のどちらかのタイミングだと思うのですが、原因の切り分けはできていません。

### エラーの内容

```console
$ cd ~/repos/sandbox/g4work/examples/basic/B1/
(~/r/s/g/e/b/B1) $ cd build
(~/r/s/g/e/b/B1) $ cmake ..
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

### 対処方法

とりあえず、Geant4をリビルド＆インストールしたら解決しました。

:::{note}

もしかしたら、アプリのビルド用ディレクトリで``ccmake ..``を実行して``CMAKE_OSX_SYSROOT``を編集してもよかったかもしれません。

ただし、この対処方法だと、アプリケーションごとに編集が必要になるはずなので、結局どこかの時点でリビルド＆インストールする必要がでてきそうです。

:::

## No LC_RPATH's found

``make install``したパスにある実行ファイルを起動したら、``no LC_RPATH's found``という実行時エラーが発生しました。
これはアプリに必要な``.dylib``（ダイナミックライブラリ）のパス設定ができておらず、実行時にライブラリへのリンクがうまくいかないのが原因です。
Geant4特有ではなく、macOSでCMakeビルドしたアプリで発生するエラーです。

### エラーの内容

```console
(build/)$ make
(build/)$ make install
(build/)$ cd ../bin
(bin/)$ ./exampleB2a
dyld[63969]: Library not loaded: @rpath/libG4Tree.dylib
  Referenced from: <30677C2E-3240-3E3D-ADB8-3ED418861748>
  Reason: no LC_RPATH's found
```

### 一時的な対処方法（``install_name_tool``）

```console
// ライブラリがあるパスを検索する
(bin/)$ mdfind libG4Tree.dylib
...
~/geant4/11.2.1/lib/libG4Tree.dylib
...

// ライブラリを追加する
(bin/)$ install_name_tool -add_rpath ~/geant4/11.2.1/lib/ ./exampleB2a
(bin/)$ ./exampleB2a
```

``install_name_tool``コマンドで、実行ファイルにライブラリのパスを追加すると、一時的に解決できます。
ライブラリのパスは検索コマンドで確認しました。
今回の場合は``~/geant4/11.2.1/lib/``に目的のファイルがありました。

:::{caution}

一時的な対策なので、アプリをリビルドするたびに、再設定が必要です。

:::

### プロジェクトごとの対処方法

```cmake
#----------------------------------------------------------------------------
# RPATH settings
#----------------------------------------------------------------------------

# 他の設定の前に追加
set(CMAKE_MAXOSX_RPATH TRUE)

# ライブラリのパスを設定（ほぼ直パス）
set(G4LIB "$ENV{HOME}/geant4/11.2.1/lib")

# ビルド時のRPATH設定
set(CMAKE_BUILD_RPATH ${G4LIB})

# インストール時のRPATH設定
set(CMAKE_INSTALL_RPATH ${G4LIB})

# 実行時のRPATH設定
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
```

``CMakeLists.txt``にRPATH設定を追加しました。
``add_executable``や``target_link_libraries``より前で設定する必要があります。

### ユーザーごとの対処方法

```bash
export DYLD_LIBRARY_PATH=$HOME/geant4/11.2.1/lib:$DYLD_LIBRARY_PATH
```

いくつものGeant4プロジェクトを抱えている（もしくはテストしている）場合は、
ユーザーの環境変数を設定したほうがよいかもしれません。
上記の設定はZshとはBashで有効です。

試していませんが、Fishの場合は以下で設定できるはずです。

```fish
set -x DYLD_LIBRARY_PATH $HOME/geant4/11.2.1/lib $DYLD_LIBRARY_PATH
```

## No "Qt5CoreConfig.cmake"

例題のアプリをビルドしたときに`Qt5CoreConfig.cmake`が見つからないというエラーが発生しました。
`Qt5CoreConfig.cmake`のパスを確認し、`CMAKE_PREFIX_PATH`オプションに指定すると解決できます。

### エラーの内容

```console
CMake Error at /opt/homebrew/share/cmake/Modules/CMakeFindDependencyMacro.cmake:78 (find_package):
  By not providing "FindQt5Core.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Qt5Core", but
  CMake did not find one.

  Could not find a package configuration file provided by "Qt5Core" with any
  of the following names:

    Qt5CoreConfig.cmake
    qt5core-config.cmake

  Add the installation prefix of "Qt5Core" to CMAKE_PREFIX_PATH or set
  "Qt5Core_DIR" to a directory containing one of the above files.  If
  "Qt5Core" provides a separate development package or SDK, be sure it has
  been installed.
Call Stack (most recent call first):
  /Users/shotakaha/geant4/v11.3.2/install/lib/cmake/Geant4/Geant4Config.cmake:371 (find_dependency)
  CMakeLists.txt:13 (find_package)
```

### 対処方法

```console
$ locage Qt5CoreConfig.cmake
/opt/homebrew/Cellar/qt@5/5.15.16_2/lib/cmake/Qt5Core/Qt5CoreConfig.cmake

$ cmake .. -DCMAKE_PREFIX_PATH=/opt/homebrew/Cellar/qt@5/5.15.16_2
```

`Qt5CoreConfig.cmake`のパスを確認します。
現在の環境では`/opt/homebrew/Cellar/qt@5/5.15.16_2`の中にありました。
このパスを`CMAKE_PREFIX_PATH`オプションに指定したら解決できました。
