# SDManagerしたい（``G4SDManager``）

```cpp
auto sm = G4SDManager::GetSDMpointer();
```

``GetSDMpointer()``で``G4SDManager``クラスを取得できます。
``G4SDManager``クラスはスレッドローカルになっています。
また、シングルトンになっていて、どこからでもこの方法で参照できます。

## 有感検出器を登録したい（``AddNewDetector``）

```cpp
// 有感検出器を作成
auto sensor = new Sensor("検出器名");

// SDManagerに追加
auto sm = G4SDManager::GetSDMpointer();
sm->AddNewDetector(sensor);
```

## 有感検出器を一覧したい（``ListTree``）

```cpp
auto sm = G4SDManager::GetSDMpointer();
sm->ListTree()

// G4WT0 > /
// G4WT0 > /TrackerSD   *** Active
// G4WT0 > /ShieldSD   *** Active
```

``ListTree``でSDManagerに登録されている有感検出器の名前と状態を確認できます。
``G4VSensitiveDetector::Initialize``の中で、
デバッグ用に確認したいときに便利です。

## HCtableしたい（``GetHCtable``）

```cpp
auto sm = G4SDManager::GetSDMpointer();
auto table = sm->GetHCtable();

G4int n_tables = table->entries();
G4debug << "HCtables= " << n_tables << G4endl;
for (G4int i = 0; i < n_tables; i++) {
    G4debug << "SDname= " << table->GetSDname(i) G4endl;
    G4debug << "HCname= " << table->GetHCname(i) G4endl;
}
```

``GetHCtable``でSDManagerに登録されているHCtableを確認できます。
また``GetSDName``で有感検出器の名前、
``GetHCname``でヒット配列の名前を取得できます。

## ヒット配列のIDをしりたい（``GetCollectionID``）

```cpp
auto sm = G4SDManager::GetSDMpointer();
G4int hcID = sm->GetCollectionID("ヒット配列名");
G4ind hcID = sm->GetCollectionID(ヒット配列名オブジェクト);
```

``GetCollectionID``でヒット配列のIDを取得できます。
IDをしりたいヒット配列の"名前"もしくはオブジェクトを引数に設定します。

## リファレンス

- [G4SDManager](https://geant4.kek.jp/Reference/11.2.0/classG4SDManager.html)
- [G4HCtable](https://geant4.kek.jp/Reference/11.2.0/classG4HCtable.html)
