# ソースコードを準備する（``wget``）

```console
// 作業用ディレクトリにダウンロードする
$ cd ~/geant4/
(~/geant4/) $ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.X.Y/geant4-v11.X.Y.zip
(~/geant4/) $ unzip geant4-v11.Y.Y.zip
```

作業用ディレクトリ（`~/geant4/`）にGeant4のソースコードを準備します。
最新版のソースコードのURLは[Geant4公式サイト](https://geant4.web.cern.ch/download/)で確認してください。

ソースコードは`.zip`、`.tar.gz`、`.tar.bz2`、`.tar`の4種類の形式で用意されています。
お好みの形式をダウンロードしてください。
僕は``.zip``形式を選択しました。

```console
// ブラウザからダウンロードしたGeant4一式を移動する
(~/geant4/) $ mv ~/Downloads/geant4-v11.X.Y.zip .
(~/geant4/) $ unzip geant4-v11.X.Y.zip
```

また、ブラウザ経由でダウンロードすることもできます。
ブラウザを使ってダウンロードしたファイルを`~/Downloads/`に保存した場合は、
作業用ディレクトリ（`~/geant4/`）に移動させてください。
上では`mv`コマンドを使っていますが、ファインダーを使ってドラッグ＆ドロップしてもOKです。

ファイルを移動したら、その場所に展開（解凍）します。
ここも上では``unzip``コマンドを使っていますが、ファイルをダブルクリックしてもOKです。

:::{note}

[過去のリリース一覧](https://geant4.web.cern.ch/download/all)や、
[CERNのGitLab](https://gitlab.cern.ch/geant4/geant4/-/releases)と
[GitHub](https://github.com/Geant4/geant4/releases)に、
これまでのリリースが公開されています。

コラボレーションで開発していて、特定のバージョンが必要な場合は、
これらのページからダウンロードできます。

:::

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
