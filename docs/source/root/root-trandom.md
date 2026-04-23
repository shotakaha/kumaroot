# 乱数生成したい（`TRandomMixMax`）

```cpp
#include <TRandomMixMax.h>

// 乱数生成器を初期化
TRandomMixMax rng;

// 0から1の一様乱数を生成
double randomValue = rng.Uniform(0, 1);
```

`TRandomMixMax`は、ROOTが提供する乱数生成器のひとつです。
高品質な乱数を生成するためのアルゴリズムを採用しています。

:::{note}

これまでは`TRandom3`を使うことが一般的でしたが、
最近は`TRandomMixMax`が推奨されているようです。

:::

## シードしたい

```cpp
TRandomMixMax rng(42);
```

乱数生成器を初期化する際にシード値を指定できます。
同じシード値を使用すると、同じ乱数列が生成されます。

## 精密な乱数生成したい（`TRandomRanluxpp`）

```cpp
#include <TRandomRanluxpp.h>
// 精密な乱数生成器を初期化
TRandomRanluxpp rng;
```

`TRandomRanluxpp`は、より高精度な乱数生成器です。
とくに科学的なシミュレーションに適しています。

## C++11で乱数生成したい（`std::mt19937`）

```cpp
#include <random>

// 乱数生成器を初期化
std::mt19937 rng(42);
// 0から1の一様乱数を生成
double randomValue = std::uniform_real_distribution<double>(0, 1)(rng);
```

`std::mt19937`は、C++11で導入された乱数生成器です。
Mersenne Twisterアルゴリズムを使用しており、高速で高品質な乱数を生成します。
ROOTの乱数生成器と組み合わせて使用できます。
