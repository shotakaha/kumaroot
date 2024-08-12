# 統計情報を表示したい（ ``gStyle->SetOptStat`` ）

```cpp
// gStyle->SetOptStat(1)
gStyle->SetOptStat(112211)
```

ヒストグラムの統計情報の表示を変更できます。
デフォルトだと
``Entries``、
``Mean``、
``Std Dev``の3種類しか表示されないので、少し増やしておきます。

引数はビットのようなものを表しています。
このビットは右から読み、
``Mean``（平均値）、
``Std Dev``（標準偏差）、
``Underflow``、
``Overflow``、
``Integral``、
``Skewness``（歪度）、
``Kurtosis``（尖度）、
に相当します（たぶん）。

最大で9くらいまでいける気がします。
0は「非表示」、
1は「表示」、
2は「エラー付きで表示」です。

```python3
from ROOT import gStyle
gStyle.SetOptStat(112211)
```
