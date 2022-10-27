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

## 外部クレートを更新したい

```bash
$ cargo update
$ cargo update --dry-run
```

依存している外部クレートを更新する場合は``cargo update``します。
最新版がインストールされ、{file}`Cargo.lock`が更新されます。

## ドキュメントを作成したい

```bash
$ cargo doc  # プロジェクトのドキュメントを作成
$ cargo doc --open  # 作成したドキュメントを開く
```

``cargo doc``でプロジェクトのドキュメントを作成できます。
依存している外部クレートのドキュメントも同時に取得できます。
