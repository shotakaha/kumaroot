# ヒットしたい（``G4HCofThisEvent`` / ``G4VHitsCollection`` / ``G4VHit``）

測定器のヒット情報は、ユーザーが実装する必要があります。
Geant4には、``G4VHit``というヒット用の純粋クラスが用意されています。
また、ヒットをリストにした``G4HitsCollection``と、そのテンプレートクラス``G4THitsCollection``もあります。

ここでは、ユーザーズガイドを参考に、これらのクラスの使い方を整理します。

:::{note}

Geant4講習会2024では、C++標準ライブラリの``std::vector``や``std::tuple``などを使って、自分でイチから実装する方法をオススメしていました。

:::

## G4VHitしたい

```cpp
#include "G4VHit.hh"

class TrackerHit : public G4VHit
{
  public:
    // ...省略...

    // ユーザー実装が必要な純粋仮想関数
    void Draw() override;
    void Print() override;

  private:
    // 測定したい値
    G4int fTrackID = -1;
    G4int fChamberNb = -1;
    G4double fEdep = 0.;
    G4ThreeVector fPos;
};

// TrackerHitクラスを型にしたテンプレート
using TrackerHitsCollection = G4THitsCollection<TrackerHit>;
```

このサンプルコードは``examples/basic/B2a/TrackerHit.hh``を参照しました。この``B2a``サンプルでは、トラッカー（＝飛跡検出器）のヒットを取得する``TrackerHit``クラスを自作していました。

保存したい値は、このようなクラスのプライベート変数に定義すればOKです。また、それらの変数へのセッターとゲッターも定義しておきます。

クラスを定義したあと、``G4THitsCollection``を使って``TrackerHit``クラスを引数とするテンプレートクラスを定義します。

## G4HitsCollectionしたい

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

``G4HCofThisEvent``は、``EndOfEvent``の中でアクセスできます。

:::

:::{seealso}

- ``examples/basic/B2/B2a/TrackerHit.hh``
- [G4VHit](https://geant4.kek.jp/Reference/11.2.0/classG4VHit.html)
- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)
- [G4HitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4HitsCollection.html)
- [G4THitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4THitsCollection.html)
- [Hits and Digitisation - Book for Toolkit Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForToolkitDeveloper/html/OOAnalysisDesign/Hit/hit.html)

:::
