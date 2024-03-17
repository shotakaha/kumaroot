# Sensitive Detectorしたい（``G4VSensitiveDetector``）

測定器のヒット情報を取得するためには、論理ボリュームにSensitive Detector（以下SD）を設定します。
SDは[G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)クラスを継承して作成します。
ひとつの論理ボリュームに複数のSDを設定できます。

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
