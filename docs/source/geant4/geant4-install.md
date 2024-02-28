# インストールしたい（``geant4``）

```console
$ mkdir ~/repos/g4home  # --> $G4HOME
```

Geant4用のディレクトリを作成し、これを``$G4HOME``と呼ぶことにします。
ディレクトリ名は任意です。
僕は``~/repos/g4home/``を作成しました。

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

## ビルドの準備をする（1）

```console
$ cd $G4HOME/g4install/
$ cd build/
$ ccmake ../geant4-v11.2.1/
```

Geant4.10からデフォルトのビルドツールが``cmake``になりました。
``cmake``には「out-of-source」というコンセプトがあるそうで、
ソースコード本体とビルドしたファイルたちは別々のディレクトリで管理するのがしきたりのようです。

そのしきたりにしたがい、事前に作成した``build``ディレクトリで作業をします。
ビルド用ディレクトリから``CMakeLists.txt``があるソースコードに向けて``ccmake``します。

``ccmake``は``cmake``のGUI版みたいなもので、実行するとターミナルにオプションの操作プロンプトが表示されます。
必要なオプションを有効にして、設定ファイルを生成（``[g] Generate``）します。

ここではひとまず以下の項目の設定しました。

| オプション名 | 設定値 | デフォルト値 |
|---|---|---|
| ``CMAKE_INSTALL_PREFIX`` | ``$G4HOME/g4install/install`` | ``/usr/local/`` |
| ``GEANT4_BUILD_MULTITHREADED`` | ``ON`` | ``ON`` |
| ``GEANT4_INSTALL_DATA`` | ``ON`` | ``OFF`` |
| ``GEANT4_INSTALL_DATADIR`` | ``$G4HOME/g4install/data`` | |
| ``GEANT4_USE_OPENGL_X11``  | ``ON`` | ``OFF`` |
| ``GEANT4_USE_RAYTRACER_X11`` | ``ON`` | ``OFF`` |
| ``GEANT4_USE_SYSTEM_EXPAT`` | ``ON`` | ``OFF``|

### ``GEANT4_USE_QT``を有効にする

```console
$ brew install qt@5
```

可視化ツールはQt（キュート）を使うと便利です。
Homebrewを使ってQt5をあらかじめインストールしておきます。
（最新版はQt6なので``@5``を指定する必要があります）

``ccmake``の段階で``GEANT4_USE_QT``の値を``ON``にすると、生成時（``[g] Generate``）にエラーとなりました。
追加で設定可能になる``QT_DIR``を``/usr/local/opt/qt@5``に設定してもエラーが解消されませんでした。
なので、ここは``cmake``をたたいて有効にしました。

```console
$ cmake -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) ../geant4-v11.2.1/
```

この状態で``ccmake ../geant4-v11.2.1/``すると、Qt5に関するパス設定が追加されていました。

## ビルドする

```console
$ cd $G4HOME/g4install/build/
$ make -j8    # プロセッサの数を指定する
$ make install
```

``cmake``で``Makefile``を生成できたので、いよいよビルド（``make``）します。
複数のプロセッサを持ったCPUであれば、``-j``オプションを使うとビルド時間を大幅に短縮できます。

ビルドが終わったら``make install``して、``CMAKE_INSTALL_PREFIX``で指定したディレクトリにGeant4をコピーします。

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
