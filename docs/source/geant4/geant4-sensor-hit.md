# ヒット操作したい（``G4VHit`` / ``G4VHitsCollection`` / ``G4HCofThisEvent``）

```cpp
#include "G4VHit.hh"

class TrackerHit : public G4VHit
{
  public:
    // 1. コンストラクターなどを定義
    // 2. new / delete を実装
    inline void* operator new(size_t);
    inline void operator delete(void*);

    // 3. 純粋仮想関数 を実装
    void Draw() override;
    void Print() override;

    // 4. セッター／ゲッターを定義
    void SetDetectorID(G4int copy_number) { fDetectorID = copy_number; };
    G4int GetDetectorID() const { return fDetectorID; };

    void SetTrackID(G4int track_id) { fTrackID = track_id; };
    G4int GetTrackID() const { return fTrackID; };

    void SetEnergyDeposit(G4double energy_deposit) { fEnergyDeposit = energy_deposit; };
    G4double GetEnergyDeposit() const { return fEnergyDeposit; };

    void SetPosition(G4ThreeVector xyz) { fXYZ = xyz; } ;
    G4ThreeVector GetPosition() const { return fXYZ; };

    void SetGlobalTime(G4double time) { fGlobalTime = time; };
    G4double GetGlobalTime() const { return fGlobalTime; };

    void SetTrackLength(G4double length) { fTrackLength = length; };
    G4double GetTrackLength() const { return fTrackLength; };

    void SetStepLength(G4double length) { fStepLength = length; };
    G4double GetStepLength() const { return fStepLength; };

  private:
    // 5. 測定したい値を定義する
    G4int fDetectorID{-1};
    G4int fTrackID{-1};
    G4double fEnergyDeposit{0.};
    G4ThreeVector fXYZ{};
    G4double fGlobalTime{0.};
    G4double fStepLength{0.};
    G4double fTrackLength{0.};

};

// TrackerHitクラスを型にしたテンプレート
using TrackerHitsCollection = G4THitsCollection<TrackerHit>;
```

測定器のヒット情報は、ユーザーが定義する必要があります。
このサンプルコードは``examples/basic/B2a/TrackerHit.hh``を参照し（ちょっと修正し）ました。
``G4VHit``クラスを継承して、トラッカー（＝飛跡検出器）のヒットを取得する``TrackerHit``クラスを作成しています。

``G4VHit``はヒット用の抽象基底クラスで、
``Draw``と``Print``の2つの仮想関数を持っています。
これらのメソッドをoverrideして定義します。

また、``new``と``delte``をインライン関数で作成しています。
これは、サンプルコードをそのまま真似しました。

ヒット情報として取得したい物理量は、プライベート変数で定義しています。
また、それらの変数へのセッターとゲッターもpublicメソッドで定義してあります。

クラスを定義したあと、``G4THitsCollection``を使って``TrackerHit``クラスを引数とするテンプレートクラスを定義してあります。
ここも、サンプルコードをそのまま真似しました。

## Print

```cpp
void TrackerHit::Print()
{
    G4debug << "TrackerHit::Print" << G4endl;

    G4debug << "DetectorID" << fDetectorID << G4endl;
    G4debug << "TrackID" << fTrackID << G4endl;
    G4debug << "XYZ" << G4BestUnit(fXYZ, "Length") << G4endl;
    G4debug << "GlobalTime" << G4BestUnit(fGlobalTime, "Time") << G4endl;
    G4debug << "EnergyDeposit" << G4BestUnit(fEnergyDeposit, "Energy") << G4endl;
    G4debug << "TrackLength" << G4BestUnit(fTrackLength, "Length") << G4endl;
    G4debug << "StepLength" << G4BestUnit(fStepLength, "Length") << G4endl;
};
```

``Print``で、ヒット配列の値を確認しています。

## Draw

```cpp
void TrackerHit::Draw()
{
    G4debug << "TrackerHit::Draw" << G4endl;
    auto vm = G4VVisManager::GetConcreteInstance();
    if (vm)
    {
        G4Circle circle(fXYZ);
        circle.SetScreenSize(4.);
        circle.SetFillStyle(G4Circle::filled);
        G4VisAttributes color{G4Colour::Red()};
        circle.SetVisAttributes(color);
        vm->Draw(circle);
    };
};
```

``Draw``で、可視化するときのヒット点の見た目を設定できます。

## ヒット情報したい（``G4VHit``）

