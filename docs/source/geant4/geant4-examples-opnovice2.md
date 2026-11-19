# OpNovice2したい（`examples/extended/optical/OpNovice2`）

OpNovice2は、OpNoviceの発展版です。
光学光子の生成と輸送を、マクロで細かく設定しながら調べられます。
水槽（`Tank`）と周りの空間（`World`）の物性、水槽の表面の物性を、マクロのコマンドで変えられます。
光子が境界面で受けた過程は、ヒストグラムに記録されます。

## ビルドしたい

```console
// サンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/extended/optical/OpNovice2
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/OpNovice2

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する（マクロは位置引数で指定する）
$ cd build
$ ./OpNovice2 electron.mac    # バッチモード
$ ./OpNovice2                 # 対話モード（vis.macを読み込む）

// クリーンする
$ cd $G4WORK/OpNovice2
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

`cmake`でビルドし、`OpNovice2`という実行ファイルを作成します。
GDMLは使わないので、GDML無効のGeant4でも、この手順でビルドできます。
手順の詳しい説明は、[付属サンプルの遊び方](geant4-examples)を参照してください。

## 形状を確認したい

形状は、次の2つの立方体です。

| 体積 | 形状 | 一辺 | 材質（既定） | 配置 |
| --- | --- | --- | --- | --- |
| World | `G4Box` | 20 m | `G4_AIR` | 原点 |
| Tank | `G4Box` | 2 m | `G4_WATER` | Worldの原点 |

Tankの材質は`/opnovice2/boxMaterial`で、Worldの材質は`/opnovice2/worldMaterial`で変えられます。
`electron.mac`では、物性を設定する前に材質を指定しています。

## マクロの流れを確認したい

付属のマクロは、目的ごとに分かれています。

| ファイル | 内容 |
| --- | --- |
| `OpNovice2.mac` | Tankの中で光学光子を1つ撃つ |
| `electron.mac` | 電子（`e-`）を撃ち、チェレンコフ光とシンチレーション光を観察する |
| `scint_by_particle.mac` | 粒子ごとに、シンチレーションの発光量や時定数を変えて撃ち分ける |
| `wls.mac` | 2種類の波長変換（WLS）を設定し、光学光子を撃つ |
| `boundary.mac` | 表面のモデル、種類、仕上げを変えて、光子の境界面の過程を記録する |
| `fresnel.mac` | 偏光を指定した光学光子を、ランダムな方向から表面に当て、反射率と透過率を入射角ごとに記録する |
| `complexRindex.mac` | 複素屈折率を持つ誘電体・金属の表面を使う |
| `coated.mac` | 薄膜コーティングでの反射と屈折を示す |
| `vis.mac` | 可視化の設定 |

`electron.mac`は、次のような流れです（抜粋）。

```cfg
/opnovice2/boxMaterial G4_BGO
/opnovice2/worldMaterial G4_AIR
/opnovice2/boxProperty RINDEX 0.000002 1.3 0.000008 1.4
/opnovice2/boxProperty ABSLENGTH 0.000002 1 0.000005 2 0.000008 3
/process/optical/cerenkov/setMaxPhotons 3
/process/optical/cerenkov/setMaxBetaChange 10
/run/initialize
/analysis/setFileName electron
/gun/particle e-
/gun/energy 1 MeV
/run/beamOn 100
```

`electron.mac`では、材質と物性を`/run/initialize`の前に設定し、ヒストグラムとファイル名は後に設定しています。
`/run/beamOn`でイベントを実行すると、`/analysis/setFileName`で指定したファイル名に、ヒストグラムが保存されます。

## 物性をマクロで設定したい

物性は、対象ごとに用意されたコマンドで設定します。

| 対象 | エネルギー依存の物性 | 定数 |
| --- | --- | --- |
| 水槽（`Tank`） | `/opnovice2/boxProperty NAME EN1 V1 EN2 V2 ...` | `/opnovice2/boxConstProperty NAME VALUE` |
| 空間（`World`） | `/opnovice2/worldProperty NAME EN1 V1 EN2 V2 ...` | `/opnovice2/worldConstProperty NAME VALUE` |
| 表面 | `/opnovice2/surfaceProperty NAME EN1 V1 EN2 V2 ...` | `/opnovice2/surfaceConstProperty NAME VALUE` |

- エネルギーは、MeV単位で書きます。`0.000002`は2 eVです。
- 値は、Geant4の内部単位で書きます。
- エネルギー依存の物性には、エネルギーと値の組を複数並べて書けます。

例えば、次のコマンドは、水槽の屈折率を2 eVで1.3、5 eVで1.32、8 eVで1.34にします。

```cfg
/opnovice2/boxProperty RINDEX 0.000002 1.3 0.000005 1.32 0.000008 1.34
```

## 境界面を設定したい

水槽の表面は、`G4OpticalSurface`を`G4LogicalBorderSurface`で、水槽とWorldの境界に置いています。

```cpp
// DetectorConstruction::Construct()（一部）
fSurface = new G4OpticalSurface("Surface");
fSurface->SetType(dielectric_dielectric);
fSurface->SetFinish(ground);
fSurface->SetMaterialPropertiesTable(fSurfaceMPT);

