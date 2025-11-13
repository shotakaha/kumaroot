# ヒストグラムしたい（`RDataFrame::Histo1D`）

```cpp
#include "ROOT/RDataFrame.hxx"

// ヒストグラムを作成
auto hist = df.Histo1D({"hist", "Distribution", 100, 0, 10}, "x");
hist->Draw();
```

データをヒストグラムで可視化します。

```python
# ヒストグラムを作成
hist = df.Histo1D(("hist", "Distribution", 100, 0, 10), "x")
hist.Draw()
```
