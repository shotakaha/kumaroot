# 論理ボリュームの外観を設定したい（``SetVisAttributes``）

```cpp
// 青色（G4Colour::Blue()）
logical_volume->SetVisAttributes(G4Colour::Blue());

// 非表示
logical_volume->SetVisAttributes(G4VisAttributes::GetInvisible());

// RGB指定など
G4VisAttributes vis = G4VisAttributes{};
vis->SetColour(red, gree, blue, alpha);
vis->SetLineStyle("unbroken");  // unbroken | dashed | dotted
vis->SetLineWidth(2.0);
logical_volume->SetVisAttributes(vis);
```

Qtウィンドウに表示されるジオメトリの可視化状態を設定できます。
``G4VisAttributes``クラスを使うと詳細に設定できます。

:::{seealso}

- [G4VisAttributes](https://geant4.kek.jp/Reference/11.2.0/classG4VisAttributes.html)
- [G4Colour](https://geant4.kek.jp/Reference/11.2.0/classG4Colour.html)
- [原色大辞典](https://www.colordic.org/)

:::
