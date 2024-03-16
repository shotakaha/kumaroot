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
```

## 知っておきたかったこと

```{toctree}
---
maxdepth: 1
---
geant4-class-reference
geant4-overview
geant4-geometry
geant4-drivers
geant4-scoring
geant4-mandatory-classes
geant4-units
geant4-cpp
```

## 例題したい

```{toctree}
---
maxdepth: 1
---
geant4-build
geant4-examples
geant4-examples-b1
geant4-examples-b2
```

## 実験したい

```cpp
G4RunManager *runManager = new G4RunManager;
runManager->SetUserInitialization(new MYDetectorConstruction);
runManager->SetUserInitialization(new MYPhysicsList);
runManager->SetUserInitialization(new MYActionInitialization);
runManager->Initialize()
```

```{toctree}
---
maxdepth: 1
---
geant4-batch
geant4-macro
geant4-runmanager
geant4-uimanager
geant4-detectorconstruction
geant4-actioninitialization
geant4-steppingaction
geant4-step
```

## 物質したい

```cpp
G4NistManager *nistManager = new G4NistManager::Instance();
G4Material *fAir = nistManager->FindOrBuildMaterial("G4_AIR");
G4Material *fWater = nistManager->FindOrBuildMaterial("G4_WATER");
```

```{toctree}
---
maxdepth: 1
---
geant4-material
geant4-element
geant4-air
geant4-water
geant4-ethanol
geant4-acrylic
geant4-vacuum
geant4-glass
geant4-petroleum
geant4-plastic-scintillator
```

## 測定器したい

```cpp
runManager->SetUserInitialization(new DetectorConstruction());
```

```{toctree}
---
maxdepth: 1
---
geant4-world
geant4-tank
geant4-pmt
geant4-calorimeter
geant4-hodoscope
geant4-qe
```

## 相互作用したい

```cpp
runManager->SetUserInitialization(new FTFP_BERT);
```

```{toctree}
geant4-physicslist
```

## ユーザーアクションしたい

```cpp
runManager->SetUserInitialization(new ActionInitialization());
```

```{toctree}
geant4-particles
geant4-particlegun
geant4-primarygeneratoraction
geant4-eventaction
geant4-track
geant4-run
```

- ``G4VUserPrimaryGeneratorAction``
- ``G4UserRunAction``
- ``G4UserEventAction``
- ``G4UserTrackingAction``
- ``G4UserSteppingAction``
- ``G4UserStackingAction``

## 測定したい

```{toctree}
geant4-scoringmanager
```

## 可視化したい

```cpp
G4VisManager* visManager = new G4VisExecutive;
visManager->Initialize();
```

```{toctree}
geant4-vismanager
```

## 未分類

```{toctree}
geant4-constants
geant4-userclasses
```

## リファレンス

- [Geant4](https://geant4.web.cern.ch/)
- [Geant4 Download](https://geant4.web.cern.ch/download/)
- [Geant4 Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/index.html)
- [Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)
