# シェルスクリプトしたい（``bash``）

```bash
#! /usr/bin/env bash

echo "Hello World"
```

``bash``を使ってシェルスクリプトを作成できます。

## シェバング

```bash
#! /usr/bin/env bash
```

シェルスクリプトの最初に、どのシェルを使うかを記述します。
``#! /bin/bash``と書いてもよいですが、環境によって違うかもしれないので、``/usr/bin/env``で返ってくるシェルを使うようにしています。

## ファイルの存在を確認したい

```bash
if ! [ -e ファイルパス ]; then
    echo "Error: File does not exist"
    exit 1
fi
```

``[ ... ]``はテスト文です。
上記のスクリプトでは、``[ -f ファイルパス ]``を使ってファイルが存在するかを確認し、ファイルがなかった場合にエラメッセージを表示して終了させています。
``-d``にするとディレクトリ、``-f``にすると通常のファイルであるかどうかが確認できます。

## コマンドの存在を確認したい（``command -v``）

```bash
if ! command -v コマンド名 >/dev/null 2>&1; then
    echo "Error: コマンド名 is missing"
    exit 1
fi
```

``command -v コマンド名``を使ってコマンドの存在を確認できます。
上記のスクリプトは、コマンドが存在しなかった場合、エラーメッセージを表示して終了させています。

## 実行結果でメッセージしたい（``$$`` / ``||``）

```bash
コマンドを実行 && echo "成功" || echo "失敗"
```

## 引数を確認したい（``$#``）

```bash
if [ $# -lt 2 ]; then
    echo "引数の数が不足しています"
    exit 1
fi
```

``$#``で引数の数を取得できます。
テスト文と組み合わせて、引数のバリデーションに使えます。

## オプション解析したい（``getopts``）

```bash
while getopts "オプション変数" opt; do
    case "${opt}" in
        変数1)
            arg1=${OPTARG}
            ;;
        h)
            ヘルプを表示する（show_help）
            ;;
        *)
            echo "Invalid option: ${option}" >&2
            exit 1
            ;;
    esac
done
```

``-h``のように、フラグとしてのオプション変数は``"h"``、
``-n 行数``のように、引数が必要な場合は``"n:"``と書きます。

## if文

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
elif 条件式2
    処理2
else
    処理（どの条件の False の場合）
fi
```

## case文

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

## for文

```bash
for 値のリスト in 変数; do
    処理
done
```

## while/until文

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

## select文

```bash
select 変数 in 値のリスト
do
    実行内容
done
```

## 関数を定義

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
