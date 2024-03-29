# 日付したい（``pendulum``）

```bash
$ pip3 install pendulum
```

[Pendulum](https://pendulum.eustace.io/)はデフォルトでタイムゾーンを考慮する日付管理パッケージです。
Python標準には``datetime``、``date``、``time``などのモジュールがありますが、どれを使ったらよいかいつも悩みます。
Pendulumはそんな悩みから解放してくれるのでオススメです。

## 現在時刻を取得したい

```python
import pendulum
now = pendulum.now()
# => DateTime(2022, 10, 24, 12, 51, 43, 38054, tzinfo=Timezone('Asia/Tokyo'))
```

## 一般的な日付フォーマットを取得したい

```python
pendulum.parse("2022-09-26T17:00:00")
# => DateTime(2022, 9, 26, 17, 0, 0, tzinfo=Timezone('UTC'))
```

```python
pendulum.parse("2022-09-26T17:00:00", tz="Asia/Tokyo")
# => DateTime(2022, 9, 26, 17, 0, 0, tzinfo=Timezone('Asia/Tokyo'))
```

## 独自の日付フォーマットを取得したい

```python
pendulum.from_format("26/Sep/2022:06:05:11 +0000", "DD/MMM/YYYY:HH:mm:ss ZZ")
# => DateTime(2022, 9, 26, 6, 5, 11, tzinfo=Timezone('+00:00'))
```

```python
pendulum.from_format("26/Sep/2022:06:05:11 +0900", "DD/MMM/YYYY:HH:mm:ss ZZ")
# => DateTime(2022, 9, 26, 6, 5, 11, tzinfo=Timezone('+09:00'))
```

ここで使ったサンプルはApacheのログに記録されている日付フォーマットです。
``parse``ではエラーがでるので``from_format``で形式を指定する必要があります。
利用できる日付トークンは[Tokens](https://pendulum.eustace.io/docs/#tokens)を参照してください。

## 日付フォーマットをISO標準に変換したい

```python
dt = pendulum.parse("2022-09-26T17:00:00")
dt.isoformat()
# => '2022-09-26T17:00:00+00:00'
```

```python
dt = pendulum.from_format("26/Sep/2022:06:05:11 +0900", "DD/MMM/YYYY:HH:mm:ss ZZ")
dt.to_iso8601_string()
# => '2022-09-26T06:05:11+09:00'
```

``parse``または``from_format``で読み込んだ日付を、ISO標準形式で出力したい場合は多いです。
``to_isoformat()``も``to_iso8601_string``も出力結果は同じです。
その他の出力可能な形式は[Common Formats](https://pendulum.eustace.io/docs/#common-formats)を参照してください。

## ひと月後の日付が欲しい

```python
dt = pendulum.date(2018, 12, 1)
dt.add(months=1)
# => Date(2019, 1, 1)
```

日付の足し算や引き算もできます。
その際、年の繰り越しもきちんと扱ってくれます。
