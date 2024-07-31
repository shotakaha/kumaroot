# ヒット配列したい（``G4VHitsCollection`` / ``G4THitsCollection``）

```cpp
G4THitsCollection<SensorHit> hit_collection;
```

ひとつイベントで発生した複数のヒットは、``SensorHit``型を持つヒット配列として保存します。
ヒット配列は``G4THitsCollection``テンプレートクラスを使って定義します。

``G4THitsCollection``は``G4VHitsCollection``を継承したテンプレートクラスですが、そのさらに親をたどると``std:vector``をベースにしているようです。

## 親クラス

- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)

```cpp
G4VHitsCollection() = default;
G4VHitsCollection(G4String detector_name, G4String collection_name);
virtual ~G4HitsCollection() = default;
virtual void DrawAllHits(){};
virtual void PrintAllHits(){};
virtual G4VHit* GetHit(size_t) const {return nullptr;};
virtual size_t GetSize() const {return 0;};
```

``G4THitsCollection``クラスは、``G4VHitsCollection``クラスを継承したテンプレートクラスです。
コンストラクターとデストラクターは、親クラスのものをそのまま使っているようです。
``GetHit``と``GetSize``は、テンプレートクラスでoverrideして再定義しています。

## テンプレートクラス

- [G4THitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4THitsCollection.html)

```cpp
G4THitsCollection();
G4THitsCollection(G4String detector_name, G4String collection_name);
~G4THitsCollection() override;
inline void* operator new(size_t);
inline void operator delete(void* aHC)
void DrawAllHits() override;
void PrintAllHits() override;
inline size_t insert(T* aHit);
inline size_t entries() const;
G4VHit* GetHit(size_t i) const override { return ((std::vector<T*>*)theCollection)[i]; };
size_t GetSize() const override { return ((std::vector<T*>*)theCollection)->size(); };
```

``G4THitsCollection``クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターの引数は、親クラスを引き継いで定義されています。
``GetHit``と``GetSize``は、内部変数``theCollection``に対する処理として再定義されています。
またその内部変数にヒットを追加するための``insert``が追加されています。

## 型エイリアスしたい（``using`` / ``typedef``）

```cpp
// C++11で導入された文法
// using コレクション名 = G4THitsCollection<ヒットクラス名>;
using SensorHitsCollection = G4THitsCollection<SensorHit>;
SensorHitsCollection hit_collection{};
SensorHitsCollection hit_collection{"DetectorName", "CollectionName"};
```

``G4THitsCollection<SensorHit>``型は名前が長いため、型エイリアスを定義して
``SensorHitsCollection``型という名前で使えるようにします。

:::{note}

``using``はC++11以降で使える型エイリアスの宣言です。
以前は``typedef``が使われていました。
基本的には同じことができるそうなのですが、高機能な``using``を使えばよいようです。

```cpp
// C言語から使われている文法
// typedef G4THitsCollection<ヒットクラス名> コレクション名;
typedef G4THitsCollection<SensorHit> SensorHitsCollection;
SensorHitsCollection hit_collection();
SensorHitsCollection hit_collection("DetectorName", "CollectionName");
```

## SensorHitクラス

``SensorHitsCollection``型は、``SensorHit``クラスのファイルの中で定義します。

```cpp
//////////////////////////////////////////////////
// SensorHit.hhで定義
// 0. 型エイリアスを
using SensorHitsCollection = G4THitsCollection<SensorHit>;

//////////////////////////////////////////////////
// Initializeの処理
// 1. ヒット配列を作成
// SDに指定したSDName、HCNameと対応させるとよいです
auto hitCollection = new SensorHitsCollection{"DetectorName", "CollectionName"};

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
