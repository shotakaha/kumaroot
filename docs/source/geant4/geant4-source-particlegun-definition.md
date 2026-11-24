# 入射粒子の種類したい（`SetParticleDefinition`）

```cpp
#include "G4ParticleTable.hh"

G4ParticleGun* fParticleGun = new G4ParticleGun(1);
G4ParticleTable* table = G4ParticleTable::GetParticleTable();

// 粒子名で検索する（例: 電子）
G4ParticleDefinition* particle = table->FindParticle("e-");
// PDGコードで検索する（例: 電子は11）
// G4ParticleDefinition* particle = table->FindParticle(11);

if (particle == nullptr) {
    G4cerr << "粒子が見つかりません" << G4endl;
    return;
}
fParticleGun->SetParticleDefinition(particle);
```

`SetParticleDefinition`で入射する粒子の種類を変更できます。

ただし、粒子名を直接指定して設定することはできません。
`G4ParticleGun`には粒子名を受け取るメソッドがないため、
まず`G4ParticleTable`から粒子情報（質量、電荷、スピンなど）を取得して、
それを`SetParticleDefinition`に渡す手順になっています。

`FindParticle`は、粒子名（`"e-"`）のほかに、PDGコード（電子は`11`）でも検索できます。
PDGコードの一覧は、下のリファレンスを参照してください。
該当する粒子がないと`nullptr`を返すため、渡す前に確認します。

## 電子にしたい

```cpp
G4ParticleDefinition* particle = table->FindParticle("e-");   // 粒子名
// G4ParticleDefinition* particle = table->FindParticle(11);  // PDGコード
fParticleGun->SetParticleDefinition(particle);
```

粒子名（`"e-"`）またはPDGコード（`11`）で指定できます。
どちらか一方を使います。

## 陽電子にしたい

```cpp
G4ParticleDefinition* particle = table->FindParticle("e+");   // 粒子名
// G4ParticleDefinition* particle = table->FindParticle(-11);  // PDGコード
fParticleGun->SetParticleDefinition(particle);
```

粒子名（`"e+"`）またはPDGコード（`-11`）で指定できます。
陽電子のPDGコードは、電子（`11`）の符号を反転した`-11`です。

## ミューオンにしたい

```cpp
G4ParticleDefinition* particle = table->FindParticle("mu-");   // 粒子名
// G4ParticleDefinition* particle = table->FindParticle(13);   // PDGコード
fParticleGun->SetParticleDefinition(particle);
```

粒子名（`"mu-"`）またはPDGコード（`13`）で指定できます。
ミューオンは、レプトンに分類されます。

## ニュートリノにしたい

```cpp
G4ParticleDefinition* particle = table->FindParticle("nu_e");   // 粒子名
// G4ParticleDefinition* particle = table->FindParticle(12);     // PDGコード
fParticleGun->SetParticleDefinition(particle);
```

粒子名（`"nu_e"`）またはPDGコード（`12`）で指定できます。
ここでは電子ニュートリノを例にしています。
ニュートリノも、レプトンに分類されます。

## ガンマ線にしたい

```cpp
G4ParticleDefinition* particle = table->FindParticle("gamma");   // 粒子名
// G4ParticleDefinition* particle = table->FindParticle(22);       // PDGコード
fParticleGun->SetParticleDefinition(particle);
```

粒子名（`"gamma"`）またはPDGコード（`22`）で指定できます。
ガンマ線（光子）は、ボソンに分類されます。

## 陽子にしたい

```cpp
G4ParticleDefinition* particle = table->FindParticle("proton");   // 粒子名
// G4ParticleDefinition* particle = table->FindParticle(2212);    // PDGコード
fParticleGun->SetParticleDefinition(particle);
```

粒子名（`"proton"`）またはPDGコード（`2212`）で指定できます。
陽子は、バリオン（重粒子）に分類されます。

## パイ中間子にしたい

```cpp
G4ParticleDefinition* particle = table->FindParticle("pi+");   // 粒子名
// G4ParticleDefinition* particle = table->FindParticle(211);   // PDGコード
fParticleGun->SetParticleDefinition(particle);
```

粒子名（`"pi+"`）またはPDGコード（`211`）で指定できます。
π⁺は、メソンに分類されます。

## リファレンス

- [G4ParticleTable](https://geant4.kek.jp/Reference/11.4.0/classG4ParticleTable.html)
- [PDG Identifiers - Particle Data Group](https://pdg.lbl.gov/2024/pdgid/PDGIdentifiers.html)
