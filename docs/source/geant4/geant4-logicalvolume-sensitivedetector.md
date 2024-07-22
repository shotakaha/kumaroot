# 論理ボリュームにSensitiveDetectorを設定したい（``SetSensitiveDetector``）

```cpp
// class SensitiveDetector: public G4VSensitiveDetector とする
auto sensitive_detector = new SensitiveDetector{};
auto logical_volume = G4LogicalVolume{...};
logical_volume->SetSensitiveDetector(sensitive_detector);

// SDManagerに追加
auto sm = G4SDManager::GetSDMpoint();
sm->AddNewDetector(sensitive_detector);
```

ヒット情報を取得したい論理ボリュームを``SensitiveDetector``に設定します。
``SensitiveDetector``は、``G4VSensitiveDetector``クラスを継承してユーザーが作成します。
また、``G4SDManager``にも追加する必要があります。

SDに設定した論理ボリュームに粒子が入射すると``ProcessHits(G4Step *aStep)``が呼ばれます。
そのメソッドの中で、ヒット情報を取捨選択します。

具体的な設定は
[](./geant4-scoring-sensitivedetector.md)と
[](./geant4-scoring-hitscollection.md)に
整理しました。

:::{seealso}
- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)

:::
