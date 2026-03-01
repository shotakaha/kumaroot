# 光センサーしたい

半導体光センサーの実装サンプルです。
光子を数えるためのヒット用クラスと、
ヒットを判定するSensitiveDetector用クラスを作成します。

## ヒット用クラスしたい（`SipmHit`）

光子1つあたりのヒット情報をまとめるためのクラスを作成します。
クラス名を`SipmHit`とし、
ヘッダーファイル（`include/SipmHit.hh`）と
ソースファイル（`src/SipmHit.cc`）を作成します。

`SipmHit`クラスでは、
SiPMのID（`fSipmID`）、
光子のエネルギー（`fEnergy`）、
光子の波長（`fWavelength`）、
光子が到達した時刻（`fArrivalTime`）、
ヒットした位置（`fPosition`）
を記録することにします。

:::{note}

SiPMはSilicone Photomultiplierの一般名称です。
浜松ホトニクスは「MPPC」の商標名で販売しています。

より汎用的にしたい場合は`PhotonCounterHit`クラス、
浜松ホトニクス製を明確にしたい場合は`MppcHit`クラス、
のように名付けてもよいかもしれません。

:::

### `include/SipmHit.hh`

```cpp
#ifndef SipmHit_h
#define SipmHit_h 1

#include "G4Allocator.h"
#include "G4THitsCollection.hh"
#include "G4ThreeVector.hh"
#include "G4VHit.hh"
#include "tls.h"

namespace NS
{
  class SipmHit : public G4VHit
  {
    public:
      SipmHit() = default;
      SipmHit(const SipmHit &) = default;
      ~SipmHit() override = default;

      SipmHit &operator(const SipmHit &) = default;
      G4bool operator==(const SipmHit &) const;

      inline void *operator new(size_t);
      inline void operator delete(void *);

      void Draw() override {};
      void Print() override;

      // Setters
      void SetSipmID(G4int id) { fSipmId = id; }
      void SetEnergy(G4double energy) { fEnergy = energy; }
      void SetWavelength(G4double wavelength) { fWavelength = wavelength; }
      void SetArrivalTime(G4double time) { fArrivalTime = time; }
      void SetPosition(G4ThreeVector position) { fPosition = position; }

      // Getters
      G4int GetSipmID() const { return fSipmID; }
      G4double GetEnergy() const { return fEnergy; }
      G4double GetWavelength() const { return fWavelength; }
      G4double GetArrivalTime() const { return fArrivalTime; }
      G4ThreeVector GetPosition() const { return fPosition; }

    private:
      G4int fSipmID{-1};
      G4double fEnergy{0.};    // eV
      G4double fWavelength{0.};    // nm
      G4double fArrivalTime{0.};   // ns
      G4ThreeVector fPosition{};
  };

  using SipmHitsCollection = G4THitsCollection<SipmHit>;
  extern G4ThreadLocal G4Allocator<SipmHit> *SipmHitAllocator;

  inline void *SipmHit::operator new(size_t)
  {
    if (!SipmHitAllocator)
      SipmHitAllocator = new G4Allocator<SipmHit>;
    return static_cast<void *>(SipmHitAllocator->MallocSingle());
  }

  inline void SipmHit::operator delete(void *hit)
  {
    SipmHitAllocator->FreeSingle(static_cast<SipmHit *>(hit));
  }
}  // namespace NS

#endif  // SipmHit_h
```

### `src/SipmHit.cc`

```cpp
#include "SipmHit.hh"

#include "G4SystemOfUnits.hh"

#include <loguru.hpp>

namespace NS
{
  G4ThreadLocal G4Allocator<SipmHit> *SipmHitAllocator = nullptr;

  // __________________________________________________
  G4bool SipmHit::operator==(const SipmHit &right) const
  {
    return (this == &right);
  }

  // __________________________________________________
  void SipmHit::Print()
  {
    VLOG_F(2, "[SipmHit] sipm_id=%d  E=%.2f eV  wl=%.1f nm  t=%.2f ns  pos=(%.1f,%.1f,%.1f) mm",
      fSipmId,
      fEnergy / eV,
      fWavelength / nm,
      fArrivalTime / ns,
      fPosition.x / mm,
      fPosition.y / mm,
      fPosition.z / mm,
    );
  }

  // __________________________________________________
  PhotonData SipmHit::ToPhotonData() const
  {
    PhotonData p;
    p.sipm_id = fSipmID;
    p.energy = fEnergy / eV;
    p.wavelength = fWavelength / nm;
    p.arrival_time = fArrivalTime / ns;
    p.pos_x = fPosition.x() / mm;
    p.pos_y = fPosition.y() / mm;
    p.pos_z = fPosition.z() / mm;
    return p;
  }
}
```

