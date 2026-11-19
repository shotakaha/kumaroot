# 付属サンプルの遊び方（``examples``）

```console
// 使いたいサンプルと作業ディレクトリを設定する（パスは自分の環境に合わせる）
$ export G4EXAMPLE=~/geant4/v11.X.Y/install/share/Geant4/examples/basic/B1
$ export G4WORK=~/repos/sandbox/g4work

// 作業ディレクトリにコピーして移動する
$ mkdir -p $G4WORK
$ cp -R $G4EXAMPLE $G4WORK/
$ cd $G4WORK/B1

// ビルドする
$ cmake -S . -B build
$ cmake --build build --parallel

// 実行する
$ cd build
$ ./exampleB1 run1.mac    # バッチモード
$ ./exampleB1             # 対話モード

// クリーンする
$ cd $G4WORK/B1
$ cmake --build build --target clean    # ビルドした実行ファイルなどを削除する
$ rm -r build                           # ビルド用ディレクトリごと削除する
```

Geant4には、使い方を示すサンプルが付属しています。
インストール先の`share/Geant4/examples`に入っていて、`basic`、`extended`、`advanced`の3つに分類されています。

サンプルは、一括ではなく1つずつ使います。
`G4EXAMPLE`に使いたいサンプルのディレクトリ、`G4WORK`に作業用ディレクトリを指定し、サンプルだけをコピーしてからビルドします。
インストール先のソースを変更せずに、自由に編集できます。
作業用ディレクトリの名前は任意ですが、ここでは`g4work`としました。

Geant4の環境変数は、あらかじめ読み込んでおいてください（[環境変数したい](geant4-install-shell)）。
ビルド・実行の汎用的な手順は[ビルドしたい](geant4-build)も参照してください。

:::{note}

サンプルごとの`README.md`に、そのサンプルの説明と実行方法（`HOW TO RUN`）があります。
マクロを`build/`にコピーする設定になっているかなどは、サンプルによって違うので確認してください。

:::

:::{note}

`examples`の中身は、Geant4のバージョンによって変わります。
このページの内容は、Geant4 11.4.0を確認したものです。

:::

## クリーンしたい

```console
// ビルドした実行ファイルなどだけを削除する（ビルドの設定は残す）
$ cd $G4WORK/B1
$ cmake --build build --target clean

// ビルド用ディレクトリごと削除する（最初からやり直す）
$ rm -r build

// コピーしたサンプルを削除する
$ rm -r $G4WORK/B1
```

ビルド用ディレクトリ（`build/`）にビルドの生成物がまとまっているので、`build/`を削除すれば、ビルド前の状態に戻ります。
`cmake --build build --target clean`は、実行ファイルなどのビルドの生成物だけを削除し、ビルドの設定（`cmake`で生成したファイル）は残します。
コピーしたサンプルを編集した場合は、`$G4WORK/B1`を削除すると編集内容も消えるので注意してください。

## basic（初級者向け）

`basic`は、Geant4の基本要素を学べるサンプルです。
まずはここから、ビルドして動かしてみるのがよいです。

| サンプル | 内容 |
| --- | --- |
| [B1](geant4-examples-b1) | 数個の立体からなる単純な形状。指定した領域の総線量を記録する |
| [B2](geant4-examples-b2) | 一様磁場の中にある、簡易な飛跡検出器。ヒットを記録する |
| [B3](geant4-examples-b3) | 陽電子放出断層撮影（PET）を模したシステム。放射線源を使う |
| [B4](geant4-examples-b4) | 2種類の物質を重ねた、簡易なカロリメーター。ヒストグラムとntupleを保存する |
| [B5](geant4-examples-b5) | ワイヤーチェンバー、ホドスコープ、カロリメーターを備えた、2アームのスペクトロメーター |

:::{note}

以前は初級者向けのサンプルは`novice`という名前でした。
Geant4 10.0で、`novice`が`basic`と`extended`にリファクタリングされたそうです。
`B2`、`B4`、`B5`は、それぞれ`novice/N02`、`novice/N03`、`extended/analysis/A01`が元になっています。

:::

## extended（中級者向け）

`extended`は、特定の分野での使い方を示すサンプルです。
分野ごとにカテゴリ（ディレクトリ）に分かれていて、カテゴリの中に複数のサンプルがあります。
Geant4以外のライブラリが必要なサンプルもあります。

