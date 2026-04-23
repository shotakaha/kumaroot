# グローバルな乱数生成器したい（`gRandom`）

```cpp
#include <TRandom.h>
// gRandomを使って乱数を生成
double randomValue = gRandom->Uniform(0, 1);  // 0から1の一様乱数を生成
```

`gRandom`は、ROOTの乱数生成器のグローバルインスタンスです。
デフォルトは`TRandom3`ですが、必要に応じて他の乱数生成器に切り替えることもできます。

```cpp
#include <TRandomMixMax.h>
// gRandomをTRandomMixMaxに切り替える
gRandom = new TRandomMixMax();
```

`gRandom`を直接書き換えることで、全体で使用される乱数生成器を変更できます。
複数の乱数生成器を同時に使用する場合は、個別にインスタンスを作成する必要があります。

:::{note}

ROOTの公式ドキュメントを参照すると、`TRandom3`は完全な乱数生成器ではないようです。
このドキュメントでは、より高品質な`TRandomMixMax`を使ってみます。

:::
