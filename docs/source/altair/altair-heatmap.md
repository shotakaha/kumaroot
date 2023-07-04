# ヒートマップしたい

```python
chart = alt.Chart(data)
    .mark_rect()
    .encode(
        alt.X("hour:O", title="時間")
        alt.Y("weekday:O", title="曜日")
        alt.Color("session:Q", title="セッション数", scale=alt.Scale(scheme="greens"))
    )
```

ヒートマップは[.mark_rect](https://altair-viz.github.io/user_guide/marks/rect.html)を使って作成します。

上記のサンプルでは、アクセスログの日時からアクセス数（＝セッション数）のヒートマップを作成しています。
あらかじめ``pandas``でデータフレームを整理して``時間``、``曜日``、``セッション数``は計算してあります。

それを使って、X軸（``alt.X``）を``時間（0 - 23）``、
Y軸（``alt.Y``）を``曜日（0 - 6）``で区切り、
Z軸（``alt.Color``）に``セッション数``を色でスケール表示させています。
スケールの色は緑を基調とした設定（``alt.Scale(scheme="greens")``）に変更しています。
