# 軸の目盛り間隔を変更したい（ ``gStyle->SetNdivisions`` ）

```cpp
gStyle->SetNdivisions(TTSSPP)

// デフォルト50分割
gStyle->SetNdivisions(000510)

// 100分割にしたい
gStyle->SetNdivisions(020510)

```

| 引数 | 説明 |
|---|---|
| ``PP`` | 軸全体の分割数 |
| ``SS`` | PP分割された目盛り１つ分の分割数 |
| ``TT`` | SS分割された目盛り１つ分の分割数 |

デフォルトは510になっています。
``PP=10``、
``SS=05``、
``TT=00``という設定値になっていて、
軸を10分割して、
その1目盛りを5分割、
ということで全体で50目盛りになります。

全体を100目盛りにする場合は、``20510``にします。
（10分割、その1目盛りを5分割、さらにその1目盛りを2分割 ＝100目盛り）

```python
from ROOT import gStyle
gStyle.SetNdivisions(000510)
```
