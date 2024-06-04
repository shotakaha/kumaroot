# 環境変数を設定する（``geant4.sh``）

```console
// CMAKE_INSTALL_PREFIX は設定したパスに変更
$ source $CMAKE_INSTALL_PREFIX/bin/geant4.sh

// 上記の設定でインストールした場合
$ source ~/geant4/bin/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（``$CMAKE_INSTALL_PREFIX/bin/``）の中に、設定スクリプト（``geant4.sh``）が用意されています。
これを読み込んでからアプリケーションをコンパイルしてください。
いつも使うような場合は、シェルの起動スクリプトに書いておくとよいです。

:::{caution}

残念ながらFish用の設定スクリプトはありません。

僕は、以下のようにGeant4を使う時だけZshに切り替えて作業することにしました。

```console
(fish) $ zsh
(zsh) $ source ~/geant4/bin/geant4.sh
(zsh) $ cd ~/repos/sandbox/g4work/examples/basic/B1/
(zsh) $ mkdir build
(zsh) $ cd build
(zsh) $ cmake ..
(zsh) $ make
(zsh) $ ./exampleB1
```

一度ビルドしたアプリケーションはFishでも起動できました。

:::
