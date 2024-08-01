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
geant4-class-reference
geant4-overview
geant4-drivers
geant4-mandatory-classes
geant4-units
geant4-constants
geant4-cpp
geant4-string
```

## 例題したい

```{toctree}
---
maxdepth: 1
---
geant4-examples
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
geant4-main
geant4-user-detectorconstruction
geant4-user-physicslist
geant4-user-actioninitialization
geant4-user-primarygeneratoraction
geant4-user-runaction
geant4-user-eventaction
geant4-user-trackingaction
geant4-user-steppingaction
```

## ステップ操作したい

```{toctree}
---
maxdepth: 2
---
geant4-run
geant4-event
geant4-track
geant4-step
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

## マネージャー操作したい

```{toctree}
---
maxdepth: 1
---
geant4-runmanager
geant4-analysismanager
geant4-particlegun
```

## ジオメトリ操作したい

```cpp
auto* rm = G4RunManagerFactory::CreateRunManager();
auto* detector = new DetectorConstruction;
rm->SetUserInitialization(detector);
```

```{toctree}
---
maxdepth: 2
---
geant4-geometry
geant4-geometry-solid
geant4-logicalvolume
geant4-physicalvolume
geant4-sensor
geant4-touchable
geant4-geometry-examples
```

## マテリアル操作したい

```cpp
auto nm = new G4NistManager::Instance();
auto air = nm->FindOrBuildMaterial("G4_AIR");
```

```{toctree}
---
maxdepth: 2
---
geant4-material
geant4-material-examples
```

## 相互作用したい

```cpp
auto* rm = G4RunManagerFactory::CreateRunManager();
auto* physics = new FTFP_BERT{};
rm->SetUserInitialization(physics);
```

```{toctree}
---
maxdepth: 1
---
geant4-physics
geant4-physics-examples
```

## 入射粒子したい

```{toctree}
---
maxdepth: 2
---
geant4-source
geant4-source-examples
```

## 記録したい

```{toctree}
---
maxdepth: 1
---
geant4-scoring
geant4-scoring-sensitivedetector
geant4-scoring-multifunctionaldetector
geant4-scoring-accumulable
```

## 可視化したい

```{toctree}
geant4-vismanager
geant4-visattributes
```

## 乱数したい

```{toctree}
---
maxdepth: 1
---
geant4-random
geant4-random-direction
```

## 対話モードしたい

```{toctree}
geant4-command
geant4-macro
```

## 外部ライブラリしたい

```{toctree}
---
maxdepth: 1
---
geant4-std-chrono
geant4-fetchcontent-loguru
geant4-fetchcontent-cxxopts
geant4-fetchcontent-tomlplusplus
```

## リファレンス

- [Geant4](https://geant4.web.cern.ch/)
- [Geant4 Download](https://geant4.web.cern.ch/download/)
- [Geant4 Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/index.html)
- [Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)
- [Geant4 初心者講習会](https://wiki.kek.jp/display/geant4/Tutorial+Notes+for+Novice+Users)（Geant4 v10.0対応）
- [Geant4 初心者講習会・研究会2024](https://wiki.kek.jp/display/geant4/Geant4+Japanese+Tutorial+for+Detector+Simulation+2024)（Geant4 v11.2準拠）
