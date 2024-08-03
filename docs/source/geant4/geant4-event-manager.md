# EventManagerしたい（``G4EventManager``）

```cpp
auto em = G4EventManager::GetEventManager();
const G4Event *event = em->GetConstCurrentEvent();
```

``G4EventManager``はイベントの進行管理を担当するManagerクラスです。
シングルトンになっているので、コードのどこからでも呼び出すことができます。

## イベント

イベント（``G4Event``）は、素粒子反応事象の基本単位です。
1回のランの中で、複数のイベント（＝素粒子反応）が発生します。

1イベントごとに、入射した粒子の情報（粒子の種類、位置、方向、エネルギー）や、
生成された粒子ごとの飛跡（``G4Track``）を管理してくれます。

## リファレンス

- [G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4EventManager.html)
