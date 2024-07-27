# ヒット配列したい（``G4VHitsCollection`` / ``G4THitsCollection``）

```cpp
// C++11で導入された文法
// using コレクション名 = G4THitsCollection<ヒットクラス名>;
using SensorHitsCollection = G4THitsCollection<SensorHit>;

// C言語から使われている文法
// typedef G4THitsCollection<ヒットクラス名> コレクション名;
typedef G4THitsCollection<SensorHit> SensorHitsCollection;
```

ユーザーが作成したヒットクラス（ここでは``SensorHit``）を使って、ヒット配列（``SensorHitsCollection``）の型エイリアスを定義しています。

``G4THitsCollection``は``G4VHitsCollection``を継承したテンプレートクラスですが、そのさらに親をたどると``std:vector``をベースにしているようです。

サンプルをいくつか確認すると``typedef``と``using``で定義されているケースがありました。
基本的には同じことができるのですが、高機能な``using``を使えばよいようです。
