# Geant4の使い方

[Geant4](https://geant4.org/)は高エネルギー物理学分野で利用されている測定器シミュレーションのツールキットです。

日本ではKEKを中心としたGeant4日本グループが定期的に初心者向け講習会を開催しています。
僕も2009年12月に開催された講習会に参加しましたが、プログラミング超初心者だったので、
自分がわからないこともわからないレベルでかなり苦労（というか挫折）した覚えがあります。

宇宙線測定のアウトリーチ活動を進めるにつれて、簡単でよいので測定器シミュレーションができたらもっと楽しいだろうなと思い、使い方の理解＆整理に再挑戦してみます。
ここでは、Geant4日本グループが公開している[初心者講習会資料](https://wiki.kek.jp/display/geant4/Tutorial+Notes+for+Novice+Users)を参考にしています。

## インストール

基本的に自分でビルドしてインストールする必要があります。
``spack``というスパコン向けのパッケージ管理ツールでのインストールを試してみたので、おまけ程度に載せておきます。

```{toctree}
---
maxdepth: 1
---
geant4-versions
geant4-install
geant4-spack
geant4-install-env
```

## エラー対処

遭遇したエラーと対処方法をまとめました。

```{toctree}
---
maxdepth: 2
---
geant4-errors
```

## 知っておきたかったこと

```{toctree}
---
maxdepth: 1
---
geant4-document
geant4-examples
geant4-class-reference
geant4-overview
geant4-drivers
geant4-mandatory-classes
geant4-units
geant4-constants
geant4-cpp
```

## 例題したい

```{toctree}
---
maxdepth: 1
---
geant4-build
geant4-examples-b1
geant4-examples-b2
geant4-examples-b3
geant4-examples-b4
geant4-examples-b5
geant4-examples-anaex03
```

## 実験したい

```{toctree}
---
maxdepth: 1
---
geant4-command
geant4-macro
geant4-batch
```

## マクロしたい

```{toctree}
---
maxdepth: 1
---
geant4-macro-setup
geant4-macro-vis
geant4-macro-gui
```

## 必須クラスしたい

```{toctree}
---
maxdepth: 1
---
geant4-detectorconstruction
geant4-physicslist
geant4-primarygeneratoraction
```

## ユーザー操作したい

```{toctree}
---
maxdepth: 1
---
geant4-runmanager
geant4-actioninitialization
geant4-analysismanager
geant4-particlegun
```

## ボリュームしたい

論理ボリュームは、Geant4空間の中に配置される前の状態で``G4LogicalVolume``クラスで作成します。
物理ボリュームは、Geant4空間に配置された論理ボリュームのことで、``G4VPhysicalVolume``を継承したクラスで作成します。

```{toctree}
---
maxdepth: 1
---
geant4-logicalvolume
geant4-logicalvolume-mass
geant4-logicalvolume-visattributes
geant4-logicalvolume-sensitivedetector
geant4-logicalvolume-fieldmanager
geant4-physicalvolume
geant4-physicalvolume-pvplacement
geant4-physicalvolume-pvreplica
```

## マテリアルしたい

```cpp
G4NistManager *nm = new G4NistManager::Instance();
auto air = nm->FindOrBuildMaterial("G4_AIR");    // 空気
auto water = nm->FindOrBuildMaterial("G4_WATER");    // 水
auto vacuum = nm->FindOrBuildMaterial("G4_Galactic");    // 真空
auto acrylic = nm->FindOrBuildMaterial("G4_PLEXIGLASS");    // アクリルガラス
auto sc = nm->FindOrBuildMaterial("G4_PLASTIC_SC_VINYLTOLUENE");    // プラスチックシンチレーター
```

```{toctree}
---
maxdepth: 1
---
geant4-nistmanager
geant4-material-table
geant4-element
geant4-material-air
geant4-material-water
geant4-material-ethanol
geant4-material-acrylic
geant4-material-vacuum
geant4-material-glass
geant4-material-petroleum
geant4-material-plastic-scintillator
```

## ジオメトリしたい

```cpp
auto* rm = G4RunManagerFactory::CreateRunManager();
auto* detector = new DetectorConstruction;
rm->SetUserInitialization(detector);
```

```{toctree}
---
maxdepth: 1
---
geant4-geometry
geant4-geometry-world
geant4-geometry-tank
geant4-pmt
geant4-calorimeter
geant4-hodoscope
geant4-qe
geant4-magneticfield
```

## 相互作用したい

```cpp
auto* rm = G4RunManagerFactory::CreateRunManager();
auto* physics = new FTFP_BERT;
rm->SetUserInitialization(physics);
```

```{toctree}
---
maxdepth: 1
---
geant4-ftfp_bert
geant4-opticalphoton
```

## ユーザーアクションしたい

```cpp
auto* rm = G4RunManagerFactory::CreateRunManager();
auto* actions = new ActionInitialization;
rm->SetUserInitialization(actions);
```

```{toctree}
---
maxdepth: 1
---
geant4-run
geant4-event
geant4-track
geant4-steppingaction
```

- ``G4UserStackingAction``

## 測定したい

```{toctree}
---
maxdepth: 1
---
geant4-scoring
geant4-scoring-manager
geant4-scoring-sensitivedetector
geant4-scoring-hitscollection
geant4-scoring-multifunctionaldetector
geant4-scoring-accumulable
```

## 入射粒子したい

```{toctree}
geant4-particletable
geant4-muon
geant4-geantino
```

## ステップ操作したい（``G4Step`` / ``G4Track``）

```{toctree}
---
maxdepth: 1
---
geant4-step
geant4-step-track
geant4-step-steplength
geant4-step-particle
geant4-step-boundary
geant4-step-status
% geant4-step-totalenergydeposit
% geant4-step-secondary
geant4-step-energy
geant4-step-volume
geant4-step-mass
geant4-step-position
geant4-step-time
geant4-step-momentum
geant4-step-velocity
geant4-step-charge
```

## 可視化したい

```{toctree}
geant4-vismanager
geant4-visattributes
```

## 外部ライブラリしたい

```{toctree}
---
maxdepth: 1
---
geant4-loguru
```

## リファレンス

- [Geant4](https://geant4.web.cern.ch/)
- [Geant4 Download](https://geant4.web.cern.ch/download/)
- [Geant4 Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/index.html)
- [Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)
- [Geant4 初心者講習会](https://wiki.kek.jp/display/geant4/Tutorial+Notes+for+Novice+Users)（Geant4 v10.0対応）
- [Geant4 初心者講習会・研究会2024](https://wiki.kek.jp/display/geant4/Geant4+Japanese+Tutorial+for+Detector+Simulation+2024)（Geant4 v11.2準拠）
