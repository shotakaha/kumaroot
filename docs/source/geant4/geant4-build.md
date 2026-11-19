# ビルドしたい（`cmake`）

ここでは、自分で作ったGeant4アプリケーション（シミュレーションコード）を`cmake`でビルドして実行する、汎用的な手順をまとめます。
Geant4本体のビルドは[インストール](geant4-install)のページを参照してください。

## 前提

- Geant4がインストール済みで、環境変数を読み込んであること（[環境変数したい](geant4-install-shell)）
- エラーが出た場合は[エラー対処](geant4-errors)を参照

```console
// Geant4アプリのプロジェクトルートを環境変数に設定する（パスは自分の環境に合わせる）
$ export G4PROJECT=~/repos/my-geant4-app

// Geant4の環境変数を読み込む（インストール先に合わせる）
$ source ~/geant4/v11.4.0/install/bin/geant4.sh
```

## プロジェクトの構造

このページでは、次の構造のプロジェクトを前提とします。

```console
$ cd $G4PROJECT
$ ls -1
app/            # ソースコードとCMakeLists.txt
README.md
...

$ ls -1 app
CMakeLists.txt       # ビルドの設定
myGeant4App.cc       # main関数
include/             # ヘッダーファイル（*.hh）
src/                 # ソースファイル（*.cc）
run1.mac             # マクロファイル（*.mac）
vis.mac
init_vis.mac
```

`CMakeLists.txt`の書き方は、後の「CMakeLists.txtしたい」の節で説明します。

## ビルドしたい

`cmake`の作法（out-of-source）にしたがい、ビルド用ディレクトリ（`build/`）でビルドします。

```console
// ビルドの設定を生成する
(G4PROJECT) $ cmake -S app -B build -DCMAKE_INSTALL_PREFIX=$G4PROJECT

// ビルドする
(G4PROJECT) $ cmake --build build --parallel

// インストールする
(G4PROJECT) $ cmake --install build
```

- `-S app`：`CMakeLists.txt`の場所を指定します。
- `-B build`：ビルド用ディレクトリを指定します。ビルドに必要なファイルはここに生成されます。
- `-DCMAKE_INSTALL_PREFIX=$G4PROJECT`：インストール先のルートを指定します。実行ファイルは`$G4PROJECT/bin/`に入ります。
- `--parallel`：並列にビルドします。

インストール先がプロジェクト内なので、システム全体への書き込み権限は不要です。

:::{note}

`file(GLOB ...)`でソースを集めているため、`src/`に新しい`.cc`ファイルを追加したときは、
`cmake -S app -B build`をもう一度実行してください。

:::

## 実行したい

```console
// 対話モード（引数なし）
(build) $ ./myGeant4App

// バッチモード（マクロを引数に指定）
(build) $ ./myGeant4App run1.mac
```

実行方法（対話モードかバッチモードか）は、`main()`関数で決まります。
引数がなければ対話モード、引数があればそれをマクロとして実行する、という実装にすると、上のように使い分けられます。

### マクロの場所

マクロファイルは、**実行するときのカレントディレクトリ**から相対パスで探されます。
そのため、マクロがあるディレクトリで実行するのが確実です。

- バッチモードの`run1.mac`は、カレントディレクトリに無いとエラーになります。
- 対話モードで`init_vis.mac`を読み込む構成にした場合は、そのファイルもカレントディレクトリに必要です。

:::{note}

`cmake --install`を実行すると`bin/`には実行ファイルだけが入り、マクロは入りません。
そのため、`bin/`から実行すると、マクロが見つからず起動に失敗します。
マクロがあるディレクトリで実行してください。

:::

:::{note}

マクロが見つからなかったときのエラーは表示されますが、プログラムの終了コードは`0`のままでした。
スクリプトでエラーを検出したい場合は、出力も確認してください。

:::

## CMakeLists.txtしたい

ここでは、最小構成の各部分の役割を確認します。
自分のアプリで必要な部分だけ残してください。

### 最小構成

まず、最低限必要な部分は次の4つです。

```cmake
cmake_minimum_required(VERSION 3.16...3.27)
project(myGeant4App)

find_package(Geant4 REQUIRED ui_all vis_all)

file(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.cc)
file(GLOB headers ${PROJECT_SOURCE_DIR}/include/*.hh)

add_executable(myGeant4App myGeant4App.cc ${sources} ${headers})
target_include_directories(myGeant4App PRIVATE include)
target_link_libraries(myGeant4App PRIVATE ${Geant4_LIBRARIES})

install(TARGETS myGeant4App DESTINATION bin)
```

:::{note}

`myGeant4App`は、自分のアプリの名前に置き換えてください。
`myGeant4App.cc`は、`main()`関数があるファイルの名前です。
プロジェクト名、ファイル名、実行ファイル名は同じにしておくと分かりやすいです。

:::

### 各部分の説明

**プロジェクト全体の設定**

```cmake
cmake_minimum_required(VERSION 3.16...3.27)
project(myGeant4App)
```

`cmake_minimum_required`は、必要なCMakeの最低バージョンを指定します。
`3.16...3.27`は「最低3.16で、3.27までのCMakeの新しい動作を使ってよい」という意味で、上限を超えるとエラーになるわけではありません。

**Geant4の検索**

```cmake
find_package(Geant4 REQUIRED ui_all vis_all)
```

Geant4の設定を取得します。
`ui_all`と`vis_all`は、対話モードと可視化を有効にするオプションです。
バッチモードだけで十分な場合は、`find_package(Geant4 REQUIRED)`にできます。

**ソースとヘッダーの取得**

```cmake
file(GLOB sources ${PROJECT_SOURCE_DIR}/src/*.cc)
file(GLOB headers ${PROJECT_SOURCE_DIR}/include/*.hh)
```

`src/`と`include/`にあるファイルを一覧にします。
ヘッダーを含めているのは、IDEで表示させるためです。
新しいファイルを追加したときは、`cmake`を再実行してください。

**実行ファイルの作成**

```cmake
add_executable(myGeant4App myGeant4App.cc ${sources} ${headers})
target_include_directories(myGeant4App PRIVATE include)
target_link_libraries(myGeant4App PRIVATE ${Geant4_LIBRARIES})
```

- `add_executable`：実行ファイルに含めるソースを指定します。
- `target_include_directories`：`include/`をヘッダーの検索パスに追加します。
- `target_link_libraries`：Geant4のライブラリをリンクします。

Geant4以外の外部ライブラリを使う場合は、`target_link_libraries`に追加してください。

**インストール**

```cmake
install(TARGETS myGeant4App DESTINATION bin)
```

実行ファイルを`${CMAKE_INSTALL_PREFIX}/bin/`にインストールします。
`-DCMAKE_INSTALL_PREFIX=$G4PROJECT`を指定しているので、`$G4PROJECT/bin/myGeant4App`になります。

:::{note}

マクロファイルは、この設定ではインストールされません（[マクロの場所](#マクロの場所)を参照）。

:::

## 関連ページ

- [付属サンプルの遊び方（`examples`）](geant4-examples)：Geant4付属のサンプルをコピーして始める
- [CMake Toolsしたい](geant4-cmake-tools)：VS Codeでの設定
- [エラー対処](geant4-errors)：ビルド時のエラー
