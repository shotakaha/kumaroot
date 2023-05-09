# 時系列データしたい

```python
# 日付データのカラムをdatetimeオブジェクトに変換
data["date"] = pd.to_datetime(data["date"])

# X軸を日付データにする
alt.Chart(data).mark_bar().encode(
    alt.X("date:T", title="日時"),
    alt.Y("pageview:Q", title="アクセス数"),
)
```

横軸を時間にしたグラフを作る場合、横軸の値は``datetime``オブジェクトでないといけません。
日付データのエンコーディングは``T``（temporal）を指定します。

## 日付の単位を変更したい

```python
alt.X("year(date):T", title="年")
alt.X("yearmonth(date):T", title="年月")
alt.X("yearmonthdate(date):T", title="年月日")
alt.X("month(date):T", title="月")
alt.X("date(date):T", title="日")
alt.X("day(date):T", title="曜日")
alt.X("hours(date):T", title="時")
alt.X("minutes(date):T", title="分")
alt.X("seconds(date):T", title="秒")
```

日付データから、``altair``上で、時間の単位を変換できます。
詳細は[TimeUnit - Altair](https://altair-viz.github.io/user_guide/transform/timeunit.html#user-guide-timeunit-transform)も参照するとよいです。

:::{hint}

個人的には、``altair``上で日付データをいろいろ操作するより、``pandas``で整理したほうが、うまくいかないときのデバッグも含めて簡単だと思います。

:::
