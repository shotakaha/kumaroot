# OpNoviceしたい（`examples/extended/optical/OpNovice`）

OpNoviceは、光学光子（optical photon）の生成と輸送を示す入門サンプルです。
水の入った水槽の中で、電子・陽電子が荷電粒子としてチェレンコフ光を出し、シンチレーション光も生成されます。
光子は吸収、レイリー散乱、ミー散乱、境界面での反射・屈折を受けます。
これらの過程は、`G4OpticalPhysics`、`G4MaterialPropertiesTable`、`G4OpticalSurface`を使って設定しています。

## ビルドしたい

```console
// サンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/extended/optical/OpNovice
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/OpNovice

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する
$ cd build
$ ./OpNovice -m OpNovice.in    # バッチモード
$ ./OpNovice                   # 対話モード（vis.macとgui.macを読み込む）

// クリーンする
$ cd $G4WORK/OpNovice
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

`cmake`でビルドし、`OpNovice`という実行ファイルを作成します。
手順の詳しい説明は、[付属サンプルの遊び方](geant4-examples)を参照してください。

:::{note}

`OpNovice`の実行ファイルは、次のオプションを受け付けます。

```console
$ ./OpNovice [-g gdmlfile] [-m macro] [-u UIsession] [-t nThreads] [-r seed]
```

- `-m`：マクロを読み込んで、バッチモードで実行します。
- `-g`：GDMLファイルから形状を読み込みます。Geant4をGDML有効でビルドしている必要があります。
- `-t`：スレッド数を指定します。マルチスレッドのビルドでのみ有効です。
- `-r`：乱数の種を指定します。

:::

## GDML無効のGeant4でビルドしたい

付属のサンプルは、GDML有効のGeant4を前提に書かれています。
GDML無効のGeant4で上の手順をそのまま実行すると、`G4GDMLParser.hh`が見つからずにビルドが失敗します。
GDMLを使わない場合は、作業用ディレクトリのコピーに次のパッチを当ててからビルドします。
インストール先のサンプルは変更しません。

まず、Geant4がGDML無効かどうかを確認します。
GDMLのヘッダが無ければ、`0`と表示されます。

```console
// GDMLのヘッダの数を数える（0ならGDML無効）
$ ls ~/geant4/v11.X.Y/install/include/Geant4 | grep -c -i gdml
```

次の内容を`opnovice-no-gdml.patch`という名前で保存します。

```diff
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -3,7 +3,7 @@
 cmake_minimum_required(VERSION 3.16...3.27)
 project(OpNovice)
 #add_definitions(-DGEANT4_USE_GDML)
-add_compile_definitions(GEANT4_USE_GDML)
+#add_compile_definitions(GEANT4_USE_GDML)
 #make using gdml the default
 OPTION( GEANT4_USE_GDML "Use gdml Option" ON)
 # printout the value of GEANT4_USE_GDML
--- a/src/OpNoviceDetectorConstruction.cc
+++ b/src/OpNoviceDetectorConstruction.cc
@@ -32,7 +32,9 @@

 #include "G4Box.hh"
 #include "G4Element.hh"
-#include "G4GDMLParser.hh"
+#ifdef GEANT4_USE_GDML
+#  include "G4GDMLParser.hh"
+#endif
 #include "G4LogicalBorderSurface.hh"
 #include "G4LogicalSkinSurface.hh"
 #include "G4LogicalVolume.hh"
@@ -272,10 +274,12 @@
   }
   opAirSurface->SetMaterialPropertiesTable(myST2);

+#ifdef GEANT4_USE_GDML
   if (fDumpGdml) {
     auto parser = new G4GDMLParser();
     parser->Write(fDumpGdmlFileName, world_phys);
   }
+#endif

   ////////////////////////////////////////////////////////////////////////////
   // test user-defined properties
--- a/src/OpNoviceDetectorMessenger.cc
+++ b/src/OpNoviceDetectorMessenger.cc
@@ -29,8 +29,8 @@
 #include "OpNoviceDetectorMessenger.hh"

 #include "OpNoviceDetectorConstruction.hh"
-#include "OpNoviceGDMLDetectorConstruction.hh"

