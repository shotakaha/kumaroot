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
[](./geant4-material-nistmanager.md)
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

int main()
{
    // 1. RunManagerを最初に作る
    auto runManager = new G4RunManager();

    // 2. どこからでも、同じRunManagerを取得できる
    auto rm = SingletonManager::RunManager();

    // 3. 最後に削除する
    delete runManager;
    return 0;
}
```

`SingletonManager`は、関数だけを持つクラスです。
オブジェクトを作らずに、`SingletonManager::RunManager()`のように呼び出します。

`RunManager`は、`main()`の最初で作ります。
作る前に取得すると、`nullptr`が返ることがあります。
取得したポインターは、`delete`しないでください。Geant4が管理しています。

取得したシングルトンは、次のように、使う場所で呼び出します。

```cpp
// DetectorConstruction.cc
#include "SingletonManager.hh"

G4VPhysicalVolume* DetectorConstruction::Construct()
{
    auto nm = SingletonManager::NistManager();
    G4Material* water = nm->FindOrBuildMaterial("G4_WATER");
    // ... 形状の構築（省略）
}
```

```cpp
// RunAction.cc
#include "SingletonManager.hh"

void RunAction::EndOfRunAction(const G4Run*)
{
    auto am = SingletonManager::AnalysisManager();
    // ... 結果の出力（省略）
}
```

使う場所の目安は次のとおりです。

- 形状の材料を決めるとき：`NistManager()`、`MaterialTable()`
- 粒子の情報を調べるとき：`ParticleTable()`
- 結果をファイルに出力するとき：`AnalysisManager()`
- 有感検出器を登録するとき：`SDManager()`
- マクロやUIコマンドを実行するとき：`UIManager()`

:::{note}

マルチスレッドでは、ワーカースレッドから呼ぶ場合の扱いを、別途確認してください。

:::
