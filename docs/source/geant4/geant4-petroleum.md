# 石油を作りたい

```cpp
G4NistManager *nm = new G4NistManager::Instance()
G4Element *H = nm->FindOrBuildElement("G_H");
G4Element *C = nm->FindOrBuildElement("G_C");
G4Element *N = nm->FindOrBuildElement("G_N");
G4Element *O = nm->FindOrBuildElement("G_O");
G4Element *S = nm->FindOrBuildElement("G_S");

G4double density;
G4int nelements;

G4Material *petroleum = new G4Material("Petroleum", density, nelements=5);
petroleum->AddElement(C, 87.*perCent);
petroleum->AddElement(H, 14.*perCent);
petroleum->AddElement(S, 5.*perCent);
petroleum->AddElement(N, 0.4*perCent);
petroleum->AddElement(O, 0.5*perCent);
```

石油の成分を調べてみると、産地によって得られる炭化水素の化合物組成は異なるようですが、元素組成はおおよそ
炭素C（83～87％）、
水素H（11～14％）、
硫黄S（5％以下）、
窒素N（0.4％以下）、
酸素O（0.5％以下）、
金属（0.5％以下）となるようです。

