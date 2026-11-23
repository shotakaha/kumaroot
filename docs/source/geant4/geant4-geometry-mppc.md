# MPPCしたい（`BuildMppc`）

```cpp
// Construct() の中
auto mppcSmall = BuildMppc(kS13360_1350CS_01);  // 有効受光面 1.3 mm 角
auto mppcLarge = BuildMppc(kS13360_3050CS);     // 有効受光面 3.0 mm 角
```

浜松ホトニクスのMPPC（S13360シリーズ）を、品番ごとのスペックから作る方法です。
`BuildMppc`は、パッケージ・シリコーン樹脂窓・受光面をまとめた論理ボリュームを1つ返します。

## スペックを定義したい（`MppcSpec`）

```cpp
#include "G4SystemOfUnits.hh"

// MPPCの品番ごとのスペック（寸法は データシート KAPD1052J を参照）
struct MppcSpec {
    G4String name;           // 品番
    G4double activeSize;     // 有効受光面の一辺 [mm]
    G4double pitch;          // ピクセルピッチ [mm]
    G4int    pixels;         // 画素数
    G4double packageX;       // パッケージ外形 X [mm]
    G4double packageY;       // パッケージ外形 Y [mm]
    G4double packageZ;       // 厚み（樹脂を含む）[mm]
    G4double resinThickness; // シリコーン樹脂の厚み [mm]
};

// S13360-1350CS-01（1.3 mm 角）
inline const MppcSpec kS13360_1350CS_01{
    "S13360-1350CS-01",
    1.3 * mm,   // 有効受光面
    0.05 * mm,  // 50 µm
    667,        // 画素数
    5.7 * mm,   // パッケージ X
    5.0 * mm,   // パッケージ Y
    1.5 * mm,   // 厚み
    0.45 * mm,  // 樹脂厚み（※図に記載なし。3050CSの値で仮置き）
};

// S13360-3050CS（3.0 mm 角）
inline const MppcSpec kS13360_3050CS{
    "S13360-3050CS",
    3.0 * mm,   // 有効受光面
    0.05 * mm,  // 50 µm
    3600,       // 画素数（60 × 60）
    6.55 * mm,  // パッケージ X
    5.9 * mm,   // パッケージ Y
    2.0 * mm,   // 厚み
    0.45 * mm,  // 樹脂厚み
};
```

`MppcSpec`は、1つのMPPCを作るのに必要な寸法をまとめた構造体です。
品番を増やすときは、構造体の値を1つ追加するだけで済みます。

:::{caution}

データシートの「受光面サイズ」と「ピクセル数」は、ピクセルピッチから計算すると次のように一致します。

- S13360-3050CS: 3.0 mm ÷ 50 µm = 60 → 60 × 60 = 3600。データシートの値と一致します
- S13360-1350CS-01: 1.3 mm ÷ 50 µm = 26 → 26 × 26 = 676。データシートは667で、ピクセルの周囲に非感度領域があるため少し小さくなります

`pixels`は、データシートの値をそのまま入れてください。計算値とは一致しないことがあります。

:::

## 量子効率を登録したい（`BuildMppcPhotocathode`）

```cpp
#include "G4LogicalVolume.hh"
#include "G4Box.hh"
#include "G4OpticalSurface.hh"
#include "G4LogicalSkinSurface.hh"

// 受光面の論理ボリュームを作る（厚さは 1 µm の仮想的な薄い板）
G4LogicalVolume* BuildMppcPhotocathode(
    const MppcSpec& spec,
    const G4String& logicalName = "MppcPhotocathode")
{
    G4double halfX = 0.5 * spec.activeSize;
    G4double halfZ = 0.5 * 1. * um;  // 厚み 1 µm の半分

    auto solid = new G4Box(logicalName + "Solid", halfX, halfX, halfZ);

    auto nm = G4NistManager::Instance();
    auto material = nm->FindOrBuildMaterial("G4_Si");

    auto logical = new G4LogicalVolume(
        solid,        // G4VSolid
        material,     // G4Material
        logicalName,  // 名前
        nullptr,      // G4FieldManager（未使用）
        nullptr,      // G4VSensitiveDetector（未使用）
        nullptr       // G4UserLimits（未使用）
    );

    // 光学表面に検出効率（EFFICIENCY）を設定する
    auto surface = new G4OpticalSurface(
        logicalName + "Surface",
        unified,           // 表面モデル
        polished,          // 表面仕上げ
        dielectric_metal   // 表面の種類（吸収する簡易モデル）
    );
    surface->SetMaterialPropertiesTable(MakeMppcPdeProperties());

    new G4LogicalSkinSurface(logicalName + "Surface", logical, surface);

    return logical;
}
```

