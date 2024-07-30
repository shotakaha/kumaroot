# ヒストグラムしたい（``hvplot.hist``）

```cpp
import pandas as pd
import hvplot.pandas

# data : pd.DataFrame
data.hvplot.hist("energy_deposit")
```

``hvplot.hist``でヒストグラムを作成できます。
Altairと比べて直感的に記述できるため、とても簡単です。

:::{seealso}

- [](../altair/altair-histogram.md)
- [](../pandas/pandas-plot-hist.md)
- [](../plotly/plotly-histogram.md)

:::

## リファレンス

- [Hist](https://hvplot.holoviz.org/reference/tabular/hist.html)J
