# 作業ディレクトリを準備する（``mkdir``）

```console
$ mkdir ~/repos/g4home
$ export G4HOME=~/repos/g4home  # $G4HOME と名付ける
$ cd $G4HOME  # 以下の作業は $G4HOME からの相対パス
$ mkdir g4install    # インストール作業用
$ mkdir g4install/install   # Geant4ツールキットをインストールするディレクトリ
$ mkdir g4install/build     # cmakeでビルド作業するためのディレクトリ
$ mkdir g4install/data      # 関連データを保存するディレクトリ
```

講習会のインストール手順を参考にしました。
インストール用とアプリケーション開発用のディレクトリは別々にしたほうがよいそうです。

僕は、Geant4関係のファイルを管理するために``~/repos/g4home/``ディレクトリを作成しました。
ここでは、このパスを``$G4HOME``としました。
各人がインストールする環境に合わせて、適宜置き換えて実行してください。

``$G4HOME``の中にインストール作業用（``$G4HOME/g4install/``）のディレクトリを作成しました。
さらに、その中に``install``、``build``、``data``の3種類のディレクトリを作成します。

## ディレクトリ構成

```console
$ tree g4home -L 2
g4home
└── g4install
    ├── build
    ├── data
    └── install
```

このようなディレクトリ構成になっていたら、次に進んでください。
