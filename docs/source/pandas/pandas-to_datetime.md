# 日付に変換したい（``to_datetime``）

```python
pd.to_datetime("2022/08/24")
```

日付の文字列を``Timestamp``型などのオブジェクトに変換できます。
だいたいの文字列を変換できます。

## タイムゾーンを追加したい（``tz_localize``）

```python
timezone = "UTC+09:00"
data["datetime"] = pd.to_datetime(data["datetime"], format="ISO8601")
if data["datetime"].dt.tz is None:
    data["datetime"] = data["datetime"].dt.tz_localize(timezone)
```

測定データの記録時刻を``datetime``というカラムに入れた状態です。
この時刻はデータ取得したスクリプトのバージョンによって
タイムゾーン情報も持っていたり（``tz-aware``）持っていなかったり（``tz-naive``）します。

``dt.tz``でタイムゾーン情報の有無を確認し、
持ってない場合に``dt.tz_localize(タイムゾーン)``でタイムゾーン情報を追加しています。
日本のタイムゾーン情報を追加する場合は``UTC+09:00``や``Asia/Tokyo``が使えます。

:::{note}

``pendulum.now()``は``tz-aware``、``datetime.datetime.now()``は``tz-naive``な
日付オブジェクトを生成するため、DAQに使ったスクリプトのバージョンによって
記録時刻に``tz-aware``／``tz-naive``が混ざってしまうことになりました。

これらは別々のファイルに記録されていて、それぞれのデータを解析する場合は問題はありませんでした。
ただし、2つのファイルのデータを結合（``pd.concat``）して、時刻を扱う解析（``resample``など）をしようとした場合、エラーが表出。
そこで、どちらのデータも``tz-aware``な日付オブジェクトに変換することにしました。

:::

## リファレンス

- [pandas.to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
