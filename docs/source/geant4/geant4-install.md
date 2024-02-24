# インストールしたい（``geant4``）

```console
$ mkdir ~/repos/g4home  # --> $G4HOME
```

Geant4は自分でコンパイルしてインストールする必要があります。
講習会のインストール手順を参考にすると、作業用のディレクトリを作成したほうがよいそうです。
その方式に倣って僕は``~/repos/g4home/``を作成しました。

ディレクトリ名は任意なので、このページでは、このディレクトリを便宜上``$G4HOME``と呼ぶことにします
（環境変数を設定したわけではありません）。
各人がインストールする環境に合わせて、適宜置き換えて実行してください。

インストール手順のステップがいくつかあるので、それぞれ分割して整理しました。
各ステップを確認しながら順番に作業してください。

```{toctree}
---
maxdepth: 1
---
geant4-install-mkdir
geant4-install-download
geant4-install-ccmake
geant4-install-qt
geant4-install-make
```

## 環境変数を設定する

```console
$ source $G4HOME/g4install/install/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（``$G4HOME/g4install/install``）の中に、設定スクリプト（``bin/geant4.sh``）が用意されています。
これを読み込んでからアプリケーションをコンパイルしてください。

いつも使うような場合は、シェルの起動スクリプトに書いておくとよいです。

:::{note}

BashとCsh用の設定スクリプトが用意されています。
Fish用の設定スクリプトが欲しい。

:::
