```{eval-rst}
.. index::
    single: CLI; find
    single: 検索＆置換したい; find
```

# ファイルを探したい（``find``）

```console
$ find 検索パス 検索パターン
```

ファイルやディレクトリを探すコマンドです。
検索パス名の末尾の``/ (trailing-slash)``はつけなくて大丈夫です。
ファイルの内容は検索できません。

:::{seealso}

[fd](./command-fd.md)というRust製の代替コマンドがあります。

:::

## オプション

```console
$ find -name パターン   # ファイル名で検索（大文字/小文字を区別する）
$ find -iname パターン  # ファイル名で検索（大文字/小文字を区別しない）
$ find -regex 正規表現  # 完全な正規表現を使うことができる
$ find -print           # 一致した完全パス名を書きだす
$ find -size 数         # ファイル容量で検索
$ find -type タイプ     # ファイルの種類で検索
$ find -cmin 数         # 数分以内に変更されたファイルを検索
$ find -ctime 数        # 数時間以内に変更されたファイルを検索
$ find -ls              # 検索結果を ls -l に書きだす
```

## ファイルの種類で探したい（``-type``）

```console
# ファイルを探したい
$ find 検索パス -type f

# ディレクトリを探したい
$ find 検索パス -type d

# 空のディレクトリを探したい
$ find 検索パス -type d -empty  # 空のディレクトリを探す
```

## 拡張子で探したい（``-name``）

```console
# HTMLファイルを探したい
$ find 検索パス -name "*.html"

# ZIPファイルを探したい
$ find 検索パス -name "*.zip"

# HTML以外のファイルを探したい
$ find 検索パス ! -name "*.html"
```

## 修正した時刻で探したい（``-mtime``）

```console
$ find 検索パス -mtime 5

# 10分以上前 - 60分以内に変更したファイルを探したい
$ find 検索パス -mmin +10 -mmin -60
```

## サイズで探したい（``-size``）

```console
# 100kB以上のファイルを探したい
$ find 検索パス -size +100k

# 10MB以上のファイルを探したい
$ find 検索パス -size +10M

# 10MB - 50MBのファイルを探したい
$ find 検索パス -size +10M -size -50M
```

## 深さを指定したい（``-depth``）

```console
# 2階層目まで探したい
$ find 検索パス -depth 2 -name "*.html"

# 4階層目まで探したい
$ find 検索パス -d 4 -name "*.html"
```

## グループ名で探したい（``-group``）

```console
$ find 検索パス -group グループ名
```

## 所有者不明のファイルを探したい（``-nouser``）

```console
# 所有者不明のHTMLファイルを探したい
$ find 検索パス -type f -nouser -name "*.html"

# グループ不明のHTMLファイルを探したい
$ find 検索パス -type f -nogroup -name "*.html"
```

## 空のディレクトリを削除したい（``-empty -delete``）

```console
$ find 検索パス -type d -empty -delete
```

``-empty``オプションを使って、空のディレクトリが検索できます。
``-delete``オプションを追加して、一括削除できます。

## GFSローテーションしたい

```bash
#!/bin/bash

# 日次：毎日；7回分を保存
# 週次：毎週日曜日；4回分を保存

SOURCE_DIR="バックアップしたいディレクトリ"
BACKUP_DIR="バックアップを保存するディレクトリ"

# バックアップ日時：ファイル名に追加
DATE=$(date +%Y%m%d)

# 日次バックアップ
tar zcvf ${BACKUP_DIR}/daily/${DATE}_backup_daily.tar.gz ${SOURCE_DIR}
find ${BACKUP_DIR}/daily/ -type f -mtime +7 -print0 | xargs -0 rm

# 週次バックアップ
if [[ $(date +%u) -eq 7 ]]; then
    tar zcvf ${BACKUP_DIR}/weekly/${DATE}_backup_weekly.tar.gz ${SOURCE_DIR}
    find ${BACKUP_DIR}/weekly/ -type f -mtime +28 -print0 | xargs -0 rm
fi
```

`-mtime`オプションを活用すると
日次・週次・月次バックアップを取得するときにローテーションが組めます。
このようなローテーションを
GFS（Grandfather-Father-Son）ローテーションと
呼ぶそうです。
