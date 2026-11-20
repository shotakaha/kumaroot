# アプリごとにバージョンを切り替えたい（`switch`）

複数のバージョンをインストールしていても、どれか1つを全体の設定にはしません。
アプリごとに、使うバージョンを指定します。

## CMakeで指定したい（`Geant4_DIR`）

アプリのビルド時に、使うバージョンを`Geant4_DIR`で指定する方法です。
環境変数を汚さず、アプリのビルド設定にバージョンが残るため、おすすめです。

```console
// ステップ1：使うバージョンのインストール先を変数に入れる
$ export G4_INSTALLED=~/geant4/v11.X.Y/install

// ステップ2：アプリのビルド時に、CMake設定ディレクトリを指定する
$ cmake -S . -B build -DGeant4_DIR=$G4_INSTALLED/lib/cmake/Geant4
```

アプリの`CMakeLists.txt`には、`find_package(Geant4 REQUIRED)`を書いてください。
`find_package`は、`Geant4_DIR`で指定されたバージョンを見つけます。

:::{note}

`lib/cmake/Geant4`が見つからない場合は、`ls $G4_INSTALLED`で`install`の中身を確認してください。

:::

## direnvで自動的に切り替えたい

アプリのディレクトリに入ったときだけ、設定を自動で読み込む方法です。
Fishでも使えます。

```console
// ステップ1：direnvをインストールする
$ brew install direnv

// ステップ2：アプリのディレクトリに設定ファイルを作る
$ cd ~/repos/my-geant4-app/
$ echo 'source ~/geant4/v11.X.Y/install/bin/geant4.sh' > .envrc

// ステップ3：設定ファイルを許可する
$ direnv allow
```

:::{note}

`direnv`をシェルで使うための初期設定は、`direnv`の公式ドキュメントに従ってください。
別のバージョンを使うアプリでは、そのアプリのディレクトリに別の`.envrc`を置きます。

:::

## 手動で切り替えたい

シェルで直接読み込む方法です。
詳しくは[](geant4-install-shell)を参照してください。

```console
$ export G4_INSTALLED=~/geant4/v11.X.Y/install
$ source $G4_INSTALLED/bin/geant4.sh
```

:::{note}

別のバージョンに切り替えるときは、新しいシェルを開いてから読み込んでください。

:::
