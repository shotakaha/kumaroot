# CMakeListsしたい

```console
$ cd ~/geant4/v11.X.Y/

// ソースツリーの最上位にあるCMakeLists.txtを確認する
$ less source/CMakeLists.txt
```

Geant4本体のビルドは、ソースに指定したディレクトリにある`CMakeLists.txt`を起点に進みます。
どのような順番でビルドが進むのかを、辿ってみることにします。

:::{note}

ビルド時にこの`CMakeLists.txt`をユーザーが編集する必要はありません。
内容を確認するときも、不用意に編集することがないように注意してください。

:::

## ビルドの流れをたどりたい

Geant4のビルドは、次の順番で`CMakeLists.txt`や`.cmake`ファイルをたどります。

```text
source/CMakeLists.txt                      # 最上位（50行程度と短い）
  └─ include(G4CMakeMain)
       └─ cmake/Modules/G4CMakeMain.cmake  # 全体の流れを決める
            ├─ 設定・オプションの読み込み
            ├─ 依存パッケージ（CLHEP、Qt、OpenGLなど）の検索
            ├─ データセットの確認・ダウンロード
            ├─ add_subdirectory(source)      # ここからライブラリを作る
            │    └─ source/source/CMakeLists.txt
            │         └─ カテゴリごとのCMakeLists.txt
            │              └─ sources.cmake（ソースファイルの一覧）
            └─ インストール用ファイルの生成（Geant4Config.cmakeなど）
```

最上位の`CMakeLists.txt`は短く、中身の多くを`cmake/Modules/`の中のファイルに任せています。
そのため、読むべき場所は`G4CMakeMain.cmake`から順にたどるのが分かりやすいです。

:::{note}

`source/`の下にさらに`source/`があります。
最上位の`source/CMakeLists.txt`は、`source/source/`の中にあるカテゴリ（`geometry`、`processes`など）を順番に読み込みます。
ディレクトリ名が同じで混乱しやすいので注意してください。

:::

## 実行ログしたい

```console
$ cmake -G Ninja -S source -B build
-- The CXX compiler identification is AppleClang ...
-- Looking for ... (依存パッケージの検索)
-- Enabled features: ... (有効になった機能の一覧)
-- Configuring done
-- Generating done
```

`cmake`を実行すると、上のような実行ログが表示されます。
大量に表示されるため、基本的に流し読みして構いません。
ビルドが途中で失敗したときに、どの段階まで進んでいたのかを確認するのに役立ちます。

- `Looking for ...`: 依存パッケージを探している段階
- `Enabled features`: オプションの設定結果をまとめた一覧
- `Configuring done`: 設定が完了した段階
- `Generating done`: ビルド用のファイルが生成された段階

`Configuring done`の後で`Generating done`が表示されていれば、ビルド用のファイルが生成されているはずです。
ビルド用のファイルはジェネレーターによって異なります。
`-G Ninja`を指定した場合は、`build.ninja`が生成されます。
`-G "Unix Makefiles"`を指定した場合は、`Makefile`が生成されます。

## オプション定義を調べたい（`cmake/Modules`）

```console
$ cd ~/geant4/v11.X.Y/source

// オプション名で検索
$ grep -rn "option(GEANT4_USE_QT" cmake/Modules
cmake/Modules/G4InterfaceOptions.cmake:62:option(GEANT4_USE_QT "Build Geant4 with Qt support" OFF)
cmake/Modules/G4InterfaceOptions.cmake:71:cmake_dependent_option(GEANT4_USE_QT_QT5 "Require Qt5 when building Qt support" OFF "GEANT4_USE_QT" OFF)

$ rg -F "option(GEANT4_USE_QT" cmake/Modules/
cmake/Modules/G4InterfaceOptions.cmake
62:option(GEANT4_USE_QT "Build Geant4 with Qt support" OFF)
71:cmake_dependent_option(GEANT4_USE_QT_QT5 "Require Qt5 when building Qt support" OFF "GEANT4_USE_QT" OFF)
```

オプションなどの設定は、`cmake/Modules/`の中の`.cmake`ファイルにまとめられています。
`grep`や`rg`などの検索コマンドで、オプション名を検索すれば、どのファイルでどのように定義されているかを確認できます。

:::{hint}

`GEANT4_USE_QT`だけで検索すると、多くの箇所がヒットしてしまいます。
`option(GEANT4_USE_QT`のように検索文字列を工夫するか、`peco`などにパイプして絞り込み検索するとよいです。

:::

:::{caution}

`rg`（ripgrep）はデフォルトで検索文字列を正規表現として認識します。
`option(GEANT4_USE_QT`のように括弧を含む文字列は、エスケープ処理するか、`-F`（`--fixed-strings`）オプションを付けて検索してください。

```console
$ rg "option(GEANT4_USE_QT" cmake/Modules/
rg: regex parse error:
    (?:option(GEANT4_USE_QT)
    ^
error: unclosed group

$ rg "option\(GEANT4_USE_QT" cmake/Modules/
cmake/Modules/G4InterfaceOptions.cmake
62:option(GEANT4_USE_QT "Build Geant4 with Qt support" OFF)
71:cmake_dependent_option(GEANT4_USE_QT_QT5 "Require Qt5 when building Qt support" OFF "GEANT4_USE_QT" OFF)

$ rg -F "option(GEANT4_USE_QT" cmake/Modules/
cmake/Modules/G4InterfaceOptions.cmake
62:option(GEANT4_USE_QT "Build Geant4 with Qt support" OFF)
71:cmake_dependent_option(GEANT4_USE_QT_QT5 "Require Qt5 when building Qt support" OFF "GEANT4_USE_QT" OFF)
```

:::


## エラーの原因を探したい

ビルドが失敗したときは、エラーメッセージの文言で`grep`すると、関係するファイルを見つけやすいです。

```console
$ cd ~/geant4/v11.X.Y/source
// エラーメッセージの一部でCMakeのファイルを探す
$ grep -rn "FATAL_ERROR" cmake/Modules | grep -i "qt"
```

詳しい情報は、`build`ディレクトリに残っているログで確認できます。

```console
$ less ~/geant4/v11.X.Y/build/CMakeFiles/CMakeConfigureLog.yaml
$ less ~/geant4/v11.X.Y/build/CMakeCache.txt
```

`CMakeCache.txt`では、オプションが意図した値になっているかを確認できます。
`cmake`を再実行しても直らないときは、`build`ディレクトリを消してから、もう一度`cmake`を実行してください。

:::{seealso}

- [](geant4-install-configure)
- [](geant4-install-configure-options)
- [](geant4-install-build)

:::

## リファレンス

- [Geant4 Installation Guide（公式）](https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/)
- [CMake公式ドキュメント](https://cmake.org/cmake/help/latest/)
