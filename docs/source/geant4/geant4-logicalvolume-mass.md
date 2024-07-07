# 論理ボリュームの質量をしりたい（``GetMass``）

```cpp
G4double mass = logical_volume->GetMass();

G4debug << "mass= " << mass / g << " [g]" << G4endl;
G4debug << "mass= " << G4BestUnit(mass, "Mass") << G4endl;
```

``GetMass``で論理ボリュームの質量を取得できます。
論理ボリュームには形状と材料（＝密度）を与えているため、
質量が計算できます。
