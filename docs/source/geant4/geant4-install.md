# インストールしたい（``geant4``）

```console
$ mkdir ~/repos/g4home  # --> $G4HOME
```

Geant4用のディレクトリを作成し、これを``$G4HOME``と呼ぶことにします。
ディレクトリ名は任意です。
僕は``~/repos/g4home/``を作成しました。


```{toctree}
geant4-install-ccmake
geant4-install-qt
geant4-install-make
```

## インストール作業用のディレクトリを作成する

```console
$ mkdir $G4HOME/g4install
$ mkdir $G4HOME/g4install/install
$ mkdir $G4HOME/g4install/build
$ mkdir $G4HOME/g4install/data
```

インストール作業用のディレクトリを作成します。
ここでは``$G4HOME/g4install``としました。
さらにその中に``install``、``build``、``data``の3種類のディレクトリを作成します。

ここでのディレクトリ構成は、次のようになっているはずです。

```console
$ ls -1 $G4HOME/g4install
build/
data/
install/
```

## ソースコードをダウンロードする

```console
$ cd $G4HOME/g4install
$ mv ~/Downloads/geant4-v11.2.1.zip .
$ unzip geant4-v11.2.1.zip
```

Geant4公式サイトから圧縮されたソースコードをダウンロードします。
ソースコードは``.zip``、``.tar.gz``、``.tar.bz2``、``.tar``の4種類の形式で用意されています。
お好みの形式をダウンロードすればよいです。

僕は``.zip``形式でダウンロードしました。
ブラウザを使ったのでファイルは``~/Downloads/``に保存されました。
このファイルを作業用ディレクトリ（``$G4HOME/g4install``）に移動します。
ここでは``mv``コマンドで移動していますが、ファインダーなどを開いてドラッグドロップしても構いません。

ソースコードを移動したら展開（解凍）します。
ここも``unzip``コマンドで展開していますが、ファイルをダブルクリックする方が簡単です。

ここまででディレクトリ構成は、次のようになっているはずです。

```console
$ ls -1 $G4HOME/g4install
build/
data/
geant4-v11.2.1/       # 展開したソースコード
geant4-v11.2.1.zip    # ダウンロードしたソースコード
install/
```

## ディレクトリ構成を確認する

```console
$ ls -1 $G4HOME/g4install/install/
bin/
include/
lib/
share/

$ ls -1 $G4HOME/g4install/data/
G4ABLA3.3/
G4EMLOW8.5/
G4ENSDFSTATE2.3/
G4INCL1.2/
G4NDL4.7/
G4PARTICLEXS4.0/
G4PII1.3/
G4SAIDDATA2.0/
PhotonEvaporation5.7/
RadioactiveDecay5.6/
RealSurface2.2/
```

## シェル変数を設定する

```console
$ source $G4HOME/g4install/install/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数を適切に設定する必要があります。
インストールしたディレクトリにあるシェルスクリプト（``bin/geant4.sh``）を読み込むと設定できます。

:::{note}

Bashを使っていることが前提のようです。
Fish用の設定スクリプトが欲しい。

:::