+
 #include "G4UIcmdWithABool.hh"
 #include "G4UIcmdWithAString.hh"
 #include "G4UIdirectory.hh"
@@ -79,12 +79,6 @@
     if (command == fVerboseCmd) dc1->SetVerbose(fVerboseCmd->GetNewBoolValue(newValue));
     if (command == fDumpGdmlCmd) dc1->SetDumpGdml(fDumpGdmlCmd->GetNewBoolValue(newValue));
     if (command == fDumpGdmlFileNameCmd) dc1->SetDumpGdmlFile(newValue);
-  }
-  else {
-    auto dc2 = dynamic_cast<OpNoviceGDMLDetectorConstruction*>(fOpNoviceDetCon);
-    if (command == fVerboseCmd) dc2->SetVerbose(fVerboseCmd->GetNewBoolValue(newValue));
-    if (command == fDumpGdmlCmd) dc2->SetDumpGdml(fDumpGdmlCmd->GetNewBoolValue(newValue));
-    if (command == fDumpGdmlFileNameCmd) dc2->SetDumpGdmlFile(newValue);
   }
 }
 //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
```

パッチは、次の3つの変更を行います。

- `CMakeLists.txt`：`GEANT4_USE_GDML`の定義をコメントアウトする
- `OpNoviceDetectorConstruction.cc`：`G4GDMLParser`の`#include`と、GDMLの書き出し部分を`#ifdef GEANT4_USE_GDML`で囲む
- `OpNoviceDetectorMessenger.cc`：GDML版の形状（`OpNoviceGDMLDetectorConstruction`）を参照する部分を削除する

パッチを当て、GDML無効を指定してビルドします。

```console
// 作業用ディレクトリのコピーに、パッチを当てる
$ cd $G4WORK/OpNovice
$ patch -p1 < ../opnovice-no-gdml.patch

// GDML無効を指定してビルドする
$ cmake -S . -B build -DGEANT4_USE_GDML=OFF
$ cmake --build build --parallel

// 実行する
$ cd build
$ ./OpNovice -m OpNovice.in
```

:::{note}

GDML無効でビルドすると、`-g`オプションは使えません。
`/OpNovice/DetectorConstruction/dumpGdml`のコマンドは残りますが、GDMLファイルは書き出されません。

:::

## マクロの流れを確認したい

付属のマクロは、次の4つです。

| ファイル | 内容 |
| --- | --- |
| `OpNovice.in` | 陽電子（`e+`）を500 keVで、10イベント撃ち、チェレンコフ光の上限を変えて1000イベント撃つ |
| `optPhoton.mac` | 光学光子を3 eVで撃ち、偏光を指定する |
| `vis.mac` | 可視化の設定。対話モードで自動的に読み込まれる |
| `gui.mac` | GUIメニューの設定。GUIセッションのときだけ読み込まれる |

`OpNovice.in`では、物理過程の詳細な出力を有効にしたあと、次のように設定しています。

```cfg
/gun/particle e+
/gun/energy 500 keV
/process/optical/cerenkov/setMaxBetaChange 1
/run/beamOn 10
/process/optical/cerenkov/setMaxPhotons 15
/process/optical/cerenkov/setTrackSecondariesFirst false
/run/beamOn 1000
```

`/process/optical/cerenkov/`のコマンドは、`G4OpticalPhysics`が用意しているメッセンジャーで設定します。
詳しくは、[光学物理](geant4-physics-opticalphysics)を参照してください。

## 物理リストを確認したい（`G4OpticalPhysics`）

物理リストは、`FTFP_BERT`をベースに、電磁過程だけを`G4EmStandardPhysics_option4`に置き換えています。
光学過程は、`G4OpticalPhysics`を追加して有効にします。

```cpp
// main()（一部）
G4VModularPhysicsList* physicsList = new FTFP_BERT;
physicsList->ReplacePhysics(new G4EmStandardPhysics_option4());
auto opticalPhysics = new G4OpticalPhysics();
physicsList->RegisterPhysics(opticalPhysics);
runManager->SetUserInitialization(physicsList);
```

`G4OpticalPhysics`は、次の光学過程を登録します。

