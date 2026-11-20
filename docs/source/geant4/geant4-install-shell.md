# 環境変数したい（`geant4.sh`）

```console
// ステップ1：使うバージョンのインストール先を変数に入れる
$ export G4_INSTALLED=~/geant4/v11.X.Y/install

// ステップ2：設定スクリプトを読み込む
$ source $G4_INSTALLED/bin/geant4.sh
```

Geant4アプリを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（`$G4_INSTALLED/bin/`）の中に、設定スクリプト（`geant4.sh`）が用意されています。
これを読み込んでからアプリをコンパイルしてください。

## 設定を確認したい（`geant4-config`）

```console
$ geant4-config --version
11.X.Y

$ which geant4-config
~/geant4/v11.X.Y/install/bin/geant4-config
```

`geant4-config`は、Geant4の設定を確認できるコマンドです。
環境変数が正しく設定されていれば、パスが通っているはずです。

## zshしたい（`~/.zshrc`）

```console
// ステップ1：~/.zshrc に追記する（よく使うバージョンの例）
export G4_VERSION=v11.X.Y
export G4_INSTALLED=~/geant4/$G4_VERSION/install
source $G4_INSTALLED/bin/geant4.sh
```

Geant4アプリの開発が中心の場合は、よく使うバージョンを`~/.zshrc`に追記しておくと便利です。
`G4_VERSION`は、Geant4のバージョンを指定する変数です。
新しいバージョンをインストールしたときは、この変数を書き換えるだけでよいようにしておきます。

## fishしたい

:::{caution}

Geant4の設定スクリプト（`geant4.sh`）は、Fishに対応していません。

:::

```console
// ステップ1：Fishの中でZshを起動する
(fish) $ zsh

// ステップ2：設定を確認する
(zsh) $ geant4-config --version
11.4.3
```

Fishを常用している場合は、Geant4を使うときだけZshに切り替えてください。
`~/.zshrc`を設定しておけば、Zshを起動するだけでGeant4の環境変数が設定されます。
