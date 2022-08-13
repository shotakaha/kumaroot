# bash

シェルスクリプトを作成するときのメモです。


## シェバング

```bash
#! /usr/bin/env bash
```

## テスト文

```bash
[ -d パス ]
[ -e パス ]
[ -f パス ]
```

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
