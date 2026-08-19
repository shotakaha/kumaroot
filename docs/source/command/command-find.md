```{eval-rst}
.. index::
    single: CLI; find
    single: 検索＆置換したい; find
```

# ファイルを検索したい（`find`）

```console
$ find [検索パス] [検索条件]

// シンボリックリンクを追跡
$ find -L [検索パス] [検索条件]

// 文字列を安全に検索（macOS/BSD版）
$ find -X [検索パス] [検索条件]

// 正規表現で検索（macOS/BSD版）
$ find -E [検索パス] [検索条件]

```

`find`コマンドで、ファイルやディレクトリを検索できます。
`[検索パス]`と`[検索条件]`を指定することで、任意の条件でファイルを抽出できます。
検索パス名の末尾の`/ (trailing-slash)`は不要です。

`-L`オプションで、シンボリックリンクを追跡して検索できます。
`-X`オプションで、文字列を安全に検索できます。
検索結果を[xargs](./command-xargs.md)に渡すときに便利です。

`-E`オプションで、正規表現を使った検索ができます。
ただし、これはmacOS/BSD版のfindコマンドでのみ使えるオプションです。

`find`はUnix初期からあるコマンドのひとつです。
そのため、最近のコマンドオプションのような
`-ショートオプション`、
`--ロングオプション`のような区別がありません。

:::{seealso}

- [](./command-fd.md)

:::

## 拡張子で探したい（`-name`）

```console
// HTMLファイルを探したい
$ find 検索パス -name "*.html"

// ZIPファイルを探したい
$ find 検索パス -name "*.zip"

// HTML以外のファイルを探したい
$ find 検索パス ! -name "*.html"

// JPEGまたはPNGファイルを探したい
$ find 検索パス \( -name "*.jpg" -o -name "*.png" \)

// 大文字/小文字を区別せずにHTMLファイルを探したい
$ find 検索パス -iname "*.HTML"
```

`-name`オプションで、検索するファイル名のパターンを指定できます。

`*.html`のようなglobパターンで、拡張子に合わせて検索できます。
NOT検索する場合は`!`を、
OR検索する場合は`-o`を使います。
`-o`を使うときは、`-name`同士が独立した条件として評価されないように
`\( ... \)`でグループ化する必要があります。
大文字/小文字を区別せずに検索したい場合は`-iname`を使います。

## ファイルの種類で探したい（`-type`）

```console
// ファイルを探したい
$ find 検索パス -type f

// ディレクトリを探したい
$ find 検索パス -type d

// シンボリックリンクを探したい
$ find 検索パス -type l

// 空のディレクトリを探したい
$ find 検索パス -type d -empty

// 実行可能なファイルを探したい
$ find 検索パス -type f -perm -u+x

// リンク切れのシンボリックリンクを探したい
$ find 検索パス -xtype l
```

`-type`オプションで、検索するファイルの種類を指定できます。
ファイル（`f`）、ディレクトリ（`d`）、シンボリックリンク（`l`）などを選択できます。
`-empty`オプションと組み合わせて、空のファイル、空のディレクトリを検索できます。
`-perm`オプションと組み合わせて、実行権限を持つファイルだけに絞り込めます。

`-xtype`は`-type`のシンボリックリンク版で、リンクの参照先を評価します。
リンク先が存在しない（壊れた）シンボリックリンクを探すのに便利です。

## タイムスタンプで探したい（`-ctime` / `-mtime` / `-atime`）

```console
// ステータス変更が7日以上前
$ find 検索パス -ctime +7

// 最終更新日が28日以内
$ find 検索パス -mtime -28

// 10分以上前 - 60分以内に変更したファイルを探したい
$ find 検索パス -mmin +10 -mmin -60

// 数分以内にステータス変更されたファイルを探したい
$ find 検索パス -cmin -10
```

`-ctime`系のオプションで、ファイルのタイムスタンプを使って検索できます。

- `-ctime`（ステータス変更日）
- `-mtime`（最終更新日）
- `-atime`（最終アクセス日）

基準は現在時刻で、
`-N`はN日**以内**、
`+N`はN日**以上前**にマッチします。

`-mmin`、`-cmin`、`-amin`を使うと、日単位ではなく分単位で指定できます。

## サイズで探したい（`-size`）

```console
// 100kB以上のファイルを探したい
$ find 検索パス -size +100k

// 10MB以上のファイルを探したい
$ find 検索パス -size +10M

// 10MB - 50MBのファイルを探したい
$ find 検索パス -size +10M -size -50M
```

`-size`オプションでファイルサイズを基準に検索できます。
`-サイズ`は**サイズ以下**、
`+サイズ`は**サイズ以上**にマッチします。
重たいファイルの削除を検討したい場合に重宝します。

## 深さを指定したい（`-maxdepth`）

```console
// 2階層目まで探したい
$ find 検索パス -maxdepth 2 -name "*.html"

// 4階層目まで探したい
$ find 検索パス -maxdepth 4 -name "*.html"
```

`-maxdepth`オプションで検索する階層の深さを指定できます。

## 正規表現で探したい（`-regex`）

```console
$ find 検索パス -regex 正規表現
```

`-regex`オプションで、ファイル名ではなくパス全体を正規表現で検索できます。
`-name`のglobパターンより複雑な条件を指定したいときに使います。

## 検索結果の出力形式を変えたい（`-print` / `-ls`）

```console
// 一致した完全パス名を書きだす（デフォルトの動作と同じ）
$ find 検索パス -print

// 検索結果を ls -l 形式で書きだす
$ find 検索パス -ls
```

`-print`オプションで、一致したファイルの完全パスを出力します。
`find`は条件を指定しなければ`-print`相当の出力をするので、
明示的に指定する機会は多くありません。
`-ls`オプションを使うと、パーミッションやサイズなど
`ls -l`と同じ形式で検索結果を確認できます。

## グループ名で探したい（`-group`）

```console
$ find 検索パス -group グループ名
```

## 所有者不明のファイルを探したい（`-nouser`）

```console
# 所有者不明のHTMLファイルを探したい
$ find 検索パス -type f -nouser -name "*.html"

# グループ不明のHTMLファイルを探したい
$ find 検索パス -type f -nogroup -name "*.html"
```

## 空のディレクトリを削除したい（`-empty -delete`）

```console
$ find 検索パス -type d -empty -delete
```

``-empty``オプションを使って、空のディレクトリが検索できます。
``-delete``オプションを追加して、一括削除できます。

## xargsしたい

```console
$ find 検索パス 検索パターン -print0 | xargs -0 コマンド
$ find 検索パス 検索パターン -X | xargs コマンド
```

`-print0`もしくは`-X`オプションで、安全な検索結果を[xargs](./command-xargs.md)に渡すことができます。

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
