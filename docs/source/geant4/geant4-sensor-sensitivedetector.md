# SensitiveDetectorしたい（`G4VSensitiveDetector`）

`G4VSensitiveDetector`は、
測定器／検出器内での有感領域で発生したヒットを収集するための抽象基底クラスです。

ユーザーはこのクラスを継承して、自作のSensitiveDetectorクラスを実装できます。
Geant4のイベント処理の枠組みに統合されており、測定に関する処理を`UserSteppingAction`などで一からを一から実装も記述するよりも、簡潔かつ効率的に実装できます。

:::{note}

**簡潔かつ効率的に実装**できるのですが、SensitiveDetectorの枠組み

:::

## 親クラス（`public G4VSensitiveDetector`）

- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.2.0/classG4VSensitiveDetector.html)

```cpp
class G4VSensitiveDetector {
  public:
    explicit G4VSensitiveDetector(G4String name);
    virtual ~G4VSensitiveDetector() = default;
    virtual void Initialize(G4HCofThisEvent*) {};
    virtual void EndOfEvent(G4HCofThisEvent*) {};
    virtual G4bool ProcessHits(G4Step *aStep, G4TouchableHistory* /*ROhist*/) = 0;
}
```

親クラス（`G4VSensitiveDetector`）の主要なメンバー関数を抜粋しました。
コンストラクターとデストラクターは、親クラスの設定を継承して使用できます。

`ProcessHits()`は、ステップが有感検出器の中にあるときに呼ばれる純粋仮想関数で、必ずオーバーライドする必要があります。

`Initialize()`はイベントの開始時に呼ばれる仮想関数で、
ヒットコレクションの初期化などに使用します。
`EndOfEvent()`はイベントの終了時に呼ばれる仮想関数で、
ヒットコレクションの登録処理などに使用します。
どちらの仮想関数も、必要に応じてオーバーライド可能です。

## Sensor

```cpp
// include/Sensor.hh

#ifndef Sensor_h
#define Sensor_h 1

#include "SensorHit.hh"

#include "G4HCofThisEvent.hh"
#include "G4Step.hh"
#include "G4TouchableHistory.hh"
#include "G4VSensitiveDetector.hh"

namespace ToyMC
{

class Sensor : public G4VSensitiveDetector
{
  public:
    Sensor(const G4String &name);
    ~Sensor() = default;

  public:
    void Initialize(G4HCofThisEvent *aHCE) override;
    void EndOfEvent(G4HCofThisEvent *aHCE) override;
    G4bool ProcessHits(G4Step *aStep, G4TouchableHistory *aTouchable) override;
};

  private:
    // SensorHitクラスで定義した型エイリアスを使って
    // 有感検出器で必要なヒット配列を準備する。
    G4int fHcID = 0;
    SensorHitsCollection *fHitsCollection{nullptr};

};  // namespace ToyMC

#endif // Sensor_h
```

上記サンプルでは、``G4VSensitiveDetector``クラスを継承して、汎用的なセンサーを仮定した``Sensor``クラスを作成しました。

``G4VSensitiveDetector``クラスは抽象基底クラスで、
``Initialize``、``ProcessHits``、``EndOfEvent``の3つの仮想関数を持っています。
これらのメソッドをoverrideして定義します。

## コンストラクター（``Sensor::Sensor``）

```cpp
Sensor::Sensor(const G4String &name) : G4VSensitiveDetector{name}
{
    ;
}
```

``SensorHit``クラスのコンストラクターで、親の``G4VSensitiveDetector``クラスの初期化が必要です。
引数（``name``）をそのまま使って、初期化リストで初期化しています。

:::{note}

``G4VSensitiveDetector``のコンストラクターには``explicit``キーワードが付けられています。
これは、**暗黙の型変換を防ぐ** ためのキーワードです。

```cpp
// OK
G4VSensitiveDetector detector{"DetectorName"};

// NG
// G4String -> G4VSensitiveDetector に勝手に変換されるのを防止
G4VSensitiveDetector detector = "DetectorName";
```

:::

## 初期化したい（``Sensor::Initialize``）

```cpp
// src/Sensor.cc

#include "Sensor.hh"

void Sensor::Initialize(G4HCofThisEvent *aHCE)
{
    // ヒット配列を初期化
    fHitsCollection = new SensorHitsCollection{};
    aHCE->AddHitsCollection(fHcID, fHitsCollection);
};
```

