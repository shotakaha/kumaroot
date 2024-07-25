# SensitiveDetectorしたい（``G4VSensitiveDetector``）

```cpp
class Sensor : public G4VSensitiveDetector
{
  public:
    Sensor();
    ~Sensor() override;

  public:
    void Initialize() override;
    void EndOfEvent() override;
    G4bool ProcessHits(G4Step *aStep) override;
}
```

## 有感検出器を設定したい（``SetSensitiveDetector``）

```cpp
#include "Geometry.hh"
#include "Sensor.hh"

#include "G4SDManager.hh"

void Geometry::ConstructSDandField()
{
    auto sensor = Sensor("検出器名");
    SetSensitiveDetector("ボリューム名", sensor);

    auto sm = G4SDManager::GetSDMpointer();
    am->AddNewDetector(sensor);
}
```

``G4VUserDetectorConstruction``から継承した
``ConstructSDandField``関数の中で、
論理ボリュームを有感検出器（``SensitiveDetector``）に設定します。

ここでは``G4VUserDetectorConstruction``が持っているprotectedなメンバー関数``SetSensitiveDetector``を使っています。
この関数は、論理ボリュームの名前を使って有感検出器を設定できます。

:::{seealso}

``G4LogicalVolume``もpublicなメンバー関数``SetSensitiveDetector``を持っています。
そちらを使って有感検出器を設定する方法もあります。

- [](./geant4-logicalvolume-sensitivedetector.md)

:::

## リファレンス

- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)
- [G4VUserDetectorConstruction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserDetectorConstruction.html)
