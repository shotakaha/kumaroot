# fd

```bash
$ fd 検索パターン 検索パス
```

## インストール

```bash
$ brew install fd
```

[find](./command-find.md)の代替コマンドです。

## ファイルの種類で探したい（``-t / --type``）

```bash
$ fd -t f  # ファイル
$ fd -t d  # ディレクトリ
$ fd --type d --type empty  #  空のディレクトリ
```

``--type``オプションを使ってファイルの種類でフィルタできます。
``--type``オプションは重ねがけできます。

## 拡張子で探したい

```bash
$ fd -e "*.html"  # HTMLファイルを探す
$ fd -e "*.zip"   # ZIPファイルを探す
$ fd -E "*.html"  # HTML以外のファイルを探す
```

## 修正した時刻で探したい

## サイズで探したい

```bash
$ fd -S +100k # 100kB以上のファイル
$ fd -S +10M  # 10MB以上のファイル
$ fd --size +10M --size -50M  # 10MB - 50MBのファイル
```

## 関連コマンド

- [](./command-find.md)
