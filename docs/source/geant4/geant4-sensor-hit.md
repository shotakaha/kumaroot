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
#include "G4Step.hh"

namespace ToyMC
{

class SensorHit : public G4VHit
{
  public:
    // 1. コンストラクターなどを定義
    SensorHit() = default;
    ~SensorHit() = default;

    // 2. new / delete を実装
    inline void* operator new(size_t);
    inline void operator delete(void* hit);

    // 3. 仮想関数 を実装
    void Draw() override;
    void Print() override;

    // 4. カスタム関数
    void Fill(G4Step *aStep);


  private:
    // 5. 測定したい値を定義する
    G4int fDetectorID{-1};
    G4int fCopyNumber{-1};
    G4int fReplicaNumber{-1};
    G4int fTrackID{-1};
    G4int fStepID{-1};
    G4double fEnergyDeposit{0.};
    G4ThreeVector fXYZ{};
    G4double fGlobalTime{0.};
    G4double fStepLength{0.};
    G4double fTrackLength{0.};

};

// __________________________________________________
// SensorHitクラス型のヒット配列テンプレートの型エイリアス
using SensorHitsCollection = G4THitsCollection<SensorHit>;

// __________________________________________________
// スレッドローカルなメモリアロケーターの定義
// マルチスレッド環境で、スレッドごとにメモリを確保
extern G4ThreadLocal G4Allocator<SensorHit> *SensorHitAllocator;

// __________________________________________________
inline void *SensorHit::operator new(size_t)
{
    // new演算子:
    // コンストラクターの前に実行される特殊関数
    // SensorHitに必要なメモリをG4Allocatorで割り当てる

    if (!SensorHitAllocator) {
        SensorHitAllocator = new G4Allocator<SensorHit>;
    }
    return (void *)SensorHitAllocator->MallocSingle();
}

// __________________________________________________
inline void SensorHit::operator delete(void *hit)
{
    // delete演算子
    // デストラクターの後に実行される特殊関数
    // new演算子で割り当てたメモリを解放する
    SensorHitAllocator->FreeSingle((SensorHit *)hit);
}

}; // namespace ToyMC
#endif
```

測定器のヒット情報は``G4VHit``クラスを継承してユーザーが定義する必要があります。
ヒット情報の取得／ファイル出力はGeant4シミュレーションで結果を得るためにとても大事なアイテムです。
しかし、初心者向けの解説を見つけることができず、このクラスの役割を理解するのにかなり苦戦しました。
ここでは、その汗と涙と努力の結晶をまとめてみました。

サンプルコードは``examples/basic/B2a/TrackerHit.hh``を参考に改変しました。
有感検出器でヒットを取得するクラスを``SensorHit``クラスと名づけました。
このクラスの役割は次のとおりです。

1. コンストラクター／デストラクターは親クラスを引き継ぐ
2. ``SensorHit``型のヒット配列の型エイリアスを定義する（``SensorHitsCollection``）
3. スレッドローカルなメモリ割り当てを定義する（``SensorHitAllocator``）
4. 最適なメモリ管理のため``new``演算子／``delete``演算子を定義する
5. ``Draw()``／``Print()``をoverrideして定義する
6. ``Fill(G4Step *aStep)``と必要なprivate変数を定義する

たくさんの役割／処理が登場するので、順番に紹介します。

## コンストラクターとデストラクター

```cpp
public:
  SensorHit() = default;
  ~SensorHit() = default;
```

``SensorHit``クラスの初期化／削除するときに実行されるコンストラクターとデストラクターは、親クラス（``G4VHit``）を引き継いでおきます。
ユーザーがカスタマイズする必要はありません。

## 型エイリアス: ``SensorHitsCollection``

```cpp
using SensorHitsCollection = G4THitsCollection<SensorHit>;
```

``SensorHitsCollection``という名前の型エイリアスを定義しています。

``G4THitsCollection``は、親をたどると``std:vector``型をベースにしたテンプレートクラスです。
なので``SensorHit``型を要素に持つ``std:vector``配列とイメージしておけばよいと思います。

```cpp
// Sensor.cc
auto fHitsCollection = new SensorHitsCollection{}
```

有感検出器のヒット情報（``SensorHit``）を格納する配列（``SensorHitsCollection``）として使います。
具体的な使い方は[Sensorクラス](./geant4-sensor-sensitivedetector.md)を参照してください。

## G4ThreadLocalとG4Allocator

```cpp
extern G4ThreadLocal G4Allocator<SensorHit> *SensorHitAllocator;
```

``SensorHitAllocator``という名前で、スレッド別にメモリ領域を割り当てるアロケーターを定義しています。
詳細は[](./geant4-sensor-hit-allocator.md)に整理しました。

## ``new``演算子と``delete``演算子

```cpp
public:
  inline void* operator new(size_t);
  inline void operator delete(void* hit);
```

``new``演算子は、コンストラクターの前に実行される特殊関数です。
ここで``SensorHitAllocator``を使って、``SensorHit``クラスに必要なメモリ領域を割り当てます。

``delete``演算子は、デストラクターの後に実行される特殊関数です。
前述した``new``演算子で割り当てたメモリ領域を解放します。

## ``Draw()``と``Print()``関数

``Draw``と``Print``は仮想関数です。
必要であればこれらををoverrideして定義します。

- [](./geant4-sensor-hit-print.md)
- [](./geant4-sensor-hit-draw.md)

## ``Fill(G4Step *aStep)``関数

``Fill``は僕が追加したカスタム関数です。
``G4Step``を引数と渡し、``Fill``の中でprivate変数に値を直接代入するという設計です。
これにより、private変数ごとのゲッター／セッターを作成する必要がなくなります。

```{toctree}
geant4-sensor-hit-print
geant4-sensor-hit-draw
geant4-sensor-hit-hitsmap
geant4-sensor-hit-hcofthisevemt
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

``G4Event``を処理する際に、たくさんの``G4VHit``（の派生クラスの）オブジェクトが生成されます。
これらのヒット情報は、配列コンテナー（``G4HitsCollection``と、そのテンプレートクラス``G4THitsCollection``）に集めることができます。

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