- `G4Cerenkov`：荷電粒子が媒質中で光速より速く進むとき、チェレンコフ光を生成する
- `G4Scintillation`：エネルギーを失った粒子が、シンチレーション光を生成する
- `G4OpAbsorption`：光子を吸収する
- `G4OpRayleigh`：光子をレイリー散乱させる
- `G4OpMieHG`：光子をミー散乱（Henyey-Greenstein）させる
- `G4OpBoundaryProcess`：境界面で、反射・屈折・吸収などを行う

:::{note}

光学光子は、物性（`G4MaterialPropertiesTable`）を定義していない物質の中では、吸収も散乱もされずに、そのまま進みます。
この動作は、光子が消えたように見えるので、まず物性の定義を確認するとよいです。

:::

## 物性を設定したい（`G4MaterialPropertiesTable`）

物性は、`OpNoviceDetectorConstruction`で、水（`Water`）と空気（`Air`）に設定しています。
プロパティの名前と値の組を、`AddProperty()`で追加します。

```cpp
// OpNoviceDetectorConstruction::DefineMaterials()（一部）
auto myMPT1 = new G4MaterialPropertiesTable();

// 屈折率（RINDEX）。エネルギーの配列と値の配列を渡す
G4int numEntries = 1;
myMPT1->AddProperty("RINDEX", &photonEnergy[0], &refractiveIndex1[0], numEntries);
for (size_t i = 1; i < photonEnergy.size(); ++i) {
  myMPT1->AddEntry("RINDEX", photonEnergy[i], refractiveIndex1[i]);
}

// 吸収長（ABSLENGTH）。spline補間を有効にする
myMPT1->AddProperty("ABSLENGTH", photonEnergy, absorption, false, true);

// シンチレーション（スペクトルと発光量）
myMPT1->AddProperty("SCINTILLATIONCOMPONENT1", energyArray, scintilFastArray, lenArray);
myMPT1->AddConstProperty("SCINTILLATIONYIELD", 50. / MeV);

// ミー散乱（MIEHG）と、その定数
myMPT1->AddProperty("MIEHG", energy_water, mie_water, false, true);
myMPT1->AddConstProperty("MIEHG_FORWARD", mie_water_const[0]);

water->SetMaterialPropertiesTable(myMPT1);
```

- `AddProperty()`：エネルギーに対する値の配列（`std::vector`またはC配列）を追加します。
- `AddConstProperty()`：エネルギーによらない定数を追加します。
- 第4引数（`createNewKey`）と第5引数（`spline`）は、既定では`false`です。

水には、ほかに`Birks`定数も設定しています。
`water->GetIonisation()->SetBirksConstant(0.126 * mm / MeV)`で、シンチレーション光のクエンチングを補正します。

物性の詳しい説明は、[G4MaterialPropertiesTable](geant4-material-propertiestable)を参照してください。

## 境界面を設定したい（`G4OpticalSurface`）

境界面は、2つの種類を使い分けています。

```cpp
// 水槽と実験ホールの境界（G4LogicalBorderSurface）
auto opWaterSurface = new G4OpticalSurface("WaterSurface");
opWaterSurface->SetType(dielectric_LUTDAVIS);
opWaterSurface->SetFinish(Rough_LUT);
opWaterSurface->SetModel(DAVIS);
new G4LogicalBorderSurface("WaterSurface", waterTank_phys, expHall_phys, opWaterSurface);

// 気泡と水の境界（G4LogicalSkinSurface）
auto opAirSurface = new G4OpticalSurface("AirSurface");
opAirSurface->SetType(dielectric_dielectric);
opAirSurface->SetFinish(polished);
opAirSurface->SetModel(glisur);
new G4LogicalSkinSurface("AirSurface", bubbleAir_log, opAirSurface);
```

- `G4LogicalBorderSurface`：2つの物理体積の間の境界です。
- `G4LogicalSkinSurface`：1つの論理体積の表面全体に適用します。気泡のように、ほかの体積に囲まれた論理体積の表面に使います。
- 気泡の表面には、反射率（`REFLECTIVITY`）と検出効率（`EFFICIENCY`）を設定しています。

```cpp
// 気泡の表面の物性
auto myST2 = new G4MaterialPropertiesTable();
myST2->AddProperty("REFLECTIVITY", ephoton, reflectivity);  // {0.3, 0.5}
myST2->AddProperty("EFFICIENCY", ephoton, efficiency);      // {0.8, 1.0}
opAirSurface->SetMaterialPropertiesTable(myST2);
```

