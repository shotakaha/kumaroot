# インストールしたい（`geant4`）

```console
$ cmake -S geant4-v11.2.1 -B build -Dオプション=...
$ cmake --build build
$ cmake --install build
```

Geant4本体は自分でビルドしてインストールする必要があります。
最新のバージョンはCMake対応しており、一般的な手順でビルド＆インストールできます。

ここでは、Geant4とCMakeの公式ドキュメントを参考にして、
複数のGeant4のバージョンを管理する（マイ）ベストプラクティスを紹介します。

## ディレクトリ構成したい

```console
~/geant4
  |-- archives/
  |    |-- geant4.v11.2.1.tar.gz
  |    |-- geant4.v11.2.2.tar.gz
  |    |-- geant4.v11.X.Y.tar.gz
  |-- v11.2.1/
  |    |-- CMakePresets.json
  |    |-- source/CMakeLists.txt
  |    |-- build/CMakeCache.txt
  |    |-- install/
  |-- v11.2.2/
  |    |-- CMakePresets.json
  |    |-- source/
  |    |-- build/
  |    |-- install/
  |-- v11.X.Y/
  |    |-- CMakePresets.json
  |    |-- source/
  |    |-- build/
  |    |-- install/
```

`~/geant4`を作成し、Geant4専用のディレクトリとしています。
この中に、バージョンごとのディレクトリを作成します。
また、ダウンロードしたソースコードも`archives`に保存しておきます。

## インストール手順のまとめ

```console
// 外部ツールを準備する
$ brew install wget
$ brew install cmake
$ brew install qt@5
$ brew install --cask xquartz
$ brew install ninja  # optional

// ディレクトリを作成する
$ mkdir -p ~/geant4
$ mkdir -p ~/geant4/archives

// ソースコードをダウンロードする
// 作業ディレクトリ: ~/geant4/archives
// 1. ~/geant4/archives にダウンロードして展開する
$ cd ~/geant4/archives
(~/geant4/archives/) $ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.2.1/geant4-v11.2.1.zip

// ソースコードを展開する
// 作業ディレクトリ: ~/geant4
$ cd ~/geant4/
(~/geant4/) $ unzip archives/geant4-v11.2.1.zip
(~/geant4/) $ mkdir v11.2.1
(~/geant4/) $ mv geant4-v11.2.1 v11.2.1/source

// ビルド構成 -> ビルド -> インストール
// 作業ディレクトリ: ~/geant4/v11.2.1
$ cd ~/geant4/v11.2.1
(~/geant4/v11.2.1/) $ cmake \
-S source \
-B build \
-DCMAKE_INSTALL_PREFIX=install \
-DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) \
-DGEANT4_INSTALL_DATA=ON \
-DGEANT4_USE_OPENGL_X11=ON \
-DGEANT4_USE_RAYTRACER_X11=ON \
-DGEANT4_USE_QT=ON
(~/geant4/v11.2.1/) $ cmake --build build --parallel
(~/geant4/v11.2.1/) $ cmake --install build --parallel

// インストール先のディレクトリ構成を確認
(~/geant4/v11.2.1/) $ tree ~/geant4/v11.2.1/install -L 1
/Users/shotakaha/geant4/v11.2.1/install
├── bin
├── include
├── lib
└── share

// 環境変数を設定する
$ source ~/geant4/v11.2.1/install/bin/geant4.sh
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
geant4-install-cmake
geant4-install-ccmake
geant4-install-make
```

また、上記の手順を再利用可能な形に整理した方法も紹介します。

```{toctree}
---
maxdepth: 2
---
geant4-install-taskfile
```
