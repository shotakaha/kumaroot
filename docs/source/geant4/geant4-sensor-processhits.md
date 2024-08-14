# ヒットの判断したい（``Sensor::ProcessHits``）

```cpp
G4bool Sensor::ProcessHits(G4Step *aStep) {};
```

有感検出器のヒットの条件はユーザーが定義する必要があります。
とはいえ、実際の検出器では、それぞれ測定できる物理量に特徴があります。
Geant4の付属サンプルなどを参考に、検出器ごとにどのようにヒット判断しているかを整理しました。

## カロリメーターしたい

```cpp
G4bool Sensor::ProcessHits(G4Step *aStep) {
    G4double energy_deposit = aStep->GetTotalEnergyDeposit();

    if (energy_deposit == 0.) {
        return false;
    }

    auto hit = new SensorHit{}
    hit->Fill(aStep);
};
```

カロリーメータはエネルギーを測定する検出器です。
検出器の中でエネルギーを落とさなかったイベントは、
スキップします。

## ドリフトチェンバーしたい

```cpp
G4bool Sensor::ProcessHits(G4Step *aStep) {

    G4double charge = aStep->GetTrack()->GetDefinition()->GetPDGCharge();

    if (charge == 0.) {
        return false;
    }

    auto hit = new SensorHit{};
    hit->Fill(aStep);

};
```

``examples/basic/B5``サンプルを参考にしました。

ドリフトチェンバーは、荷電粒子が通過した位置を測定する検出器です。
（基本的に）中性粒子には反応しないため、
電荷を持たないトラックはスキップします。

## 光電子増倍管したい

```cpp
G4bool Sensor::ProcessHits(G4Step *aStep) {
    auto particle = aStep->GetTrack()->GetDefinition()

    if (particle != G4OpticalPhoton::Definition()) {
        return false;
    };

    auto hit = new SensorHit{};
    hit->Fill(aStep);
}
```

``extended/optical/LXe``サンプルを参考にしました。
光電子増倍管は、イベントで発生した光子の数を測定する検出器です。
粒子の種類が``opticalphoton``でない場合は、スキップします。

:::{note}

``GetDefinition``と比較する場合は
``G4OpticalPhoton::Definition``、
``GetParticleName``と比較する場合は
``"opticalphoton"``です。

:::
