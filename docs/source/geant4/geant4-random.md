# 乱数したい（``G4Random::getTheSeed``）

```cpp
#include "Randomize.hh"

long seed = G4Random::getTheSeed();
// long seed = CLHEP::HepRandom::getTheSeed();

G4debug << "Current seed: " << seed << G4endl;
// Current seed: 3
```

``G4Random``で乱数シードを操作できます。
読み込むヘッダーファイル名は``Randomize.hh``なので、注意が必要です。

:::{note}

``G4Random``は``CLHEP::HepRandom``のエイリアスです。
``CLHEP::HepRandom``を直接使う場合、``Randomize.hh``のインクルードは不要です。

:::

## 乱数設定を保存／復元したい（``G4Random::saveEngineStatus``）

```cpp
#include "Randomize.hh``

G4Random::showEngineStatus();
G4Random::saveEngineStatus("ファイル名");
G4Random::restoreEngineStatus("ファイル名");
```

``saveEnginStatus``でファイルに保存できます。
デフォルトのファイル名は``Config.conf``になっています。

```console
$ cat Config.conf
mixmax state, file version 1.0
N=17; V[N]={414469184642473095, 1887497230718120570, 2195475624800485765, 932596286296600524, 218172641998458221, 1120322260615769150, 539175102615237389, 1629436967027825808, 719649398285478826, 1292536263533526791, 1569870862419815394, 1958103466980645205, 824192756230114970, 1491737190745264678, 601594138938872905, 896013831305951495, 207235109353979734}; counter=17; sumtot=51334242799068912;
```

## 時刻ベースの乱数を設定したい（``G4Random::setTheSeeds``）

```cpp
#include <chrono>
#include "Randomize.hh"

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
G4Random::setTheSeeds(seeds);
```

``<chrono>``モジュールを使って時刻ベースの乱数を設定する方法です。

:::{seealso}

- [CLHEP::HepRandom](https://geant4.kek.jp/Reference/11.2.0/classCLHEP_1_1HepRandom.html)
- [CLHEP::HepRandomEngine](https://geant4.kek.jp/Reference/11.2.0/classCLHEP_1_1HepRandomEngine.html)
- [The HEPRandom module in CLHEP](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Fundamentals/global.html#the-heprandom-module-in-clhep)
- [CLHEP Document](https://proj-clhep.web.cern.ch/proj-clhep/)

:::
