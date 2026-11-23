# 型エイリアスしたい（`G4Types.hh`）

Geant4の基本型は、`G4Types.hh`で定義されています。
プラットフォームごとの型の実装の違いを吸収するため、C++の基本型に`G4`の接頭辞を付けたエイリアスを使います。

## 型を確認したい

| エイリアス | 元の型 |
|---|---|
| `G4double` | `double` |
| `G4float` | `float` |
| `G4int` | `int` |
| `G4long` | `long` |
| `G4bool` | `bool` |
| `G4complex` | `std::complex<G4double>` |

Windowsで使うDLLのエクスポート・インポート用マクロ（`G4DLLEXPORT`、`G4DLLIMPORT`）も、`G4Types.hh`で定義されています。

## 使いたい

```cpp
#include "G4Types.hh"
#include "G4String.hh"
#include "G4SystemOfUnits.hh"

G4String name = "Geant4";     // std::stringに相当
G4int numberOfParticles = 1;  // intに相当
G4double energy = 1.0 * GeV;  // doubleに相当
```

:::{note}

`G4Types.hh`だけでは、`G4String`と`GeV`は使えません。

- `G4String`は`G4String.hh`で定義されています（`globals.hh`を読み込んでも使えます）。
- `GeV`などの単位は`G4SystemOfUnits.hh`で定義されています。

:::

## 関連ヘッダーを確認したい

- `G4Types.hh`：基本型とDLLマクロ
- `G4String.hh`：`G4String`
- `G4SystemOfUnits.hh`：単位（`GeV`、`MeV`など）
- `globals.hh`：上記をまとめて読み込む一括ヘッダー

コーディングの慣習は、[Geant4のコーディングガイドライン](geant4-cpp-geant4)も参照してください。
