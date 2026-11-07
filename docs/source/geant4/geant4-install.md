# インストールしたい（`geant4`）

Geant4本体はソースコードを自分でビルドしてインストールする必要があります。
ここでは、Geant4の公式ドキュメントを参考にして、複数のバージョンを管理する（マイ）ベストプラクティスを紹介します。

::: {seealso}

ここで紹介する手順をまとめたリポジトリも作成しました。

- [qumasan/g4setup](https://gitlab.com/qumasan/g4setup)

:::

前提として
`~/geant4`にGeant4専用のディレクトリを作成し、その中でバージョンごとにディレクトリを作成して管理することにします。
また、ダウンロードしたソースコードは`~/geant4/archives/`に保存することとします。

```text
~/geant4
  |-- archives/    # ソース（圧縮ファイル）の保存用
  |    |-- geant4.v11.3.2.tar.gz
  |    |-- geant4.v11.4.0.tar.gz
  |    |-- geant4.v11.4.3.tar.gz
  |-- v11.3.2/    # バージョンごとの作業ディレクトリ
  |-- v11.4.0/
  |-- v11.4.3/
      |-- source/    # ソース一式
      |-- build/     # ビルド用のディレクトリ
      |-- install/   # インストール先のディレクトリ
```

## インストール手順のまとめ

```console
// 外部ツールを準備する
$ brew install wget
$ brew install cmake
$ brew install qt    # or qt@5
$ brew install --cask xquartz
$ brew install ninja  # optional

// ディレクトリを作成する
$ mkdir -p ~/geant4
$ mkdir -p ~/geant4/archives

// ソースコードをダウンロードする
// 作業ディレクトリ: ~/geant4/archives
// 1. ~/geant4/archives にダウンロードして展開する
$ cd ~/geant4/archives
(~/geant4/archives/) $ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.4.3/geant4-v11.4.3.zip

// ソースコードを展開する
// 作業ディレクトリ: ~/geant4
$ cd ~/geant4/
(~/geant4/) $ unzip archives/geant4-v11.4.3.zip
(~/geant4/) $ mkdir v11.4.3
(~/geant4/) $ mv geant4-v11.4.3 v11.4.3/source

// ビルド構成 -> ビルド -> インストール
// 作業ディレクトリ: ~/geant4/v11.4.3
$ cd ~/geant4/v11.4.3
(~/geant4/v11.4.3/) $ cmake \
-S source \
-B build \
-DCMAKE_INSTALL_PREFIX=install \
-DCMAKE_PREFIX_PATH=$(brew --prefix qt) \
-DGEANT4_INSTALL_DATA=ON \
-DGEANT4_USE_OPENGL_X11=ON \
-DGEANT4_USE_RAYTRACER_X11=ON \
-DGEANT4_USE_QT=ON
(~/geant4/v11.4.3/) $ cmake --build build --parallel
(~/geant4/v11.4.3/) $ cmake --install build --parallel

// インストール先のディレクトリ構成を確認
(~/geant4/v11.4.3/) $ tree ~/geant4/v11.4.3/install -L 1
/Users/shotakaha/geant4/v11.4.3/install
├── bin
├── include
├── lib
└── share

// 環境変数を設定する
$ source ~/geant4/v11.4.3/install/bin/geant4.sh
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
geant4-install-configure
geant4-install-ccmake
geant4-install-build
geant4-install-clean
```

また、上記の手順を再利用可能な形に整理した方法も紹介します。

```{toctree}
---
maxdepth: 2
---
geant4-install-taskfile
```
