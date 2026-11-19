# シングルトン・パターン

シングルトン・パターンとは、あるクラスのインスタンスをプログラム全体で1つだけに制限し、どこからでも同じインスタンスにアクセスできるしくみです。
Geant4の主要クラスでは、このシングルトン・パターンが採用されており、
ユーザーはプログラムのどこからでも同じインスタンスにアクセスできます。

ここでは、ユーザーのコードから直接使うことが多いシングルトンだけを紹介します。

## 全体を制御したい（`G4RunManager`）

```cpp
auto rm = G4RunManager::GetRunManager();
```

`G4RunManager`はGeant4シミュレーション全体を統括する中核的なシングルトンです。
ジオメトリの構築（`G4VUserDetectorConstruction`）、
物理プロセスの定義（`G4VUserPhysicsList`）、および
ユーザーアクション（`G4UserRunAction`など）を登録し、
シミュレーションの初期化、実行、終了までの一連の流れを管理します。

:::{seealso}

詳しくは[](./geant4-run-manager.md)に整理しました。

:::

## 材質したい（`G4NistManager`）

```cpp
auto nm = G4NistManager::Instance();
```

`G4NistManager`は、NISTに準拠した元素や物質を簡単に取得・生成できるシングルトンです。
これにより、どこからでも同じ物質データにアクセスできます。

:::{seealso}

詳しくは
[](./geant4-material-nmmanager.md)
に整理しました。

:::

## Materialしたい（`G4MaterialTable`）

```cpp
auto table = G4Material::GetMaterialTable();
for (auto* material: *table) {
    G4cout << material->GetName()
    << " rho= " << material->GetDensity()/(g/cm3)
    << " g/cm3" << G4endl;
}
```

`G4MaterialTable`は、すべての物質（`G4Material`）の一覧を保存するシングルトンです。

`G4Material::GetMaterialTable()`でテーブルにアクセスできます。
テーブルは`std::vector<G4Material*>`の`typedef`になっています。
このテーブルを使うことで、登録済みのすべての物質に簡単にアクセスできます。

:::{seealso}

詳しくは
[](./geant4-material-table.md)
に整理しました。

:::

## Particleしたい（`G4ParticleTable`）

```cpp
auto pt = G4ParticleTable::GetParticleTable();
```

`G4ParticleTable`は、Geant4内の粒子が定義されたテーブルです。
このテーブルから粒子の情報を検索できます。

## PhysicalVolumeしたい（`G4PhysicalVolumeStore`）

```cpp
auto pvs = G4PhysicalVolumeStore::GetInstance();
```

`G4PhysicalVolumeStore`はすべての物理ボリュームを管理するインスタンスです。
物理ボリュームを定義すると、自動でこのインスタンスに追加されます。
登録された物理ボリュームを検索できます。

## LogicalVolumeしたい（`G4LogicalVolumeStore`）

```cpp
auto lvs = G4LogicalVolumeStore::GetInstance();
```

`G4LogicalVolumeStore`はすべての論理ボリュームを管理するインスタンスです。
論理ボリュームを定義すると、自動でこのインスタンスに追加されます。
登録された論理ボリュームを検索できます。

## SensitiveDetectorしたい（`G4SDManager`）

```cpp
auto sm = G4SDManager::GetSDMpointer();
```

`G4SDManager`はGeant4のSensitive Detectorを管理するシングルトンです。
このマネージャーを通じて、Sensitive Detectorの登録や取得を行うことができます。

## UIコマンドしたい（`G4UImanager`）

```cpp
auto um = G4UImanager::GetUIpointer();
um->ApplyCommand("/run/initialize");
um->ApplyCommand("/run/beamOn 100");
```

`G4UImanager`はGeant4のUIコマンドを管理するシングルトンです。
マクロファイルの実行やUIコマンドの発行に使います。

## ファイル出力したい（`G4AnalysisManager`）

```cpp
auto am = G4AnalysisManager::Instance();
```

`G4AnalysisManager`は、シミュレーションで得られた結果を管理するインスタンスです。
ROOT、CSV、XMLなど複数の形式に出力できます。

:::{seealso}

詳しくは
[](./geant4-analysismanager.md)
に整理しました。

:::

## 統一したい（`SingletonManager`）

```cpp
// SingletonManager.hh
#pragma once

#include "G4RunManager.hh"
#include "G4NistManager.hh"
#include "G4SDManager.hh"
#include "G4ParticleTable.hh"
#include "G4Material.hh"
#include "G4AnalysisManager.hh"
#include "G4UImanager.hh"

class SingletonManager {
public:
    // RunManager
    static G4RunManager* RunManager() {
        return G4RunManager::GetRunManager();
    }

    // NIST Manager
    static G4NistManager* NistManager() {
        return G4NistManager::Instance();
    }

    // SD Manager
    static G4SDManager* SDManager() {
        return G4SDManager::GetSDMpointer();
    }

    // Particle Table
    static G4ParticleTable* ParticleTable() {
        return G4ParticleTable::GetParticleTable();
    }

    // Material Table
    static G4MaterialTable* MaterialTable() {
        return G4Material::GetMaterialTable();
    }

    // Analysis Manager
    static G4AnalysisManager* AnalysisManager() {
        return G4AnalysisManager::Instance();
    }

    // UI Manager
    static G4UImanager* UIManager() {
        return G4UImanager::GetUIpointer();
    }

    // ここに必要なシングルトンを追加可能
};
```

