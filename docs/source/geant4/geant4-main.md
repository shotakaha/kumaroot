# メイン関数したい（``main()``）

```cpp
// ユーザー定義クラスを読み込む
#include "Geometry.hh"
#include "ActionInitialization.hh"

// Geant4のクラスを読み込む
#include "G4RunManagerFactory.hh"
#include "FTFP_BERT.hh"    // 標準の物理モデルのひとつ

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    // ジオメトリの設定
    auto geometry = new Geometry{};
    rm->SetUserInitialization(detector);

    // 物理モデルの設定
    auto physics = new FTFP_BERT{};
    rm->SetUserInitialization(physics);

    // ユーザーアクションの設定
    auto actions = new ActionInitialization{};
    rm->SetUserInitialization(actions);

    // 実験開始
    rm->Initialize();
    G4int n_events = 100;
    rm->BeamOn(n_events);

    // 実験終了
    delete rm;
    return 0;
}
```

Geant4でシミュレーションを実行する場合の、
バッチモード用の必要最低限の`main()`関数の構成例です。

このサンプルでは、次の3つの要素を設定しています。

1. `geometry` : `G4VUserDetectorConstruction`を継承したユーザー定義クラス
2. `physics` : `FTFP_BERT`（Geant4標準の物理モデルのひとつ）
3. `actions` : `G4VUserActionInitialization`を継承したユーザー定義クラス

:::{seealso}

- [](./geant4-user-detectorconstruction.md)
- [](./geant4-user-physicslist.md)
- [](./geant4-user-actioninitialization.md)
- [](./geant4-user-runaction.md)
- [](./geant4-user-eventaction.md)
- [](./geant4-user-trackingaction.md)
- [](./geant4-user-steppingaction.md)

:::

## クラスが呼ばれる順番

```cpp
{
G4RunManagerFactory::CreateRunManager();
new Geometry{};
new FTFP_BERT{};
new ActionInitialization{};
ActionInitialization::BuildForMaster();

// G4RunManager::Initializeを実行すると、測定器がセットアップがされる
G4RunManager::Initialize();
Geometry::Construct() {
    SetupVolumes()
};
Geometry::ConstructSDandField() {
    new TrackerSD{"/TrackerSD", "TrackerHitsCollection"}
    new TrackerSD{"/ShieldSD", "ShieldHitsCollection"}
};

// G4RunManager::BeamOn()を実行すると、入射粒子がセットアップされる
G4RunManager::BeamOn()
ActionInitialization::Build();
new PrimaryGenerator{};
PrimaryGenerator::GeneratePrimaries() {
    SetupGunMuons();
};
// 有感検出器での処理
TrackerSD::Initialize();
TrackerSD::ProcessHits() {
    TrackerHit::operator new
    TrackerHit::TrackerHit()
    TrackerHit::Fill()
    TrackerHit::Print()
}
TrackerSD::ProcessHits() { ... }
TrackerSD::ProcessHits() { ... }
TrackerSD::EndOfEvent()
{
    "File opened: mc_data/kamaboko_00000_2024-07-30T13h05m.csv"
    TrackerHit::ToCsvString();
    TrackerHit::ToCsvString();
    TrackerHit::ToCsvString();
    "File closed: mc_data/kamaboko_00000_2024-07-30T13h05m.csv"
    TrackerHit::operator delete
}
delete G4RunManager();
delete Geometry();
delete FTFP_BERT();
delete ActionInitialization();
```

クラスが呼ばれる順番を確認しました。
``G4RunManager::Initialize``すると測定器がセットアップされることを確認しました。
``G4RunManager::BeamOn``すると入射粒子がセットアップされることを確認しました。
有感検出器（ここでは``TrackerSD``）のヒット処理の流れを確認しました。

## リファレンス

- [How to Define the main() Program](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html)
