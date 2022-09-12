# fd

```bash
$ brew install fd
```

[find](./command-find.md)の代替コマンドです。

## ファイルの種類で探したい

```bash
$ fd -t f パターン ディレクトリ  # ファイル
$ fd -t d パターン ディレクトリ  # ディレクトリ
```

## 拡張子で探したい

```bash
$ fd -S +100k # 100kB以上のファイル
$ fd -S +10M  # 10MB以上のファイル
$ fd --size +10M --size -50M  # 10MB - 50MBのファイル
```

## 修正した時刻で探したい

## サイズで探したい


## 関連コマンド

- [](./command-find.md)
