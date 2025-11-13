# 統計量を計算したい（`Mean` / `Max`/ `Min`）

```cpp
#include "ROOT/RDataFrame.hxx"
#include <iostream>

// 平均値を計算
auto mean_x = df.Mean("x");
std::cout << mean_x.GetValue() << std::endl;

// 最大値・最小値
auto max_x = df.Max("x");
auto min_x = df.Min("x");
```

指定したカラムに対して、簡単な統計情報を計算できます。

---

```python
# 平均値を計算
mean_x = df.Mean("x")
print(mean_x.GetValue())

# 最大値・最小値
max_x = df.Max("x")
min_x = df.Min("x")
```
