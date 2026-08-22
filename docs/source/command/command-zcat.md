# 圧縮ファイルを眺めたい（`zcat` / `zless`）

```console
$ zcat -f 圧縮ファイル.gz

$ zless 圧縮ファイル.gz
$ zmore 圧縮ファイル.gz

// macOS
$ gzcat 圧縮ファイル.gz
```

`zcat`は、gzip形式の圧縮ファイルを展開せずに中身を標準出力に表示するコマンドです。
`zless`や`zmore`は、展開せずに中身をページングして表示するコマンドです。

`gzcat`は、macOSやFreeBSDなどの一部の環境で使える`zcat`です。

:::{caution}

macOSの`zcat`は、`.Z`形式の拡張子を期待するため、`.gz`ファイルをそのまま渡すとエラーになります。
`-f`（`--force`）オプションを付けるか、`gzcat`を使いましょう。

:::

:::{note}

`zcat`や`zless`は、あるブロックサイズごとにストリーミングして標準出力に表示します。
そのため、`zcat`で大きな圧縮ファイルを展開しても、ディスク容量やメモリを圧迫することはほとんどありません。

:::

## 圧縮ファイルをまとめて表示したい（`zcat` / `gzcat`）

```console
$ zcat -f 圧縮ファイル.gz
$ gzcat 圧縮ファイル.gz
```

`zcat`（macOSでは`gzcat`）で、圧縮ファイルの中身を展開せずにまとめて標準出力に表示できます。

## 圧縮ファイルをページャーで見たい（`zless` / `zmore`）

```console
$ zless 圧縮ファイル.gz
$ zmore 圧縮ファイル.gz
```

`zless`や`zmore`で、圧縮ファイルの中身を展開せずにページャーでスクロールしながら見られます。

## 圧縮ファイルを検索したい（`zgrep`）

```console
$ zgrep '検索パターン' 圧縮ファイル.gz
```

`zgrep`で、圧縮ファイルを展開せずに中身を検索できます。
複数の圧縮ファイルをまとめて指定することもできます。

## Apacheログを集計したい

Apacheのアクセスログは、ログローテーションして月ごとにgzip形式で圧縮されていることが多いです。
これを毎月、展開して集計するのは手間がかかる上にディスク容量も圧迫します。
`zcat`でストリーミングしつつ集計するのが便利です。

```console
// ステータスコード別に集計する（全期間まとめて）
$ zcat -f access_log.*.gz | grep -oE '" [0-9]{3} ' | tr -d '" ' | sort | uniq -c | sort -rn
```

```console
// アクセス数の多いIP TOP10（1ファイル分）
$ zcat -f access_log.2026-08-01.gz | awk '{print $1}' | sort | uniq -c | sort -rn | head -10
```

```console
// アクセスの多いURL TOP10（1ファイル分）
$ zcat -f access_log.2026-08-01.gz | awk -F'"' '{print $2}' | awk '{print $2}' | sort | uniq -c | sort -rn | head -10
```

```console
// 404になっているURLだけ抽出する（全期間まとめて）
$ zcat -f access_log.*.gz | awk '$9 == 404 {print $7}' | sort | uniq -c | sort -rn | head -20
```

```console
// 月別アクセス数の推移
$ for f in access_log.2026-*.gz; do
    n=$(zcat -f "$f" | wc -l)
    echo "$f: $n"
  done
```

`zcat -f`で複数の圧縮済みログをまとめて展開しつつ、`awk`・`grep`・`sort`にパイプで渡して集計できます。
ステータスコードの抽出は`awk '{print $9}'`でも取れますが、リクエスト行やUser-Agentにスペースが含まれていると列がずれるため、`"`とステータスコードの並びを正規表現で狙う方が確実です。

:::{seealso}

- [](./command-tar.md)

:::
