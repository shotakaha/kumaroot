# 多機能検出器したい（``G4MultiFunctionalDetector``）

```cpp
G4MultiFunctionalDetector *detector = new G4MultiFunctionalDetector("検出器の名前");

G4String filter_name, particle_name;
G4SDParticleFilter *electron_filter = new G4SDParticleFilter(filter_name="electronFilter", particle_name="e-");

G4VPrimitiveScorer *primitive;
// エネルギー損失（＝ステップごとのエネルギー損失の総和）
primitive = new G4PSEnergyDeposit("energy_deposit");
primitive->SetFilter(electron_filter);
detector->RegisterPrimitive(primitive);

// ボリューム内で生成された二次粒子の数
primitive = new G4PSNofSecondary("n_secondary");
primitive->SetFilter(electron_filter);
detector->RegisterPrimitive(primitive);
```

``G4MultiFunctionalDetector``は``G4VSensitiveDetector``クラスを継承した簡易的なSensitive Detectorです。
``G4VSDFilter``の派生クラスと``G4VPrimitiveScorer``の派生クラスを追加することでスコアリングできます。

[G4MultiFunctionalDetector and G4VPrimitiveScorer](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Detector/hit.html#g4multifunctionaldetector-and-g4vprimitivescorer)を参照してください。

## スコアリングしたい（``G4VPrimitiveScorer``）

```cpp
G4VPrimitiveScorer *primitive;

// トラックの長さ（＝セル内のステップ長の総和）
primitive = new G4PSTrackLength("track_length");
// トラックの長さ（＝セル内を通過した粒子のステップ長の総和）
primitive = new G4PSPassageTrackLength("passage_track_length");

// エネルギー損失（＝ステップごとのエネルギー損失の総和）
primitive = new G4PSEnergyDeposit("energy_deposit");

// ボリューム内の粒子数（＝通過した粒子のトラック数）
primitive = new G4PSPassageCurrent("passage_current");
// ボリュームあたりのフラックス（＝ボリューム内のトラック長／ボリュームの体積）
primitive = new G4PSCellFlux("cell_flux");
// ボリュームあたりのフラックス（＝ボリューム内を通過した粒子のトラック長／ボリュームの体積）
primitive = new G4PSPassageCellFlux("passage_cell_flux");

// 生成された二次粒子の数
primitive = new G4PSNofSecondary("n_secondary");
// ステップ数
primitive = new G4PSNofStep("n_step");
// セル内の電荷（＝ボリューム内で停止した粒子の電荷の総和）
primitive = new G4PSCellCharge("cell_charge");
```

## フィルターしたい（``G4SDParticleFilter``）

```cpp
G4SDParticleFilter *gamma_filter = new G4SDParticleFilter("gammaFilter", "gamma");
G4SDParticleFilter *electron_filter = new G4SDParticleFilter("electronFilter", "e-");
G4SDParticleFilter *positron_filter = new G4SDParticleFilter("positronFilter", "e+");

G4SDParticleFilter *ep_filter = new G4SDParticleFilter("epFilter");
ep_filter->add("e-");
ep_filter->add("e+");

G4SDParticleFilter *charged_filter = new G4SDChargedFilter("chargedFilter");
G4SDParticleFilter *neutral_filter = new G4SDNeutralFilter("neutralFilter");
```

``G4SDParticleFilter``で、粒子の種類を絞るフィルターを作成できます。
``gamma_filter``を通すと、ガンマ線だけが測定できます。
``add("粒子名")``で複数の粒子を対象とするフィルターを作成できます。

そのほかにも電荷フィルター（``G4SDChargedFilter``と``G4SDNeutralFilter``）、
運動エネルギーフィルター（``G4SDKineticEnergyFilter``）、
粒子＆運動ネルギーフィルター（``G4SDParticleWithEnergyFilter``）があります。
