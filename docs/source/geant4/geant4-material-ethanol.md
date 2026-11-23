# エタノールを作りたい（``G4_ETHYL_ALCOHOL``）

```cpp
G4NistManager *nm = G4NistManager::Instance()
G4Material *ethanol = nm->FindOrBuildMaterial("G4_ETHYL_ALCOHOL")
```

:::{seealso}

- [G4Material](https://geant4.kek.jp/Reference/11.2.0/classG4Material.html)
- [G4NistManager](https://geant4.kek.jp/Reference/11.2.0/classG4NistManager.html)

:::
