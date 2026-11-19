# WLSしたい（`examples/extended/optical/wls`）

WLSは、波長変換（WLS：Wavelength Shifting）ファイバーを使った検出器を扱うサンプルです。
シンチレーションバーの中にWLSファイバーを通し、発生した光子が、ファイバーを伝わって光検出器（MPPC）に届くまでを確認できます。
光子が全反射しながら伝わる様子や、波長が変換される様子を、光学物理の設定と一緒に扱います。

OpNovice2やLXeが、物性や検出器の構成を中心にしているのに対して、WLSは光子の輸送に焦点を当てています。

## ビルドしたい

```console
// サンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/extended/optical/wls
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/wls

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する（マクロは位置引数で指定する）
$ cd build
$ ./wls ../electron.mac    # バッチモード
$ ./wls                    # 対話モード（vis.macを読み込む）

// クリーンする
$ cd $G4WORK/wls
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

`cmake`でビルドし、`wls`という実行ファイルを作成します。
GDMLは使わないので、GDML無効のGeant4でも、この手順でビルドできます。
手順の詳しい説明は、[付属サンプルの遊び方](geant4-examples)を参照してください。

## 形状を確認したい

検出器は、次の部品で構成されています。

- **シンチレーションバー**：ポリスチレン製の角柱。長さは既定で1.1 m、断面の一辺は9.5 mmです。
- **WLSファイバー**：バーの中心の穴に通す、PMMA製のファイバー。既定の半径は0.5 mmです。長さは`/WLS/setWLSLength`で指定し、`electron.mac`では1 mにしています。
- **クラッド**：ファイバーを覆う層。層の数は`/WLS/setNumOfLayers`で0〜2層に設定します。
- **コーティング**：バーの表面を覆う反射材。酸化チタン（TiO₂）15%とポリスチレン85%の混合物です。
- **ミラー**：ファイバーの端に置く反射面。`/WLS/setMirror true`で有効にします。
- **光検出器（MPPC）**：ファイバーの端に置く光検出器。形状は、円形（`Circle`）か正方形（`Square`）から選べます。

形状は、`WLSDetectorConstruction`で作ります。
形状に関するパラメータは、すべて`/WLS/`のコマンドで変えられます。

:::{note}

README の説明は、単純なファイバーの形状を前提にしています。
現在のソースには、シンチレーションバーやコーティングを含む形状も定義されています。
付属のマクロ（`electron.mac`）は、この形状を使っています。

:::

## 物質を選びたい

ファイバーのコアやクラッドには、いくつかの物質を使えます。
屈折率は、物質ごとに次のとおりです。

| 物質 | 屈折率 |
| --- | --- |
| PMMA | 1.60 |
| Pethylene | 1.49 |
| FPethylene | 1.42 |
| Polystyrene | 1.60 |
| Silicone | 1.46 |

空気（`G4_AIR`）と真空（`G4_Galactic`）も使えます。
物質の詳しい定義は、`WLSMaterials`で行っています。

## マクロの流れを確認したい

付属のマクロは、次の3つです。

| ファイル | 内容 |
| --- | --- |
| `electron.mac` | 10 MeVの電子を、GPS（一般粒子源）で10イベント撃つ。形状はこのマクロで設定する |
| `wls.in` | 2.10 eVの光学光子を、GPSで撃つ。最後のランは10000イベント |
| `vis.mac` | 可視化の設定。対話モードで読み込まれる |

`electron.mac`は、次のような流れです（抜粋）。

```cfg
/WLS/setPhotonDetGeometry Circle
/WLS/setWLSLength 1. m
/WLS/setWLSRadius 0.5 mm
/WLS/setMirror true
/WLS/setBarLength 1.1 m
/run/initialize
/gps/particle e-
/gps/energy 10 MeV
/gps/pos/type Plane
/gps/pos/shape Circle
/gps/pos/radius 0.5 mm
/run/beamOn 10
```

`electron.mac`では、形状のコマンドを`/run/initialize`の前に、GPSの設定を後に置いています。

## 光子の輸送と物理過程を設定したい

光学物理は、ほかのサンプルと同じように、`FTFP_BERT`をベースに、電磁過程を`G4EmStandardPhysics_option4`に置き換えて、`G4OpticalPhysics`を追加しています。

WLSの物性（吸収、発光、屈折率など）は、`WLSMaterials`で定義しています。
表面の性質は、次のコマンドで変えられます。

- `/WLS/setSurfaceRoughness`：ファイバーとクラッドの境界の粗さ
- `/WLS/setMirrorPolish`、`/WLS/setMirrorReflectivity`：ミラーの仕上げと反射率
- `/WLS/setPhotonDetPolish`、`/WLS/setPhotonDetReflectivity`：MPPCの仕上げと反射率

光子の偏光と、発光の時定数は、次のコマンドで変えられます。

- `/WLS/gun/optPhotonPolar`：光子の偏光の角度
- `/WLS/gun/setDecayTimeConstant`：発光の時定数

光子が反射を繰り返す回数には、上限があります。
上限を超えた光子は、途中で消されます。
上限は、`/stepping/setBounceLimit`で変えられます。既定値は100000です。0を指定すると、上限を無効にします。

## ヒットと集計を確認したい

光子がMPPCの表面で吸収されると、ヒットとして記録されます。
ヒットには、MPPC上の位置、光子がファイバーを出た位置、到達時刻、エネルギーが含まれます。

ヒストグラムは、`WLSRunAction`で次の3つを作ります。

- `Energy`：光子のエネルギー（2 eVから）
- `Time`：到達時刻（0〜100 ns）
- `Number of photons`：1イベントあたりの光子数（0〜100）

ランの終わりには、1イベントあたりの平均の光子数が、過程ごとに表示されます。

## 結果を確認したい

`electron.mac`（10 MeVの電子、10イベント）を実行すると、ランの終わりに次のような集計が表示されます（一例です）。

```text
Average number per event:
 TIR:          1.53e+05 +- 7.05e+04
 Exiting:      3.22e+05 +- 1.6e+05
 Bounced:      1.17e+04 +- 5.94e+03
 Clad1 Bounce: 7.88e+03 +- 4.04e+03
 Reflected:    1.81e+04 +- 8.63e+03
 Mirror:       14.3 +- 6.62
 Detector hit: 10.8 +- 5.83
```

全反射（TIR）や、ファイバーからの放出（Exiting）などの光子数が、非常に大きく表示されています。
ファイバーの中では、光子が多くの反射を繰り返すためです。
MPPCに届いた光子（Detector hit）は、1イベントあたり約10.8個でした。

`wls.in`（2.10 eVの光学光子、10000イベント）を実行すると、MPPCへのヒットは0個でした（一例です）。
このマクロは、光子の入射角を`/gps/ang/mintheta 180.0 deg`と`/gps/ang/maxtheta 90.0 deg`で指定しています。
最小値が最大値より大きいため、入射角の範囲が意図どおりでない可能性があります。
入射角の範囲を確認してから、結果を解釈してください。

## 次に読むサンプル

WLSで光子の輸送を理解したら、次のサンプルに進むとよいです。

- [LXe](geant4-examples-lxe)：液体キセノンの検出器と、光電子増倍管（PMT）での光子の検出を扱います。
- [OpNovice2](geant4-examples-opnovice2)：物性や表面の設定を、マクロで細かく扱います。
