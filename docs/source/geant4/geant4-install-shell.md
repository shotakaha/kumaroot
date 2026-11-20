# 環境変数したい（`geant4.sh`）

```console
// 使うバージョンのインストール先を変数に入れる（v11.4.3の例）
$ export G4_INSTALLED=~/geant4/v11.4.3/install

// 設定スクリプトを読み込む
$ source $G4_INSTALLED/bin/geant4.sh
```

Geant4のアプリケーションを作るには、Geant4に関する環境変数の設定が必要です。
インストール先（`$G4_INSTALLED/bin/`）の中に、設定スクリプト（`geant4.sh`）が用意されています。
これを読み込んでからアプリケーションをコンパイルしてください。

複数のバージョンを共存させています。
そのため、`~/.zshrc`などの起動スクリプトには書かないでください。
使うバージョンを決めてから、そのシェルで読み込みます。

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

残念ながらFish用の設定スクリプトはありません。

:::

Fishで作業している場合は、Geant4を使うときだけZshに切り替えてから読み込みます。

```console
// ステップ1：Fishの中でZshを起動する
(fish) $ zsh

// ステップ2：使うバージョンのインストール先を変数に入れる
(zsh) $ export G4_INSTALLED=~/geant4/v11.4.3/install

// ステップ3：設定スクリプトを読み込む
(zsh) $ source $G4_INSTALLED/bin/geant4.sh

// ステップ4：設定を確認する
(zsh) $ geant4-config --version
11.4.3
```

:::{note}

別のバージョンに切り替えるときは、新しいシェルを開いてから`export`と`source`をやり直してください。

:::
