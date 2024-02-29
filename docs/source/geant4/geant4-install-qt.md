# ビルドの準備する（``cmake``）

```console
$ cd ~/repost/g4home/g4install/build
$ cmake -DMAKE_INSTALL_PREFIX=$G4HOME/g4install/install -DGEANT4_INSTALL_DATA=ON -DGEANT4_INSTALL_DATADIR=$G4HOME/g4install/data -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_USE_QT=ON -DCMAKE_PREFIX_PATH=$(brew --prefix qt@5) ../geant4-v11.2.1/
```

``ccmake``を使うと視覚的にオプションを設定できました。
しかし、設定項目に最初からでてこないオプションがあったりして、痒いところに手が届かない感じがありました。
そのようなときは、やはりコマンドラインを直接叩くのが有効です。

ディレクトリ構成は前ページと同じになっているはずです。
このようなディレクトリ構成になっていたら、次に進んでください。