`BuildMppcPhotocathode`は、受光面の論理ボリュームを作る関数です。
光子が受光面に入ったときの検出は、`EFFICIENCY`（検出効率、PDE）で決まります。

PDEは、データシートのグラフ（50 µmピッチ、Typ. 25 ℃）からの読み取り値です。
PDEの波長依存を次の表に入れます。

```cpp
#include "G4MaterialPropertiesTable.hh"
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"

// PDE テーブル（波長 [nm] は降順、PDE は [0, 1]）
// 450 nm で 40 % は、データシートの Vover = 3 V の値
inline const PmtQETable kMppcPde = {
    {900., 800., 700., 600., 500., 450., 400., 350., 300., 270.},  // 波長 [nm]
    {0.03, 0.08, 0.15, 0.26, 0.38, 0.40, 0.37, 0.30, 0.22, 0.00},  // PDE [-]
};

// PDE を EFFICIENCY として登録する（geant4-qe の MakeEfficiencyProperties を使う）
inline G4MaterialPropertiesTable* MakeMppcPdeProperties()
{
    return MakeEfficiencyProperties(kMppcPde);
}
```

`PmtQETable`と`MakeEfficiencyProperties`は、[量子効率したい](geant4-qe)で作った関数です。
構造体の名前は`PmtQETable`ですが、中身は波長と効率の組なので、MPPCのPDEにもそのまま使えます。

:::{hint}

PDEは、クロストーク・アフターパルスを含みません。
また、窓の透過率を含んだ値なので、`geant4-qe`のcautionと同じく、受光面の表面に直接設定してください。

:::

## MPPCを組み立てたい（`BuildMppc`）

```cpp
G4LogicalVolume* BuildMppc(
    const MppcSpec& spec,
    const G4String& logicalName = "MPPC")
{
    auto nm = G4NistManager::Instance();

    // 外形（樹脂を含む全体）を入れる空間
    G4double halfX = 0.5 * spec.packageX;
    G4double halfY = 0.5 * spec.packageY;
    G4double halfZ = 0.5 * spec.packageZ;
    auto envelopeSolid = new G4Box(logicalName + "Envelope", halfX, halfY, halfZ);
    auto envelope = new G4LogicalVolume(
        envelopeSolid,
        nm->FindOrBuildMaterial("G4_AIR"),
        logicalName + "Envelope",
        nullptr,  // G4FieldManager（未使用）
        nullptr,  // G4VSensitiveDetector（未使用）
        nullptr   // G4UserLimits（未使用）
    );

    // セラミックパッケージ（下側）
    G4double packageHalfZ = 0.5 * (spec.packageZ - spec.resinThickness);
    auto packageSolid = new G4Box(logicalName + "PackageSolid", halfX, halfY, packageHalfZ);
    auto packageLogical = new G4LogicalVolume(
        packageSolid,
        nm->FindOrBuildMaterial("G4_ALUMINUM_OXIDE"),  // セラミック（Al2O3）で代用
        logicalName + "Package",
        nullptr,  // G4FieldManager（未使用）
        nullptr,  // G4VSensitiveDetector（未使用）
        nullptr   // G4UserLimits（未使用）
    );
    G4double packageZ = -halfZ + packageHalfZ;  // 下端からの位置
    new G4PVPlacement(
        nullptr,                         // 回転なし
        G4ThreeVector(0., 0., packageZ), // 配置
        packageLogical,                  // 配置する論理ボリューム
        logicalName + "Package",         // 物理ボリュームの名前
        envelope,                        // 親（外形の論理ボリューム）
        false,                           // pMany（未使用）
        0,                               // コピー番号
        true                             // 重なりチェック
    );

    // シリコーン樹脂窓（上側）
    // NIST の材料にシリコーン樹脂がないので、屈折率 1.41 を設定した SiO2 で代用する
    auto resinSolid = new G4Box(logicalName + "ResinSolid", halfX, halfY, 0.5 * spec.resinThickness);
    auto resinMaterial = nm->FindOrBuildMaterial("G4_SILICON_DIOXIDE");
    std::vector<G4double> photonEnergies{2.0 * eV, 3.5 * eV};
    std::vector<G4double> rIndex{1.41, 1.41};          // シリコーン樹脂の屈折率
    std::vector<G4double> absLength{1. * m, 1. * m};   // 樹脂中の吸収長
    auto mpt = new G4MaterialPropertiesTable();
    mpt->AddProperty("RINDEX", photonEnergies, rIndex);
    mpt->AddProperty("ABSLENGTH", photonEnergies, absLength);
    resinMaterial->SetMaterialPropertiesTable(mpt);
    auto resinLogical = new G4LogicalVolume(
        resinSolid,
        resinMaterial,
        logicalName + "Resin",
        nullptr,  // G4FieldManager（未使用）
        nullptr,  // G4VSensitiveDetector（未使用）
        nullptr   // G4UserLimits（未使用）
    );
    G4double resinZ = halfZ - 0.5 * spec.resinThickness;  // 上端からの位置
    auto resinPV = new G4PVPlacement(
        nullptr,
        G4ThreeVector(0., 0., resinZ),
        resinLogical,
        logicalName + "Resin",
        envelope,
        false,
        0,
        true
    );

    // 受光面（樹脂の下面に置く）
    auto photocathode = BuildMppcPhotocathode(spec);
    G4double photoZ = -0.5 * spec.resinThickness + 0.5 * um;  // 樹脂の下面の少し上
    new G4PVPlacement(
        nullptr,
        G4ThreeVector(0., 0., photoZ),
        photocathode,
        logicalName + "Photocathode",
        resinLogical,
        false,
        0,
        true
    );

    return envelope;
}
```

