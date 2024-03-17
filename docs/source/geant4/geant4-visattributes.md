# 可視化したい（``G4VisAttributes``）

```cfg
/vis/set/color 0. 0. 1. 0.5    # [red] [green] [blue] [alpha]
/vis/viewer/set/style wireframe
/vis/geometry/set/visibility ボリューム名 0 true
```

```cpp
G4Colour color = G4Colour(0., 0., 1., 0.5);    // red, green, blue, alpha
G4VisAttributes *attributes = new G4VisAttributes(color);
attributes->SetVisibility(true);
attributes->SetForcedWireframe(true);
pLogicalVolume->SetVisAttributes(attributes);
```
