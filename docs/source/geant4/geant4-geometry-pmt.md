# PMTを作りたい（``BuildPMT``）

```cpp
G4LogicalVolume *BuildPMT()
{
    // パラメーター設定
    G4String logical_name{"PMTWindow"};
    G4String material_name{"G4_PLEXIGLASS"};
    G4double radius{3.81 * cm};  // 3in.管
    G4double thickness{1.0 * mm};

    // 形状を定義
    // PMTの入射窓を、平たい円柱で作成
    G4double r_min{0. * cm};
    G4double r_max{radius};
    G4double half_z{0.5 * thickness};
    G4double s_phi{0. * deg};
    G4double d_phi{360. * deg};

    auto solid = new G4Tubs{
        "pmtSolid",
        r_min,    // 内径
        r_max,    // 外径
        half_z,   // 高さ（厚み）
        s_phi,    // 開始角度
        d_phi,    // 回転角
    };

    // 材料を定義
    // 入射窓はプレキシガラス（アクリル）に設定
    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial("G4_PLEXIGLASS");

    // 論理ボリュームを定義
    auto logical = new G4LogicalVolume(
        solid,        // G4VSolid
        material,     // G4Material
        logical_name  // 名前
    );

    return logical;
}
```

光電子増倍管（PMT）の入射窓だけを作成しました。
PMTに入射した光子の数を知りたい場合は、``G4SensitiveDetector``を追加し、データを残す必要があります。

## 光子数を数えたい（``PMTSD``）

光子数を数えるためには、最低限つぎの設定が必要です。

1. **`G4VSensitiveDetector`を継承したクラスを作成する**
   `ProcessHits()`をオーバーライドし、入射してきたトラックが``G4OpticalPhoton``かどうかを判定します。
2. **入射窓の論理ボリュームに`SetSensitiveDetector()`で登録する**
3. **`G4SDManager`にセンシティブディテクターを登録する**
4. **ヒット数をカウントするコンテナ（``G4THitsCollection``など）を用意する**
   イベントごとの光子数を集計し、``EventAction``などで取り出せるようにします。

光子はほとんどの場合、入射窓に到達した時点で吸収・終了させたいので、
``ProcessHits()``内で``track->SetTrackStatus(fStopAndKill)``するのが一般的です。

```cpp
// PMTSD.hh
#pragma once

#include "G4VSensitiveDetector.hh"

class PMTSD : public G4VSensitiveDetector
{
    public:
        PMTSD(const G4String& name);
        G4bool ProcessHits(G4Step* step, G4TouchableHistory*) override;
        G4int GetNumPhotons() const { return fNumPhotons; }

    private:
        G4int fNumPhotons = 0;
};
```

```cpp
// PMTSD.cc
#include "PMTSD.hh"

#include "G4OpticalPhoton.hh"
#include "G4Step.hh"
#include "G4Track.hh"

PMTSD::PMTSD(const G4String& name)
    : G4VSensitiveDetector(name)
{
}

G4bool PMTSD::ProcessHits(G4Step* step, G4TouchableHistory*)
{
    auto track = step->GetTrack();

    // 光子以外のトラックは無視する
    if (track->GetDefinition() != G4OpticalPhoton::OpticalPhotonDefinition()) {
        return false;
    }

    fNumPhotons++;
    track->SetTrackStatus(fStopAndKill);  // 光子はここで吸収・終了させる

    return true;
}
```

``PMTSD``は``ProcessHits()``内でトラックが``G4OpticalPhoton``かどうかを判定し、
該当する場合のみ``fNumPhotons``をインクリメントします。

``BuildPMT()``の中で、入射窓の論理ボリュームにセンシティブディテクターを登録します。

```cpp
G4LogicalVolume *BuildPMT()
{
    // ...（形状・材料の定義は省略）

    auto logical = new G4LogicalVolume(
        solid,        // G4VSolid
        material,     // G4Material
        logical_name  // 名前
    );

    // センシティブディテクターを登録
    auto sd = new PMTSD("PMTSD");
    G4SDManager::GetSDMpointer()->AddNewDetector(sd);
    logical->SetSensitiveDetector(sd);

    return logical;
}
```

これで、PMTの入射窓に光子が入射するたびに``fNumPhotons``がカウントされます。
イベントごとの光子数を集計したい場合は、``EventAction``などから``GetNumPhotons()``を取得してください。

## PMTを配置したい

```cpp
G4LogicalVolume* SetupPmtArray()
{
    // 親ボリューム（別途作成済みのものを使う）
    auto container = BuildWorld();

    // 子ボリューム = PMTを準備する
    auto element = BuildPMT();

    // PMTを5本並べる
    std::vector<int> elements{101, 102, 103, 104, 105};
    for (G4int id: elements) {
        auto rotation = G4RotationMatrix{};
        auto direction = G4ThreeVector{};
        auto origin = G4Transform3D{rotation, direction};
        new G4PVPlacement(
            origin,
            element,
            "Container",
            container,
            false,
            id,  // copy_number
            true
        );
    }

    return container;
}
```

複数本のPMTを配置したいケースは多いと思います。
ここでは横一列に並べようとしています。
