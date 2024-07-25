# マテリアルしたい（``G4Material``）

```cpp
G4NistManager *nm = new G4NistManager::Instance();
G4Material *pWater = nm->FindOrBuildMaterial("G4_WATER");
```

``G4Material``を使って素材を作成します。

現実世界と同じように、Geant4の世界でも
物質（``G4Material``）は元素（``G4Element``）の組み合わせ、
元素は同位体（``G4Isotope``）の組み合わせで合成できるようになっています。

標準的な素材の場合、``G4NistManager``を使ってNISTのデータベースにある物質や元素を参照して使うのが簡単です。

:::{toctree}
geant4-material-nistmanager
geant4-material-table
geant4-material-material
geant4-material-element
geant4-material-isotope
:::
