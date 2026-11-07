# ソースコードを準備したい

```console
$ mkdir -p ~/geant4/archives
$ cd ~/geant4/archives
$ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.4.3/geant4-v11.4.3.zip

$ cd ~/geant4/
$ unzip archives/geant4-v11.4.3.zip
$ mv -n archives/geant4-v11.4.3 v11.4.3/source
```

`wget`コマンドでGeant4のソースコードをダウンロードし、`unzip`コマンドで展開します。
ダウンロードしたソースコード本体（圧縮ファイル）は`~/geant4/archives/`に保存し、展開したソースコード一式は`~/geant4/v11.4.3/source`にリネームします。

利用可能なGeant4のバージョンは
[Geant4公式サイト](https://geant4.web.cern.ch/download/all)
で確認できます。
より古いバージョンが必要な場合は
[Geant4のGitHubリポジトリ](https://github.com/Geant4/geant4/releases)
で確認できます。

## ダウンロードしたい（`wget`）

```console
$ cd ~/geant4/archives
$ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.X.Y/geant4-v11.X.Y.zip
```

[wgetコマンド](../command/command-wget.md)でソースコードをダウンロードします。
作業ディレクトリは`~/geant4/archives/`です。

ソースコードは`.zip`、`.tar.gz`、`.tar.bz2`、`.tar`の4種類の形式で用意されています。
お好みの形式をダウンロードしてください。
僕は`.zip`形式を選択しました。

:::{note}

ブラウザを使ってダウンロードした場合は、通常`~/Downloads/`に保存されます。
`mv`コマンド、もしくはファインダーを使ってドラッグ＆ドロップして、
作業用ディレクトリ（`~/geant4/archives/`）に移動させてください。

```console
// ブラウザからダウンロードしたGeant4一式を移動する
(~/geant4/archives/) $ mv ~/Downloads/geant4-v11.X.Y.zip .
```

:::

## 展開したい（`unzip`）

```console
// 展開する
$ cd ~/geant4/
(~/geant4/) $ unzip archives/geant4-v11.X.Y.zip
(~/geant4/) $ ls -1
archives/geant4-v11.X.Y.zip
geant4-v11.X.Y/
```

`unzip`コマンドでZIP形式のファイルを展開します。
作業ディレクトリは`~/geant4/`です。

## リネームしたい（`mv`）

```console
$ cd ~/geant4/
(~/geant4/) $ mv geant4-v11.X.Y v11.X.Y/source
```

ダウンロードしたZIP形式のファイルは`~/geant4/archives/`に移動し、
展開したソース一式（＝ディレクトリ）は`~/geant4/v11.X.Y/source`にリネームします。

:::{note}

Geant4のソースコードはウェブ上にあるため、
パソコンのディスク容量が節約したい場合、アーカイブ用は削除しても問題ありません。

:::

## ディレクトリ構成

```console
$ tree ~/geant4 -L 1
geant4/
├── archives/
│   ├── geant4-v11.4.3.zip  // ダウンロードしたファイル
├── v11.4.3/
│   ├── source/      // 展開したソースコード一式
```

このようなディレクトリ構成になっていたら、次に進んでください。
