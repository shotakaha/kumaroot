# インストールしたい（``geant4``）

```console
// 外部ツールを準備する
$ brew install --cask cmake
$ brew install --cask xquartz
$ brew install qt@5

// Geant4用ディレクトリを作成する
$ mkdir ~/geant4

// ソースコードをダウンロードする
$ cd ~/geant4/
(~/geant4/) $ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.2.1/geant4-v11.2.1.zip
(~/geant4/) $ unzip geant4-v11.2.1.zip

// cmakeでビルド作業するディレクトリを作成する
(~/geant4/) $ mkdir build

// 現在のディレクトリ構成を確認する
(~/geant4/) $ ls -1
build/
geant4-v11.2.1/
geant4-v11.2.1.zip

// cmakeのビルド用ディレクトリに移動する
(~/geant4/) $ cd build

// cmakeのビルドオプションを設定
(~/geant4/build/) $ cmake \
-DCMAKE_INSTALL_PREFIX=~/geant4/11.2.1/ \
-DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) \
-DGEANT4_INSTALL_DATA=ON \
-DGEANT4_USE_OPENGL_X11=ON \
-DGEANT4_USE_RAYTRACER_X11=ON \
-DGEANT4_USE_QT=ON \
../geant4-v11.2.1/

// ccmakeでビルドオプションを確認する
(~/geant4/build/) $ ccmake ../geant4-v11.2.1/

// 設定ファイルなどが生成されていることを確認
(~/geant4/build/) $ ls
// もともと空だったディレクトリに
// いろいろファイルができていることを確認する

// ビルドする
(~/geant4/build/) $ make -j8

// インストールする
(~/geant4/build/) $ make install

// インストール先のディレクトリ構成を確認
(~/geant4/build/) $ tree ~/geant4/11.2.1/ -L 1
/Users/shotakaha/geant4/11.2.1/
├── bin
├── include
├── lib
└── share

// 環境変数を設定する
$ source ~/geant4/bin/geant4.sh
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
geant4-install-cmake
geant4-install-ccmake
geant4-install-make
geant4-install-env
geant4-install-errors
```



