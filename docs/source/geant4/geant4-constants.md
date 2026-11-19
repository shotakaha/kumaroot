# 物理定数したい（`G4PhysicalConstants.hh`）

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

CLHEPライブラリの物理定数を`using`宣言で読み込んでいます。
読み込んだ後は、`CLHEP::`を付けずに名前だけで使えます。

| 名前 | 値 | 単位 |
|---|---|---|
| `CLHEP::pi` | $3.141592653589793$ | （無次元） |
| `CLHEP::c_light` | $2.99792458 \times 10^{8}$ | m / s |
| `CLHEP::h_Planck` | $4.135667696923859 \times 10^{-15}$ | eV s |
| `CLHEP::hbar_Planck` | $6.582119569509066 \times 10^{-16}$ | eV s |
| `CLHEP::hbarc` | $1.9732705 \times 10^{-7}$ | eV m |

## 波長をエネルギーに変換したい

```cpp
#include <vector>

#include "G4PhysicalConstants.hh"
#include "G4SystemOfUnits.hh"

std::vector<G4double> WavelengthToEnergy(const std::vector<G4double>& wavelength)
{
    // wavelength: 波長（Geant4の内部単位の値）
    // energy: エネルギー（[eV]）
    const G4double h = CLHEP::h_Planck;  // [MeV ns]
    const G4double c = CLHEP::c_light / (m/ns);  // [m/ns] に変換
    std::vector<G4double> energy;
    for (auto length : wavelength) {
        length = length / m;  // [m] に変換
        G4double e = h * c / length / eV;  // [eV] に変換
        energy.push_back(e);
    }
    return energy;
}

// 使い方: 波長 500 nm を eV に変換する
// auto e = WavelengthToEnergy({500 * nm});
```

:::{math}

E = h\nu = \frac{hc}{\lambda}

:::
