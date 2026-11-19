# B2したい（`examples/basic/B2`）

![](./fig/exampleB2.png)

`examples/basic/B2`は、固定標的と複数のチェンバーを並べた飛跡検出器です。
外部磁場を与えると粒子が曲がる様子を観察できます。

このサンプルで学べるポイントは、次のとおりです。

- 検出器の形状（固定標的とチェンバーの配置）
- `Sensitive Detector`と`Hit`によるヒットの記録
- マクロで材質や条件を変えること
- 磁場の設定と、ステップ長の制限

`examples/basic/B2/`の中には、`B2a`と`B2b`のディレクトリがあります。
どちらも同じ装置をシミュレーションしますが、チェンバーの作り方が違います。
`B2a`は単純な円筒としてチェンバーを配置し、`B2b`はパラメータ化されたボリューム（`G4PVParameterised`）として配置します。

`B2a`と`B2b`は、それぞれ独立したプロジェクトです。
使いたいほうだけをコピーして、ビルドします。

## ビルドしたい（`B2a`）

```console
// サンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/basic/B2/B2a
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/B2a

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する
$ cd build
$ ./exampleB2a run1.mac    # バッチモード
$ ./exampleB2a             # 対話モード

// クリーンする
$ cd $G4WORK/B2a
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

`cmake`でビルドし、`exampleB2a`という実行ファイルを作成します。
手順の詳しい説明は、[付属サンプルの遊び方](geant4-examples)を参照してください。

実行ファイルは、`build/`の中に作成されます。
`B2a`の`CMakeLists.txt`は、マクロファイル（`run1.mac`など）を`build/`にコピーするので、`build/`で実行できます。
`./exampleB2a`を実行するときにマクロファイルを指定するとバッチモード、指定しないと対話モードになります。

## ビルドしたい（`B2b`）

```console
// サンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/basic/B2/B2b
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/B2b

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する
$ cd build
$ ./exampleB2b run1.mac    # バッチモード
$ ./exampleB2b             # 対話モード

// クリーンする
$ cd $G4WORK/B2b
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

実行ファイルは`exampleB2b`です。
手順は`B2a`と同じです。`B2b`の`run1.mac`は、`B2a`と同じ内容です。

## 全体の組み立てしたい（`exampleB2a.cc`）

```cpp
//////////////////////////////////////////////////
// exampleB2a.cc（一部を省略）
//////////////////////////////////////////////////
auto runManager = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);

// Detector construction
runManager->SetUserInitialization(new B2a::DetectorConstruction());

// Physics list
auto physicsList = new FTFP_BERT;
physicsList->RegisterPhysics(new G4StepLimiterPhysics());
runManager->SetUserInitialization(physicsList);

// User action initialization
runManager->SetUserInitialization(new B2::ActionInitialization());
```

`G4RunManagerFactory`でランマネージャーを作成し、検出器（`B2a::DetectorConstruction`）、物理リスト、ユーザーアクション（`B2::ActionInitialization`）を登録しています。
物理リストには、`FTFP_BERT`に`G4StepLimiterPhysics`を追加しています。

実行方法の切り替えは`B1`と同じです。
引数がなければ対話モードで、`init_vis.mac`を実行します。GUIが使える場合は、さらに`gui.mac`も実行します。
引数があれば、それをマクロファイルとして実行するバッチモードになります。

## 検出器の形状を作りたい（`DetectorConstruction`）

`B2a`の検出器は、固定標的と複数の円筒型トラッカーで構成されています。

- **固定標的**：入射粒子が最初に衝突する部分です。材質はマクロで変更できます。
- **チェンバー（トラッカー）**：ターゲットと同軸に複数枚配置されています。`B2a`は1枚ずつ`G4PVPlacement`で配置し、`B2b`は`ChamberParameterisation`を使って`G4PVParameterised`で配置します。

`B2a`と`B2b`を比べると、同じ形状を作る2つの方法の違いが理解しやすくなります。

## ヒットを記録したい（`Sensitive Detector`と`Hit`）

チェンバーの論理ボリューム`Chamber_LV`に、`TrackerSD`を割り当てています。

```cpp
// B2a::DetectorConstruction::ConstructSDandField()
auto trackerSD = new TrackerSD(trackerChamberSDname, "TrackerHitsCollection");
G4SDManager::GetSDMpointer()->AddNewDetector(trackerSD);
SetSensitiveDetector("Chamber_LV", trackerSD, true);
```

`TrackerSD::ProcessHits()`は、ステップごとに呼ばれます。
そのステップでエネルギー損失が0より大きいときだけ、`TrackerHit`を作って記録します。

`TrackerHit`には、次の情報が入ります。

| 情報 | 内容 |
| --- | --- |
| `fTrackID` | ヒットを作った粒子の`TrackID` |
| `fChamberNb` | どのチェンバーか（コピー番号） |
| `fEdep` | そのステップでのエネルギー損失 |
| `fPos` | ステップ終点の位置 |

