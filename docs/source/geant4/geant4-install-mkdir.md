# 作業ディレクトリを準備する（``mkdir``）

```console
$ mkdir ~/repos/g4home       # 以降 $G4HOME と表記する
$ mkdir $G4HOME/g4install    # インストール作業用
$ mkdir $G4HOME/g4install/install   # Geant4ツールキットをインストールするディレクトリ
$ mkdir $G4HOME/g4install/build     # cmakeでビルド作業するためのディレクトリ
$ mkdir $G4HOME/g4install/data      # 関連データを保存するディレクトリ
```

講習会のインストール手順を参考にしました。
インストール用とアプリケーション開発用のディレクトリは別々にしたほうがよいそうです。

僕は、Geant4関係のファイルを管理するために``~/repos/g4home/``ディレクトリを作成しました。
これを便宜上``$G4HOME``と呼ぶことにします。
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
