# ディレクトリ容量したい（`du`）

```console
$ du -sh ディレクトリ名
```

`du`コマンドでディレクトリの容量を確認できます。
`-sh`オプションで、指定したディレクトリのサイズを集計できます。

## 最終更新日をしりたい（`--time`）

```console
$ du --time ディレクトリ名
$ du --time --time-style=iso ディレクトリ名
$ du --time --time-style=long-iso ディレクトリ名
$ du --time --time-style=full-iso ディレクトリ名
$ du --time --time-style=+%Y-%m-%dT%H:%M:%S%z ディレクトリ名
```

`--time`オプションで対象ディレクトリの最終更新日を確認できます。
`--time-style`オプションで表示形式を変更できます。
デフォルトは`long-iso`形式です。
フォーマット指定子は[date](./command-date.md)コマンドと同じです。

## CSV形式にしたい

```bash
#!/usr/bin/env bash

set -euo pipefail

# CSVファイルに追加する実行日時をISO8601形式で取得
ISO8601=$(date +%Y-%m-%dT%H:%M:%S%z)
# ファイル名に利用する日付フォーマット（YMD形式）
YMD=$(date +%Y%m%d)

# du -s: --summary
# du -m: --block-size=1MB
# awk -v 変数名="値"
du -sm ディレクトリ名 | awk -v date="${ISO8601}" '{print date "," $1 "," $2}' > ${YMD}_usage.csv

exit 0
```

ディレクトリ容量をモニタリングしたときに、CSV形式に変換したサンプルです。
`du`コマンドの出力はタブ区切りになっているので、`awk`コマンドで簡易的な変換処理をしています。
`awk -v`オプションで変数名`date`を定義し、出力に追加しています。
