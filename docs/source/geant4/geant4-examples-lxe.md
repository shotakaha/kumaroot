# LXeしたい（`examples/extended/optical/LXe`）

LXeは、液体キセノン（LXe）のシンチレータ検出器を扱うサンプルです。
液体キセノンの周りに光電子増倍管（PMT）を並べ、ガンマ線や荷電粒子を撃ち込みます。
発生した光子が、どのようにPMTで検出されるかを確認できます。

OpNoviceやOpNovice2が光子の振る舞いを中心にしているのに対して、LXeは検出器の構成と、光子の検出までを扱います。
また、形状をオブジェクト指向で組み立てる方法と、実行中に形状を変える方法も示しています。

## ビルドしたい

```console
// サンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/extended/optical/LXe
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/LXe

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する（マクロは位置引数で指定する）
$ cd build
$ ./LXe LXe.mac    # バッチモード
$ ./LXe            # 対話モード（vis.macを読み込む）

// クリーンする
$ cd $G4WORK/LXe
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

`cmake`でビルドし、`LXe`という実行ファイルを作成します。
GDMLは使わないので、GDML無効のGeant4でも、この手順でビルドできます。
手順の詳しい説明は、[付属サンプルの遊び方](geant4-examples)を参照してください。

:::{note}

バッチモードでも、`/vis/enable`の箇所で「no graphics system」という警告が表示されます。
これは、可視化の出力先が無いことを示すだけで、シミュレーションの結果には影響しません。

:::

## 形状を確認したい

検出器は、次の部品で構成されています。

- **LXe本体**：液体キセノンの直方体。既定の寸法は、17.8 cm × 17.8 cm × 22.6 cmです。
- **PMT**：LXe本体の周りに並べる光電子増倍管。配置する数は`nx`、`ny`、`nz`で決まります。既定値は、順に2、2、3です。
- **ハウジング**：LXe本体を囲む容器。厚さは、既定で0.0635 cmです。
- **球**：LXe本体の中に置ける反射用の球。既定で有効になっています。
- **WLSスラブとファイバー**：波長変換（WLS）に使う部品。既定では無効です。

形状は、`LXeMainVolume`クラスで定義しています。
このクラスは`G4PVPlacement`を継承していて、回転、位置、親の体積を渡すだけで配置できます。

```cpp
// LXeMainVolume のコンストラクタ（宣言のみ）
LXeMainVolume(G4RotationMatrix* pRot,
              const G4ThreeVector& tlate,
              G4LogicalVolume* pMotherLogical,
              G4bool pMany,
              G4int pCopyNo,
              LXeDetectorConstruction* c);
