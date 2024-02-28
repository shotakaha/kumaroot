# 石油を作りたい

```cpp
G4NistManager *nist = new G4NistManager::Instance()
G4Element *H = nist->FindOrBuildElement("G_H");
G4Element *C = nist->FindOrBuildElement("G_C");
G4Element *N = nist->FindOrBuildElement("G_N");
G4Element *O = nist->FindOrBuildElement("G_O");
G4Element *S = nist->FindOrBuildElement("G_S");

G4double density;
G4int nelements;

G4Material *Petroleum = new G4Material("Petroleum", density, nelements=5);
Petroleum->AddElement(C, 87.*perCent);
Petroleum->AddElement(H, 14.*perCent);
Petroleum->AddElement(S, 5.*perCent);
Petroleum->AddElement(N, 0.4*perCent);
Petroleum->AddElement(O, 0.5*perCent);
```

石油の成分を調べてみると、産地によって得られる炭化水素の化合物組成は異なるようですが、元素組成はおおよそ
炭素C（83～87％）、
水素H（11～14％）、
硫黄S（5％以下）、
窒素N（0.4％以下）、
酸素O（0.5％以下）、
金属（0.5％以下）となるようです。

