# 日付したい（``date``）

```console
$ date
Thu Jan 11 15:11:05 JST 2024
```

## ISO8601形式で出力したい

```console
$ date +%Y-%m-%dT%H:%M:%SZ
2024-01-11T15:12:51Z
```

ISO8601形式で表示したい場合は、自分でフォーマットを指定する必要があります。


## Unixtimeで出力したい

```console
$  date +%s
1704953493
```

``+%s``オプションでUnix時間（秒）に変換できます。

## スクリプトの実行時間を計測したい

```bash
SECONDS=0
（スクリプトを実行）
echo "Duration: " $SECONDS
```

``bash``には``$SECONDS``という内部変数があり、スクリプトの実行時間を返してくれます。
スクリプトの冒頭で``SECONDS=0``して初期化しておきます。

``date``コマンドを使いたい場合は、最初と最後に``date +%s``でユニックス時間を取得し、その差分を計算すればよいと思います。

## 日時を設定したい（``--set``）

```console
$ date -s "2024-01-11 15:00:00"
Thu Jan 11 15:00:00 JST 2024
```

``-s``オプションで日時を設定できます。

:::{hint}

Raspberry Piは内部クロックを持たないため、電源をOFFにしている間は時計が止まります。
スマホなどにテザリング接続して、時刻を自動修正することもできますが、
オフライン環境で再起動した場合は、時刻を手動で設定しなおす必要があります。

:::
