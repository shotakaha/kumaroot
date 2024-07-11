# 乱数したい（``G4Random``）

```cpp
#include "G4Random.hh"

long seed = CLHEP::HepRandom::getTheSeed();

G4debug << "Current seed: " << seed << G4endl;
```

## 乱数設定を保存／復元したい

```cpp
#include "G4Random.hh"

CLHEP::HepRandom::showEngineStatus();
CLHEP::HepRandom::saveEngineStatus("ファイル名");
CLHEP::HepRandom::restoreEngineStatus("ファイル名");
```

## 時刻ベースの乱数を設定したい

```cpp
#include <chrono>
#indlude "G4Random.hh"

long seeds[2];

// 現在時刻
auto now = std::chrono::high_resolution_clock::now();
// エポックからの時刻に変換
auto duration = now.time_since_epoch();

// ナノ秒に変換してシードにする
seeds[0] = duration.count();
// 一様乱数と組み合わせてシードにする
seeds[1] = duration.count() * G4UniformRand();

// シードをセットする
CLHEP::HepRandom::setTheSeeds(seeds);
```

``<chrono>``モジュールを使って時刻ベースの乱数を設定する方法です。
