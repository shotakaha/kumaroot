# ヒートマップしたい

```console
chart = alt.Chart(data)
    .mark_rect()
    .encode(
        alt.X("hour:O").axis(labelAngle=0, format="%e").title("時間"),
        alt.Y("weekday:O").title("曜日"),
        alt.Color("pageview:Q").title("ページビュー"),
    )
```

ヒートマップは[.mark_rect](https://altair-viz.github.io/user_guide/marks/rect.html)を使って作成します。

上記のサンプルは、アクセスログの日時からアクセス数のヒートマップを作成する場合を想定しました。
あらかじめ``pandas``でデータフレームを整理して``時間``、``曜日``、``ページビュー``は計算してあります。
