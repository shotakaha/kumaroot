# フィルターしたい（`RDataFrame::Filter`）

```cpp
#include "ROOT/RDataFrame.hxx"

// 条件に合うデータを抽出
auto filtered_df = df.Filter("x > 0 && y < 100");
```

`RDataFrame::Filter`メソッドで特定の条件に合うデータだけを抽出できます。

```python
# 条件に合うデータを抽出
filtered_df = df.Filter("x > 0 and y < 100")
```
