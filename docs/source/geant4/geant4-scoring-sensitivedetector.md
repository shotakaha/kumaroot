# Sensitive Detectorしたい（``G4VSensitiveDetector``）

測定器のヒット情報を取得するために、``G4VSensitiveDetector``を継承したクラスを作成します。
``G4VSensitiveDetector``クラスは純粋仮想クラスであり、
``Initialize``、``ProcessHits``、``EndOfEvent``の3つのメソッドを
自作クラス内で上書きして定義します。

作成したSDインスタンスは、論理ボリュームに設定します。
さらに、SensitiveDetecotrManagerに追加します。

:::{seealso}

- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)

:::

## Hitクラスしたい（``std::tuple``）

```cpp
Hit = std::tuple<G4double, G4double, G4double>
```


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
        SensitiveDetector(const G4String name)
        void Initialize(G4HCofThisEvent *aHCE) override
        void EndOfEvent(G4HCofThisEvent *aHCE) override
        G4bool ProcessHits(G4Step *aStep, G4TouchableHistory *aTouchable) override
}

#endif // SensitiveDetector_h
```

SDのクラスを自作する場合、
``Initialize``、
``EndOfEvent``、
``ProcessHits``、
の3つのメソッドを実装する必要があります。

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
void SensitiveDetector::ProcessHits(G4Step *aStep, G4TouchableHitory *aTouchable)
{
    // スコアリングの本体を記述する
    // ステップのあるジオメトリを取得するためにG4TouchableHistoryを使う

}
```

``ProcessHitss``にスコアリングしたい内容を記述します。
この関数はステップが発生するたびに自動的に呼び出されます。

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
