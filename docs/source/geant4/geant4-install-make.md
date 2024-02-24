# ビルドする（``make`` / ``make install``）

```console
$ cd $G4HOME/g4install/build/
$ make -j8    # プロセッサの数を指定する
$ make install
```

ビルド用ディレクトリで``make``コマンドを実行します。
複数のプロセッサを持ったCPUを使っている場合は、``-j 利用するプロセッサー数``オプションを使いましょう。

``GEANT4_INSTALL_DATA=ON``にしたので、Geant4用データのダウンロードからはじました。
ネットワーク環境に接続した状態で行うとよいと思います。

ビルドが終わったら``make install``コマンドを実行します。
``CMAKE_INSTALL_PREFIX``で指定したディレクトリにGeant4がインストール（コピー）されます。

:::{note}

デフォルトで``CMAKE_INSTALL_PREFIX=/usr/local/``になっています。
この場合は、管理者パスワードの入力が必要かもしれません。

:::

## ディレクトリ構成

```console
$ ls -1 $G4HOME/g4install/build/
```

```console
$ ls -1 $G4HOME/g4install/install/
bin/
include/
lib/
share/
```

```console
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
