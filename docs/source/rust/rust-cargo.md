# プロジェクト管理（``cargo``）

```bash
$ cargo new プロジェクト名
$ cargo build
$ cargo run
$ cargo check
```

``rust``をインストールすると``rustc``コマンドと``cargo``コマンドがついてきます。
プロジェクトを管理する場合は``cargo``を使うとよさそうです。

## プロジェクトを作成したい

```bash
$ cargo new プロジェクト名
```

Rustのルールとしてプロジェクト名はスネークケースにする必要があります。

## ビルドしたい

```bash
$ cargo build
$ cargo build --release
```

## ビルド＆実行したい

```bash
$ cargo run
```

## ビルドできるかを確認したい

```bash
$ cargo check
```

実行ファイルを作成せずに、ビルド可能かを確認できます。
``cargo build``より高速に動作するので、コードを書きながらチェックするのにもってこいです。
