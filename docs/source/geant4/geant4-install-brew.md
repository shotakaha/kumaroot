# 外部ツールを準備する（``brew install``）

```console
$ brew install --cask cmake
$ brew install --cask xquartz
$ brew install qt@5
```

Geant4のビルドに必要な外部ツールをあらかじめインストールしておきます。

Geant4.10からデフォルトのビルドツールが``cmake``になったので、``cmake``は必須です。
可視化ツールにOpenGLとQtを利用したいので、XQuartzとQt5を追加しています。

その他、使うことが分かっているツールがあれば、あらかじめインストールしておくとよいです。
インストールできたら、次に進んでください。
