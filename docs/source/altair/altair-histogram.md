# ヒストグラムしたい

```python
chart = alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("age:Q", bin=True),
        y="count()"
    )
```

イベント参加者の年代（``age``）の度数分布（ヒストグラム）を作成する場合を想定しています。
プロットの種類に棒グラフ（``mark_bar()``を選択し、X軸に年代、Y軸は``altair``にビルトインの``count()``を使って、エントリー数を代入しています。

## リファレンス

- https://altair-viz.github.io/gallery/simple_histogram.html
