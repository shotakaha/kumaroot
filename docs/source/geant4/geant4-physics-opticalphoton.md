# Optical Photonしたい（``G4OpticalPhysics``）

**Optical Photon**は原子間の間隔に比べて波長が長い光子のことです。
ガンマ線とことなり、光子は物質の境界面での反射・透過の物理ロセスを考えないといけません。

そのため、チェレンコフ光（``G4Cerenkov``）や
シンチレーション光（``G4Scintillation``）などの光子は、ガンマ線（``G4Gamma``）とは別の粒子として定義されています。

```cpp
#include "G4OpticalPhoton.hh"

auto physics = G4OpticalPhoton::Definition();

// 以下の2つのstaticメソッドはDefinition()と同じ
auto physics = G4OpticalPhoton::OpticalPhotonDefinition();
auto physics = G4OpticalPhoton::OpticalPhoton();
```

## 物理モデルに追加したい

```cpp
int main()
{
    G4VModularPhysicsList *physics_list = new FTFP_BERT;
    G4OpticalPhysics *optical_physics = new G4OpticalPhysics();

    physics_list->RegisterPhysics(optical_physics);
    runManager->SetUserInitialization(physics_list);
}
```

``G4OpticalPhysics``の物理コンストラクターを、物理リストに追加することで、光子のふるまいを扱えるようになります。

- ``G4Cerenkov``
- ``G4Scintillation``
- ``G4OpAbsorption``
- ``G4OpRaylegh``
- ``G4OpMieHG``
- ``G4OpWLS``、``G4OpWLS2``
- ``G4OpBoundary``

