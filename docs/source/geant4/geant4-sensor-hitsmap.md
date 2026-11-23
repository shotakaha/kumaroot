# ヒット辞書したい（``G4THitsMap``）

```cpp
#include "G4THitsMap.hh"

// ヒット辞書を作成（検出器名、コレクション名）
auto hitsMap = new G4THitsMap<G4double>(detName, colName);

// コピー番号をキーにして、エネルギー損失を積算する
(*hitsMap)[copyNo] += edep;
```

``G4HitsMap``は、辞書型で保存できるヒット配列です。
イベントごとにデータを出力せず、積算する場合に使います。

## リファレンス

- [G4VHitsCollection](https://geant4.kek.jp/Reference/11.2.0/classG4VHitsCollection.html)
- [G4THitsMap](https://geant4.kek.jp/Reference/11.2.0/classG4THitsMap.html)
