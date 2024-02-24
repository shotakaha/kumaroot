# ``GEANT4_USE_QT``を有効にする

```console
$ brew install qt@5
$ cmake -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) ../geant4-v11.2.1/
```

可視化ツールにはQt（キュート）を使うと便利なので``GEANT4_USE_QT``を有効にします。
ただし、前述した``ccmake``で有効にしてもmacOSではうまく設定ファイルを生成できませんでした。
なので、``cmake``コマンドにオプションをつけて実行しました。

Qt5はあらかじめインストールしておきます。
Homebrewでインストールできますが、最新版はQt6なので``@5``を指定しました。

```console
$ ccmake ../geant4-v11.2.1/
```

この段階で、あらためて``ccmake ../geant4-v11.2.1/``で確認すると、
Qt5に関するパス設定が追加されていました。
（あとでスクショを掲載する）

:::{note}

ここまでの設定は``cmake``を使うと1回で実行できます。
前ページのオプション設定とQtを有効にする場合は、次のように入力します

```console
$ cmake -DMAKE_INSTALL_PREFIX=$G4HOME/g4install/install -DGEANT4_INSTALL_DATA=ON -DGEANT4_INSTALL_DATADIR=$G4HOME/g4install/data -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) ../geant4-v11.2.1/
```

:::
