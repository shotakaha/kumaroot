```{eval-rst}
.. index::
    single: CLI; fd
    single: 検索＆置換したい; fd
    single: Rust Alternatives; fd
```

# ファイルを検索したい（`fd`）

```console
$ fd 検索条件 検索パス
```

[find](./command-find.md)の代替コマンドです。
{file}`.gitignore`に書かれているファイルは無視してくれます。
`find`と引数の位置が入れ替わっているのはちょっと罠です。

検索パターンはデフォルトで正規表現として扱われます。
globパターンを使いたい場合は`--glob`オプションを付けます。

:::{seealso}

- [](./command-find.md)

:::

## インストール

```console
$ brew install fd
```

## 拡張子で探したい（`-e` / `--extension`）

```console
// HTMLファイルを探したい
$ fd -e html 検索パス

// ZIPファイルを探したい
$ fd -e zip 検索パス
```

`--extension`オプションを使ってファイルの拡張子を指定して検索できます。
`find -name "*.html"`とは異なり、`.`や`*`を付けずに拡張子名だけを指定します。

## ファイルの種類で探したい（`-t` / `--type`）

```console
// ファイルを探したい; find 検索パス -type f
$ fd -t f 検索パス

// ディレクトリを探したい; find 検索パス -type d
$ fd -t d 検索パス

// シンボリックリンクを探したい; find 検索パス -type l
$ fd -t l 検索パス

// 空のディレクトリを探したい; find 検索パス -type d -empty
$ fd -t d -t empty 検索パス

// 実行可能なファイルを探したい
$ fd -t x 検索パス
```

`--type`オプションを使ってファイルの種類で検索できます。
`--type`オプションは重ねがけできるので`-t d -t empty`で空のディレクトリを検索できます。
`-t x`（`executable`）で実行可能なファイルを検索できます。

## タイムスタンプで探したい（`--changed-within` / `--changed-before`）

```console
// 7日以内に変更されたファイルを探したい
$ fd --changed-within 7d 検索パス

// 28日以上前から変更されていないファイルを探したい
$ fd --changed-before 28d 検索パス
```

`--changed-within`・`--changed-before`オプションで、
ファイルの最終更新日時（`find`の`-mtime`相当）を基準に検索できます。
`find`のように作成日・最終アクセス日を個別に指定するオプションはありません。

## サイズで探したい（`-S` / `--size`）

```console
// 100kB以上のファイルを探したい
$ fd -S +100k 検索パス

// 10MB以上のファイルを探したい
$ fd -S +10M 検索パス

// 10MB - 50MBのファイルを探したい
$ fd -S +10M -S -50M 検索パス
```

`--size`オプションでファイルサイズを基準に検索できます。

## 深さを指定したい（`-d` / `--max-depth`）

```console
// 2階層目まで探したい
$ fd -d 2 検索パターン 検索パス

// 4階層目まで探したい
$ fd -d 4 検索パターン 検索パス
```

`--max-depth`オプションで検索する階層の深さを指定できます。

## 正規表現で探したい（デフォルト）

```console
$ fd 正規表現 検索パス
```

`fd`は検索パターンをデフォルトで正規表現として扱います。
`find -regex`のように専用オプションは不要です。
globパターンを使いたい場合は`--glob`オプションを付けます。

## 検索結果の出力形式を変えたい（`--exec-batch ls -l`）

```console
// 検索結果を ls -l 形式で書きだす
$ fd 検索パターン 検索パス -X ls -l
```

`find -ls`に相当する専用オプションはありませんが、
`-X`/`--exec-batch`オプションで`ls -l`を呼び出すことで同じ結果が得られます。

## 空のディレクトリを削除したい

```console
$ fd -t d -t empty 検索パス -X rmdir
```

`-t d -t empty`で空のディレクトリを検索し、
`-X`/`--exec-batch`オプションで`rmdir`を呼び出すと一括削除できます。

## パイプ処理したい（`-x` / `-X`）

```console
$ fd 検索条件 検索パス -x コマンド
$ fd 検索条件 検索パス -X コマンド
```

`fd`には`xargs`相当の機能が組み込まれています。
`-x`/`--exec`は検索結果1件ごとにコマンドを実行し、
`-X`/`--exec-batch`は検索結果をまとめて1回のコマンドに渡します。