`SingletonManager`は、Geant4のシングルトンを1つにまとめて取得できるようにした自作クラスです。
シングルトンを取得するメソッドは、Geant4内部での命名規則が統一されておらずクラスごとに若干違いがあります。
上記のクラスは、メソッド名の違いを気にせず、統一的にアクセスできるようにしたラッパーです。

```cpp
#include "SingletonManager.hh"

void Example() {
    auto rm = SingletonManager::RunManager();
    auto nm = SingletonManager::NistManager();
    auto sm = SingletonManager::SDManager();
    auto pt = SingletonManager::ParticleTable();
    auto mt = SingletonManager::MaterialTable();
    auto am = SingletonManager::AnalysisManager();
    auto um = SingletonManager::UIManager();

    // 例えば NIST から材料を取得
    G4Material* water = nm->FindOrBuildMaterial("G4_WATER");
}
```

`SingletonManager.hh`を読み込み、必要なシングルトンを生成＆取得します。

## アプリの中で使いたい（`SingletonManager`）

```cpp
// main.cc
#include "G4RunManager.hh"
#include "SingletonManager.hh"

#include "ActionInitialization.hh"
#include "DetectorConstruction.hh"
#include "PhysicsList.hh"

int main()
{
    auto rm = new G4RunManager();
    rm->SetUserInitialization(new DetectorConstruction());
    rm->SetUserInitialization(new PhysicsList());
    rm->SetUserInitialization(new ActionInitialization());
    rm->Initialize();

    // マクロは、SingletonManager経由で実行する
    SingletonManager::UIManager()->ApplyCommand("/control/execute run.mac");

    delete rm;
    return 0;
}
```

`main()`では、`RunManager`を作って初期化します。
作るのは`new`で行い、`SingletonManager`は取得に使います。
`RunManager`は、`main()`の中で作った`rm`をそのまま使えば十分です。
`SingletonManager`の`RunManager()`は、`main()`以外で取得したいときに使います。

`RunManager`を作る前に取得すると、`nullptr`が返ることがあります。
取得したポインターは、`delete`しないでください。Geant4が管理しています。

次は、形状を作る`DetectorConstruction`での使い方です。

```cpp
// DetectorConstruction.cc
#include "SingletonManager.hh"

#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"

G4VPhysicalVolume* DetectorConstruction::Construct()
{
    auto nm = SingletonManager::NistManager();
    G4Material* water = nm->FindOrBuildMaterial("G4_WATER");

    auto solidWorld = new G4Box("World", 1. * m, 1. * m, 1. * m);
    auto logicWorld = new G4LogicalVolume(solidWorld, water, "World");
    return new G4PVPlacement(nullptr, G4ThreeVector(), logicWorld, "World", nullptr, false, 0, true);
}
```

`FindOrBuildMaterial`は、登録済みの材料があればそれを返します。
なければ、NISTのデータから材料を作ります。
材料名は、`G4_WATER`のように`G4_`で始まる名前で指定します。

次は、結果を保存する`RunAction`での使い方です。

```cpp
// RunAction.cc
#include "SingletonManager.hh"

#include "G4Run.hh"
#include "G4SystemOfUnits.hh"

RunAction::RunAction()
{
    auto am = SingletonManager::AnalysisManager();
    am->SetDefaultFileType("root");
    am->CreateH1("Edep", "Energy deposit", 100, 0., 10. * MeV);
}

void RunAction::BeginOfRunAction(const G4Run*)
{
    SingletonManager::AnalysisManager()->OpenFile("output");
}

void RunAction::EndOfRunAction(const G4Run*)
{
    auto am = SingletonManager::AnalysisManager();
    am->Write();
    am->CloseFile();
}
```

ヒストグラムは、コンストラクターで作ります。
ファイルは、ランの開始時に開き、ランの終了時に書き出して閉じます。
ヒストグラムへの値の記録は、`EventAction`や`SteppingAction`などで`FillH1()`を呼んで行います。

使う場所の目安は次のとおりです。

- 材料を取得するとき：`NistManager()`
- 登録済みの材料を一覧するとき：`MaterialTable()`
- 粒子の情報を調べるとき：`ParticleTable()`
- 結果を保存するとき：`AnalysisManager()`
- 有感検出器を登録するとき：`SDManager()`
- マクロやUIコマンドを実行するとき：`UIManager()`

:::{note}

マルチスレッドでは、ワーカースレッドから呼ぶ場合の扱いを、別途確認してください。

:::
