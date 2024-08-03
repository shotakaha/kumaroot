# OpticalPhysicsしたい（``G4OpticalPhysics``）

```cpp
int main()
{
    G4VModularPhysicsList *physics = new FTFP_BERT{};
    G4OpticalPhysics *optical_physics = new G4OpticalPhysics{};

    physics->RegisterPhysics(optical_physics);
    rm->SetUserInitialization(physics);
}
```

``FTFP_BERT``モデルに``OpticalPhysics``を追加しています。

**Optical Photon**は原子間の間隔に比べて波長が長い光子のことです。
ガンマ線とは異なり、光子は物質の境界面での反射・透過の物理ロセスを考える必要があります。

Geant4では、ガンマ線（``G4Gamma``）とOptical Photon（``G4OpticalPhoton``）は別々のクラスで定義されていて、お互いが変換されることはありません。

Optical Photonは、チェレンコフ放射（``G4Cerenkov``）や
シンチレーション光（``G4Scintillation``）の物理プロセスで放出されます。

また、
吸収（``G4OpAbsorption``）、
レイリー散乱（``G4OpRayleigh``）、
ミー散乱（``G4OpMieHG``）、
波長変換（``G4OpWLS``と``G4OpWLS2``）、
境界での散乱（``G4OpBoundary``）、
の物理プロセスを通じて相互作用します。
