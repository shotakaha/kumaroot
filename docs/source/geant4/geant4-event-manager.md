# EventManagerしたい（``G4EventManager``）

```cpp
auto em = G4EventManager::GetEventManager();
const G4Event *event = em->GetConstCurrentEvent();
```

`G4EventManager`は、イベント処理全体を統括する中核的な管理クラスです。
各イベントの初期化、一次粒子の入射、トラッキング、ステッピング、ヒットの記録など、
1イベント分の処理フローを統合的に制御します。

このクラスは事実上のシングルトンとして設計されており、
`RunAction`や`TrackingAction`など、どのユーザーアクションクラスからでも、
`G4EventManager::GetEventManager()`を通じてアクセスできます。

## イベント

イベント（`G4Event`）は、素粒子反応事象の基本単位です。
1回のランの中で、複数のイベント（＝素粒子反応）が発生します。

1イベントごとに、入射した粒子の情報（粒子の種類、位置、方向、エネルギー）や、
生成された粒子ごとの飛跡情報（`G4Track`）を管理できます。

## リファレンス

- [G4Event](https://geant4.kek.jp/Reference/11.2.0/classG4EventManager.html)