`/hits/verbose 2`を指定すると、記録されたヒットの内容が表示されます。
形状（検出器）と測定（ヒット）を別々のクラスで扱う、という設計を学べます。

## マクロで条件を変えたい（`DetectorMessenger`）

`DetectorMessenger`は、材質などを変えるコマンドを`/B2/det/`以下に提供します。

| コマンド | 役割 |
| --- | --- |
| `/B2/det/setTargetMaterial`（例：`G4_WATER`） | 固定標的の材質を変える |
| `/B2/det/setChamberMaterial`（例：`G4_Ar`） | チェンバーの材質を変える |
| `/B2/det/stepMax`（例：`1.0 mm`） | トラッカー領域の最大ステップ長を設定する |

再ビルドせずに条件を切り替えられるので、マクロを順番に実行して結果を比べる、という使い方ができます。

## 磁場を設定したい（`G4GlobalMagFieldMessenger`）

飛跡検出器全体に、一様な磁場を設定できます。

```cpp
// B2a::DetectorConstruction::ConstructSDandField()
G4ThreeVector fieldValue = G4ThreeVector();
fMagFieldMessenger = new G4GlobalMagFieldMessenger(fieldValue);
fMagFieldMessenger->SetVerboseLevel(1);
```

```cfg
# run1.mac
/globalField/verbose 1
/globalField/setValue 0.2 0 0 tesla
```

ソースでは、磁場の値をゼロ（`G4ThreeVector()`）にして`G4GlobalMagFieldMessenger`を作成しています。
このクラスが`/globalField/`以下のコマンドを提供するので、マクロの`/globalField/setValue`で磁場を設定できます。
値を非ゼロにすると一様な磁場が自動的に作られ、荷電粒子の飛跡が曲がるようになります。

## ステップ長を制限したい（`G4StepLimiterPhysics`と`/B2/det/stepMax`）

磁場の中では、粒子の飛跡を細かく刻まないと曲がりを正しく計算できません。
そこで、物理リストに`G4StepLimiterPhysics`を追加し、トラッカー領域の最大ステップ長を`/B2/det/stepMax`で設定します。

この上限を有効にするには、`G4StepLimiterPhysics`が必要です。
上限を小さくするほど精度は上がりますが、計算時間も長くなります。
精度と計算時間のトレードオフを考えるきっかけになります。

## 物理リストしたい（`FTFP_BERT`）

`basic/B2`では、Geant4標準のモジュール型物理リストにある`FTFP_BERT`モデルを使っています。
`FTFP_BERT`は、高エネルギー側で`FTFP`、低エネルギー側で`BERT`に自動で切り替わるようになっている物理モデルです。

## 入射粒子したい（`PrimaryGeneratorAction`）

入射粒子は`PrimaryGeneratorAction`で`G4ParticleGun`を使って生成されます。
初期状態では、陽子を3 GeVで +Z方向に入射しています。
この粒子の種類やエネルギーは、マクロ（`/gun/particle`や`/gun/energy`）で変更できます。

## run1.macで流れを確認したい

`run1.mac`では、5つの条件で粒子を入射しています。
上から順に実行すると、「ヒットを観察する」→「材質を変える」→「磁場を加える」→「粒子を変える」の順に条件が変わります。

```cfg
# 入射粒子: デフォルト値（種類: 陽子、エネルギー: 3 GeV、方向: (0, 0, 1)）
# 表示レベル: 変更あり
/tracking/verbose 1
/run/beamOn 1
```

```cfg
# 入射粒子: デフォルト値
# 表示レベル: 変更あり
/tracking/verbose 0
/hits/verbose 2
/run/beamOn 1
```

```cfg
# 入射粒子: デフォルト値
# 表示レベル: 変更なし
## /tracking/verbose 0
## /hits/verbose 2
# ターゲットの材料を変更
/B2/det/setTargetMaterial G4_WATER
/B2/det/setChamberMaterial G4_Ar
/run/beamOn 3
```

```cfg
# 入射粒子: 陽子、エネルギー: 0.3 GeVに変更
# 表示レベル: 変更なし
## /tracking/verbose 0
## /hits/verbose 2
# 磁場を印加
/globalField/verbose 1
/globalField/setValue 0.2 0 0 tesla
/B2/det/stepMax 1.0 mm
/gun/energy 0.3 GeV
/run/beamOn 3
```

```cfg
# 入射粒子: ミューオン（mu-）、エネルギー: 300 MeVに変更
# 表示レベル: 変更なし
/gun/particle mu-
/gun/energy 300 MeV
/run/beamOn 3
```

## リファレンス

- [Example B2](https://geant4-userdoc.web.cern.ch/Doxygen/examples_doc/html/ExampleB2.html)
