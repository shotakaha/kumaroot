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
