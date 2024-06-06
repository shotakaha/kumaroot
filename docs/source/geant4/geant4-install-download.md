# ソースコードを準備する（``wget``）

```console
// 作業用ディレクトリにダウンロードする
$ cd ~/geant4/
(~/geant4/) $ wget
(~/geant4/) $ unzip geant4-v11.2.1.zip
```

```console
// ブラウザからダウンロードしたGeant4一式を移動する
(~/geant4/) $ mv ~/Downloads/geant4-v11.2.1.zip .
(~/geant4/) $ unzip geant4-v11.2.1.zip
```

作業用ディレクトリ（``~/geant4/``）にGeant4のソースコードを準備します。
ソースコードの最新版は[Geant4公式サイト](https://geant4.web.cern.ch/download/)からダウンロードできます。

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
$ tree ~/geant4 -L 1
geant4/
├── build
├── geant4-v11.2.1      // 展開したソースコード一式
└── geant4-v11.2.1.zip  // ダウンロードしたファイル

3 directories, 1 file
```

このようなディレクトリ構成になっていたら、次に進んでください。
