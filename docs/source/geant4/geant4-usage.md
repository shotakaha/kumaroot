# Geant4の使い方

[Geant4](https://geant4.org/)は高エネルギー物理学分野で利用されている測定器シミュレーションのツールキットです。

日本ではKEKを中心としたGeant4日本グループが定期的に初心者向け講習会を開催しています。
僕も2009年12月に開催された講習会に参加しましたが、プログラミング超初心者だったので、
自分がわからないこともわからないレベルでかなり苦労（というか挫折）した覚えがあります。

宇宙線測定のアウトリーチ活動を進めるにつれて、簡単でよいので測定器シミュレーションができたらもっと楽しいだろうなと思い、使い方の理解＆整理に再挑戦してみます。
ここでは、Geant4日本グループが公開している[初心者講習会資料](https://wiki.kek.jp/display/geant4/Tutorial+Notes+for+Novice+Users)を参考にしています。

```{toctree}
---
maxdepth: 1
---
geant4-install
geant4-build
geant4-examples
geant4-runmanager

```

## 物質したい

```{toctree}
---
maxdepth: 1
---
geant4-material
geant4-element
geant4-water
geant4-air
geant4-acrylic
geant4-vacuum
geant4-glass
geant4-petroleum
```

## 測定器したい

- ``G4VUserDetectorConstruction``

## 相互作用したい

- ``G4VUserPhysicsList``

## 粒子したい

- ``G4VUserPrimaryGeneratorAction``
- ``G4UserRunAction``
- ``G4UserEventAction``
- ``G4UserTrackingAction``
- ``G4UserSteppingAction``
- ``G4UserStackingAction``

## リファレンス

- [Geant4](https://geant4.web.cern.ch/)
- [Geant4 Download](https://geant4.web.cern.ch/download/)
- [Geant4 Book for Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/index.html)
- [Geant4 Material Database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html)
