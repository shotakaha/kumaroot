# キャンバスを無地にしたい（ ``gROOT->SetStyle`` ）

```cpp
gROOT->SetStyle("Plain");
```

:::{note}

``ROOT v5.30`` 以前はキャンバスの背景が灰色だったのでこの設定が必須でした。
それ以降のバージョンはデフォルトで無地になっているので、この設定は必要はありません。

ちなみに、いないと思いますが、昔のキャンバス（＝灰色っぽいやつ）を使う場合は
 ``Classic`` を指定します。
:::

```python
from ROOT import gROOT
gROOT.SetStyle("Plain");
```
