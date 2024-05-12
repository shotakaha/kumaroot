# 作業ディレクトリを準備する（``mkdir``）

```console
// Geant4用ディレクトリを作成する
$ mkdir ~/repos/g4home
$ mkdir ~/repos/g4home/g4install  # ビルド＆インストール用
$ mkdir ~/repos/g4home/g4work   # アプリケーション開発用

$ export G4HOME=~/repos/g4home
$ export G4INSTALL=$G4HOME/g4install
$ export G4WORK=$G4HOME/g4work

// ビルド作業用のディレクトリを作成する
$ cd ~/repos/g4home/g4build
$ mkdir 11.2.1  # インストール先
$ mkdir build   # cmakeのビルド作業用
```

公式ドキュメントと講習会のインストール手順を参考にしました。
ビルド＆インストール用とアプリケーション開発用のディレクトリは、別々にしたほうがよいそうです。

僕の場合、パソコンを変えても同じように作業できるようにGeant4関係はひとつのディレクトリ（``~/repos/g4home/``）にまとめることにしています。
このパスを``$G4HOME``としておきます。

その中に、ビルド＆インストール用（``$G4HOME/g4install/``）とアプリケーション開発用（``$G4HOME/g4work/``）のディレクトリを作成しました。
ビルド＆インストール用のディレクトリの中には、
Geant4のインストール先に指定するディレクトリ（``$G4BUILD/11.2.1/``）と
cmakeでビルド作業するためのディレクトリ（``$G4INSTALL/build/``）を作成しました、
各人がインストールする環境に合わせて、適宜置き換えて実行してください。

:::{note}

Geant4に必要なデータセット用のディレクトリを作成する場合もあるようです。

```console
$ mkdir $G4INSTALL/data/
```

:::

## ディレクトリ構成

```console
$ tree g4home -L 2
g4home
├── g4install
│   ├── 11.2.1
│   ├── build
│   ├── geant4-v11.2.1      # 次のページで用意する
│   └── geant4-v11.2.1.zip  # 次のページで用意する
└── g4work
```

このようなディレクトリ構成になっていたら、次に進んでください。
