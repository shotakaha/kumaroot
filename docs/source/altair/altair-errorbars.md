# エラーバーしたい（``mark_errorbar``）

```python
# tmp（気温の平均値）とtmp_std（気温の標準偏差）
data["tmp_min"] = data["tmp"] - data["tmp_std"]
data["tmp_max"] = data["tmp"] + data["tmp_std"]

# time（時刻）をX軸にする
base = alt.Chart(data).encode(alt.X("time"))

# tmp（気温の平均値）をY軸にする
marks = base.mark_point().encode(alt.Y("tmp"))

# tmp_minとtmp_maxをエラーバーにする
errors = base.mark_errorbar().encode(
    alt.Y("tmp_min"),
    alt.Y2("tmp_max"),
)

marks + errors
```

エラーバー付きの散布図を作成する場合は、
``mark_point``と``mark_errorbar``を組み合わせて使います。

``mark_point``では、プロットしたい値を設定します。
``mark_errorbar`では、`alt.Y`と`alt.Y2`にエラーバーの範囲を設定します。
エラーバーの取りうる範囲は、あらかじめ計算しておきます。

:::{seealso}

- [](../pandas/pandas-plot-errorbars.md)
- [](../plotly/plotly-errorbars.md)
- [](../hvplot/hvplot-errorbars.md)

:::

```python
def errorbars(data: pd.DataFrame, x: str, y: str, e: str):
    copied = data.copy()
    copied["min"] = copied[y] - copied[e]
    copied["max"] = copied[y] + copied[e]

    base = alt.Chart(data).encode(alt.X(x))
    marks = base.mark_point().encode(alt.Y(y))
    errors = base.mark_errorbar().encode(
        alt.Y("min"),
        alt.Y2("max")
    )
    charts = {}
    charts["errorbars"] = marks + errors
    charts["marks"] = marks
    charts["errors"] = errors
    return charts
```

## リファレンス

- [Scatter Plot with Error Bars](https://altair-viz.github.io/gallery/simple_scatter_with_errorbars.html)
- [Error Bars with Confidence Interval](https://altair-viz.github.io/gallery/errorbars_with_ci.html)
- [Error Bars with Standard Deviation](https://altair-viz.github.io/gallery/errorbars_with_std.html)
- [Line Chart with Confidence Interval Band](https://altair-viz.github.io/gallery/line_with_ci.html)