```

形状の情報は、`LXeDetectorConstruction`が保持していて、`LXeMainVolume`が`CopyValues()`で受け取ります。
論理体積は、同じ種類の体積ごとに一度だけ作り、`static`なメンバとして保持します。

## 形状を実行中に変えたい

形状のパラメータは、`/LXe/detector/`のコマンドで変えられます。

| コマンド | 内容 |
| --- | --- |
| `/LXe/detector/dimensions x y z unit` | LXe本体の寸法 |
| `/LXe/detector/housingThickness` | ハウジングの厚さ |
| `/LXe/detector/pmtRadius` | PMTの外径 |
| `/LXe/detector/nx`、`ny`、`nz` | PMTの数（各方向） |
| `/LXe/detector/volumes/sphere` | 反射用の球の有無 |
| `/LXe/detector/reflectivity` | ハウジングの反射率 |
| `/LXe/detector/volumes/wls`、`lxe` | WLSスラブの有無と、LXe本体の有無 |
| `/LXe/detector/nfibers` | WLSファイバーの本数 |
| `/LXe/detector/defaults` | すべての値を既定値に戻す |

形状を変えるセッター（例：`SetDimensions()`）は、最後に`G4RunManager::GetRunManager()->ReinitializeGeometry()`を呼びます。
これにより、次のランの前に、新しい寸法で形状が作り直されます。

```cpp
// LXeDetectorConstruction::SetDimensions()（一部）
void LXeDetectorConstruction::SetDimensions(G4ThreeVector dims)
{
  fScint_x = dims[0];
  fScint_y = dims[1];
  fScint_z = dims[2];
  G4RunManager::GetRunManager()->ReinitializeGeometry();
}
```

## マクロの流れを確認したい

付属のマクロは、次の4つです。

| ファイル | 内容 |
| --- | --- |
| `LXe.mac` | 511 keVのガンマ線を200イベント撃つ。既定の形状を使う |
| `cerenkov.mac` | 200 MeVのμ⁺を10000イベント撃ち、1ステップだけ進ませる。発光を止めて、チェレンコフ光だけを見る |
| `photon.mac` | 7.07 eVの光学光子を10イベント撃つ。光子の輸送を確認する |
| `wls.mac` | WLSファイバーを15本配置し、511 keVの電子を撃つ |

`LXe.mac`は、次のような流れです（抜粋）。

```cfg
/LXe/detector/MainScintYield 10000
/gun/particle gamma
/gun/energy 511 keV
/LXe/pmtThreshold 4
/run/beamOn 200
```

`cerenkov.mac`では、`/LXe/detector/MainScintYield 0`で発光量を0にして、チェレンコフ光だけを観察しています。

## 物性（シンチレーション）を設定したい

液体キセノンのシンチレーションは、`LXeDetectorConstruction`で物性を定義しています。

```cpp
// LXeDetectorConstruction（一部）
fLXe_mt->AddConstProperty("SCINTILLATIONYIELD", 12000. / MeV);
fLXe_mt->AddConstProperty("SCINTILLATIONTIMECONSTANT1", 20. * ns);
fLXe_mt->AddConstProperty("SCINTILLATIONTIMECONSTANT2", 45. * ns);
fLXe_mt->AddConstProperty("SCINTILLATIONYIELD1", 1.0);
fLXe_mt->AddConstProperty("SCINTILLATIONYIELD2", 0.0);
```

発光量は、`/LXe/detector/MainScintYield`で、MeVあたりの光子数として変えられます。
WLSファイバーの発光量は、`/LXe/detector/WLSScintYield`で変えられます。

## PMTでの検出を理解したい

PMTの光電面（フォトカソード）には、光学表面（`G4OpticalSurface`）を付けています。
光電面の体積は光子を透過させないので、光子は境界面で止まります。
このとき、境界面の過程（`G4OpBoundaryProcess`）の状態が`Detection`になります。

`LXeSteppingAction`は、この状態を見つけると、`LXePMTSD`の`ProcessHits_boundary()`を呼びます。
この仕組みにより、光電面で検出された光子を、PMTのヒットとして記録します。
ふつうの検出器のように、体積の中を進む粒子から`ProcessHits()`で信号を取るのとは違う方法です。

## ヒストグラムで分布を記録したい

LXeには、あらかじめ7個のヒストグラムが用意されています。

| 番号 | 名前 | 内容 |
| --- | --- | --- |
| 1 | hits per event | 1イベントあたりのヒット数 |
| 2 | hits above threshold | しきい値以上のヒット数 |
| 3 | scintillation | 1イベントあたりのシンチレーション光子数 |
| 4 | Cerenkov | 1イベントあたりのチェレンコフ光子数 |
| 5 | absorbed | 1イベントあたりの吸収された光子数 |
| 6 | boundary absorbed | 境界面で吸収された光子数 |
| 7 | E dep | シンチレータでのエネルギー付与 |

ヒストグラムは、`/analysis/h1/set`で有効にします。
`cerenkov.mac`では、次のように設定しています。

```cfg
/analysis/setFileName cerenkov
/analysis/h1/set 1 50 0 50
/analysis/h1/set 4 100 0 200
/analysis/h1/set 7 100 0 20 MeV
```

## 結果を確認したい

ランの終わりには、ヒット数や光子数の集計が表示されます。
`LXe.mac`（511 keVのガンマ線、200イベント）を実行すると、次のような集計が表示されます（一例です）。

```text
The run was 200 events.
Number of hits per event:	 1294 +- 14.29
Number of hits per event above threshold:	 31.81 +- 0.1602
Number of scintillation photons per event :	 4306 +- 0
Number of Cerenkov photons per event:	 0.64 +- 0.06247
Number of absorbed photons per event :	 3013 +- 31.61
Total energy deposition in scintillator per event:	 513.7 +- 5.299 keV.
```

表示されたエネルギー付与は約514 keVで、入射したガンマ線の511 keVに近い値です。

`cerenkov.mac`（200 MeVのμ⁺、10000イベント）を実行すると、次のような集計が表示されます（一例です）。
発光量を0にしているので、シンチレーション光子は0になり、チェレンコフ光子だけが現れます。

```text
The run was 10000 events.
Number of hits per event:	 13.51 +- 0.0979
Number of scintillation photons per event :	 0 +- 0
Number of Cerenkov photons per event:	 53.54 +- 0.3473
Number of absorbed photons per event :	 33.52 +- 0.2223
Number of photons absorbed at boundary per event:	 6.509 +- 0.04497
Total energy deposition in scintillator per event:	 6732 +- 40.36 keV.
```

`photon.mac`（光学光子、7.07 eV、10イベント）は、光子の輸送を確認するための簡単なマクロです。
1イベントあたり、約0.3回のヒットと約0.7回の吸収が表示されます（一例です）。

## WLSを使いたい

`wls.mac`では、LXe本体をオフにして、WLSファイバーだけを使います。

```cfg
/LXe/detector/volumes/wls 1
/LXe/detector/volumes/lxe 0
/LXe/detector/nfibers 15
/LXe/detector/WLSScintYield 10000
/gun/particle e-
/gun/energy 511 keV
/run/beamOn 100
```

WLSの物性（吸収、発光、発光時刻）は、`LXeDetectorConstruction`の`fiberProperty`などで定義しています。

## 次に読むサンプル

LXeで検出器の構成と光子の検出を理解したら、次のサンプルに進むとよいです。

- `extended/optical/wls`：波長変換ファイバーを、より詳しく扱います。
- [OpNovice2](geant4-examples-opnovice2)：物性や表面の設定を、マクロで細かく扱います。
