# fd

```bash
$ fd 検索パターン 検索パス
```

## インストール

```bash
$ brew install fd
```

[find](./command-find.md)の代替コマンドです。

## ファイルの種類で探したい

```bash
$ fd -t f  # ファイル
$ fd -t d  # ディレクトリ
```

## 拡張子で探したい


## 修正した時刻で探したい

## サイズで探したい

```bash
$ fd -S +100k # 100kB以上のファイル
$ fd -S +10M  # 10MB以上のファイル
$ fd --size +10M --size -50M  # 10MB - 50MBのファイル
```

## 関連コマンド

- [](./command-find.md)
