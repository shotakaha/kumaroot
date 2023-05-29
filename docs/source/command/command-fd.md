```{eval-rst}
.. index::
    single: CLI; fd
    single: Find & Replace; fd
    single: Rust Alternatives; fd
```

# ファイルを探したい（``fd``）

```console
$ fd 検索パターン 検索パス
```

[find](./command-find.md)の代替コマンドです。
{file}`.gitignore`に書かれているファイルは無視してくれます。
``find``と引数の位置が入れ替わっているのはちょっと罠です。

## インストール

```console
$ brew install fd
```

## ファイルの種類で探したい（``-t`` / ``--type``）

```console
# ファイルを探したい; find 検索パス -type f
$ fd -t f 検索パス

# ディレクトリを探したい; find 検索パス -type d
$ fd -t d 検索パス

# 空のディレクトリを探したい; find 検索パス -type d --empty
$ fd --type d --type empty 検索パス
```

``--type``オプションを使ってファイルの種類で検索できます。
``--type``オプションは重ねがけできるので``--type d --type empty``で空のディレクトリを検索できます。

## 拡張子で探したい（``-e`` / ``--extension``）

```console
# HTMLファイルを探したい
$ fd -e "*.html" 検索パス

# ZIPファイルを探したい
$ fd -e "*.zip" 検索パス

# HTML以外のファイルを探したい
$ fd -E "*.html" 検索パス
```

``--extension``オプションを使ってファイルの拡張子を指定して検索できます。

## 修正した時刻で探したい

## サイズで探したい（``-S`` / ``--size``）

```console
# 100kB以上のファイルを探したい
$ fd -S +100k 検索パス

# 10MB以上のファイルを探したい
$ fd -S +10M 検索パス

# 10MB - 50MBのファイルを探したい
$ fd --size +10M --size -50M 検索パス
```

## 深さを指定したい（``--d`` / ``--max-depth``）