auto surface = new G4LogicalBorderSurface("Surface", fTank, world_PV, fSurface);
```

表面は、次のマクロのコマンドで変えられます。

- `/opnovice2/surfaceModel`：モデル（`glisur`、`unified`、`LUT`、`DAVIS`）
- `/opnovice2/surfaceType`：種類（`dielectric_metal`、`dielectric_dielectric`、`dielectric_LUT`、`dielectric_LUTDAVIS`）
- `/opnovice2/surfaceFinish`：仕上げ（`polished`、`ground`、`Rough_LUT`、`Polished_LUT`など）
- `/opnovice2/surfaceSigmaAlpha`：粗さ（ground仕上げなどで使う）
- `/opnovice2/stepping/killOnSecondSurface`：2つ目の表面に入った光子を殺す。表面での散乱だけを見たいときに使う

`boundary.mac`は、これらのコマンドを組み合わせて、表面の設定を変えながら光子を撃ちます。
設定ごとに`/analysis/setFileName`でファイル名を変えているので、結果を比べられます。

## ヒストグラムで分布を記録したい

OpNovice2には、あらかじめ26個のヒストグラムが用意されています。
主なものは、次のとおりです。

| 番号 | 内容 |
| --- | --- |
| 1 | チェレンコフ光のスペクトル |
| 2 | シンチレーション光のスペクトル |
| 3 | シンチレーション光の発生時刻 |
| 4〜6 | WLSの吸収スペクトル、発光スペクトル、発光時刻 |
| 7〜9 | WLS2の吸収スペクトル、発光スペクトル、発光時刻 |
| 10 | 境界面での過程の状態（`G4OpBoundaryProcessStatus`） |
| 11〜19 | 表面で散乱・屈折した光子の運動量の向き |
| 20〜26 | 屈折、反射、全反射、吸収、透過などの割合 |

番号11から26は、表面の+X側から入った光子だけを記録します。
表面での最初の相互作用だけを記録します。

ヒストグラムは、`/analysis/h1/set`で、ビン数と範囲を指定して有効にします。
単位は、エネルギーがeV、時間がnsに固定されています。

```cfg
/analysis/h1/set 1 100 0 10    # チェレンコフ光のスペクトル。0〜10 eVを100ビン
/analysis/h1/set 3 400 0 200   # シンチレーション時刻。0〜200 nsを400ビン
```

- `/analysis/setFileName`：ファイル名を指定する（既定は`opnovice2`）
- `/analysis/h1/setAscii`：テキストのファイルにも書き出す

## 結果を確認したい

ランの終わりには、光子の生成と過程の数の集計が表示されます。
`electron.mac`（電子 1 MeV、100イベント）を実行すると、次のような集計が表示されます（一例です）。

```text
Number of events: 100
Average number of Cerenkov photons created per event: 44
 Average energy per photon: 5.2 eV.
Average number of scintillation photons created per event: 3e+03
```

チェレンコフ光のエネルギーは、`/tracking/verbose 1`以上にすると、光子ごとの群速度も表示されます。

## 物理過程を調整したい

チェレンコフ光とシンチレーション光は、`/process/optical/`のコマンドで調整します。

- `/process/optical/cerenkov/setMaxPhotons`：1ステップあたりの、チェレンコフ光の最大数
- `/process/optical/cerenkov/setMaxBetaChange`：ステップごとの速度の変化量の上限
- `/process/optical/scintillation/setByParticleType`：粒子ごとに発光の設定を変える
- `/process/optical/scintillation/setFiniteRiseTime`：発光の立ち上がり時間を有効にする
- `/process/optical/wls/setTimeProfile`：WLSの発光時刻の分布（`delta`など）

`scint_by_particle.mac`は、粒子ごとに発光の量や時定数を変えて、電子・陽子・α粒子などを撃ち分けます。
`wls.mac`は、WLSの吸収長（`WLSABSLENGTH`）、発光の成分（`WLSCOMPONENT`）、1回の波長変換で出る光子数（`WLSMEANNUMBERPHOTONS`）などを設定しています。

## 次に読むサンプル

OpNovice2で、物性や表面の設定を詳しく扱えるようになったら、次のサンプルに進むとよいです。

- `extended/optical/LXe`：液体キセノンの検出器と、光電子増倍管（PMT）での光子の検出を扱います。
- `extended/optical/wls`：波長変換ファイバーを扱います。