境界面の詳しい説明は、[G4OpticalSurface](geant4-physics-opticalphoton)を参照してください。

## 形状を読み込みたい（`-g`とGDML）

形状は、`OpNoviceDetectorConstruction`でコードとして定義しています。
同じ形状は、`gdml/NoviceExample.gdml`にも書かれているので、`-g`オプションで読み込めます。

```console
$ ./OpNovice -g gdml/NoviceExample.gdml -m OpNovice.in
```

GDMLを使うには、Geant4をGDML有効でビルドしている必要があります。
GDML無効のGeant4では、`-g`を指定するとエラーになります。

形状の寸法は、次のとおりです。

| 体積 | 形状 | 寸法 | 材質 |
| --- | --- | --- | --- |
| World | `G4Box` | 一辺の半分が15 m | Air |
| expHall | `G4Box` | 一辺の半分が10 m | Air |
| Tank | `G4Box` | 水槽 | Water |
| Bubble | `G4Box` | 気泡。水槽の中の(0, 2.5 m, 0)に置く | Air |

## 光子数を数えたい（`StackingAction`、`EventAction`）

光子の数は、`OpNoviceStackingAction`と`OpNoviceEventAction`で数えます。

- `OpNoviceStackingAction::ClassifyNewTrack()`：生成された光学光子のうち、二次粒子であるものを、生成過程（`Cerenkov`か`Scintillation`）ごとに数えます。
- `OpNoviceStackingAction::NewStage()`：イベントの終わりに、数えた値をランに加えます。
- `OpNoviceSteppingAction`：光子の各ステップで、レイリー散乱、吸収、ミー散乱、境界面の過程が起きたかを判定します。
- `OpNoviceEventAction`：イベントごとの値を、ランに加えます。

`OpNoviceRun`は、これらの値を集計して、ランの終わりに表示します。
`OpNovice.in`を実行すると、次のような集計結果が表示されます（一例です）。

```text
Primary particle was: e+ with energy 500 keV.
Number of events: 1000
Average number of Cerenkov photons created per event: 16.5 +- 5.48
Average number of scintillation photons created per event: 67.4 +- 8.16
Average number of optical Rayleigh interactions per event: 7.81 +- 2.97
Average number of optical absorption interactions per event: 34.9 +- 6.11
Average number of optical Mie interactions per event: 0.118 +- 0.341
Average number of optical boundary interactions per event: 191 +- 28.9
```

:::{note}

`StackingAction`で数えるのは、二次粒子として生成された光子だけです。
一次粒子として`optPhoton.mac`で撃った光子は、チェレンコフ光やシンチレーション光としては数えられません。

:::

## 一次粒子を変えたい（`/OpNovice/gun/optPhotonPolar`）

一次粒子は、`G4ParticleGun`で撃ちます。
既定は、陽電子（`e+`）を500 keVで撃つ設定です。
`/gun/particle`と`/gun/energy`で、粒子とエネルギーを変えられます。

光学光子を撃つときは、偏光も指定できます。
`OpNovicePrimaryGeneratorMessenger`が、`/OpNovice/gun/optPhotonPolar`コマンドを用意しています。

```cfg
/gun/particle opticalphoton
/gun/energy 3 eV
/gun/direction 5 -3 0
/OpNovice/gun/optPhotonPolar    # 偏光をランダムに決める
/run/beamOn 10
```

- 引数に角度（`deg`）を渡すと、(k, n)面に対する偏光の角度を指定できます。
- 引数を省略すると、偏光の角度をランダムに決めます。
- 光子ではない粒子に対して実行すると、警告を出して無視されます。

## 次に読むサンプル

OpNoviceで光学過程の基本をつかんだら、次のサンプルに進むとよいです。

- `extended/optical/OpNovice2`：物性のテーブルや、チェレンコフ光とシンチレーション光の検証を、より詳しく扱います。
- `extended/optical/LXe`：液体キセノンの検出器と、光電子増倍管（PMT）での光子の検出を扱います。
- `extended/optical/wls`：波長変換ファイバーを扱います。
