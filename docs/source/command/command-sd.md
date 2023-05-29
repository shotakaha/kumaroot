```{eval-rst}
.. index::
    single: CLI; sd
    single: Find & Replace; sd
    single: Rust Alternatives; sd
```

# 置換したい（``sd``）

```bash
$ brew install sd
$ sd --version
sd 0.7.6
```

```bash
$ sd '検索パターン' '置換パターン' 文字列
$ head -n 100 ファイル名 | sd 検索パターン 置換パターン
$ cat ファイル名 | sd 検索パターン 置換パターン
```

文字列やファイルの中身をパターン検索して置換するコマンドです。
[sed](./command-sed.md)のRust代替コマンドで、引数が直感的に指定できるようになっています。

:::{seealso}

- [](./command-sed.md)

:::

## ログをLTSV形式に置換したい

```bash
$ head -n 100 ssl_access_log | \
  sd '^^(\\S+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+\\-]\\d{4})\\] "(\\S+)\\s?(\\S+)?\\s?(\\S+)?" (\\d{3}|-) (\\d+|-)\\s?"?([^"]*)"?\\s?"?([^"]*)?"?' \
  'remote_host: $1, remote_logname: $2, remote_user: $3, request_time: $4, request_method: $5, request_url: $6, request_http_version: $7, status: $8, byte_sent: $9, referer: $10, user_agent: $11'
```

Apacheのcombined形式のログをLTSV（Labeled Tab-Separated Values）形式に変換しています。
10万行くらいの処理なら一瞬でした。
100万行を越えたら一瞬・・・とは言えなかったですが、自作のPythonスクリプトを回すより遥かに速かったです。
・・・もう、これを使ったシェルスクリプトを書いた方がよさそう・・・。

```bash
# あとでためす
$ gzip -d ファイル名.gz | sd '検索パターン' 'LTSV形式' > 出力ファイル名
```
