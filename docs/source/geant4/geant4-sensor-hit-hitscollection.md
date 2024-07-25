# ヒット配列したい（``G4VHitsCollection`` / ``G4THitsCollection``）

```cpp
// C++11で導入された文法
// using コレクション名 = G4THitsCollection<ヒットクラス名>;
using TrackerHitsCollection = G4THitsCollection<TrackerHit>;

// C言語から使われている文法
// typedef G4THitsCollection<ヒットクラス名> コレクション名;
typedef G4THitsCollection<TrackerHit> TrackerHitsCollection;
```

``G4THitsCollection``は``G4VHitsCollection``を継承したテンプレートクラスです。
引数に自作のヒットクラス名をして、ヒット配列を生成できます。

サンプルをいくつか確認すると``typedef``と``using``で定義されているケースがありました。
基本的には同じことができるのですが、高機能な``using``を使えばよいようです。
