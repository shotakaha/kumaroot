# 物理定数したい（``G4PhysicalConstants.hh``）

```cpp
using CLHEP::alpha_rcl2;
using CLHEP::amu;
using CLHEP::amu_c2;
using CLHEP::Avogadro;
using CLHEP::Bohr_radius;
using CLHEP::c_light;
using CLHEP::c_squared;
using CLHEP::classic_electr_radius;
using CLHEP::e_squared;
using CLHEP::electron_charge;
using CLHEP::electron_Compton_length;
using CLHEP::electron_mass_c2;
using CLHEP::elm_coupling;
using CLHEP::epsilon0;
using CLHEP::fine_structure_const;
using CLHEP::h_Planck;
using CLHEP::halfpi;
using CLHEP::hbar_Planck;
using CLHEP::hbarc;
using CLHEP::hbarc_squared;
using CLHEP::k_Boltzmann;
using CLHEP::kGasThreshold;
using CLHEP::mu0;
using CLHEP::neutron_mass_c2;
using CLHEP::pi;
using CLHEP::pi2;
using CLHEP::proton_mass_c2;
using CLHEP::STP_Pressure;
using CLHEP::STP_Temperature;
using CLHEP::twopi;
using CLHEP::twopi_mc2_rcl2;
using CLHEP::Bohr_magneton;
using CLHEP::nuclear_magneton;
using CLHEP::universe_mean_density;
```

CLHEPライブラリの物理定数を読み込み、グローバル変数として使えるようになっています。

| 名前 | 値 | 単位 |
|---|---|---|
| ``CLHEP::pi`` | 3.141592653589793d | |
| ``CLHEP::c_light`` | $299.792458$ | km / s |
| ``CLHEP::h_Planck`` | $4.135669239559144 \times 10^{-12}$ | eV s |
| ``CLHEP::hbar_Planck`` | $6.582122024689376 \times 10^{-13}$ |eV s |
| ``CLHEP::hbarc`` | $1.9732705406375647 \times 10^{-10}$ | eV m |

## 波長をエネルギーに変換したい

```cpp
#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnit.hh"

std::vector<G4double> WavelengthToEnergy(const std::vector<G4double>& wavelength)
{
    // wavelength [m]
    // energy [eV]
    // h_Planck = 4.135669239559144e-12 [eV s]
    // c_light  = 299.792458 [km / s]
    const G4double h = CLHEP::h_Planck;
    const G4double c = CLHEP::c_light / m;  // [m] に変換
    std::vector<G4double> energy;
    for (auto length : wavelength) {
        length = length / m;     // [m] に変換
        G4double e = h * c / length / eV;  // [eV] に変換
        energy.push_back(e);
    };
    return energy;
};
```

:::{math}

E = h\nu = \frac{hc}{\lambda}

:::
