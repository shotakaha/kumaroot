# ヒストグラムの線の太さを一括で変更したい（ ``gStyle->SetHistLineWidth`` ）

```cpp
gStyle->SetHistLineWidth(2)
```

デフォルトの外枠線は少し細い気がするので、太くしておきます。
ただし、たくさんのヒストグラムを重ね描きするときは、埋もれてしまって見えにくくなることもあるので注意が必要です。

```python
from ROOT import gStyle

gStyle.SetHistFillColor(色)
gStyle.SetHistFillStyle(スタイル)
gStyle.SetHistLineColor(色)
gStyle.SetHistLineStyle(スタイル)
gStyle.SetHistLineWidth(線幅)
```
