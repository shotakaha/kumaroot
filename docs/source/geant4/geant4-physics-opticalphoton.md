# Optical Photonしたい（``G4OpticalPhysics``）

```cpp
#include "G4OpticalPhoton.hh"

auto physics = G4OpticalPhoton::Definition();

// 以下の2つのstaticメソッドはDefinition()と同じ
auto physics = G4OpticalPhoton::OpticalPhotonDefinition();
auto physics = G4OpticalPhoton::OpticalPhoton();
```

**Optical Photon**は原子間の間隔に比べて波長が長い光子のことです。
ガンマ線とは異なり、光子は物質の境界面での反射・透過の物理ロセスを考える必要があります。

Geant4では、ガンマ線（``G4Gamma``）とOptical Photon（``G4OpticalPhoton``）は別々のクラスで定義されていて、お互いが変換されることはありません。

Optical Photonは、
チェレンコフ放射（``G4Cerenkov``）、
シンチレーション光（``G4Scintillation``）、
遷移放射（``G4TransitionRadiation``）
の物理プロセスで放出されます。
