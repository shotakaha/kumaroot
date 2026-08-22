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

## 圧縮ファイルを表示したい（`zcat` / `gzcat`）

```console
$ zcat -f 圧縮ファイル.gz
$ gzcat 圧縮ファイル.gz
```

`zcat`（macOSでは`gzcat`）で、圧縮ファイルの中身を展開せずにまとめて標準出力に表示できます。

## 圧縮ファイルをページャーしたい（`zless` / `zmore`）

```console
$ zless 圧縮ファイル.gz
$ zmore 圧縮ファイル.gz
```

`zless`や`zmore`で、圧縮ファイルの中身を展開せずにページャーでスクロールしながら見られます。

## 圧縮ファイルを検索したい（`zgrep` / `rg -z`）

```console
$ zgrep '検索パターン' 圧縮ファイル.gz
$ rg -z '検索パターン' 圧縮ファイル.gz
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

// ripgrepを使う場合（-Eなしで拡張正規表現が使える）
$ zcat -f access_log.*.gz | rg -o '" [0-9]{3} ' | tr -d '" ' | sort | uniq -c | sort -rn
```

`zcat -f access_log.*.gz`で、複数の月のアクセスログをまとめて展開します。
`rg -o '" [0-9]{3} '`で、ステータスコードの部分だけを抽出し、`tr -d '" '`で余計な文字を削除します。
`sort | uniq -c | sort -rn`で、ステータスコードごとに件数を集計して降順に並べます。

`*access_log.*.gz`にすると、HTTPとHTTPSのログをまとめて集計できます。
`*access_log.2026-*.gz`にすると、2026年のログだけを集計できます。

```console
// アクセス数の多いIP TOP10（1ファイル分）
$ zcat -f access_log.2026-08-01.gz | awk '{print $1}' | sort | uniq -c | sort -rn | head -10
```

```console
// アクセスの多いURL TOP10（1ファイル分）
$ zcat -f access_log.2026-08-01.gz | awk -F'"' '{print $2}' | awk '{print $2}' | sort | uniq -c | sort -rn | head -10

// 静的アセットやbot・不正アクセス系のパスを除外して、ページとして意味のあるURLに絞る
$ zcat -f access_log.2026-08-01.gz | awk -F'"' '{print $2}' | awk '{print $2}' | \
    grep -vE '\.(js|css|png|jpe?g|gif|svg|ico|woff2?|ttf|map|xml|txt|json)($|\?)' | \
    grep -vE '^/(wp-|\.well-known|\.env|xmlrpc\.php|feed$|\?)' | \
    grep -v '^$' | \
    sort | uniq -c | sort -rn | head -10
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

アクセスの多いURLをそのまま集計すると、`.js`や`.css`などの静的アセットや、`/wp-login.php`のような脆弱性スキャン・bot系のアクセスが上位を占めてしまいがちです。
`grep -v`で拡張子・パスのパターンを除外していくと、実際に読まれているページに近いランキングになります。
除外パターンはサイトの構成やアクセス傾向によって変わるので、自分のログを見ながら調整するとよいです。

:::{seealso}

- [](./command-tar.md)

:::
