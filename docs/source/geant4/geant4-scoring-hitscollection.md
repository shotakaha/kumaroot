# ヒットしたい（``G4VHit`` / ``G4VHitsCollection`` / ``G4HCofThisEvent``）

測定器のヒット情報は、ユーザーが定義する必要があります。
ヒット用の抽象基底クラスである``G4VHit``を継承して実装します。

``G4Event``を処理する際に、たくさんの``G4VHit``（の派生クラスの）オブジェクトが生成されます。
これらのヒット情報は、配列コンテナー（``G4HitsCollection``と、そのテンプレートクラス``G4THitsCollection``）に集めることができます。

ここでは[Hits - Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/hit.html)を参考に、これらのクラスの使い方を整理します。

:::{note}

Geant4講習会2024では、C++標準ライブラリの``std::vector``や``std::tuple``などを使って、自分でイチから実装する方法をオススメしていました。

:::

## G4VHitしたい

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
    void SetTrackID(G4int track_id) { fTrackID = track_id; };
    G4int GetTrackID() { return fTrackID; };

    void SetChamberNumber(G4int chamber_number) { fChamberNumber = chamber_number; };
    G4int GetChamberNumber() { return fChamberNumber; };

    void SetEnergyDeposit(G4double energy_deposit) { fEnergyDeposit = energy_deposit; };
    G4double GetEnergyDeposit() { return fEnergyDeposit; };

    void SetPosition(G4ThreeVector xyz) { fPosition = xyz; } ;
    G4ThreeVector GetPosition() { return fPosition; };

    void SetGlobalTime(G4double global_time) { fGlobalTime = global_time; };
    G4double GetGlobalTime() { return fGlobalTime; };

  private:
    // 5. 測定したい値を定義する
    G4int fTrackID = -1;
    G4int fChamberNumber = -1;
    G4double fEnergyDeposit = 0.;
    G4ThreeVector fPosition;
    G4double fGlobalTime = -1;
};

// TrackerHitクラスを型にしたテンプレート
using TrackerHitsCollection = G4THitsCollection<TrackerHit>;
```

このサンプルコードは``examples/basic/B2a/TrackerHit.hh``を参照し（ちょっと修正し）ました。
``G4VHit``クラスを継承して、トラッカー（＝飛跡検出器）のヒットを取得する``TrackerHit``クラスを作成しています。

取得したい値はクラス内のプライベート変数で定義すればOKです。
また、それらの変数へのセッターとゲッターも定義しておきます。

クラスを定義したあと、``G4THitsCollection``を使って``TrackerHit``クラスを引数とするテンプレートクラスを定義します。

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
