# 付属サンプルの遊び方（``examples``）

```console
// 作業ディレクトリを作成して移動する
$ mkdir ~/repos/sandbox/g4work/
$ cd ~/repos/sandbox/g4work/

// Geant4のサンプルをコピーする
(~/r/s/g4work/) $ cp ~/geant4/11.2.1/share/Geant4/examples .

// サンプルの中身を確認する
(~/r/s/g4work/) $ ls -1 examples
CMakeLists.txt
GNUmakefile
History
README
README.HowToRun
README.HowToRunMT
advanced/     // advancedサンプル
basic/        // basicサンプル
extended/     // extendedサンプル
novice
```

Geant4付属のサンプルは、インストール先の`$CMAKE_INSTALL_PREFIX/shared/Geant4/examples`にあります。

それを作業用ディレクトリにコピーしてから編集します。
作業用ディレクトリの名前は任意ですが、慣例（？）で`g4work`としました。
コピーした`examples`ディレクトリの中を確認すると
`basic`、
`extended`、
`advanced`
に分類されていることがわかります。

:::{note}

以前は初級者向けのサンプルは`novice`という名前でした。
Geant4 10.0で、`novice`が`basic`と`extended`に
リファクタリングされたそうです。

:::

`basic`は初級者向けでGeant4の基本要素が学べるようになっています。
まずは`basic`に含まれるサンプルを実際にビルドして、動かすところからはじめるのがよいです。

`extended`は中級者向けで、特定分野における使い方を示したサンプルとなっています。
`advanced`は上級者向けで、実際の導入例に近い、より完成度の高いサンプルとなっています。
シミュレーションの目的が明確な場合は、
これらのサンプルの中から目的に近いものを選び、改造していくのが効率的です。

どのサンプルも`out-of-source`ビルドを前提としており、
CMakeを使って共通の手順でビルドできるようになっています。
