# トラックの粒子をしりたい（``G4Track::GetParticleDefinition``）

```cpp
// G4Track *aTrack
auto particle = aTrack->GetParticleDefinition();

// その他
aTrack->GetDynamicParticle();
aTrack->GetDefinition();
```

## 粒子名をしりたい（``GetParticleName``）

```cpp
G4String particle_name = particle->GetParticleName();
G4debug << "ParticleName=" << particle_name << G4endl;
// ParticleName=gamma
// ParticleName=mu-
```

## PDG番号をしりたい（``GetPDGEncoding``）

```cpp
G4int particle_id = particle->GetPDGEncoding();
G4debug << "PDGEncoding=" << particle_id << G4endl;
// PDGEncoding=22    // gamma
// PDGEncoding=13    // mu-
```

``GetPDGEncoding``でPDG（Particle Data Group）でMC用に定義された粒子の固有番号を取得します。
解析でフィルタリングするとき、粒子名ではなく、この番号を使うと便利なこともあるので、出力データに追加しておくとよいと思います。

## 粒子を判別したい

```cpp
if (aTrack->GetDefinition() == G4OpticalPhoton::OpticalPhotonDefinition())
{
  // 光子の場合の処理;
};

if (aTrack->GetDefinition() == G4Electron::ElectronDefinition())
{
  // 電子の場合の処理;
}
```

## リファレンス

- [G4Track](https://geant4.kek.jp/Reference/11.2.0/classG4Track.html)
- [G4ParticleDefinition](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleDefinition.html)
- [Monte Carlo Particle Numbering Scheme - PGD(2024)](https://pdg.lbl.gov/2024/reviews/rpp2024-rev-monte-carlo-numbering.pdf)
