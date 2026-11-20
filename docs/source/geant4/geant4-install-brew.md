# 外部ツールを準備する（`brew install`）

```console
// ダウンロードに必要なコマンド
$ brew install wget

// ビルドに必要なコマンド
$ brew install cmake
$ brew install ninja

// 描画に必要なツール
$ brew install --cask xquartz  # OpenGLを使う場合
$ brew install qt    # Qt6を使う場合
$ brew install qt@5  # Qt5を使う場合
```

Geant4のビルド／インストールに必要な外部ツールをあらかじめインストールしておきます。
すべてHomebrewでインストールできます。

Geant4は4.10から`cmake`を使ったビルドがデフォルトになりました。
また、さまざまな可視化ドライバに対応していますが、開発やメンテナンスが停滞しているドライバも多数あります。
ここ数年（2025年ころ）は、`Qt`と`OpenGL`の組み合わせがベストです。

## ダウンロードしたい（`wget`）

```console
$ brew install wget
```

[wget](../command/command-wget.md)は、HTTP/HTTPS/FTPなどのプロトコルでファイルをダウンロードするコマンドです。
Geant4のソースコード（圧縮ファイル）をダウンロードするために使います。

## ビルドしたい（`cmake` / `ninja`）

```console
$ brew install cmake
```

`cmake`はGeant4.10からデフォルトになったビルドツールです。
これまでの`./configure`の代替となる、クロスプラットフォーム対応のコマンドラインツールです。

```console
$ brew install ninja
```

`ninja`は`make`の代替となるビルドコマンドです。
モダンなツールが好きな場合は、こちらをインストールしてください。

:::{note}

`ninja`でも`make`でも、同じソースを、同じオプションでビルドした場合の結果（バイナリなど）は同じになります。
一般に`ninja`のほうが`make`より高速にビルドできるらしいです。

:::

## 描画したい（`xquartz` / `qt` / `qt@5`）

```console
$ brew install --cask xquartz  # OpenGLを使う場合
```

`xquartz`はmacOSでX11を使うためのツールです。
OpenGLを使う場合に必要です。

```console
$ brew install qt    # Qt6を使う場合
$ brew install qt@5  # Qt5を使う場合
```

Qtは、クロスプラットフォーム対応のGUIツールキットです。
Geant4の可視化ドライバとして、Qt5またはQt6を使うことができます。

:::{note}

Geant4のバージョンによって、デフォルトで使われるQtが異なります。

- Qt6：v11.4.0以降のデフォルトです。Qt5を使う場合は、`-DGEANT4_USE_QT_QT5=ON`を指定します。
- Qt5：v11.4.0より前のデフォルトです。Qt6を使う場合は、`-DGEANT4_USE_QT_QT6=ON`を指定します。

Qt6はv11.1.0からサポートされているようですが、v11.2.1ではQt6ではビルドに失敗しました。

:::

## 番外編 : WSL2を準備する

WindowsにGeant4をインストールする場合、WSL2環境を利用します。

:::{caution}

公式のインストールガイド（v11.4）では、WSLでのビルドと利用は公式にサポートされていません。
問題が起きた場合は、Geant4の公式フォーラム（Discourse）で相談できます。

:::

```console
$ apt install build-essential
$ brew install cmake
$ brew install qt@5
```

WSL2の場合、`build-essential`でgccなどをインストールします。
また、`cmake`と`qt@5`の追加インストールが必要です。
描画バックエンドにWaylandを使う場合は、X11系のドライバにXWaylandが必要です。
