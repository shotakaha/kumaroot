# エラー対処

## CMake Error at CMakeLists.txt

Geant4関係の環境変数が設定されていないと``cmake``するときにエラーとなります。
``$CMAKE_INSTALL_PREFIX/bin/geant4.sh``にある設定用のスクリプトを読み込ませて解決できます。

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

たぶん``Xcode.app``を更新したため、アプリケーションがビルドできなくなりました。
``CMAKE_OSX_SYSROOT``に設定されるSDKツールのバージョンが変わってしまったのが原因のようです。

```diff
- /Library/Developer/CommandLineTools/SDKs/MacOSX14.2.sdk   # Geant4インストール時に指定されたバージョン（自動）
+ /Library/Developer/CommandLineTools/SDKs/MacOSX14.4.sdk   # Xcode更新後のバージョン
```

スクリプトや環境変数の再設定で解決する方法は分かりませんでした。
Geant4をリビルド＆インストールしたら解決しました。

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


