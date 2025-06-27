# 外部ツールを準備する（`brew install`）

```console
// ビルド用ツール
$ brew install cmake
$ brew install ninja

// 描画用ツール
$ brew install qt@5
$ brew install --cask xquartz
```

Geant4のビルドに必要な外部ツールとして
`CMake`、
`Xquartz`、
`Qt`、
`Nijna`（オプション）をインストールします。

その他、使うことが分かっているツールがあれば、あらかじめインストールしておくとよいです。
インストールできたら、次に進んでください。

## ビルドツール（`cmake` / `ninja`）

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

`ninja`でも`make`でも、
同じソースを、同じオプションでビルドした場合の結果（バイナリなど）は同じになります。
一般に`ninja`のほうが`make`より高速にビルドできるらしいです。

:::

## 描画ツール（`qt@5` / `xquartz`）

```console
$ brew install qt@5
$ brew install --cask xquartz
```

`Qt`と`OpenGL`の組み合わせでGeant4のシミュレーション結果を可視化できます。
X11（XQuartz）はOpenGL、Qt5はQtの利用に必要です。

:::{note}

`brew install qt`ではQt6がインストールされます。
v11.1以降ではQt6がサポートされたようですが、うまくビルドできませんでした。
Qt5に対するサポートもまだ残っているので、当面は`brew install qt@5`でQt5を指定するのがよさそうです。

:::

:::{note}

Geant4はさまざまな可視化ドライバに対応していますが、
開発やメンテナンスが停滞しているドライバも多数あります。
ここ数年（2025年）は、`Qt`と`OpenGL`の組み合わせがベストです。

:::

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
