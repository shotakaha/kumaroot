# シェルスクリプトしたい（`bash`）

```console
$ bash スクリプトファイル.sh
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

## ファイルの存在を確認したい（`-e` / `-f` / `-d`）

```bash
if ! [ -e ファイルパス ]; then
    echo "Error: File does not exist"
    exit 1
fi
```

`[ ... ]`はテスト文です。
上記のスクリプトでは、`[ -e ファイルパス ]`を使ってファイル（またはディレクトリ）が存在するかを確認し、なかった場合にエラーメッセージを表示して終了させています。
`-f`にすると通常のファイルであるか、`-d`にするとディレクトリであるかまで確認できます。

## コマンドの存在を確認したい（`command -v`）

```bash
if ! command -v コマンド名 >/dev/null 2>&1; then
    echo "Error: コマンド名 is missing"
    exit 1
fi
```

`command -v コマンド名`を使ってコマンドの存在を確認できます。
上記のスクリプトは、コマンドが存在しなかった場合、エラーメッセージを表示して終了させています。

## 実行結果でメッセージしたい（`&&` / `||`）

```bash
コマンドを実行 && echo "成功" || echo "失敗"
```

`&&`で前のコマンドが成功した場合の処理を、`||`で失敗した場合の処理をつなげられます。

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

## 条件分岐したい（`if`）

```bash
if 条件式; then
    条件式が True の場合の処理
fi
```

```bash
if 条件式; then
    条件式が True の場合の処理
else
    条件式が False の場合の処理
fi
```

```bash
if 条件式1; then
    処理1
elif 条件式2; then
    処理2
else
    処理（どの条件も False の場合）
fi
```

`if`で条件分岐できます。
`elif`で条件を追加、`else`でどの条件にも一致しなかった場合の処理を書けます。

## パターンで分岐したい（`case`）

```bash
case 変数 in
    パターン1)
        処理1
        ;;
    パターン2)
        処理2
        ;;
    *)
        処理
        ;;
esac
```

`case`で、変数の値がどのパターンに一致するかで処理を分岐できます。
`if`で同じ変数を何度も比較するより簡潔に書けます。

## 繰り返し処理したい（`for`）

```bash
for 変数 in 値のリスト; do
    処理
done
```

`for`で、値のリストを順に変数へ入れながら処理を繰り返せます。

## 条件を満たすまで繰り返したい（`while` / `until`）

```bash
# 条件式を満たしている間
while 条件式; do
    処理
done
```

```bash
# 条件式を満たすまで
until 条件式; do
    処理
done
```

`while`は条件式が真の間、`until`は条件式が真になるまで処理を繰り返します。

## 選択肢から選ばせたい（`select`）

```bash
select 変数 in 値のリスト
do
    実行内容
done
```

`select`で、値のリストを番号付きで表示し、ユーザーに選択させられます。

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
