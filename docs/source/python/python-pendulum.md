# 日付したい（``pendulum``）

```bash
$ pip3 install pendulum
```

```python
import pendulum
now = pendulum.now()
# 2024-09-10 22:34:08.405761+09:00
```

`pendulum`はデフォルトでタイムゾーン情報を含む（`tz-aware`な）日付モジュールです。

## 現在時刻を取得したい（`pendulum.now`）

```python
import pendulum
now = pendulum.now()
# DateTime(2024, 9, 10, 22, 34, 8, 405761, tzinfo=Timezone('Asia/Tokyo'))

print(now)
# 2024-09-10 22:34:08.405761+09:00
```

``now``で、タイムゾーン情報を含んだ（`tz-aware`な）現在時刻の日時オブジェクトを取得できます。
タイムゾーン情報は、システムの情報が参照されます。

## 日付から文字列にしたい（`format`）

```python
dt = pendulum.now()
dt.format("YYYY-MM-DDTHH:mm:ss.SSSSSSZ")
# 2024-09-10T22:34:08.405761+09:00

# YYYY: 西暦（4桁）
# MM: 月（2桁; 0埋め）
# DD: 日（2桁; 0埋め）
# HH: 時（2桁; 24h）
# mm: 分（2桁; 0埋め）
# ss: 秒（2桁; 0埋め）
# SSSSSS: マイクロ秒（6桁; 0埋め）
# Z: タイムゾーン; UTCオフセット

# 時h分m秒s にして時刻を読みやすくした
dt.format("YYYY-MM-DDTHH[h]mm[m]ss[s]SSSSSS[us]Z")
# 2024-09-10T22h34m08s405761us+09:00
```

`format`で、日付オブジェクトを文字列に変換できます。
変換するときに、フォーマットを指定できます。
エスケープしたい文字列は`[]`で囲みます。

```python
dt.to_iso8601_string()
# => '2022-09-26T06:05:11+09:00'
```

日付オブジェクトをISO8601形式の文字列に変換したい場合は、``to_iso8601_string`が便利です。
また、その他の一般的な出力形式は[Common Formats](https://pendulum.eustace.io/docs/#common-formats)を参照してください。

## 文字列から日付にしたい（`pendulum.parse`）

```python
pendulum.parse("2022-09-26T17:00:00")
# => DateTime(2022, 9, 26, 17, 0, 0, tzinfo=Timezone('UTC'))
```

```python
pendulum.parse("2022-09-26T17:00:00", tz="Asia/Tokyo")
# => DateTime(2022, 9, 26, 17, 0, 0, tzinfo=Timezone('Asia/Tokyo'))
```

`parse`で、日付の文字列を日付オブジェクトに変換できます。
よく使われている日付の並びであれば、自動で推定してくれます。
第二引数にタイムゾーン名を指定できます。

## 独自の文字列から日付にしたい（`pendulum.from_format`）

```python
pendulum.from_format("26/Sep/2022:06:05:11 +0000", "DD/MMM/YYYY:HH:mm:ss ZZ")
# => DateTime(2022, 9, 26, 6, 5, 11, tzinfo=Timezone('+00:00'))
```

```python
pendulum.from_format("26/Sep/2022:06:05:11 +0900", "DD/MMM/YYYY:HH:mm:ss ZZ")
# => DateTime(2022, 9, 26, 6, 5, 11, tzinfo=Timezone('+09:00'))
```

`from_format`で、独自形式の文字列を日付オブジェクトに変換できます。
上記のサンプルは、Apacheのアクセスログに記録されている日付フォーマットです。
``parse``ではエラーがでるので``from_format``で形式を指定する必要があります。
利用できる日付トークンは[Tokens](https://pendulum.eustace.io/docs/#tokens)を参照してください。

## UNIX時間を日付にしたい（`pendulum.from_timestamp`）

```python
import time
import pendulum
unix_time = time.time()
# 1725976467.508806

dt = pendulum.from_timestamp(unix_time)
# 2024-09-10 13:54:27.508806+00:00
```

`from_timestamp`でUNIX時間を日付オブジェクトに変換できます。
UNIX時間は`time`モジュールを使って取得できます。

## ひと月後の日付が欲しい

```python
dt = pendulum.date(2018, 12, 1)
dt.add(months=1)
# => Date(2019, 1, 1)
```

日付の足し算や引き算もできます。
その際、年の繰り越しもきちんと扱ってくれます。
