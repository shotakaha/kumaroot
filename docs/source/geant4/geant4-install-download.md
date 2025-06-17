# ソースコードを準備する

最新版のソースコードのURLは[Geant4公式サイト](https://geant4.web.cern.ch/download/)で確認してください。

:::{note}

[過去のリリース一覧](https://geant4.web.cern.ch/download/all)や、
[CERNのGitLab](https://gitlab.cern.ch/geant4/geant4/-/releases)と
[GitHub](https://github.com/Geant4/geant4/releases)に、
これまでのリリースが公開されています。

コラボレーションで開発していて、特定のバージョンが必要な場合は、
これらのページからダウンロードできます。

:::

## 作業ディレクトリ

```console
$ cd ~/geant4/
(~/geant4/) $
```

作業ディレクトリは`~/geant4/`です。

## ダウンロードする（`wget`）

```console
// ダウンロードする
(~/geant4/) $ wget https://gitlab.cern.ch/geant4/geant4/-/archive/v11.X.Y/geant4-v11.X.Y.zip
```

作業用ディレクトリ（`~/geant4/`）にGeant4のソースコードをダウンロードします。
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

ダウンロードしたファイルを、その場で展開します。
`zip`形式でダウンロードしたので`unzip`します。

## 移動する（`mv`）

```console
// 移動する
(~/geant4/) $ mv geant4-v11.X.Y.zip archives/
(~/geant4/) $ mv geant4-v11.X.Y v11.X.Y/source
```

ダウンロードしたファイルは`~/geant4/archives/`に移動し、
展開したソース一式（＝ディレクトリ）は`~/geant4/v11.X.Y/source`にリネームします。

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
