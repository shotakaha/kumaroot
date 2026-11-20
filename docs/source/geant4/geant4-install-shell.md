# 環境変数したい（`geant4.sh`）

```console
// 使うバージョンのインストール先を変数に入れる
$ export G4_INSTALLED=~/geant4/v11.X.Y/install

// 設定スクリプトを読み込む
$ source $G4_INSTALLED/bin/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（`$G4_INSTALLED/bin/`）の中に、設定スクリプト（`geant4.sh`）が用意されています。
これを読み込んでからアプリケーションをコンパイルしてください。

よく使うバージョンは、`~/.zshrc`で読み込めるようにしておくと便利です。
バージョンを`G4_VERSION`に入れておくと、切り替えるときは、この1行を書き換えるだけで済みます。

```console
// ~/.zshrc に追記する（よく使うバージョンの例）
export G4_VERSION=v11.X.Y
export G4_INSTALLED=~/geant4/$G4_VERSION/install
source $G4_INSTALLED/bin/geant4.sh
```

別のバージョンを使いたいときは、`G4_VERSION`を書き換えて、新しいシェルを開きます。
または、そのシェルで`export`と`source`をやり直します。

## 設定を確認したい（`geant4-config`）

`$G4_INSTALLED/bin/`にインストールされる`geant4-config`で、Geant4の設定を確認できます。

```console
// ステップ1：インストール先のgeant4-configを直接指定する
$ $G4_INSTALLED/bin/geant4-config --version
11.4.3

// ステップ2：設定を読み込んだ後は、コマンド名だけで実行できる
$ source $G4_INSTALLED/bin/geant4.sh
$ geant4-config --version
11.4.3
```

## Fishしたい

:::{caution}

Geant4の設定スクリプト（`geant4.sh`）は、Fishに対応していません。

:::

Fishで作業している場合は、Geant4を使うときだけZshに切り替えてから読み込みます。

```console
// ステップ1：Fishの中でZshを起動する
(fish) $ zsh

// ステップ2：使うバージョンのインストール先を変数に入れる
(zsh) $ export G4_INSTALLED=~/geant4/v11.X.Y/install

// ステップ3：設定スクリプトを読み込む
(zsh) $ source $G4_INSTALLED/bin/geant4.sh

// ステップ4：設定を確認する
(zsh) $ geant4-config --version
11.4.3
```

:::{note}

別のバージョンに切り替えるときは、新しいシェルを開いてから`export`と`source`をやり直してください。

:::
