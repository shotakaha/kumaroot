# 日付したい（``date``）

```console
$ date
Thu Jan 11 15:11:05 JST 2024
```

## フォーマットしたい（`+表示形式`）

```console
// 年月日
$ date +%Y-%m-%d
20241018

// 年月
$ date +%Y%m
202410

// 週
$ date +%U
41

// 文字列入り
$ date +%U週目
41週目
```

`+表示形式`オプションで日付のフォーマットを変更できます。
とても柔軟で、フォーマット指定子のほかに、文字列もそのまま表示できます。

| 表示内容 | 指定子 |
|---|---|
| 年 | `%Y` / `%y` |
| 月 | `%m`（01-12） / `%B` / `%b` / `%h` |
| 日 | `%d`（01-31） |
| 時 | `%H`（00-24） / `%I`（00-12） / `%p`（AM/PM） |
| 分 | `%M`（00-59） |
| 秒 | `%S`（00-59） |
| 曜日 | `%A` / `%a` / `%U` / `%u`（1-7） / `%w`（0-6） |
| 日数・週数 | `%j`（001-366） / `%W`（00-52） |
| タイムゾーン | `%z`（+09:00） / `%Z`（JST） |

指定子の大文字／小文字と表示内容の対応が覚えにくいので、毎回調べたほうがよいです。

## ISO8601形式で出力したい

```console
$ date +%Y-%m-%dT%H:%M:%S%z
2024-10-18T12:02:15+0900

// 空白を含む場合は""で囲む
$ date +"%Y-%m-%d %H:%M:%S%z"
2024-10-18 12:03:42+0900
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

## 日付を変換したい（`-d`）

```bash
# Apacheログの日付
accessed_date="Mon Oct 23 14:23:42.123456 2024"

# "月 日 年 時刻" に並び替える
parsed_date=$(echo "${accessed_date}" | awk '{print $2 " " $3 " " $6 " " $4}')
echo ${parsed_date}

# ISO8601形式に変換する
formatted_date=$(date -d "${parsed_date}" +"%Y-%m-%dT%H:%M:%S")
```

`-d`オプションで
