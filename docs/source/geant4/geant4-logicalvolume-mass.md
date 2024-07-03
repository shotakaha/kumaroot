# 論理ボリュームの質量をしりたい（``GetMass``）

```cpp
G4double mass = logical_volume->GetMass();
```

``GetMass``で論理ボリュームの質量を取得できます。
論理ボリュームには形状と材料（＝密度）を与えているため、
質量を計算してくれます。
