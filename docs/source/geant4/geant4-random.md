# 乱数したい（``G4Random``）

```cpp
#include "G4Random.hh"

long seed = CLHEP::HepRandom::getTheSeed();

G4debug << "Current seed: " << seed << G4endl;
// Current seed: 3
```

## 乱数設定を保存／復元したい

```cpp
#include "G4Random.hh"

CLHEP::HepRandom::showEngineStatus();
CLHEP::HepRandom::saveEngineStatus("ファイル名");
CLHEP::HepRandom::restoreEngineStatus("ファイル名");
```

``saveEnginStatus``でファイルに保存できます。
デフォルトのファイル名は``Config.conf``になっています。

```console
$ cat Config.conf
mixmax state, file version 1.0
N=17; V[N]={414469184642473095, 1887497230718120570, 2195475624800485765, 932596286296600524, 218172641998458221, 1120322260615769150, 539175102615237389, 1629436967027825808, 719649398285478826, 1292536263533526791, 1569870862419815394, 1958103466980645205, 824192756230114970, 1491737190745264678, 601594138938872905, 896013831305951495, 207235109353979734}; counter=17; sumtot=51334242799068912;
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