``G4Event``を処理する際に、たくさんの``G4VHit``（の派生クラスの）オブジェクトが生成されます。
これらのヒット情報は、配列コンテナー（``G4HitsCollection``と、そのテンプレートクラス``G4THitsCollection``）に集めることができます。

ここでは[Hits - Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/hit.html)を参考に、これらのクラスの使い方を整理します。

## メモリ管理したい（``G4Allocator``）

```cpp
#include "G4VHit.hh"
#include "G4Allocator.hh"

class TrackerHit : public G4VHit
{
    inline void* operator new(size_t);
    inline void operator delete(void*);
};

//////////////////////////////////////////////////
// （スレッドローカルな）グローバル変数を定義
extern G4ThreadLocal G4Allocator<TrackerHit>* TrackerHitAllocator;

//////////////////////////////////////////////////
inline void* TrackerHit::operator new(size_t)
{
    // new演算子でメモリを割り当てるとき
    // {
    //     TrackerHit *hit = new TrackerHit();
    // }
    // 1. TrackerHitAllocatorに割り当てられたメモリのポインターを取得する
    // 2. 初期化されてない場合は、新しくG4Allocator<TrackerHit>オブジェクトを作成
    if(!TrackerHitAllocator) {
        TrackerHitAllocator = new G4Allocator<TrackerHit>;
    }
    return (void *) TrackerHitAllocator->MallocSingle();
};

//////////////////////////////////////////////////
inline void TrackerHit::operator delete(void *hit)
{
    // delete演算子でメモリを解放するとき
    //
    // {
    //     TrackerHit *hit = new TrackerHit();
    //     delete hit
    // }
    //
    // 1. TrackerHitAllocatorに割り当てられたメモリのポインターを解放する
    TrackerHitAllocator->FreeSingle((TrackerHit*)hit);
};
```

``G4Allocator``は、ヒープ領域に高速にメモリを割り当ててくれるGeant4のクラスです。
このクラスは必須ではありませんが、C++のメモリ管理に詳しくない場合は使うことがオススメされています。
自作したヒットクラスの中で、``new``演算子と``delete``演算子をインライン関数でオーバーロードして、
``G4Allocator``を使うようにカスタマイズしています。

## ヒット配列したい（``G4VHitsCollection`` / ``G4THitsCollection``）

```cpp
// C++11で導入された文法
// using コレクション名 = G4THitsCollection<ヒットクラス名>;
using TrackerHitsCollection = G4THitsCollection<TrackerHit>;

// C言語から使われている文法
// typedef G4THitsCollection<ヒットクラス名> コレクション名;
typedef G4THitsCollection<TrackerHit> TrackerHitsCollection;
```

``G4THitsCollection``は``G4VHitsCollection``を継承したテンプレートクラスです。
引数に自作のヒットクラス名をして、ヒット配列を生成できます。

サンプルをいくつか確認すると``typedef``と``using``で定義されているケースがありました。
基本的には同じことができるのですが、高機能な``using``を使えばよいようです。

## ヒット辞書したい（``G4THitsMap``）

``G4HitsMap``は、辞書型で保存できるヒット配列です。
イベントごとにデータを出力せず、積算する場合に使います。

## イベントのヒットしたい（``G4HCofThisEvent``）

```cpp
// SensitiveDetector: public G4VSensitiveDetector

void SensitiveDetector::EndOfEvent(G4HCofThisEvent *aHC) {

    // HitsCollectionの数を取得する
    G4int nHC = aHC->GetNumberOfCollections();

    for (G4int i=0; i<nHC; i++) {
        auto hc = aHC->GetHC(i);
        G4int nHit = hc->GetSize();
        for (G4int j=0; j<nHit; j++) {
            auto hit = hc->GetHit(j);
        }
    }
}
```

``G4Event``は``G4HCofThisEvent``というヒット配列を持っています。
イベントごとのヒット情報は、このオブジェクト（のポインター）を介してアクセスてきます。

:::{seealso}

- ``examples/basic/B2/B2a/TrackerHit.hh``
- [G4VHit](https://geant4.kek.jp/Reference/11.2.0/classG4VHit.html)
- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)
- [G4HitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4HitsCollection.html)
- [G4THitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4THitsCollection.html)
- [Hits - Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/hit.html)
- [Hits and Digitisation - Book for Toolkit Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForToolkitDeveloper/html/OOAnalysisDesign/Hit/hit.html)

:::