``Initialize``は、``G4EventManager``がイベント処理を開始する時に実行されます（``BeginOfEventAction``より先に実行されます）。

``G4HCofThisEvent``は、ひとつイベント（``G4Event``）に紐づいたヒット配列（``G4HitsCollection``）です。

イベントの開始時に、このヒット配列を初期化しておきます。

## 集計したい（``Sensor::EndOfEvent``）

```cpp
// src/Sensor.cc

#include "Sensor.hh"

void Sensor::EndOfEvent(G4HCofThisEvent *aHCE)
{
    G4int entries = fHitsCollection->entries();
    // ヒット配列を取得
    aHCE->Get...

};
```

``EndOfEvent``はイベントの最後に呼ばれます。
``G4HCofThisEvent``からヒット配列を取り出し、
ヒット配列のデータを集計したり、
ファイルに書き出したりできます。

## ヒット処理したい（``Sensor::ProcessHits``）

```cpp
// src/Sensor.cc

#include "Sensor.hh"

#include "G4Step.hh"

G4bool Sensor::ProcessHits(G4Step *aStep, G4TouchableHistory* /* aTouchable */) {

    // ヒットを残さない場合

    // 例1: エネルギー損失がない
    if (aStep->GetTotalEnergy() <= 0) {
        return false;
    }

    // 例2: 中性粒子
    if (aStep->GetTrack()->...粒子の電荷を取得 == 0) {
        return false;
    }

    // ヒット処理の準備
    auto pre_step = aStep->GetPreStepPoint();
    auto track = aStep->GetTrack();
    auto pv = aStep->GetPreStepPoint()->GetPhysicalVolume();
    auto lv = pv->GetLogicalVolume();

    // SensorHitオブジェクトを作成
    auto hit = new SensorHit{};

    // ヒット情報を代入
    // - SensorHit::Fill(G4Step *aStep)のカスタム関数を追加
    // - SensorHitの内部変数に値を代入
    hit->Fill(aStep);

    // 代入したヒット情報を確認
    hit->Print();

    // ヒット配列にヒット（SensorHit）を追加
    fHitsCollection->insert(hit);

    return true;
};
```

``ProcessHits``はSensitiveDetectorのヒット情報を処理するときのメインの関数です。
データを残すかどうかの条件や、
どのようなデータを取得するかは、
ユーザーがこの関数の中で実装します。
この関数は、ステップが有感検出器の中にあるとき、自動的に呼ばれます。

ひとつめの引数は``(G4Step *aStep)``になっているので、
[G4Step操作](./geant4-step.md)や
[G4Track操作](./geant4-track.md)でできることを使って、
取得したい値を定義できます。
ふたつめの引数は``(G4TouchableHistory*)``となっていますが、
これはもう使われてない（obsolete）そうです。

:::{hint}

おそらく[UserSteppingAction](./geant4-user-steppingaction.md)の亜種です。
（たぶん）G4SDManagerが管理してくれているため、ステップが有感検出器の中にあるとき、ユーザーが境界判断しなくても、自動的に呼ばれます。
SensitiveDetectorを使う方が楽ちんです。

測定器のヒット情報を知りたい場合は、SensitiveDetectorだけを定義すればOKです。

:::

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-track.md)
- [](./geant4-logicalvolume.md)
- [](./geant4-physicalvolume.md)

:::

## 有感検出器を設定したい（``SetSensitiveDetector``）

```cpp
#include "Geometry.hh"
#include "Sensor.hh"

#include "G4SDManager.hh"

void Geometry::ConstructSDandField()
{
    // Sensorを作成
    auto sensor = new Sensor("検出器名");

    // 論理ボリュームに割り当て
    SetSensitiveDetector("論理ボリューム名", sensor);

    // SDManagerに追加
    auto sm = G4SDManager::GetSDMpointer();
    sm->AddNewDetector(sensor);
}
```

有感検出器として利用するためには、
``Sensor``クラスのオブジェクトを論理ボリュームに割り当て、
さらに``G4SDManager``に登録します。

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
- [Hits - Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/hit.html)
- [Geometry - Book for Toolkit Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForToolkitDeveloper/html/OOAnalysisDesign/Geometry/geometry.html)
