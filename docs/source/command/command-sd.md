```{eval-rst}
.. index::
    single: CLI; sd
    single: 検索＆置換したい; sd
    single: Rust Alternatives; sd
```

# テキストを置換したい（`sd`）

```console
$ sd '検索パターン' '置換パターン' ファイル名
$ コマンド | sd '検索パターン' '置換パターン'
```

`sd`は、ファイルの中身をテキスト置換できるコマンドです。
[sed](./command-sed.md)のRust代替コマンドで、引数が直感的に指定できるようになっています。

:::{seealso}

- [](./command-sed.md)

:::

## インストールしたい（`sd`）

```console
$ brew install sd
$ sd --version
sd 1.0.0
```

`sd`はHomebrewでインストールできます。

## すべて置換したい

```console
$ echo "aaa" | sd 'a' 'b'
bbb
```

`sd`はデフォルトで、1行の中でマッチしたすべての箇所を置換します。
`sed`と違って`g`フラグは不要です。

## 部分置換したい（`sd --max-replacements`）

```console
$ echo "aaa" | sd --max-replacements 1 'a' 'b'
baa
$ echo "aaa" | sd -n 1 'a' 'b'
```

`--max-replacements`（`-n`）オプションで、置換する回数の上限を指定できます。
`-n 1`にすると、最初にマッチした箇所だけを置換します。

## 置換内容を事前確認したい（`sd --preview`）

```console
$ sd --preview '検索パターン' '置換パターン' ファイル名
$ sd -p '検索パターン' '置換パターン' ファイル名
```

`--preview`（`-p`）オプションで、置換結果を標準出力に表示できます。

`sd`は、`sed`と異なり、デフォルトで末尾に渡したファイル名を上書きします。
`--preview`オプションで、変更内容を確認しておくと安全です。

```console
$ cat ファイル名 | sd '検索パターン' '置換パターン' > 出力ファイル名
```

より安全に置換したい場合は、上記のようにパイプで標準出力に出力して、別のファイルに書き込む方法もあります。

## 文字列をそのまま置換したい（`sd --fixed-strings`）

```console
$ echo "a.b.c" | sd '.' 'X'
XXXXX
$ echo "a.b.c" | sd --fixed-strings '.' 'X'
aXbXc
$ echo "a.b.c" | sd -F '.' 'X'
aXbXc
```

`--fixed-strings`（`-F`）オプションで、検索パターンと置換パターンをリテラル文字列として扱えます。

`sd`の検索パターンはデフォルトで正規表現として扱われます。
`.`のような特殊文字は「任意の1文字」にマッチしてしまうため、`--fixed-strings`で見たままの文字列であることを指示する必要があります。

## 大文字小文字を区別せず置換したい（`sd --flags i`）

```console
$ echo "Hello World" | sd -f i 'hello' 'HI'
HI World
```

`--flags`（`-f`）オプションで、正規表現の挙動を変更できます。
`i`は大文字小文字を区別しない（case-insensitive）フラグです。
複数のフラグを`-f mc`のようにまとめて指定することもできます。

| フラグ | 意味 |
| --- | --- |
| `c` | 大文字小文字を区別する（デフォルト） |
| `i` | 大文字小文字を区別しない |
| `m` | 複数行モードで`^`・`$`をマッチさせる |
| `e` | 複数行モードを無効にする（デフォルト） |
| `s` | `.`を改行にもマッチさせる |
| `w` | 単語全体のみにマッチさせる |

## 複数行を置換したい（`sd --across`）

```console
$ printf 'foo\nbar\n' | sd 'foo\nbar' 'X'
foo
bar
$ printf 'foo\nbar\n' | sd --across 'foo\nbar' 'X'
X
```

`--across`（`-A`）オプションで、改行をまたいだパターンにもマッチできます。

`sd`はデフォルトで入力を1行ずつ処理するため、`foo\nbar`のように改行をまたぐパターンは通常マッチしません。
`--across`で、入力全体を1つのまとまりとして扱うことで対応できます。

連続するログ行のまとめ直しや、改行を含むタグの置換など複数行にまたがるブロック
を扱うときに使います。

:::{note}

入力全体を一度にメモリへ読み込むため、大きなファイルの処理では注意が必要です。

:::

## 後方参照を使いたい（`$1`）

```console
$ echo "2024-01-15" | sd '(\d+)-(\d+)-(\d+)' '$3/$2/$1'
15/01/2024
```

`()`で囲んだ部分は、マッチした文字列を`$1`・`$2`・`$3`のように置換パターン側で再利用できます。
`sed`の`\1`と違い、バックスラッシュなしの`$1`という書き方です。

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
