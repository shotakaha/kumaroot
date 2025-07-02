# シングルトン・パターン

Geant4の主要クラスには「シングルトン・パターン」が採用されています。
このため、ユーザーはどこからでも同一のインスタンスにアクセスできます。

## G4RunManager

```cpp
auto rm = G4RunManager::GetRunManager();
```

`G4RunManager`はGeant4シミュレーション全体を統括する中核的なシングルトンです。
ジオメトリ構築（`G4VUserDetectorConstruction`）、
物理プロセスの定義（`G4VUserPhysicsList`）、および
ユーザーアクション（`G4UserRunAction`など）を登録し、
初期化、実行、終了までの一連の流れを管理します。

:::{seealso}

詳しくは[](./geant4-run-manager.md)に整理しました。

:::

## G4NistManager

```cpp
auto nm = G4NistManager::Instance();
```

`G4NistManager`は、NISTに準拠した元素や物質を簡単に取得・生成できるシングルトンです。

:::{seealso}

詳しくは
[](./geant4-material-nistmanager.md)
に整理しました。

:::

## G4MaterialTable

```cpp
auto table = G4MaterialTable::GetMaterialTable();
for (auto* material: *table) {
    G4cout << material->GetName() << " rho= " << material->GetDensity()/(g/cm3) << " g/cm3" << G4endl;
}
```

`G4MaterialTable`は、すべての物質（`G4Material`など）のインスタンスの一覧を保持する静的テーブルです。

:::{seealso}

詳しくは
[](./geant4-material-table.md)
に整理しました。

:::

## G4ParticleTable

```cpp
auto pt = G4ParticleTable::GetParticleTable();
```

`G4ParticleTable`は、Geant4内の粒子が定義されたテーブルです。
このテーブルから粒子の情報を検索できます。

## G4ProcessTable

```cpp
auto pt = G4ProcessTable::GetProcessTable();
```

`G4ProcessTable`で物理プロセスを一覧できます。

## G4SDManager

```cpp
auto sm = G4SDManager::GetSDMpointer();
```

## G4UIManager

```cpp
auto um = G4UIManager::GetUIpointer();
```

## G4GeometryManager

```cpp
auto gm = G4GeometryManager::GetInstance();
```

`G4GeometryManager`はすべてのジオメトリを管理するインスタンスです。

## G4PhysicalVolumeStore

```cpp
auto pvs = G4PhysicalVolumeStore::GetInstance();
```

`G4PhysicalVolumeStore`はすべての物理ボリュームを管理するインスタンスです。
物理ボリュームを定義すると、自動でこのインスタンスに追加されます。
登録された物理ボリュームを検索できます。

## G4LogicalVolumeStore

```cpp
auto lvs = G4LogicalVolumeStore::GetInstance();
```

`G4LogicalVolumeStore`はすべての論理ボリュームを管理するインスタンスです。
論理ボリュームを定義すると、自動でこのインスタンスに追加されます。
登録された論理ボリュームを検索できます。

## G4SolidStore

```cpp
auto ss = G4SolidStore::GetInstance();
```

`G4SolidStore`はすべてのソリッド（形状）を管理するインスタンスです。
ソリッドを定義すると、自動でこのインスタンスに追加されます。
登録されたソリッドを検索できます。

---

## G4ProductionCutsTable

```cpp
auto pct = G4ProductionCutsTable::GetProductionCutsTable();
```

`G4ProductionCutsTable`はすべての領域（`G4Region`）に設定されたカット値を統括管理するインスタンスです。
このテーブルには、各粒子をトラッキングする際のエネルギーしきい値などが含まれています。

## G4TransportationManager

```cpp
auto tm = G4TransportationManager::GetTransportationManager();
```

`G4TransportationManager`はナビゲーションとフィールドの統合管理を行うシングルトンです。
トラッキング時の空間移動処理や電磁場の適用に関係します。

## G4LossTableManager

```cpp
auto ltm = G4LossTableManager::Instance();
```

`G4LossTableManager`は、電磁過程（とくにエネルギー損失）に関する情報を一括して管理するためのインスタンスです。
`G4EmProcessOptions` などと連携して使用します。

## G4FieldManagerStore

```cpp
auto fms = G4FieldManagerStore::GetInstance();
```

`G4FieldManagerStore`は、複数の電磁場管理オブジェクト（`G4FieldManager`）を保持するストアです。
それぞれの論理ボリュームに設定されたフィールド管理を一元的に扱います。

## G4AnalysisManager

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
