# ビルドしたい（`cmake`）

```console
// 環境を準備する
$ export G4PROJECT=~/repos/my-geant4-app
$ source ~/geant4/v11.4.0/install/bin/geant4.sh

// ビルドする
$ cd $G4PROJECT
$ cmake -S app -B build -DCMAKE_INSTALL_PREFIX=$G4PROJECT
$ cmake --build build --parallel
$ cmake --install build

// 実行する（マクロがある app/ で実行する）
$ cd app
$ $G4PROJECT/bin/myGeant4App             # 対話モード
$ $G4PROJECT/bin/myGeant4App run1.mac    # バッチモード
```

自分で作ったGeant4アプリを`cmake`でビルドして実行する汎用的な手順です。
Geant4本体のビルドは[インストール](geant4-install)のページを参照してください。
ビルドでエラーが出た場合は、[エラー対処](geant4-errors)を参照してください。

## 前提：環境変数

- Geant4がインストール済みで、環境変数を読み込んであること（[環境変数したい](geant4-install-shell)）
- `$G4PROJECT`は、Geant4アプリのプロジェクトルートです（パスは自分の環境に合わせてください）
- `geant4.sh`のパスは、Geant4のインストール先に合わせてください

## 前提：アプリの構造

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

ここで紹介する手順は、Geant4アプリが上の構造になっていることを前提とします。
`CMakeLists.txt`の書き方は、後の「CMakeLists.txtしたい」の節で説明します。

## ビルドしたい

```console
$ cd $G4PROJECT

// ビルドの設定を生成する
$ cmake -S app -B build -DCMAKE_INSTALL_PREFIX=$G4PROJECT

// ビルドする
$ cmake --build build --parallel

// インストールする
$ cmake --install build
```

`cmake`の作法（out-of-source）にしたがい、ビルド用ディレクトリ（`build/`）でビルドします。

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
// マクロがある app/ に移動する
$ cd $G4PROJECT/app

// 対話モード（引数なし）
$ $G4PROJECT/bin/myGeant4App

// バッチモード（マクロを引数に指定）
$ $G4PROJECT/bin/myGeant4App run1.mac
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
そのため、`bin/`や`build/`などマクロが無いディレクトリで実行すると、マクロが見つからず起動に失敗します。

:::

:::{note}

マクロが見つからなかったときのエラーは表示されますが、プログラムの終了コードは`0`のままでした。
スクリプトでエラーを検出したい場合は、出力も確認してください。

:::

## CMakeLists.txtしたい

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

`app/CMakeLists.txt`の最小構成です。
`myGeant4App`は、自分のアプリの名前に置き換えてください。
プロジェクト名、`main()`関数があるファイル名、実行ファイル名は同じにしておくと分かりやすいです。

### 各行の説明

- `cmake_minimum_required`：必要なCMakeの最低バージョンを指定します。
  `3.16...3.27`は「最低3.16で、3.27までのCMakeの新しい動作を使ってよい」という意味で、上限を超えるとエラーになるわけではありません。
- `project`：プロジェクト名を指定します。
- `find_package(Geant4 REQUIRED ui_all vis_all)`：Geant4の設定を取得します。
  `ui_all`と`vis_all`は、対話モードと可視化を有効にするオプションです。
  バッチモードだけで十分な場合は、`find_package(Geant4 REQUIRED)`にできます。
- `file(GLOB ...)`：`src/`と`include/`にあるファイルを一覧にします。
  ヘッダーを含めているのは、IDEで表示させるためです。
- `add_executable`：実行ファイルに含めるソースを指定します。
- `target_include_directories`：`include/`をヘッダーの検索パスに追加します。
- `target_link_libraries`：Geant4のライブラリをリンクします。
  Geant4以外の外部ライブラリを使う場合は、ここに追加します。
- `install(TARGETS ...)`：実行ファイルを`${CMAKE_INSTALL_PREFIX}/bin/`にインストールします。
  `-DCMAKE_INSTALL_PREFIX=$G4PROJECT`を指定しているので、`$G4PROJECT/bin/myGeant4App`になります。
  マクロファイルはインストールされません（[マクロの場所](#マクロの場所)を参照）。

## 関連ページ

- [付属サンプルの遊び方（`examples`）](geant4-examples)：Geant4付属のサンプルをコピーして始める
- [CMake Toolsしたい](geant4-cmake-tools)：VS Codeでの設定
- [エラー対処](geant4-errors)：ビルド時のエラー
