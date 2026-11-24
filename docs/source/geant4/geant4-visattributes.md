# 可視化したい（`G4VisAttributes`）

```cpp
#include "G4VisAttributes.hh"

G4Colour color(0., 0., 1., 0.5);    // red, green, blue, alpha
G4VisAttributes* attributes = new G4VisAttributes(color);
attributes->SetVisibility(true);
attributes->SetForceWireframe(true);
logicVolume->SetVisAttributes(attributes);
```

```cfg
/vis/geometry/set/colour Envelope 0 0 0 1 0.5    # [論理ボリューム名] [深さ] [red] [green] [blue] [opacity]
/vis/geometry/set/visibility Envelope 0 true
/vis/viewer/set/style wireframe
```

ボリュームの色、表示、描画スタイルは、`G4VisAttributes`で設定します。
マクロでは`/vis/geometry/set/*`コマンドで設定できます。

`logicVolume`は、色を設定したい`G4LogicalVolume`です。

:::{seealso}

- [G4VisAttributes](https://geant4.kek.jp/Reference/11.4.0/classG4VisAttributes.html)

:::