## SensitiveDetectorしたい（`SipmSD`）

光子（`G4OpticalPhoton`）を検出できるようにSensitiveDetectorを作成します。

### `include/SipmSD.hh`

```cpp
#ifndef SipmSD_h
#define SipmSD_h 1

#include "SipmHit.hh"

#include "G4VSensitiveDetector.hh"

namespace NS
{
  class SipmSD : public G4VSensitiveDetector
  {
    public:
      SipmSD(const G4String &name, const G4String &hitsCollectionName);
      ~SipmSD() override = default;

      void Initialize(G4HCofThisEvent *hce) override;
      G4bool ProcessHits(G4Step *aStep, G4TouchableHistory *) override;
      void EndOfEvent(G4HCofThisEvent *hce) override;

    private:
      SipmHitsCollection *fHitsCollection = nullptr;
  };

}  // namespace NS

#endif  // SipmSD_h
```

### `src/SipmSD.cc`

```cpp
#include "SipmSD.hh"

#include "G4Event.hh"
#include "G4EventManager.hh"
#include "G4OpticalPhoton.hh"
#include "G4SDManager.hh"
#include "G4Step.hh"
#include "G4SystemOfUnits.hh"
#include "G4Track.hh"

#include <loguru.cpp>

namespace NS
{
  SipmSD::SipmSD(const G4String &name, const G4String &hitsCollectionName) : G4VSensitiveDetector(name)
  {
    VLOG_F(2, "SipmSD: name=%s  collection=%s",
      name.c_str(),
      hitsCollectionName.c_str()
    );
    collectionName.insert(hitsCollectionName);
  }

  // __________________________________________________
  void SipmSD::Initialize(G4HCofThisEvent * /*hce*/)
  {
    fHitsCollection = new SipmHitsCollection{SensitiveDetectorName, collectionName[0]};
  }

  // __________________________________________________
  G4bool SipmSD::ProcessHits(G4Step *aStep, G4TouchableHistory *)
  {
    // Accept optical photons only
    auto particle = aStep->GetTrack()->GetParticleDefinition();
    if (particle != G4OpticalPhoton::OpticalPhotonDefinition())
    {
      return false;
    }

    auto pre = aStep->GetPreStepPoint();
    auto track = aStep->GetTrack();

    // Photon energy and wavelength
    G4double energy = pre->GetTotalEnergy();    // MeV
    G4double wavelength = (CLHEP::h_Planck * CLHEP::c_light) / energy;

    auto hit = new SipmHit();
    hit->SetSipmID(pre->GetTouchableHandle()->GetCopyNumber());
    hit->SetEnergy(energy);
    hit->SetWavelength(wavelength);
    hit->SetArrivalTime(pre->GetGlobalTime());
    hit->SetPosition(pre->GetPosition());
    hit->Print();

    fHitsCollection->insert(hit);

    // Kill the photon after detection
    track->SetTrackStatus(fStopAndKill);

    return true;
  }

  // __________________________________________________
  void SipmSD::EndOfEvent(G4HCofThisEvent * /*hce*/)
  {
    VLOG_SCOPE_F(1, "SipmSD::EndOfEvent");

    G4int n_hits = fHitsCollection->entries();
    VLOG_F(2, "n_photons: %d", n_hits);

    const G4Event *event = G4EventManager::GetEventManager()->GetConstCurrentEvent();
    G4int event_id = event->GetEventID();

    std::vector<PhotonData> photons;
    photons.reserve(n_hits);
    for (G4int i = 0; i < n_hits; ++i)
    {
      auto *h = static_cast<SipmHit *>(fHitsCollection->GetHit(i));
      photons.push_back(h->ToPhotonData());
    }

    // EventWriter::Instance()->AddPhotons(event_id, photons);
  }

}  // namespace NS
```
