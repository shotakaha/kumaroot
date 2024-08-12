# ヒストグラムの見た目を変更したい（``gStyle->SetHistLineWidth``）

```cpp
gStyle->SetHistLineWidth(1);

gStyle->SetHistLineStyle(0);
gStyle->SetHistLineColor(1);

gStyle->SetHistFillStyle(0);
gStyle->SetHistFillColor(1);
```

ヒストグラムの見た目のデフォルト値を変更できます。
外枠線は少し細い気がするので、太くしてもよいと思います。
ただし、たくさんのヒストグラムを重ね描きするときは、埋もれてしまって見えにくくなることもあるので注意が必要です。

```python
from ROOT import gStyle

gStyle.SetHistLineWidth(線幅)

gStyle.SetHistLineColor(色)
gStyle.SetHistLineStyle(スタイル)

gStyle.SetHistFillColor(色)
gStyle.SetHistFillStyle(スタイル)
```
