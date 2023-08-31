# 日付に変換したい（``to_datetime``）

```python
pd.to_datetime("2022/08/24", format="%Y/%m/%d")
```

日付の文字列を``Timestamp``型などのオブジェクトに変換できます。
変換する文字列のフォーマットを``format``で指定できます。
だいたいの文字列を変換できます。

## タイムゾーンを追加したい（``tz_localize``）

```python
data["datetime"] = pd.to_datetime(data["datetime"], format="ISO8601")
timezone = "UTC+09:00"
if data["datetime"].dt.tz is None:
    data["datetime"] = data["datetime"].dt.tz_localize(timezone)
```

データを記録したときの時刻の文字列が``datetime``というカラムに入った状態を想定しています。
時刻のタイムゾーン情報を持っているかを``dt.tz``で確認できます。

タイムゾーン情報も持っている場合（``tz-aware``）はそのまま、
タイムゾーン情報を持っていない場合（``tz-naive``）は、``dt.tz_localize(タイムゾーン)``でタイムゾーン情報を追加しています。
日本のタイムゾーン情報を追加する場合は``UTC+09:00``や``Asia/Tokyo``が使えます。

:::{note}

``pendulum.now()``は``tz-aware``、``datetime.datetime.now()``は``tz-naive``な日付オブジェクトを生成します。
``tz-aware``なデータと``tz-naive``なデータを持つデータフレームをそのまま結合（``pd.concat``）したらエラーがでました。
上記のように、どちらのデータも``tz-aware``な日付オブジェクトに変換して対処しました。

:::

## リファレンス

- [pandas.to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
