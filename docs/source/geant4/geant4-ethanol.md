# エタノールを作りたい（``G4_ETHYL_ALCOHOL``）

```cpp
G4NistManager *nist = G4NistManager::Instance()
G4Material *Ethanol = nist->FindOrBuildMaterial("G4_ETHYL_ALCOHOL")
```

