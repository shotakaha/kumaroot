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
