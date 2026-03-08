# 光学光子したい（`G4OpticalPhoton`）

```cpp
#include "G4OpticalPhoton.hh"
#include "G4PhysicalConstants.hh"
#include "G4VProcess.hh"
#include "G4AnalysisManager.hh"

G4bool OpticalSD::ProcessHits(G4Step* aStep, G4TouchableHistory*)
{
    // OpticalSDは、PMTやSiPMなどを想定して自作した光センサー用のSensitiveDetector
    // ProcessHitsの中で「光学光子」をフィルタリング

    G4Track* track = aStep->GetTrack();

    // 1. 光学光子であるかの確認
    // 光学光子 =
    // G4OpticalPhoton::Definitions() or
    // G4OpticalPhoton::OpticalPhoton() or
    // G4OpticalPhoton::OpticalPhotonDefinition()
    if (track->GetDefinition() != G4OpticalPhoton::Definition()) {
        return false;
    }

    // 2. 光学光子を計測
    G4double energy = track->GetTotalEnergy();
    G4double wavelength = (h_Planck * c_light) / energy;
    G4double time = track->GetGlobalTime();
    G4ThreeVector pos = aStep->GetPostStepPoint()->GetPosition();

    // 3. 光学光子を生成したプロセス名を取得
    // プロセス名が取得できない場合は"Primary"（一次入射）
    const G4VProcess* process = track->GetCreatorProcess();
    G4String processName = (process) ? process->GetProcessName() : "Primary";

    // 4. AnalysisManagerに保存
    G4AnalysisManager* am = G4AnalysisManager::Instance();
    am->FillNtupleDColumn(0, energy / eV);
    am->FillNtupleDColumn(1, wavelength / nm);
    am->FillNtupleDColumn(2, time / ns);
    am->FillNtupleDColumn(3, pos.x() / mm);
    am->FillNtupleDColumn(4, pos.y() / mm);
    am->FillNtupleDColumn(5, pos.z() / mm);
    am->FillNtupleSColumn(6, processName);
    am->AddNtupleRow();

    // 5. 検出した光子を消去
    // 光センサーの受光面で吸収。計算コストを抑える。
    track->SetTrackStatus(fStopAndKill);

    return true;
}
```

`G4OpticalPhoton`（光学光子）は、光を「波」として扱うクラスです。
反射、屈折、吸収、波長変換などの物理プロセスをシミュレーションしたい場合に使います。

上記のサンプルは、
光電子増倍管（PMT）や半導体光検出器（SiPM）の受光面で、
光学光子を測定することを想定したものです。
トラック情報から`G4OpticalPhoton`であることを確認し、
光学光子1つずつの基本情報と生成元のプロセスを取得しています。
受光面に到達したあとの計算は不要なので、`fStopAndKill`で吸収されたものとみなしています。
