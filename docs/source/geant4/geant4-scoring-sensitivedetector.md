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

## ProcessHits

```cpp

#include "TrackerHit.hh"

G4bool SensitiveDetector::ProcessHits(G4Step *aStep, G4TouchableHistory* /* aTouchable */)
{
    G4debug << "SensitiveDetector::ProcessHits" << G4endl;

    //
    auto pre_step = aStep->GetPreStepPoint();
    auto track = pre_step->GetTrack();
    auto pv = pre_step->GetPhysicalVolume();
    auto lv = pv->GetLogicalVolume();

    // TrackerHitを作成して代入
    // - TrackerHitはG4VHitを継承して、別ファイル（TrackerHit.hh/.cc）に作成
    // - 各種セッターはTrackerHitで定義する
    // - 値をセットするときに単位計算をしておく
    TrackerHit *newHit = new TrackerHit{};
    newHit->SetDetectorID(pv->GetCopyNo());
    newHit->SetTrackID(track->GetTrackID());
    newHit->SetPVName(pv->GetName());
    newHit->SetLVName(lv->GetName());
    newHit->SetGlobalTime(pre_step->GetGlobalTime() / ns);
    newHit->SetXYZ(pre_step->GetPosition() / mm);
    newHit->SetEnergyDeposit(aStep->GetTotalEnergyDeposit() / MeV);
    newHit->SetTrackLength(track->GetTrackLength() / cm);
    newHit->SetStepLength(track->GetStepLength() / cm);

    // ヒット情報を確認
    newHit->Print();

    // ヒット配列にヒットを追加
    fHitsCollection->insert(newHit);

    return true;

}
```

``ProcessHits``は、ヒット情報を処理するメインのメソッドです。

ひとつめの引数は``(G4Step *aStep)``になっているので、
[G4Step操作](./geant4-step.md)や
[G4Track操作](./geant4-track.md)でできることを使って、
取得したい値を定義できます。

ふたつめの引数は``(G4TouchableHistory*)``となっていますが、
これはもう使われてない（obsolete）そうです。

このメソッドは、SD内でステップ処理が発生するたびに自動的に呼び出されます。
（たぶん）G4SDManagerが管理してくれているため、
ユーザーが境界判断しなくていいので楽ちんです。

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-track.md)
- [](./geant4-physicalvolume.md)
- [](./geant4-logicalvolume.md)

:::

## Initialize

```cpp
void SensitiveDetector::Initialize(G4HCofThisEvent *aHCE)
{
    G4debug << "SensitiveDetector::Initialize" << G4endl;

    // ヒット用の配列（TrackerHitsCollection）を初期化
    fHitsCollection = new TrackerHitsCollection{};

    // "ヒット配列名"で、G4SDManagerからヒット配列IDを取得
    // aHCEにTrackerHitsCollectionを追加
    G4int hcID = G4SDManager::GetSDMpointer()->GetCollectionID("ヒット配列名");
    aHCE->AddHitsCollection(hcID, fHitsCollection);

};
```

``Initialize``は、``G4EventManager``がイベント処理を開始する時に実行されます
（``BeginOfEventAction``より先に実行されます）。

ここで、イベントのヒットコレクションを初期化したり、
自前のデータ構造を定義したりします。

## EndOfEvent

```cpp
void SensitiveDetector::EndOfEvent(G4HCofThisEvent *aHCE)
{
    G4debug << "SensitiveDetector::EndOfEvent" << G4endl;

}
```

``EndOfEvent``はイベントの最後に呼ばれます。
ステップごとに足し上げたスコアをヒットコレクションなどに保存します。

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
