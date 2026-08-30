# 待機処理したい（`until`）

```console
$ until ping -c1 example.com >/dev/null 2>&1; do
    sleep 1
done
```

`until`は、条件コマンドが成功するまで、処理を繰り返すシェルの制御構文です。
条件コマンドの終了ステータスが`0`になるまで、`do ... done`の中の処理を繰り返します。

「〜が起動するまで待つ」「〜が成功するまでリトライする」といった待機処理に向いています。

:::{seealso}

- [](./command-sleep.md)
- [](./command-expect.md)

:::

## 条件が成立するまで繰り返したい（`until ... do ... done`）

```console
$ until 条件コマンド; do
    繰り返す処理
done
```

`until`のあとに書いたコマンドを実行し、
終了ステータスが`0`以外（失敗）なら`do ... done`の中を実行して、また条件を試します。
終了ステータスが`0`（成功）になった時点でループを抜けます。

```console
$ i=0
$ until [ "$i" -ge 3 ]; do
    echo "$i回目"
    i=$((i + 1))
done
0回目
1回目
2回目
```

`[ "$i" -ge 3 ]`（iが3以上）が成立するまで繰り返すので、0〜2回目が実行されます。

## ポートが開くまで待ちたい（`nc -z`）

```console
$ until nc -z localhost 5432; do
    echo "PostgreSQLの起動を待っています..."
    sleep 1
done
$ echo "起動しました"
```

`nc -z`はポートに接続できれば終了ステータス`0`を返します。
接続できるまで1秒おきに再試行し、開いたら次の処理に進みます。

Dockerコンテナーやテスト用DBの起動待ちでよく使うパターンです。

## 成功するまでリトライしたい（`curl -f`）

```console
$ until curl -fsS https://example.com/health; do
    echo "リトライします"
    sleep 5
done
```

`curl -f`はHTTPエラー（4xx / 5xx）のとき終了ステータスを`0`以外にします。
デプロイ直後のヘルスチェックなど、成功するまで待ちたいときに使います。

:::{note}

無限にリトライすると止まらなくなるので、回数の上限を付けておくと安全です。

```console
$ n=0
$ until curl -fsS https://example.com/health || [ "$n" -ge 10 ]; do
    n=$((n + 1))
    sleep 5
done
```

:::

## ファイルができるまで待ちたい（`[ -f ]`）

```console
$ until [ -f /tmp/build.done ]; do
    sleep 2
done
$ echo "ビルド完了ファイルを検出しました"
```

`[ -f ファイル ]`はファイルが存在すれば成立します。
別プロセスの完了を、目印のファイルで待つときに使えます。

## リファレンス

- [Bash Reference Manual: Looping Constructs](https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs)
- [fish: until はない（`while not` を使う）](https://fishshell.com/docs/current/cmds/while.html)