| カテゴリ | 内容 | 代表的なサンプル |
| --- | --- | --- |
| `analysis` | Geant4のanalysisや外部ツールによるヒストグラム作成 | [AnaEx03](geant4-examples-anaex03) |
| `biasing` | イベントバイアス、スコアリング、逆モンテカルロ | `GB01`、`ReverseMC01` |
| `common` | 他のサンプルで再利用できる共通クラス | `exCommon` |
| `electromagnetic` | 電磁相互作用の物理シミュレーション（ヒストグラム付き） | `TestEm1`、`TestEm5` |
| `errorpropagation` | 誤差伝播ユーティリティ（Geant4e）の使い方 | `errProp` |
| `eventgenerator` | 一次粒子の生成方法（粒子銃、GPS、HepMC、Pythia） | `particleGun`、`exgps` |
| `exoticphysics` | 特殊なシミュレーション（古典的な磁気単極子など） | `monopole` |
| `field` | 磁場中のシミュレーション | `field01`、`BlineTracer` |
| `g3tog4` | `g3tog4`変換ツールの使い方 | `clGeometry` |
| `geometry` | 形状に関する個別の例 | `transforms` |
| `hadronic` | ハドロン物理のシミュレーション（ヒストグラム付き） | `Hadr01`、`Hadr04` |
| `medical` | 医療物理への応用 | `DICOM` |
| `optical` | 光学プロセスのシミュレーション | `OpNovice`、`LXe`、`wls` |
| `parallel` | MPIを使ったイベントレベルの並列化 | `MPI` |
| `parameterisations` | 高速シャワーのパラメータ化（`gflash`）、機械学習の推論 | `gflash`、`Par04` |
| `persistency` | 形状（GDMLかASCII）とシミュレーション出力の保存 | `gdml` |
| `physicslists` | 参照物理リストとビルダーの使い方 | `factory` |
| `polarisation` | 偏極を含む物理プロセス | `Pol01` |
| `radioactivedecay` | 放射性同位体の崩壊と、誘導放射能のシミュレーション | `rdecay01` |
| `runAndEvent` | 一次粒子とヒットの情報の関連づけ、ユーザー情報クラスの使い方 | `RE01` |
| `visualization` | 可視化機能とグラフィックスのカスタマイズ | `userVisAction` |

## advanced（上級者向け）

`advanced`は、実際のシミュレーション研究に使われている、完成したアプリケーションです。
Geant4の配布物に含まれていますが、保守と更新は各サンプルの作者の責任です。
データの処理（可視化、解析、保存）にGeant4以外のライブラリが必要なものがあるので、詳しくはサンプルごとの`README`を確認してください。

Geant4 11.4.0では、次の36個が含まれています。

`CaTS`、
`ChargeExchangeMC`、
`HGCal_testbeam`、
`IAEAphsp`、
`ICRP110_HumanPhantoms`、
`ICRP145_HumanPhantoms`、
`STCyclotron`、
`air_shower`、
`amsEcal`、
`brachytherapy`、
`composite_calorimeter`、
`dna`、
`doiPET`、
`eFLASH_radiotherapy`、
`eRosita`、
`exp_microdosimetry`、
`fastAerosol`、
`gammaknife`、
`gammaray_telescope`、
`gorad`、
`hadrontherapy`、
`human_phantom`、
`iort_therapy`、
`lAr_calorimeter`、
`medical_linac`、
`microbeam`、
`microelec_SEY`、
`microelectronics`、
`nanobeam`、
`purging_magnet`、
`stim_pixe_tomography`、
`underground_physics`、
`xray_SiliconPoreOptics`、
`xray_TESdetector`、
`xray_fluorescence`、
`xray_telescope`

## 目的に合わせて選びたい

シミュレーションの目的が明確な場合は、これらのサンプルの中から目的に近いものを選び、改造していくのが効率的です。

- Geant4を初めて使う場合は、`basic/B1`から始める
- 検出器の応答（ヒットの記録）を知りたい場合は、`basic/B2`、`basic/B5`
- カロリメーターの例は、`basic/B4`
- 光子の生成と輸送は、`extended/optical`
- 磁場の扱いは、`extended/field`
- 電磁相互作用の確認は、`extended/electromagnetic`
