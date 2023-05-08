# 時間データしたい

```python
alt.Chart(data).mark_bar().encode(
    alt.X("date:T", title="日時"),
    alt.Y("pageview:Q", title="アクセス数"),
)
```

見出しがわかりにくいかもしれませんが、横軸を時間にしたグラフを作りたいです
日付オブジェクトを任意の時間単位に変換するには[TimeUnit - Altair](https://altair-viz.github.io/user_guide/transform/timeunit.html#user-guide-timeunit-transform)も参照するとよいです。
