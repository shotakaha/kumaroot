# ソースコードを準備する

最新版のソースコードを[Geant4公式サイト](https://geant4.web.cern.ch/download/)で確認し、ダウンロードします。

特定のバージョンが必要な場合は、

[過去のリリース一覧](https://geant4.web.cern.ch/download/all)や、
[CERNのGitLab](https://gitlab.cern.ch/geant4/geant4/-/releases)、
[GitHub](https://github.com/Geant4/geant4/releases)、
からダウンロードできます。

## ダウンロードする（`wget`）

```console
$ cd ~/geant4/
// ダウンロードする
(~/geant4/) $ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.X.Y/geant4-v11.X.Y.zip
```

[wgetコマンド](../command/command-wget.md)でソースコードをダウンロードします。
`~/geant4/`で作業します。
ソースコードは`.zip`、`.tar.gz`、`.tar.bz2`、`.tar`の4種類の形式で用意されています。
お好みの形式をダウンロードしてください。
僕は`.zip`形式を選択しました。

:::{note}

ブラウザを使ってダウンロードした場合は、通常`~/Downloads/`に保存されます。
`mv`コマンド、もしくはファインダーを使ってドラッグ＆ドロップして、
作業用ディレクトリ（`~/geant4/`）に移動させてください。

```console
// ブラウザからダウンロードしたGeant4一式を移動する
(~/geant4/) $ mv ~/Downloads/geant4-v11.X.Y.zip .
```

:::

## 展開する（`unzip`）

```console
// 展開する
(~/geant4/) $ unzip geant4-v11.X.Y.zip
(~/geant4/) $ ls -1
geant4-v11.X.Y.zip
geant4-v11.X.Y/
```

`unzip`コマンドでZIP形式のファイルを展開します。

## リネームする（`mv`）

```console
// アーカイブに移動する
(~/geant4/) $ mv geant4-v11.X.Y.zip archives/

// リネームする
(~/geant4/) $ mv geant4-v11.X.Y v11.X.Y/source
```

ダウンロードしたZIP形式のファイルは`~/geant4/archives/`に移動し、
展開したソース一式（＝ディレクトリ）は`~/geant4/v11.X.Y/source`にリネームします。

:::{note}

Geant4のソースコードはウェブ上にあるため、
パソコンのディスク容量が節約したい場合、アーカイブを手元に残す必要はありません。

:::

## ディレクトリ構成

```console
$ tree ~/geant4 -L 1
geant4/
├── archives/
│   ├── geant4-v11.2.1.zip  // ダウンロードしたファイル
├── v11.2.1/
│   ├── source/      // 展開したソースコード一式
```

このようなディレクトリ構成になっていたら、次に進んでください。
