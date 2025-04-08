# 外部ツールを準備する（``brew install``）

Geant4のビルドに必要な外部ツールは、あらかじめインストールが必要です。

Geant4.10からデフォルトのビルドツールが`cmake`になったので、`cmake`は必須です。
可視化ツールにOpenGLとQtを利用したいので、X11（XQuartz）とQt5を追加しています。

その他、使うことが分かっているツールがあれば、あらかじめインストールしておくとよいです。
インストールできたら、次に進んでください。

## macOSの場合

```console
$ brew install --cask cmake
$ brew install --cask xquartz
$ brew install qt@5
```

macOSの場合`cmake`のCaskをインストールします。
また、X11が必要なので`XQuartz`をインストールします。

## WSL2を準備する

```console
$ brew install cmake
$ brew install qt@5
```

WSL2の場合、`cmake`と`qt@5`の追加インストールが必要です。
描画バックエンドは`Wayland`に対応しているため、
X11（XQuartz）の追加インストールは不要です。
