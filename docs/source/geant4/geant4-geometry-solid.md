# 形状を作成する（``G4VSolid``）

```cpp
G4Box("name", half_x, half_y, half_z);
G4Tubs("name", r_min, r_max, half_z, s_phi, d_phi);
```

箱型（``G4Box``）、円柱型（``G4Tubs``）など基本的な立体クラスが用意されています。
これらは``G4VSolid``を継承したクラスになっています。
また、これらのクラスから作ったオブジェクトをブーリアン演算して、より複雑な形を作ることもできるようです。

実際に、どのような立体クラスがあり、どういう引数が必要なのかはクラスリファレンスを参照してください。

:::{hint}

公式のドキュメントやクラスリファレンスには、使い方の参考になるサンプルコードがありません。
基本的には、クラスリファレンスでクラス名とその引数を確認して、実際に使ってみる必要があります。

:::

:::{seealso}

- [G4VSolid](https://geant4.kek.jp/Reference/11.2.0/classG4VSolid.html)
- [G4Box](https://geant4.kek.jp/Reference/11.2.0/classG4Box.html)
- [G4Tubs](https://geant4.kek.jp/Reference/11.2.0/classG4Tubs.html)

:::
