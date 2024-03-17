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
/// \file B1/src/DetectorConstruction.cc
/// \brief Implementation of the B1::DetectorConstruction class

#include "DetectorConstruction.hh"

#include "G4RunManager.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4Tubs.hh"
#include "G4Cons.hh"
#include "G4Orb.hh"
#include "G4Sphere.hh"
#include "G4Trd.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"

namespace B1
{

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

    G4VPhysicalVolume *DetectorConstruction::Construct()
    {
        // Get nist material manager
        G4NistManager *nist = G4NistManager::Instance();

        // Option to switch on/off checking of volumes overlaps
        //
        G4bool checkOverlaps = true;

        //
        // World
        //
        G4double world_x = 1. * m;
        G4double world_y = 1. * m;
        G4double world_z = 1. * m;
        G4Material *fAir = nist->FindOrBuildMaterial("G4_AIR");

        auto pWorldSolid = new G4Box(
            "WorldSolid",
            0.5 * world_x,
            0.5 * world_y,
            0.5 * world_z); // its size

        auto pWorldLogical = new G4LogicalVolume(
            pWorldSolid,     // its solid
            fAir,            // its material
            "WorldLogical"); // its name

        G4RotationMatrix rotation;
        G4ThreeVector direction;
        G4Transform3D location;

        rotation = G4RotationMatrix();
        direction = G4ThreeVector();
        location = G4Transform3D(rotation, direction);

        auto pWorldPhysical = new G4PVPlacement(
            location,
            pWorldLogical,         // its logical volume
            "WorldPhysical",        // its name
            nullptr,         // its mother  volume
            false,           // no boolean operation
            0,               // copy number
            checkOverlaps);  // overlaps checking

        //
        // Tank
        //
        G4double diameter = 39.3 * cm;
        G4double height = 41.4 * cm;
        G4double rmin, rmax, z, sphi, dphi;
        auto pTankSolid = new G4Tubs(
            "TankSolid",
            rmin = 0.,
            rmax = 0.5 * diameter,
            z = 0.5 * height,
            sphi = 0. * deg,
            dphi = 360. *deg);

        // Fill tank with water
        G4Material *fWater = nist->FindOrBuildMaterial("G4_WATER");
        auto pTankLogical = new G4LogicalVolume(
            pTankSolid,
            fWater,
            "TankLogical");

        //rotation = G4RotationMatrix(0.*deg, 90.*deg, 0.*deg);
        rotation = G4RotationMatrix(0.*deg, 90*deg, 0*deg);
        direction = G4ThreeVector();
        location = G4Transform3D(rotation, direction);

        new G4PVPlacement(
            location,
            pTankLogical,         // its logical volume
            "TankPhysical",        // its name
            pWorldLogical,         // its mother  volume
            false,           // no boolean operation
            0,               // copy number
            checkOverlaps);  // overlaps checking

        fScoringVolume = pTankLogical;

        //
        // always return the physical World
        //
        return pWorldPhysical;
    }

    //....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

}
