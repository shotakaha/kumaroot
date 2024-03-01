# インストールしたい（``geant4``）

```console
// 外部ツールを準備する
$ brew install --cask cmake
$ brew install --cask xquartz
$ brew install qt@5

// 作業ディレクトリを準備する
$ mkdir ~/repos/g4home  # --> $G4HOME
$ mkdir ~/repos/g4home/g4install/
$ mkdir ~/repost/g4home/g4install/build/
$ mkdir ~/repost/g4home/g4install/install/
$ mkdir ~/repost/g4home/g4install/data/

// ソースコードを準備する
$ cd ~/repos/g4home/g4install/
$ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.2.1/geant4-v11.2.1.zip
$ unzip geant4-v11.2.1.zip

// 作業用ディレクトリでビルド準備する
$ cd ~/repost/g4home/g4install/build
$ cmake -DMAKE_INSTALL_PREFIX=$G4HOME/g4install/install -DGEANT4_INSTALL_DATA=ON -DGEANT4_INSTALL_DATADIR=$G4HOME/g4install/data -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) ../geant4-v11.2.1/

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
geant4-install-ccmake
geant4-install-cmake
geant4-install-make
```

## 環境変数を設定する

```console
$ source $G4HOME/g4install/install/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（``$G4HOME/g4install/install``）の中に、設定スクリプト（``bin/geant4.sh``）が用意されています。
これを読み込んでからアプリケーションをコンパイルしてください。

いつも使うような場合は、シェルの起動スクリプトに書いておくとよいです。

:::{note}

BashとCsh用の設定スクリプトが用意されています。
Fish用の設定スクリプトが欲しい。

:::
