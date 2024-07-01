# インストール／ビルド時のエラーと対処法

## CMake Error at CMakeLists.txt

アプリケーションをはじめてビルド、もしくは``cmake``からリビルドするときに、Geant4関係の環境変数が設定されていないとエラーになります。
``$CMAKE_INSTALL_PREFIX/bin/geant4.sh``にある設定用のスクリプトを読み込ませて解決できます。

:::{note}
すでに``cmake``したことがあり、ビルド用ディレクトリに``CMakeCache.txt``がある場合は、環境変数を読み込まなくても``make -j8``でビルドできます（たぶん）。
:::

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

## C compiler - broken

久しぶりに使ってみたら、アプリケーションがビルドできなくなりました。
OSの更新、Xcodeの更新、CMakeの更新のどこかのタイミングでビルドできなくなってしまったと思うのですが、どれが原因か切り分けられていません。

エラーを確認すると
``CMAKE_OSX_SYSROOT``に設定されているSDKツールのバージョンと、現在のシステムに存在するSDKのバージョンが変わってしまったのが原因だと思います。

```diff
- /Library/Developer/CommandLineTools/SDKs/MacOSX14.2.sdk   # Geant4インストール時に指定されたバージョン（自動）
+ /Library/Developer/CommandLineTools/SDKs/MacOSX14.4.sdk   # 現在のシステムに存在するバージョン
```

とりあえず、Geant4をリビルド＆インストールしたら解決しました。

:::{note}

もしかしたら、アプリのビルド用ディレクトリで``ccmake ..``を実行して``CMAKE_OSX_SYSROOT``を編集してもよかったかもしれません。

ただし、この対処方法だと、アプリケーションごとに編集が必要になるはずなので、結局どこかの時点でリビルド＆インストールする必要がでてきそうです。

:::

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

## no LC_RPATH's found

```console
(build/)$ make
(build/)$ make install
(build/)$ cd ../bin
(bin/)$ ./exampleB2a
dyld[63969]: Library not loaded: @rpath/libG4Tree.dylib
  Referenced from: <30677C2E-3240-3E3D-ADB8-3ED418861748>
  Reason: no LC_RPATH's found
```

``make install``したパスの実行ファイルを起動すると``no LC_RPATH's found``というエラーがでた。
これはアプリに必要な``.dylib``（ダイナミックライブラリ）のパス設定がうまくできていないのが原因で、
Geant4特有ではなく、macOSでCMakeビルドしたアプリに起きるエラーです。

### 一時的な対処（``install_name_tool``）

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

検索コマンドでライブラリのパスを確認しました。
今回の場合は``~/geant4/11.2.1/lib/``に目的のファイルがありました。
``install_name_tool``コマンドで、実行ファイルにライブラリのパスを追加しました。
どのパスからでも実行できるようになりました。

:::{caution}

この対策だと、アプリを再ビルドするたびに、設定しなおす必要があります。

:::

### CMakeLists.txtを修正する

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

### 環境変数を設定する

```bash
export DYLD_LIBRARY_PATH=$HOME/geant4/11.2.1/lib:$DYLD_LIBRARY_PATH
```

いくつものGeant4プロジェクトを抱えている（もしくはテストしている）場合は、
環境変数を設定したほうがよいかもしれません。
上記の設定はZshとはBashで有効です。

試していませんが、Fishの場合は以下で設定できるはずです。

```fish
set -x DYLD_LIBRARY_PATH $HOME/geant4/11.2.1/lib $DYLD_LIBRARY_PATH
```
