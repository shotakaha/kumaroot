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
/// \file B1/src/PrimaryGeneratorAction.cc
/// \brief Implementation of the B1::PrimaryGeneratorAction class

#include "PrimaryGeneratorAction.hh"

#include "G4LogicalVolumeStore.hh"
#include "G4LogicalVolume.hh"
#include "G4Box.hh"
#include "G4Tubs.hh"
#include "G4RunManager.hh"
#include "G4ParticleGun.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "G4SystemOfUnits.hh"
#include "Randomize.hh"

namespace B1
{

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

    PrimaryGeneratorAction::PrimaryGeneratorAction()
    {
        G4int n_particle = 1;
        fParticleGun = new G4ParticleGun(n_particle);

        // default particle kinematic
        G4ParticleTable *particleTable = G4ParticleTable::GetParticleTable();
        G4String particle_name;
        G4ParticleDefinition *particle = particleTable->FindParticle(particle_name="mu-");
        fParticleGun->SetParticleDefinition(particle);
        fParticleGun->SetParticleMomentumDirection(G4ThreeVector(0., -1., 0.));
        fParticleGun->SetParticleEnergy(500. * MeV);
    }

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

    PrimaryGeneratorAction::~PrimaryGeneratorAction()
    {
        delete fParticleGun;
    }

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

    void PrimaryGeneratorAction::GeneratePrimaries(G4Event *aEvent)
    {
        // this function is called at the begining of ecah event
        //

        // In order to avoid dependence of PrimaryGeneratorAction
        // on DetectorConstruction class we get Envelope volume
        // from G4LogicalVolumeStore.

        G4double tank_rmax = 0;
        G4double tank_z = 0;

        if (!fTank)
        {
            G4LogicalVolume *pTankLogical = G4LogicalVolumeStore::GetInstance()->GetVolume("TankLogical");
            if (pTankLogical)
                fTank = dynamic_cast<G4Tubs *>(pTankLogical->GetSolid());
        }

        if (fTank)
        {
            tank_rmax = fTank->GetOuterRadius();
            tank_z = fTank->GetZHalfLength() * 2;
        }
        else
        {
            G4ExceptionDescription msg;
            msg << "Envelope volume of box shape not found.\n";
            msg << "Perhaps you have changed geometry.\n";
            msg << "The gun will be place at the center.";
            G4Exception("PrimaryGeneratorAction::GeneratePrimaries()",
                        "MyCode0002", JustWarning, msg);
        }

        G4double size = 0.8;
        G4double x0 = size * tank_rmax * (G4UniformRand() - 0.5);
        G4double z0 = size * tank_rmax * (G4UniformRand() - 0.5);
        G4double y0 = 0.5 + tank_z;

        fParticleGun->SetParticlePosition(G4ThreeVector(x0, y0, z0));

        fParticleGun->GeneratePrimaryVertex(aEvent);
    }

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

}
