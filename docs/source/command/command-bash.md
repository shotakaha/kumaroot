# シェルスクリプトしたい（`bash`）

```console
$ bash スクリプトファイル.sh
$ コマンド実行 && echo "成功" || echo "失敗"
```

`bash`は、Bourne Shell（`sh`）を拡張したシェルです。
対話シェルとしても、シェルスクリプトを実行するインタプリタとしても使われます。

:::{note}

`bash`は、長らくLinuxやmacOSの標準シェルとして使われてきました。
しかし、Ubuntuでは2006年以降、シェルスクリプトが参照する`/bin/sh`が`bash`ではなく`dash`に変更されました。
2019年リリースのmacOS Catalina以降、新規ユーザーのデフォルトログインシェルが`bash`から`zsh`に変更されました。

:::

## インストールしたい（`bash`）

```console
$ brew install bash
$ bash --version
```

`bash`はHomebrewでインストールできます。

```console
$ /bin/bash --version
GNU bash, version 3.2.57(1)-release (arm64-apple-darwin25)
Copyright (C) 2007 Free Software Foundation, Inc.
```

macOSに標準でインストールされている`bash`は、バージョン3系で古いです。

## Hello Worldしたい（`echo`）

```bash
#!/usr/bin/env bash

echo "Hello World"
```

## シェバングしたい（`#!/usr/bin/env bash`）

```bash
#!/usr/bin/env bash
```

`#!`ではじまる行をシェバング（shebang）と呼びます。
シェルスクリプトを実行する際には、どのシェルで実行するかを指定する必要があります。
`/usr/bin/env`で環境変数`PATH`から`bash`を探して実行するように指定するのが一般的です。

```bash
#!/bin/bash
```

`#!/bin/bash`のように、シェルの絶対パスを指定することもできます。
しかし、この方法では、実行環境によってはエラーになる場合があります。
`#!/usr/bin/env bash`の方が、より移植性の高い書き方です。

## おまじないしたい（`set -euo pipefail`）

```bash
#!/usr/bin/env bash

set -euo pipefail
```

`set -euo pipefail`は、シェルスクリプトの実行時にエラーが発生した場合に、即時にスクリプトを終了させるための設定です。

`-e`は、コマンドが失敗した場合にスクリプトを終了させます。
`-u`は、未定義の変数を参照した場合にスクリプトを終了させます。
`-o pipefail`は、パイプライン内のいずれかのコマンドが失敗した場合にスクリプトを終了させます。

「おまじない」と思って、シェルスクリプトの冒頭に書いておくとよいです。

## テストしたい（`[ ... ]` / `test`）

```bash
if test 条件式; then
    条件式が True の場合の処理
fi
```

`test`は、条件式を評価するためのコマンドです。
`if`文と組み合わせて、条件分岐を作成できます。

```bash
if [ 条件式 ]; then
    条件式が True の場合の処理
fi
```

`[ ... ]`は、`test`の別名でより一般的に使われます。

```bash
if [ ! 条件式 ]; then
    条件式が False の場合の処理
fi
```

`!`を使うことで、条件式の否定を評価できます。

## ファイルを確認したい（`test -f` / `test -d`）

```bash
if [ ! -f ファイルパス ]; then
    echo "Path is not a regular file"
    exit 1
fi
```

`test -f`で、指定したパスが通常のファイルであるかを確認できます。

```bash
if [ ! -d ディレクトリパス ]; then
    echo "Path is not a directory"
    exit 1
fi
```

`test -d`で、指定したパスがディレクトリであるかを確認できます。

```bash
if [ ! -e パス ]; then
    echo "File or directory does not exist"
    exit 1
fi
```

`test -e`で、指定したパスが存在するかを確認できます。

## コマンドの存在を確認したい（`command -v`）

```bash
if ! command -v コマンド名 >/dev/null 2>&1; then
    echo "Error: コマンド名 is missing"
    exit 1
fi
```

`command -v コマンド名`を使ってコマンドの存在を確認できます。
上記のスクリプトは、コマンドが存在しなかった場合、エラーメッセージを表示して終了させています。

## 引数を確認したい（`$#`）

```bash
if [ $# -lt 2 ]; then
    echo "引数の数が不足しています"
    exit 1
fi
```

`$#`で引数の数を取得できます。
テスト文と組み合わせて、引数のバリデーションに使えます。

## オプション解析したい（`getopts`）

```bash
while getopts "n:h" opt; do
    case "${opt}" in
        n)
            arg1=${OPTARG}
            ;;
        h)
            show_help
            ;;
        *)
            echo "Invalid option: ${opt}" >&2
            exit 1
            ;;
    esac
done
```

`-h`のように、フラグとしてのオプション変数は`"h"`、
`-n 行数`のように、引数が必要な場合は`"n:"`と書きます。

