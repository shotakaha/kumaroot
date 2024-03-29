//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
//
/// \file B1/src/SteppingAction.cc
/// \brief Implementation of the B1::SteppingAction class

#include "SteppingAction.hh"
#include "EventAction.hh"
#include "DetectorConstruction.hh"

#include "G4Step.hh"
#include "G4Event.hh"
#include "G4RunManager.hh"
#include "G4LogicalVolume.hh"

namespace B1
{

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

    SteppingAction::SteppingAction(EventAction *aAction)
        : fEventAction(aAction)
    {
    }

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

    void SteppingAction::UserSteppingAction(const G4Step *aStep)
    {
        if (!fScoringVolume)
        {
            const auto detConstruction = static_cast<const DetectorConstruction *>(
                G4RunManager::GetRunManager()->GetUserDetectorConstruction());
            fScoringVolume = detConstruction->GetScoringVolume();
        }

        // get volume of the current step
        G4LogicalVolume *volume = aStep->GetPreStepPoint()->GetTouchableHandle()->GetVolume()->GetLogicalVolume();

        // check if we are in scoring volume
        if (volume != fScoringVolume)
            return;

        // collect energy deposited in this step
        G4double energy_deposit = aStep->GetTotalEnergyDeposit();
        fEventAction->AddEnergyDeposit(energy_deposit);

        // テスト
        auto point = aStep->GetPreStepPoint();
        auto position = point->GetPosition();
        auto local_time = point->GetLocalTime();
        auto global_time = point->GetGlobalTime();
        auto proper_time = point->GetProperTime();
        auto total_energy = point->GetTotalEnergy();
        auto charge = point->GetCharge();
        auto status = point->GetStepStatus();

        G4cout << "StepStatus: " << status << G4endl;
        G4cout << "Position: " << position << G4endl;
        G4cout << "Local Time: " << local_time << G4endl;
        G4cout << "Global Time: " << global_time << G4endl;
        G4cout << "Proper Time: " << proper_time << G4endl;
        G4cout << "Total Energy: " << total_energy << G4endl;
        G4cout << "Total Energy Deposit: " << energy_deposit << G4endl;
        G4cout << "Charge: " << charge << G4endl;

        auto track = aStep->GetTrack();
        auto track_id = track->GetTrackID();
        G4cout << "Track ID: " << track_id << G4endl;
    }

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

}