`BuildMppc`は、外形の論理ボリューム（`G4LogicalVolume*`）を1つ返します。
中には、下側のセラミックパッケージ、上側のシリコーン樹脂窓、その下面の受光面が入っています。
受光面は樹脂の子になっているので、`SetupMppc`で配置すると一緒に置かれます。

:::{hint}

1350CS-01の樹脂厚みは、データシートの図に記載がありません。
このページでは、3050CSと同じ0.45 mmを仮置きしています。実際の値は、メーカーに問い合わせて確認してください。

:::

:::{note}

このページのMPPCは、受光面を1枚の薄い板として表しています。
50 µmのピクセル構造は作っていません。
画素ごとの応答（ガイガーモードの発火）が必要な場合は、受光面を`G4PVReplica`で`pixels`個に分割してください。

:::

## MPPCを配置したい（`SetupMppc`）

```cpp
G4VPhysicalVolume* SetupMppc(
    G4VPhysicalVolume* parent,
    G4LogicalVolume* mppc,  // BuildMppc()の戻り値
    G4int copyNo,
    const G4ThreeVector& position = G4ThreeVector(),
    const G4String& physicalName = "MPPC")
{
    // 回転なしで配置する
    G4RotationMatrix rotation;

    return new G4PVPlacement(
        G4Transform3D(rotation, position),  // 回転と位置
        physicalName,                       // 物理ボリュームの名前
        mppc,                               // 配置する論理ボリューム
        parent,                             // 親ボリューム
        false,                              // pMany（未使用）
        copyNo,                             // コピー番号
        true                                // 重なりチェック
    );
}
```

`SetupMppc`は、`SetupPmt`と同じ形で、`BuildMppc`が返したMPPCを親ボリュームに置きます。
検出の登録（SensitiveDetector）は、[PMTを作りたい](geant4-geometry-pmt)の`ConstructSDandField()`と同じ方法で、受光面の論理ボリュームに登録します。

:::{seealso}

- [](./geant4-geometry-pmt.md)
- [](./geant4-qe.md)
- [](./geant4-material-propertiestable.md)

:::

## 参考：S13360シリーズのスペック

| 項目 | S13360-1350CS-01 | S13360-3050CS |
|---|---|---|
| 有効受光面 | 1.3 × 1.3 mm | 3.0 × 3.0 mm |
| ピクセルピッチ | 50 µm | 50 µm |
| 画素数 | 667 | 3600 |
| パッケージ | セラミック | セラミック |
| 外形 | 5.7 × 5.0 mm、厚み 1.5 mm | 6.55 × 5.9 mm、厚み 2.0 mm |
| 窓（シリコーン樹脂）の屈折率 | 1.41 | 1.41 |
| 開口率 | 74 % | 74 % |
| 感度波長範囲 | 270〜900 nm | 270〜900 nm |
| PDE（450 nm、Vover = 3 V） | 40 % | 40 % |

出典: 浜松ホトニクス「S13360シリーズ」データシート（KAPD1052J）。PDEの波長依存はグラフからの読み取り値です。
