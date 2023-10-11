# データ点したい（``.encode``）

```python
alt.Char(data).mark_bar().encode(
    alt.X("datetime:T)", title="時刻"),
    alt.Y("pageview", title="アクセス数"),
)
```

``altair``でデータ点を指定する場合、``エンコード``と呼びます。
（文字やファイルのエンコードとは関係ないです）

データ点を指定する際に、データのタイプを指定できます。
連続的なデータの場合は``Q``（quantative）、
離散的なデータの場合は``O``（ordinal）もしくは``N``（nominal）、
時系列データの場合は``T``（temporal）を指定します。

詳しくは [Encoding Data Types](https://altair-viz.github.io/altair-viz-v4/user_guide/encoding.html#encoding-data-types) を参照してください。

## データを集計したい（``aggregate``）

```python
alt.Chart(data).mark_bar().encode(
    alt.X("datetime:T").title("アクセス日時"),
    alt.Y("pagevnew:Q", aggregate="sum").title("アクセス日時（累計）")
)
```

グラフを作成するときに、データを集計できます。
X軸（[altair.X](https://altair-viz.github.io/user_guide/generated/channels/altair.X.html)）やY軸の``aggregate``オプションを使って集計方法を指定します。
集計方法は、平均値（``mean``）、合計値（``sum``）、中央値（``median``）、最小値（``min``）、最大値（``max``）、計数値（``count``）から選んでください。
