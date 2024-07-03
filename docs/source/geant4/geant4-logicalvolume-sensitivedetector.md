# 論理ボリュームをSensitiveDetectorにしたい（``SetSensitiveDetector``）

```cpp
// class SensitiveDetector: public G4VSensitiveDetector とする
auto sensitive_detector = new SensitiveDetector{};
auto logical_volume = G4LogicalVolume{...};
logical_volume->SetSensitiveDetector(sensitive_detector);
```

``SetSensitiveDetector``で、物理量を測定したい論理ボリュームを**SensitiveDetector（有感検出器）**に設定できます。

:::{seealso}

- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)

:::
