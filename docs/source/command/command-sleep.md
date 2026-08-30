# スリープしたい（`sleep`）

```console
$ sleep 5
```

`sleep`は、指定した時間だけ処理を停止するコマンドです。

スクリプトの中で「少し待ってから次に進む」「ループの中で間隔をあける」といった用途に使います。

:::{seealso}

- [](./command-bash.md)

:::

## 秒を指定したい

```console
$ sleep 3
$ echo "3秒待った"
```

引数に数値を渡すと、その秒数だけ停止します。
小数も使えます（`sleep 0.5`で0.5秒）。

## 分・時間・日を指定したい（`m` / `h` / `d`）

```console
$ sleep 5m     # 5分
$ sleep 1h     # 1時間
$ sleep 1d     # 1日
```

数値のあとに単位を付けられます。

- `s` … 秒（省略時のデフォルト）
- `m` … 分
- `h` … 時間
- `d` … 日

:::{note}

単位が使えるのはGNU版（Linux）の`sleep`です。
macOS標準の`sleep`は秒のみで、`sleep 5m`はエラーになります。
macOSでは`brew install coreutils`で入る`gsleep`がGNU版です。

:::

## ループで間隔をあけたい

```console
$ while true; do
    date
    sleep 60
done
```

無限ループの中に`sleep`を入れると、一定間隔で処理を繰り返せます。
上の例は1分ごとに時刻を表示し続けます。

`sleep`を入れないと、ループがCPUを使い切って回り続けます。

## 起動を待ってから実行したい

```console
$ my-server &
$ sleep 2
$ curl http://localhost:8080/
```

バックグラウンドで起動したプロセスの準備を待つために、固定秒数の`sleep`を挟むことがあります。

ただし待ち時間は環境で変わるため、確実に待つなら
[シェルスクリプトしたい（`bash`）](command-bash.md)の`until`ループで
「接続できるまで待つ」と書くほうが安定します。

## リファレンス

- [sleep(1) - Linux manual page](https://man7.org/linux/man-pages/man1/sleep.1.html)
- [coreutils: sleep invocation](https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html)
