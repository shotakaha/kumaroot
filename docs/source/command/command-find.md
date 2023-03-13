# ファイルを探したい（``find``）

```bash
$ find 検索したいパス 検索したいパターン
```

ファイルやディレクトリを探すコマンドです。
検索パス名の末尾の``/ (trailing-slash)``はつけなくて大丈夫です。
ファイルの内容は検索できません。

## オプション

```bash
find -name パターン   # ファイル名で検索
find -regex 正規表現  # 完全な正規表現を使うことができる
find -print           # 一致した完全パス名を書きだす
find -size 数         # ファイル容量で検索
find -type タイプ     # ファイルの種類で検索
find -cmin 数         # 数分以内に変更されたファイルを検索
find -ctime 数        # 数時間以内に変更されたファイルを検索
find -ls              # 検索結果を ls -l に書きだす
```

## ファイルの種類で探したい（``-type``）

```bash
$ find 検索パス -type f  # ファイルを探す
$ find 検索パス -type d  # ディレクトリを探す
```

## 拡張子で探したい（``-name``）

```bash
$ find 検索パス -name "*.html"    # HTMLファイルを探す
$ find 検索パス -name "*.zip"     # ZIPファイルを探す
$ find 検索パス ! -name "*.html"  # HTML以外のファイルを探す
```

## 修正した時刻で探したい（``-mtime``）

```bash
$ find 検索パス -mtime 5
$ find 検索パス -mmin +10 -mmin -60  # 10分以上、60分以内に変更したファイル
```

## サイズで探したい（``-size``）

```bash
$ find 検索パス -size +100k  # 100kB以上のファイル
$ find 検索パス -size +10M   # 10MB以上のファイル
$ find 検索パス -size +10M -size -50M  # 10MB - 50MBのファイル
```

## 深さを指定したい（``-depth``）

```bash
$ find 検索パス -depth 2 -name "*.html"  # 2階層目まで探す
$ find 検索パス -d 4 -name "*.html"      # 4階層目まで探す
```

## グループ名で探したい（``-group``）

```bash
$ find 検索パス -group グループ名
```

## 所有者不明のファイルを探したい（``-nouser``）

```bash
$ find 検索パス -type f -nouser -name "*.html"   # 所有者不明
$ find 検索パス -type f -nogroup -name "*.html"  # グループ不明
```

## 空のディレクトリを探したい（``-empty -delete``）

```bash
$ find 検索パス -type d -empty -delete
```

``-empty``オプションを使って、空のディレクトリが検索できます。
``-delete``オプションを追加して、一括削除できます。

## 関連コマンド

- [](./command-fd.md)
