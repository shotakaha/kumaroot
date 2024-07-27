# ヒット情報したい（``G4VHit``）

有感検出器でのヒット情報を格納するためには
``G4VHit``クラスを継承したクラスを作成します。

## 親クラス

- [G4VHit](https://geant4.kek.jp/Reference/11.2.0/classG4VHit.html)

```cpp
G4VHit() = default;
virtual G4VHit() = default;
virtual void Draw() {};
virtual void Print() {};
```

コンストラクターとデストラクターはデフォルトのままでOKです。
``Draw()``は、イベントを描画するときのヒット点の見た目を調整する関数です。
``Print()``は、ヒットの情報を出力する関数です。
どちらも仮想関数になっているため、必要に応じて自作クラスでoverrideします。

## SensorHitクラス

```cpp
#ifndef SensorHit_h
#define SensorHit_h 1

#include "G4VHit.hh"

class SensorHit : public G4VHit
{
  public:
    // 1. コンストラクターなどを定義
    SensorHit() = default;
    ~SensorHit() = default;

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
using SensorHitsCollection = G4THitsCollection<SensorHit>;

#endif
```

測定器のヒット情報は、ユーザーが定義する必要があります。
このサンプルコードは``examples/basic/B2a/TrackerHit.hh``を参照し（ちょっと修正し）ました。

有感検出器でのヒットを取得する``SensorHit``クラスを、
``G4VHit``クラスを継承して作成しています。

``G4VHit``はヒット用の抽象基底クラスで、
``Draw``と``Print``の2つの仮想関数を持っています。
これらのメソッドをoverrideして定義します。

また、``new``と``delte``をインライン関数で作成しています。
これは、サンプルコードをそのまま真似しました。

ヒット情報として取得したい物理量は、プライベート変数で定義しています。
また、それらの変数へのセッターとゲッターもpublicメソッドで定義してあります。

クラスを定義したあと、``G4THitsCollection``を使って``TrackerHit``クラスを引数とするテンプレートクラスを定義してあります。
ここも、サンプルコードをそのまま真似しました。

``G4Event``を処理する際に、たくさんの``G4VHit``（の派生クラスの）オブジェクトが生成されます。
これらのヒット情報は、配列コンテナー（``G4HitsCollection``と、そのテンプレートクラス``G4THitsCollection``）に集めることができます。

```{toctree}
geant4-sensor-hit-print
geant4-sensor-hit-draw
geant4-sensor-hit-allocator
geant4-sensor-hit-hitscollection
geant4-sensor-hit-hitsmap
```

## 有感検出器とヒット用クラス

このページでは「汎用的なヒット」という意味で``SensorHit``としました。
可能な限りすべてのデータを取得してファイルに書き出し、
解析でフィルタリングしようという魂胆です。
こういうことができるのが、シミュレーションのおもしろい部分かなと思います。

もし、具体的な検出器があり、その完全再現を目指すならば、それらに特化したクラスを作成するとよいかもしれません。

:::{hint}

1. 飛跡検出器 → ``TrackerHit``
1. カロリメーター → ``CaloHit``
1. ホドスコープ → ``HodoHit``
1. ピクセル検出器 → ``PixelHit``
1. 光電子増倍管 → ``PmtHit``
1. MPPC → ``MppcHit``

:::

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

## リファレンス

- ``examples/basic/B2/B2a/TrackerHit.hh``
- [G4VHit](https://geant4.kek.jp/Reference/11.2.0/classG4VHit.html)
- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)
- [G4HitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4HitsCollection.html)
- [G4THitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4THitsCollection.html)
- [Hits - Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/hit.html)
- [Hits and Digitisation - Book for Toolkit Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForToolkitDeveloper/html/OOAnalysisDesign/Hit/hit.html)
