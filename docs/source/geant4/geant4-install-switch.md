# バージョンを切り替えたい（`switch`）

```console
$ source ~/geant4/v11.3.2/install/bin/geant4.sh
$ geant4-config --version
11.3.2

$ source ~/geant4/v11.4.3/install/bin/geant4.sh
$ geant4-config --version
11.4.3
```

Geant4のバージョンを切り替えてアプリを作成することは多くないと思いますが、いちおう切り替え方を紹介します。
利用したいバージョンの設定スクリプトを読み込ませればOKです。

## プロジェクトで設定したい

```console
$ cmake -S app -B build -DGeant4_DIR=$HOME/geant4/v11.X.Y/install/lib/cmake/Geant4
```

`Geant4_DIR`は、Geant4のCMake設定ディレクトリを変更できるオプションです。
ビルドに使いたいバージョンの`lib/cmake/Geant4`を指定します。

:::{caution}

プロジェクトの`CMakeLists.txt`に`find_package(Geant4 REQUIRED)`が必要です。

:::

:::{note}

`-D`の値の中では`~`が展開されない場合があるため、`$HOME`を使っています。

:::
