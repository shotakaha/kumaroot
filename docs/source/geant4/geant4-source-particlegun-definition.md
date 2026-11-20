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

## リファレンス

- [G4ParticleTable](https://geant4.kek.jp/Reference/11.2.0/classG4ParticleTable.html)
- [PDG Identifiers - Particle Data Group](https://pdg.lbl.gov/2024/pdgid/PDGIdentifiers.html)
