# 自作ヒットしたい（``std::tuple``）

```cpp
Hit = std::tuple<G4double, G4double, G4double>
```

C++標準の配列コンテナーを使って、ヒット情報をユーザーが定義します。

:::{note}

Geant4講習会2024では、C++標準ライブラリの``std::vector``や``std::tuple``などを使って、自分でイチから実装する方法をオススメしていました。

:::

## 自作ヒットしたい（``G4VHit``）

Geant4には``G4VHit``や``G4VHitsCollection``というヒット用の配列クラスがあります。
「C++はいまいち分からん」というひとは、こちらを使ってみるのもいいかもしれません。
詳しくは[](./geant4-sensor-hit-hitscollection.md)に整理しました。

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-track.md)
- [](./geant4-physicalvolume.md)
- [](./geant4-logicalvolume.md)

:::
