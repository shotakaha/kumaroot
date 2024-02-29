# マテリアルしたい（``G4NistManager``）

```cpp
#include "G4NistManager.hh"

G4NistManager *nistManager = new G4NistManager::GetInstance();

G4Element *H = nistManager->FindOrBuildElement("G4_H")
G4Element *O = nistManager->FindOrBuildElement("G4_O")

G4Material *H2O = nistManager->FindOrBuildMaterial("G4_WATER")
G4Material *Air = nistManager->FindOrBuildMaterial("G4_AIR")
```

``G4NistManager``を使って、NISTの材料データベースにある元素や化合物などのマテリアルを作成できます。
元素（``G4Element``）が欲しい時は``FindOrBuildElement``メソッド、
物質（``G4Material``）が欲しい時は``FindOrBuildElement``メソッドを使います。

利用可能なマテリアル名は[Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)を参照してください。
水素（``G4_H``）からカリフォルニウムまでの元素や、
水（``G4_WATER``）、空気（``G4_AIR``）、
素粒子・原子核実験でよく利用するような材料（``G4_lXe``、``G4_PbWO4``、``G4_STAINLESS-STEEL``、``G4_Galactic``（＝真空））なども定義されています。

一般的な物質が欲しい場合は、まずこのリストから探すのがよいと思います。
