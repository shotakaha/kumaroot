# 入射粒子を分布したい（``G4GeneralParticleSource``）

```cpp
void PrimaryGenerator::GeneratePrimaries(G4Event *aEvent)
{
    auto gps = G4GeneralParticleSource{};
    gps->SetParticleDefinition(...);
    gps->SetNumberOfParticles(...);

    gps->SetFlatSampling(true);
    gps->SetMultipleVertex(true);

    // G4EventにGPSを追加する
    gps->GeneratePrymaryVertex(aEvent);
};
```

``G4GeneralParticleSource``はGeant4標準のPrimaryGeneratorのひとです。
``G4ParticleGun``と異なり、平面上に入射粒子を生成できます。

## リファレンス

- [G4GeneralParticleSource](https://geant4.kek.jp/Reference/11.2.0/classG4GeneralParticleSource.html)
- [Geant4 General Particle Source - Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/generalParticleSource.html)
