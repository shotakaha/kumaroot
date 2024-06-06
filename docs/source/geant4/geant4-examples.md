# 付属サンプルで遊べる（``examples``）

```console
$ mkdir ~/repos/sandbox/g4work/  # 作業ディレクトリを作成
$ cd ~/repos/sandbox/g4work/
(~/r/s/g4work/) $ cp ~/geant4/11.2.1/share/Geant4/examples .
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

Geant4付属のサンプルは、インストール先の``$CMAKE_INSTALL_PREFIX/shared/Geant4/examples``にあります。

それを作業用ディレクトリにコピーしています。
作業用ディレクトリの名前は任意ですが、慣例（？）で``g4work``としました。
``examples``ディレクトリの中を確認すると``basic``、``extended``、``advanced``に分類されていることがわかります。

Geant4のアプリケーションをゼロから作り始めるのはとても大変だと思います。
まず、``basic``にあるサンプルを動かすところからはじめて、自分の目的に近いサンプルを見つけ、改造していくのがよいと思います。

:::{note}

以前は初心者向けのサンプルは``novice``という名前でした。
Geant4 10.0で、``novice``が``basic``と``extended``にリファクタリングされたそうです。

:::
