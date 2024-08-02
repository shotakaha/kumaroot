# 可変長配列したい（``std::vector``）

```cpp
#include <vector>

std::vector<int> vec{1, 2, 3, 4, 5};  // int型の配列
size_t size = vec.size();             // 配列のサイズ
size_t capacity = vec.capacity();     // 配列の最大サイズ
```

``std::vector``で可変長配列を定義できます。
要素に高速にアクセスできたり、
自動的にメモリ領域を拡張してくれたり、
とても使い勝手のよい設計になっているそうです。

:::{note}

``G4VHitsCollection``は``std::vector``クラスを継承しています。

:::

## 要素を追加したい（``push_back``）

```cpp
std::vector<float> vec{0.1, 0.2, 0.3, 0.4, 0.5};  // float型の配列
vec.push_back(0.6);    // 配列の末尾に追加
```

``push_back``で配列の末尾に要素を追加できます。

## 全要素を削除したい（``clear``）

```cpp
vec.clear()
```

``clear``で配列の要素をすべて削除できます。

## リファレンス

- [std::vector](https://cpprefjp.github.io/reference/vector/vector.html)