## ディスク容量を監視したい（`if`）

```bash
#!/usr/bin/env bash

usage=$(df / | awk 'NR==2 {gsub("%","",$5); print $5}')

if [ "${usage}" -ge 90 ]; then
    echo "Warning: disk usage is ${usage}%"
    exit 1
fi
```

`if`で条件分岐できます。
`df`でルートパーティションの使用率を取得し、90%以上ならエラーメッセージを出して終了します。
cronで定期実行すれば、簡易的なディスク容量監視スクリプトになります。

```bash
#!/usr/bin/env bash

if [ -f ".env" ]; then
    source .env
else
    echo "Error: .env file not found" >&2
    exit 1
fi
```

`else`を使うと、条件に一致しなかった場合の処理も書けます。
`.env`ファイルがあれば読み込み、なければエラーで終了する、よくある設定読み込みパターンです。

```bash
#!/usr/bin/env bash

branch=$(git branch --show-current)

if [ "${branch}" = "main" ]; then
    echo "Error: cannot push directly to main" >&2
    exit 1
elif [ "${branch}" = "" ]; then
    echo "Error: not on any branch (detached HEAD?)" >&2
    exit 1
else
    git push origin "${branch}"
fi
```

`elif`で条件を追加できます。
現在のブランチが`main`なら拒否し、ブランチ名が取得できなければ（detached HEADなど）エラーにし、それ以外なら`push`する、という3分岐のガードスクリプトです。

## サブコマンドを実装したい（`case`）

```bash
#!/usr/bin/env bash

subcommand="${1:-help}"

case "${subcommand}" in
    start)
        echo "starting..."
        ;;
    stop)
        echo "stopping..."
        ;;
    status)
        echo "checking status..."
        ;;
    help|*)
        echo "usage: $0 {start|stop|status}"
        ;;
esac
```

`case`で、変数の値がどのパターンに一致するかで処理を分岐できます。
`start`・`stop`・`status`のようなサブコマンドを受け取って処理を切り替える自作CLIによくある構造です。
`help|*`のように`|`で複数パターンをまとめられ、`*`は「どれにも一致しなかった場合」を拾う受け皿になります。

## 複数ファイルをまとめて処理したい（`for`）

```bash
#!/usr/bin/env bash

for file in *.jpg; do
    convert "${file}" -resize 50% "resized_${file}"
done
```

`for`で、値のリストを順に変数へ入れながら処理を繰り返せます。
カレントディレクトリの`.jpg`ファイルすべてをリサイズして、別名で保存する例です。
グロブ（`*.jpg`）はそのまま`in`の後に書くだけで展開されます。

```bash
#!/usr/bin/env bash

for host in web01 web02 web03; do
    echo "=== ${host} ==="
    ssh "${host}" uptime
done
```

サーバーのリストを直接書いて、`ssh`で同じコマンドを順番に実行する例です。
台数が多い場合は`hosts.txt`から`while read`で読み込む方法（下記）に切り替えるとよいです。

## サーバーが起動するまで待ちたい（`while` / `until`）

```bash
#!/usr/bin/env bash

until curl -sf http://localhost:8080/health >/dev/null; do
    echo "waiting for server..."
    sleep 2
done

echo "server is up"
```

`until`は条件式が真になるまで処理を繰り返します。
ヘルスチェック用エンドポイントが応答するまで2秒おきにリトライし、起動を待つデプロイスクリプトなどでよく使うパターンです。

```bash
#!/usr/bin/env bash

while read -r line; do
    echo "processing: ${line}"
done < hosts.txt
```

`while`は条件式が真の間、処理を繰り返します。
`hosts.txt`を1行ずつ読み込んで処理する、ファイル入力の定番パターンです。
`for line in $(cat hosts.txt)`と書くと、空白を含む行やスペース区切りで意図せず分割されてしまうため、`while read`のほうが安全です。

## メニューから選ばせたい（`select`）

```bash
#!/usr/bin/env bash

PS3="deploy先を選んでください: "
select env in staging production quit; do
    case "${env}" in
        staging)
            echo "deploying to staging..."
            break
            ;;
        production)
            echo "deploying to production..."
            break
            ;;
        quit)
            exit 0
            ;;
        *)
            echo "invalid option"
            ;;
    esac
done
```

`select`で、値のリストを番号付きで表示し、ユーザーに選択させられます。
`PS3`でプロンプト文字列を指定でき、`case`と組み合わせて選択結果ごとに処理を分けるのが基本形です。
対話的にデプロイ先を選ばせたいスクリプトなどに向いています。

## 関数を定義したい

```bash
function 関数名
{
    実行内容
}
```

```bash
関数名()
{
    実行内容
}
```

どちらの書き方でも関数を定義できます。
`function`キーワードはbash独自の拡張で、後者の書き方はPOSIX準拠のシェルでも使えます。
