# 日付したい（`datetime`）

```python
from datetime import datetime
now = datetime.now().astimezone()
# datetime.datetime(2024, 9, 10, 22, 24, 19, 633527, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST'))

print(now)
# 2024-09-10 22:24:19.633527+09:00
```

`datetime.datetime`はPython標準の日付モジュールです。
デフォルトでは、タイムゾーン情報を含まない（`tz-naive`な）日時オブジェクトを取得できます。

Python3.6から`astimezone`というメソッドが使えるようになっていて、
タイムゾーン情報を含む（`tz-aware`な）日時オブジェクトが簡単に取得できるようになっています。

## 現在時刻したい（`now`）

```python
from datetime import datetime
now = datetime.now()
# 2024-09-10 21:48:43.918516

now = datetime.now().astimezone()
# 2024-09-10 21:48:43.918516+09:00
```

`now`で現在日時を取得できます。
デフォルトは`tz-naive`な日時オブジェクトですが、
`astimezone`で`tz-aware`な日時オブジェクトに変換できます。

## 日付から文字列にしたい（`strftime`）

```python
from datetime import datetime
now = datetime.now().astimezone()
now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

# %Y: 西暦（4桁）
# %m: 月（2桁; 0埋め）
# %d: 日（2桁; 0埋め）
# %H: 時（24h; 0埋め）
# %M: 分（60m; 0埋め）
# %S: 秒（60s; 0埋め）
# %f: マイクロ秒（6桁; 0埋め）
# %z: タイムゾーン；UTCオフセット
# %Z: タイムゾーン名
```

`strftime`で日付オブジェクトを文字列に変換できます。
変換するときに、フォーマットを指定できます。

## 文字列から日付にしたい（`strptime`）

```python
from datetime import datetime

date_string = "2024-09-10 22:18:34"
datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# datetime.datetime(2024, 9, 10, 22, 18, 34)
```

`strptime`で、日付の文字列を日付オブジェクトに変換できます。
第一引数に文字列を指定し、
第二引数に読み込む時のフォーマットを指定します。

```python
from datetime import datetime
date_string = "2024-09-10T22:18:34"
datetime.fromisoformat(date_string)
# datetime.datetime(2024, 9, 10, 22, 18, 34)
```

日付がISO8601形式の文字列になっている場合は、
`fromisoformat`が使えます。

## UNIX時間を日付にしたい（`fromtimestamp`）

```python
import time
from datetime import datetime
unix_time = time.time()
# 1725973811.99409

datetime.fromtimestamp(unix_time)
# datetime.datetime(2024, 9, 10, 22, 13, 2, 835681)
```

`fromtimestamp`でUNIX時間を日付オブジェクトに変換できます。
UNIX時間は`time`モジュールを使って取得できます。

:::{note}

`datetime.time`モジュールと
`time`モジュールは別物です。

:::

## その他の操作をしたい

```python
from datetime import datetime  # datetime.datetimeオブジェクト
from datetime import date  # datetime.dateオブジェクト
from datetime import time  # datetime.timeオブジェクト
from datetime import timezone  # datetime.timezoneオブジェクト
from datetime import tzinfo
from datetime import timedelta  # datatime.timedeltaオブジェクト
```

`datetime`モジュールの中にはいろいろなサブモジュールがはいっています。
`import datetime`ですべてをインポートしてもよいですが、
自分が必要なモジュールを選んでおくと、コードが読みやすくなります。

## リファレンス

- [datetime](https://docs.python.org/ja/3/library/datetime.html)
