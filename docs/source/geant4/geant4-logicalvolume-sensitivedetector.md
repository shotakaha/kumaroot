# 論理ボリュームにSensitiveDetectorを設定したい（``SetSensitiveDetector``）

```cpp
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4Material.hh"
#include "G4SDManager.hh"
#include "G4Step.hh"
#include "G4TouchableHistory.hh"
#include "G4VSensitiveDetector.hh"

// G4VSensitiveDetector を継承して、SensitiveDetector を作る
class SensitiveDetector : public G4VSensitiveDetector {
 public:
  explicit SensitiveDetector(const G4String& name) : G4VSensitiveDetector(name) {}

  G4bool ProcessHits(G4Step* aStep, G4TouchableHistory* rOhist) override;
};

// 論理ボリュームを作り、SensitiveDetector を設定する
void Build(G4Box* solid, G4Material* material)
{
  auto sensitive_detector = new SensitiveDetector("SensitiveDetector");
  auto logical_volume = new G4LogicalVolume(solid, material, "LogicalVolume");
  logical_volume->SetSensitiveDetector(sensitive_detector);

  // G4SDManagerに追加
  auto sm = G4SDManager::GetSDMpointer();
  sm->AddNewDetector(sensitive_detector);
}
```

ヒット情報を取得したい論理ボリュームに``SensitiveDetector``を設定します。
``SensitiveDetector``は、``G4VSensitiveDetector``クラスを継承して自分で作成します。
また、``G4SDManager``にも追加する必要があります。

SensitiveDetectorを設定した論理ボリュームの中をステップが通るたびに``ProcessHits(G4Step* aStep, G4TouchableHistory* rOhist)``が呼ばれます。
このメソッドで、記録するヒットを選びます。

具体的な設定は
[](./geant4-scoring-sensitivedetector.md)と
[](./geant4-scoring-hitscollection.md)に
整理しました。

## SensitiveDetectorが必要か判断したい

SensitiveDetectorは、検出器のヒット情報を、体積ごとにイベントのデータとして集めるための仕組みです。
次の表で、必要かどうかを判断できます。

| 状況 | SensitiveDetector | 代わりの方法 |
| --- | --- | --- |
| 検出器のヒット（エネルギー付与、位置、時刻など）を、体積ごとに集めたい | 必要 | - |
| 1イベントの合計値（線量、エネルギー付与の合計など）だけが欲しい | 不要 | スコアリング（`G4ScoringManager`、`G4MultiFunctionalDetector`） |
| 遮蔽材、空気、ワールドなど、測定しない体積 | 不要 | - |
| 飛跡の描画だけをしたい | 不要 | 可視化の機能 |

:::{note}

SensitiveDetectorを設定していない体積では、`ProcessHits()`は呼ばれません。
エラーや警告は出ないので、ヒットが記録されないときは、まずその体積にSensitiveDetectorが設定されているかを確認してください。

:::

## SensitiveDetectorを使う利点

SensitiveDetectorを使うと、ヒットの記録を次の点で簡単にできます。

- **体積の判定をGeant4に任せられる**：`G4UserSteppingAction`で自分が体積を判定しなくても、SensitiveDetectorを設定した体積のステップだけで`ProcessHits()`が呼ばれます。
- **ヒットをイベントごとに整理できる**：ヒットは`G4VHitsCollection`にまとめられ、イベントの終わりに`G4HCofThisEvent`から取り出せます。
- **マルチスレッドに対応しやすい**：ワーカースレッドごとにSensitiveDetectorが作られ、ヒットもスレッドごとに集められます。自分でスレッドの扱いを書く必要はありません。
- **ほかの機能と連携できる**：スコアリング（`G4MultiFunctionalDetector`）や、ヒットの可視化と組み合わせられます。

一方で、ヒットのクラスを作る手間が増えます。
記録する情報が少なく、1つの体積の合計値だけで済むなら、`G4UserSteppingAction`で数える方が簡単な場合もあります。

:::{seealso}

ここでは個別の論理ボリュームにSensitiveDetectorを設定する方法を紹介しましたが、多くのサンプルでは、ジオメトリ用クラスの``ConstructSDandField``の中で``SetSensitiveDetector``を呼んでいます。
マルチスレッドでは、この関数がワーカースレッドごとに呼ばれるため、スレッドごとにSensitiveDetectorを作れます。
詳しくは次のページを参照してください。

- [](./geant4-sensitivedetector.md)

:::

## リファレンス

- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.4.0/classG4LogicalVolume.html)
- [G4VSensitiveDetector](https://geant4.kek.jp/Reference/11.4.0/classG4VSensitiveDetector.html)
