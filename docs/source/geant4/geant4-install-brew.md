# 外部ツールを準備する（`brew install`）

Geant4のビルドに必要な外部ツールをインストールします。
その他、使うことが分かっているツールがあれば、あらかじめインストールしておくとよいです。
インストールできたら、次に進んでください。

## ビルドツール（`cmake` / `ninja`）

```console
$ brew install cmake
```

Geant4.10からデフォルトのビルドツールが`cmake`になりました。

```console
$ brew install ninja
```

`ninja`は`make`に代わるビルドコマンドです。
モダンなツールが好きな場合は、インストールしてください。

:::{note}

一般に`ninja`のほうが`make`より高速にビルドできるらしいです。
同じソースを、同じオプションでビルドした場合、ビルド結果は同じになります。

:::

## 描画ツール（`qt@5` / `xquartz`）

```console
$ brew install qt@5
$ brew install --cask xquartz
```

Geant4のシミュレーション結果を可視化するためにOpenGLとQtを利用します。
X11（XQuartz）はOpenGL、Qt5はQtの利用に必要です。

## 番外編 : WSL2を準備する

WindowsにGeant4をインストールする場合、WSL2環境を利用します。

```console
$ apt install build-essential
$ brew install cmake
$ brew install qt@5
```

WSL2の場合、`build-essential`でgccなどをインストールします。
また、`cmake`と`qt@5`の追加インストールが必要です。
描画バックエンドは`Wayland`に対応しているため、X11（XQuartz）の追加インストールは不要です。
