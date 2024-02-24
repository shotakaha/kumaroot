# ビルドの下準備したい（``cmake`` / ``ccmake``）

```console
$ cd $C4HOME/g4install/build/
$ ccmake ../geant4-v11.2.1/
```

``cmake``（もしくは``ccmake``）を使って、ビルドに必要なファイルを作成します。
ビルド用ディレクトリから``CMakeLists.txt``があるソースコードに向けて``cmake``（もしくは``ccmake``）します。

僕は``ccmake``を使いました。
``ccmake``は``cmake``のGUI版みたいなもので、実行するとターミナルにオプションの操作プロンプトが表示されます。
オプションを変更する作業が視覚的に確認できるため、とても便利でした。
今回はひとまず以下の項目の設定しました。

| オプション名 | 設定値 | デフォルト値 |
|---|---|---|
| ``CMAKE_INSTALL_PREFIX`` | ``$G4HOME/g4install/install`` | ``/usr/local/`` |
| ``GEANT4_BUILD_MULTITHREADED`` | ``ON`` | ``ON`` |
| ``GEANT4_INSTALL_DATA`` | ``ON`` | ``OFF`` |
| ``GEANT4_INSTALL_DATADIR`` | ``$G4HOME/g4install/data`` | |
| ``GEANT4_USE_OPENGL_X11``  | ``ON`` | ``OFF`` |
| ``GEANT4_USE_RAYTRACER_X11`` | ``ON`` | ``OFF`` |
| ``GEANT4_USE_SYSTEM_EXPAT`` | ``ON`` | ``OFF``|

オプション設定が終わったら、``[g] Generate``を入力し、設定に必要なファイルを自動生成します。

:::{note}

Geant4.10からデフォルトのビルドツールが``cmake``になりました。
``cmake``には「out-of-source」というコンセプトがあり、
ソースコード本体とビルドしたファイルは別々のディレクトリで管理するしきたりがあるようです。
そのしきたりにしたがい、ここでの作業はすべて、事前に作成した``build``ディレクトリの中で実行します。

:::
