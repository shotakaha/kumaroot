# デフォルトの色を変更したい（ ``gROOT->GetColor->SetRGB`` ）

```cpp
gROOT->GetColor(3)->SetRGB(0.00, 0.70, 0.00); // 3: Bright Green -> Green
gROOT->GetColor(5)->SetRGB(1.00, 0.50, 0.00); // 5: Bright Yellow -> Orange
gROOT->GetColor(7)->SetRGB(0.15, 0.29, 0.56); // 7: Bright Cyan -> China Blue
gROOT->GetColor(8)->SetRGB(0.22, 0.37, 0.04); // 8: Dull Green -> Leaf Green
gROOT->GetColor(9)->SetRGB(0.50, 0.30, 0.70); // 9: Dull Navy -> Purple
```

ROOTのデフォルト配色は、蛍光が強すぎてとてもとても見えにくい色が何色かあります。
それらを、以下のようにもう少し落ち着いた色に変更します。

| 数値 | デフォルト色 | 変更後の色 |
|---|---|---|
| 1 | 黒 | |
| 2 | 赤 | |
| 3 | 緑（蛍光） | 緑 |
| 4 | 青 | |
| 5 | 黄（蛍光） | 橙 |
| 6 | マゼンタ | |
| 7 | シアン（蛍光） | China Blue |
| 8 | Dull Green | Leaf Green |
| 9 | Dull Navy | Purple |
| 10 | 白 | Purple |

上2つは奥村さんのページからコピペしました。
最後のはシアンを紫っぽい色に変更しました。

RGBの度合いは自分の好みで選んでください。
手順としては、RGBの値を検索（Wikipedia使用すると良い）->
その値を256（ほんとは255かも？）で割るだけです。

```python
from ROOT import gROOT

gROOT.GetColor(3).SetRGB(0.00, 0.70, 0.00); // 3: Bright Green -> Green
gROOT.GetColor(5).SetRGB(1.00, 0.50, 0.00); // 5: Bright Yellow -> Orange
gROOT.GetColor(7).SetRGB(0.15, 0.29, 0.56); // 7: Bright Cyan -> China Blue
gROOT.GetColor(8).SetRGB(0.22, 0.37, 0.04); // 8: Dull Green -> Leaf Green
gROOT.GetColor(9).SetRGB(0.50, 0.30, 0.70); // 9: Dull Navy -> Purple
```

## リファレンス

- [The Rainbow Color Map - ROOT公式ブログ](https://root.cern/blog/rainbow-color-map/)
