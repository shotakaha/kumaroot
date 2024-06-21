# 環境変数したい（``geant4.sh``）

```console
// CMAKE_INSTALL_PREFIX は設定したパスに変更
$ source $CMAKE_INSTALL_PREFIX/bin/geant4.sh

// 上記の設定でインストールした場合
$ source ~/geant4/bin/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（``$CMAKE_INSTALL_PREFIX/bin/``）の中に、設定スクリプト（``geant4.sh``）が用意されています。
これを読み込んでからアプリケーションをコンパイルしてください。
いつも使うような場合は、シェルの起動スクリプトに書いておくとよいです。

## 設定を確認したい（``geant4-config``）

``${CMAKE_INSTALL_PREFIX}/bin/``にインストールされる``geant4-config``で、
Geant4の設定を確認できます。

```console
$ ./geant4/11.2.1/bin/geant4-config

$ geant4-config --prefix
~/geant4/11.2.1

$ geant4-config --version
11.2.1

$ geant4-config --cxxstd
17

$ geant4-config --cflags
-I/usr/X11R6/include
-DG4VIS_USE_OPENGL
-DG4UI_USE_TCSH
-DG4UI_USE_QT
-DG4VIS_USE_OPENGLQT
-DG4VIS_USE_TOOLSSG_QT_GLES
-I/usr/local/opt/qt@5/lib/QtCore.framework
-I/usr/local/opt/qt@5/lib/QtCore.framework/Headers
-I/usr/local/opt/qt@5/.//mkspecs/macx-clang
-I/usr/local/opt/qt@5/lib/QtGui.framework
-I/usr/local/opt/qt@5/lib/QtGui.framework/Headers
-I/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX14.4.sdk/System/Library/Frameworks/OpenGL.framework/Headers
-I/usr/local/opt/qt@5/lib/QtWidgets.framework
-I/usr/local/opt/qt@5/lib/QtWidgets.framework/Headers
-I/usr/local/opt/qt@5/lib/QtOpenGL.framework
-I/usr/local/opt/qt@5/lib/QtOpenGL.framework/Headers
-F/usr/local/Cellar/qt@5/5.15.13_1/lib
-DG4UI_USE_QT3D
-DG4VIS_USE_OPENGLX
-DG4VIS_USE_TOOLSSG_X11_GLES
-W -Wall -pedantic
-Wno-non-virtual-dtor
-Wno-long-long
-Wwrite-strings
-Wpointer-arith
-Woverloaded-virtual
-Wno-variadic-macros
-Wshadow
-pipe
-Qunused-arguments
-DGL_SILENCE_DEPRECATION
-pthread
-ftls-model=initial-exec
-std=c++17
-I/Users/shotakaha/geant4/11.2.1/include/Geant4

$ geant4-config --libs
-L/Users/shotakaha/geant4/11.2.1/lib-lG4OpenGL
-lG4visQt3D
-lG4Tree
-lG4FR
-lG4GMocren
-lG4visHepRep
-lG4RayTracer
-lG4VRML
-lG4ToolsSG
-lG4vis_management
-lG4modelin
-lG4interfaces
-lG4geomtext
-lG4mctruth
-lG4analysis
-lG4error_propagation
-lG4readout
-lG4physicslists
-lG4run
-lG4event
-lG4tracking
-lG4parmodels
-lG4processes
-lG4digits_hits
-lG4track
-lG4particles
-lG4geometry
-lG4materials
-lG4graphics_reps
-lG4intercoms
-lG4global
-lG4clhep
-lG4zlib
-lG4ptl





```


## Fishしたい

:::{caution}

残念ながらFish用の設定スクリプトはありません。

:::

僕は、以下のようにGeant4を使う時だけZshに切り替えて作業することにしました。

```console
(fish) $ zsh
(zsh) $ source ~/geant4/bin/geant4.sh
(zsh) $ cd ~/repos/sandbox/g4work/examples/basic/B1/
(zsh) $ mkdir build
(zsh) $ cd build
(zsh) $ cmake ..
(zsh) $ make
(zsh) $ ./exampleB1
```

一度``cmake``して得られた設定ファイル群があれば、
Fishの中で``make``したり、アプリケーションを実行したりできました。
