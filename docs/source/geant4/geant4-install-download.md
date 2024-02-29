# ソースコードを準備する

```console
$ cd $G4HOME/g4install
$ mv ~/Downloads/geant4-v11.2.1.zip .
$ unzip geant4-v11.2.1.zip
```

インストール作業用ディレクトリ（``$G4HOME/g4install/``）にGeant4のソースコードを準備します。
ソースコードの最新版は[Geant4公式サイト](https://geant4.web.cern.ch/download/)からダウンロードします。

:::{note}

特定のバージョンを使いたい場合は[過去のリリース一覧](https://geant4.web.cern.ch/download/all)から選択できます（[CERNのGitLab](https://gitlab.cern.ch/geant4/geant4/-/releases)や[GitHub](https://github.com/Geant4/geant4/releases)でも公開されています）。

:::

ソースコードは``.zip``、``.tar.gz``、``.tar.bz2``、``.tar``の4種類の形式で用意されています。お好みの形式をダウンロードしてください。

僕は``.zip``形式を選択しました。
ブラウザを使ってダウンロードし、ファイルを``~/Downloads/``に保存しました。
ダウンロードしたファイルはそのまま作業用ディレクトリ（``$G4HOME/g4install``）に移動します。
上では``mv``コマンドを使っていますが、ファインダーを使ってドラッグ＆ドロップしてもOKです。

ファイルを移動したら、その場所に展開（解凍）します。
ここも上では``unzip``コマンドを使っていますが、ファイルをダブルクリックしてもOKです。

## ディレクトリ構成

```console
$ tree g4home -L 3
g4home
└── g4install
    ├── build
    ├── data
    ├── geant4-v11.2.1    # 展開したソースコード一式
    │   ├── CHANGELOG -> ReleaseNotes
    │   ├── CITATION.cff
    │   ├── CMakeLists.txt
    │   ├── CONTRIBUTING.rst
    │   ├── LICENSE
    │   ├── README.rst
    │   ├── ReleaseNotes
    │   ├── cmake
    │   ├── config
    │   ├── environments
    │   ├── examples
    │   ├── packaging
    │   └── source
    ├── geant4-v11.2.1.zip    # ダウンロードしたファイル
    └── install
```

このようなディレクトリ構成になっていたら、次に進んでください。

