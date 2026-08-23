# パッケージ管理したい（`port`）

```console
$ port search パッケージ名
$ port variants パッケージ名
$ port install パッケージ名
$ port uninstall パッケージ名
```

`port`は、MacPortsを使ってパッケージ管理するコマンドです。
Unix系のツールやライブラリ環境をmacOS上に構築できます。
`variants`を変更することで、ツールごとの微調整が可能です。

:::{note}

このページは、僕の歴史的なメモとして残しています。
大学院生だった2009年から2014年ころまではMacPortsを使ってパッケージ管理していました。
その後、新しくmacを買い替えた際にHomebrewに完全移行したため、現在は利用していません。

:::

:::{note}

MacPortsは、2009年にHomebrewが登場するまで、macOS向けのパッケージ管理ツールの定番のひとつとして広く使われていました。

2002年にDarwinPortsという名前で始まったプロジェクトで、2005年にバージョン1.0がリリースされ、
2006年に現在の名前（MacPorts）になりました。

現在も開発が継続しており、2025年10月にはバージョン2.11.6、2026年にも2.12系がリリースされています（[MacPorts公式サイト](https://www.macports.org/)）。
最新のmacOS（Tahoe）にも対応しており、Apple SiliconとIntelの両方で使えます。

:::

## インストールしたい（MacPorts）

[MacPorts公式サイトのインストール手順](https://www.macports.org/install.php)にしたがって、MacPortsをインストールしてください。

## パッケージをインストールしたい（`port install`）

```console
$ sudo port install パッケージ名
```

`port install`で、指定したパッケージをインストールできます。
パッケージに必要な依存関係も自動的にインストールされます。

:::{note}

MacPortsは、ソースコードからビルドするため、インストールに時間がかかることがありました。
最近では、ビルド済みのバイナリを優先的に探すようになっており、インストールにかかる時間は短縮されています。

:::

:::{note}

バイナリが用意されていないパッケージや、`variants`をカスタム指定した場合などは、その場でソースコードからビルドされるため、インストールに時間がかかることがあります。

:::

## バリアントを確認したい（`port variants`）

```console
$ port variants パッケージ名
```

`port variants`で、指定したパッケージで選択できるバリアント（オプション機能）を確認できます。
バリアントは、標準では有効になっていない追加機能を有効にしたり、逆に標準の機能を無効にしたりするためのオプションです。

```console
// バリアントを有効にする
$ sudo port install パッケージ名 +バリアント名

// バリアントを無効にする
$ sudo port install パッケージ名 -バリアント名
```

`+バリアント名`でバリアントを有効にしてインストールでき、`-バリアント名`で標準では有効なバリアントを無効にできます。

:::{note}

`variants`をカスタム指定した場合、その場でソースコードからビルドされるため、インストールに時間がかかります。

:::

## パッケージを探したい（`port search`）

```console
$ port search 検索パターン

// 例：ブラウザを検索
$ port search browser
```

`port search`で、MacPortsで管理されているパッケージ（ポート）を検索できます。

## パッケージの詳細を調べたい（`port info`）

```console
$ port info パッケージ名
```

`port info`で、指定したパッケージの詳細情報を表示できます。
パッケージの説明や依存パッケージ、提供元ウェブサイトなどを調べることができます。

## パッケージを更新したい（`port upgrade`）

```console
// ポートツリー（パッケージリスト）を更新する
$ sudo port selfupdate

// 更新が必要なパッケージを表示する
$ port outdated

// パッケージを更新する
$ sudo port upgrade outdated
```

`sudo port selfupdate`で、MacPortsが参照するポートツリーを最新の状態に更新できます。
パッケージ自体は更新されません。

`port outdated`で、更新が必要なパッケージを一覧できます。

`sudo port upgrade outdated`で、更新があるパッケージをすべて更新できます。
`sudo port upgrade パッケージ名`で、指定したパッケージだけを更新することもできます。

## インストール済みパッケージを確認したい（`port installed`）

```console
$ port installed
```

`port installed`で、インストール済みのパッケージ名を一覧できます。

## パッケージを削除したい（`port uninstall`）

```console
$ sudo port uninstall パッケージ名
```

`port uninstall`で、インストール済みのパッケージを削除できます。

## 不要なファイルを削除したい（`port clean`）

```console
// 古いバージョンやビルドファイルを削除する
$ sudo port clean --all パッケージ名

// 使われなくなった依存パッケージをまとめて削除する
$ sudo port uninstall leaves
```

`port clean`で、ビルド時に残ったファイルやキャッシュを削除できます。

`port uninstall leaves`で、依存関係だけでインストールされていて、今はどこからも参照されなくなったパッケージ（leaves）をまとめて削除できます。
