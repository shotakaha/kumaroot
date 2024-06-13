# エタノールを作りたい（``G4_ETHYL_ALCOHOL``）

```cpp
G4NistManager *nm = G4NistManager::Instance()
G4Material *ethanol = nm->FindOrBuildMaterial("G4_ETHYL_ALCOHOL")
```
