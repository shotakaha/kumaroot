# アクリルを作りたい

```cpp
G4NistManager *nist = G4NistManager::Instance()
G4Element H = nist->FindOrBuildElement("G4_H")
G4Element C = nist->FindOrBuildElement("G4_C")
G4Element O = nist->FindOrBuildElement("G4_O")

G4Material *Acrylic = new G4Material("Acrylic", density=1.18*g/cm3, nelements=3);
Acrylic->AddElement(C, 5);
Acrylic->AddElement(O, 2);
Acrylic->AddElement(H, 8);
```

アクリル材（アクリル樹脂）はNISTデータになかったので、自分で作ります。
構成する元素の情報はNISTデータを参照しています。
