# 圧縮／解凍したい（``gzip``）

```bash
// -c: --stdout, --to-stdout
$ gzip -c ファイル名 > ファイル名.gz
```

ひとつのファイルを圧縮するときは``gzip``コマンドを使います。
``-c``オプションを必ずつけて、結果をリダイレクトして圧縮ファイルに書き出します。

:::{warning}

``gzip ファイル名``すると``ファイル名``が上書きされます。
必ず``-c``オプションをつけましょう。

:::

## 展開したい（``-dc``）

```console
// -d: --decompress, --uncompress
$ gzip -cd ファイル名.gz > ファイル名
$ gzip -c -d ファイル名.gz > ファイル名
```

``-d``オプションで展開できます。
``-c``オプションを必ずつけて、結果をリダイレクトして展開ファイルに書き出します。
標準出力に吐き出された結果をパイプして使うこともできます。

:::{hint}

ウェブサイトのログを解析（[goaccess](./command-goaccess.md)）するときに使っています。

```console
$ gzip -cd ログファイル.gz | goaccess --log-format COMBINED -o ログファイル.html
```

:::
