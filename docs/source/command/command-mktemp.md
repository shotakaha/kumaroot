# 一時ファイルしたい（`mktemp`）

```console
$ mktemp
/var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tmp.AfnWksCOe2

$ mktemp --tmpdir=.
tmp.EBOCpr7uXX
```

`mktemp`で一時ファイルを作成できます。
ファイルは`$TMPDIR`に作成されます。
`--tmpdir`オプションでファイルの生成先を変更できます。

ファイル名がランダムに生成されるので、他のスクリプトとの競合を避けることができます。
単体で使うより、シェルスクリプトに組み込むことで力を発揮します。

## ファイル名したい

```console
$ mktemp -t example
/var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/example.QaYKwbG8BA


$ mktemp example-XXXXXX
example-uJrVLB
```

`-t`オプションで、ファイル名のprefixを変更できます。
デフォルトは`tmp`になっています。

また、引数にファイル名のテンプレートを指定できます。
`XXXXX`の部分が`X`の数だけランダムな文字に置換されます。

:::{note}

`x`（小文字）ではダメでした。
また、`X`のあとに文字列があってもダメでした。
なので、`example-XXX.txt`のように拡張子をつけることはできません。

:::

## ディレクトリしたい（`-d` / `--directory`）

```console
$ mktemp --directory
/var/folders/tv/9pv2t92113g5hw2kp4g351_00000gn/T/tmp.t6ZigUBJUV

$ mktemp --directory --tmpdir=.
./tmp.yuE8DXF3Hx
```

`--directory`オプションで一時的なディレクトリを作成できます。
`--tmpdir`オプションと組み合わせて、任意のディレクトリの中に作成できます。

## スクリプトしたい

```bash
#!/usr/bin/env bash

set -euo pipefail

# Owner-only permissions
# Dumps contain user data and password hashes
umask 077

# Configuration
SAVEDIR=${HOME}/wp-sqldump/
DATABASE=$(wp config get DB_NAME)
YMD=$(date +%Y%m%d)
EXPIRE_DAYS=+10

# File path
DUMPFILE=${SAVEDIR}/backup_${DATABASE}_${YMD}.sql.gz

# Ensure save directory exists
mkdir -p ${SAVEDIR}

# Dump SQL to a temp file
TMPFILE=$(mktemp ${SAVEDIR}/.dump.XXXXXX.sql.gz)
trap 'rm -f ${TMPFILE}' EXIT
mysqldump --single-transaction --routines --triggers ${DATABASE} | gzip > ${TMPFILE}
# Move temp file to final destination
mv ${TMPFILE} ${DUMPFILE}

# Remove old dumps
find ${SAVEDIR} -type f -name "backup_${DATABASE}_*.sql.gz -mtime ${EXPIRE_DAYS} -delete

exit 0
```

WordPressのデータベースをバックアップするスクリプトのサンプルです。
`mysqldump`の出力を`mktemp`で作成した一時ファイルに書き込んでから、`mv`で最終的なファイル名に変更しています。

`mktemp`で作成した一時ファイルを経由することで、バックアップ中の不具合で壊れたダンプが残ることを防げます。
また、`trap`処理することで、スクリプトが途中で終了しても一時ファイルが残らないようにしています。
