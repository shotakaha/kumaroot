# Sensitive Detectorしたい（``G4VSensitiveDetector``）

```cpp
#ifndef SensitiveDetector_h
#define SensitiveDetector_h 1

#include "G4HCofThisEvent.hh"
#include "G4Step.hh"
#include "G4TouchableHistory.hh"
#include "G4VSensitiveDetector.hh"

class SensitiveDetector : public G4VSensitiveDetector
{
  public:
    SensitiveDetector(const G4String name);
    void Initialize(G4HCofThisEvent *aHCE) override;
    void EndOfEvent(G4HCofThisEvent *aHCE) override;
    G4bool ProcessHits(G4Step *aStep, G4TouchableHistory *aTouchable) override;
}

#endif // SensitiveDetector_h
```

測定器のヒット情報を取得するために、論理ボリュームを``SensitiveDetector``に設定します。
``SensitiveDetector``は、``G4VSensitiveDetector``クラスを継承してユーザーが作成します。

``G4VSensitiveDetector``クラスは抽象基底クラスで、
``Initialize``、``ProcessHits``、``EndOfEvent``の3つの仮想関数を持っています。
これらのメソッドをoverrideして定義します。

作成したSesnsitiveDetectorは、論理ボリュームに追加し、
さらに、G4SDManagerに追加します。
詳しくは[](./geant4-logicalvolume-sensitivedetector.md)に整理しました。

:::{seealso}

- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)
- [Hits - Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/hit.html)
- [Geometry - Book for Toolkit Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForToolkitDeveloper/html/OOAnalysisDesign/Geometry/geometry.html)

:::

## 自作ヒットしたい（``std::tuple``）

```cpp
Hit = std::tuple<G4double, G4double, G4double>
```

C++標準の配列コンテナーを使って、ヒット情報をユーザーが定義します。

## 自作ヒットしたい（``G4VHit``）

Geant4には``G4VHit``や``G4VHitsCollection``というヒット用の配列クラスがあります。
「C++はいまいち分からん」というひとは、こちらを使ってみるのもいいかもしれません。
詳しくは[](./geant4-scoring-hitscollection.md)に整理しました。

:::{note}

Geant4講習会2024では、C++標準ライブラリの``std::vector``や``std::tuple``などを使って、自分でイチから実装する方法をオススメしていました。

:::

## Initialize

```cpp
void SensitiveDetector::Initialize(G4HCofThisEvent *aHCE)
{


}
```

``Initialize``はイベントの開始時に呼ばれます。
このイベントのヒットコレクションを初期化します。
自前のデータ構造も定義できます。

## EndOfEvent

```cpp
void SensitiveDetector::EndOfEvent(G4HCofThisEvent *aHCE)
{

}
```

``EndOfEvent``はイベントの最後に呼ばれます。
ステップごとに足し上げたスコアをヒットコレクションなどに保存します。

## ProcessHits

```cpp
void SensitiveDetector::ProcessHits(G4Step *aStep, G4TouchableHitory* /* aTouchable */)
{
    // スコアリングの本体を記述する
    // *aTouchableはobsolete

    // ステップ操作
    G4double step_length = aStep->GetStepLength();
    G4double energy_deposit = aStep->GetEnergyDeposit();

    // ステップポイント操作
    G4StepPoint *pre_step = aStep->GetPreStepPoint();
    G4ThreeVector xyz = pre_step->GetPosition();
    G4double time = pre_step->GetGlobalTime();

    // ボリューム操作
    auto pv = pre_step->GetPhysicalVolume();
    G4String pv_name = pv->GetName();
    G4int pv_number = pv->GetCopyNo();
    auto lv = pv->GetLobicalVolume();
    G4Material material = lv->GetMaterial();
    G4double mass = lv->GetMass();
}
```

``ProcessHitss``にスコアリングしたい内容を記述します。
この関数はステップが発生するたびに自動的に呼び出されます。

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-track.md)
- [](./geant4-physicalvolume.md)
- [](./geant4-logicalvolume.md)

:::

## 論理ボリュームに割り当てたい（``SetSensitiveDetector``）

```cpp
G4VPhysicalVolume* DetectorConstruction::Construct()
{
    // 自作のSDインスタンスを作成する
    SensitiveDetector *pSD = new SensitiveDetector("/myDetector/検出器名");

    // SD管理者に追加する
    auto sdManager = G4SDManager::GetSDMpointer();
    sdManager->AddNewDetector(pSD);

    // 論理ボリュームに割り当てる
    SetSensitiveDetector(pLogicalVolume, pSD);
}
```

``DetectorConstruction::Construct``で、論理ボリュームにSensitiveDetectorを設定します。
設定の手順は以下のとおりです。

1. 自作SDのインスタンスを作成します
2. SD Managerに追加します
3. SDにしたい論理ボリュームに割り当てます
