# ヒストグラムしたい

```python
chart = alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X("age:Q").bin(),
        y="count()"
    )
```

ヒストグラムは[.mark_bar](https://altair-viz.github.io/user_guide/marks/bar.html)を使って作成します。

上記サンプルは、イベントのアンケートで集計した参加者の年代（``age``）の度数分布（ヒストグラム）を作成する場合を想定しました。
プロットの種類に棒グラフ（``mark_bar()``を選択し、X軸に年代、Y軸は``altair``にビルトインの``count()``を使って、エントリー数を代入しています。
