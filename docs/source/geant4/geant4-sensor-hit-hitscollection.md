# ヒット配列したい（``G4VHitsCollection`` / ``G4THitsCollection``）

```cpp
//////////////////////////////////////////////////
// SensorHit.hhで定義
// 0. 型エイリアスを
using SensorHitsCollection = G4THitsCollection<SensorHit>;

//////////////////////////////////////////////////
// Initializeの処理
// 1. ヒット配列を作成
auto hitCollection = new SensorHitsCollection{"HitsCollection", "SensorHit"};

//////////////////////////////////////////////////
// ProcessHitsの処理
// 2. ヒットを新しく作成
SensorHit *hit = new SensorHit{};
hit->Fill(aStep);  // G4Step *aStep とする

// 3. ヒット配列にヒットを追加
// ここでは同じヒットを複数回追加しているが、
// 実際には別のステップで取得したヒットを追加する
hitCollection->insert(hit);
hitCollection->insert(hit);
hitCollection->insert(hit);
hitCollection->insert(hit);

//////////////////////////////////////////////////
// EndOfEventの処理
// 4. データを確認
G4int entries = hitCollection->entries();
for (G4int i = 0; i < entries; i++)
{
    //SensorHit * h = (*hitCollection)[i]
    SensorHit *h = hitCollection->GetHit(i);
    h->Print();
}
```

有感検出器でヒットがあった場合のヒット配列の処理の流れを、
ユーザー定義が必要な関数と対応させてみました。

## 型エイリアスしたい（``using`` / ``typedef``）

```cpp
// C++11で導入された文法
// using コレクション名 = G4THitsCollection<ヒットクラス名>;
using SensorHitsCollection = G4THitsCollection<SensorHit>;

// C言語から使われている文法
// typedef G4THitsCollection<ヒットクラス名> コレクション名;
typedef G4THitsCollection<SensorHit> SensorHitsCollection;
```

ユーザーが作成したヒットクラス（ここでは``SensorHit``）を使って、ヒット配列（``SensorHitsCollection``）の型エイリアスを定義しています。

``G4THitsCollection``は``G4VHitsCollection``を継承したテンプレートクラスですが、そのさらに親をたどると``std:vector``をベースにしているようです。

サンプルをいくつか確認すると``typedef``と``using``で定義されているケースがありました。
基本的には同じことができるのですが、高機能な``using``を使えばよいようです。

## リファレンス

- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)
- [G4THitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4THitsCollection.html)
