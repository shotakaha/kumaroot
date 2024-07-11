# 乱数シードをしりたい（``G4Event::GetRandomNumberStatus``）

```cpp
// G4Event *aEvent
G4String status = aEvent->GetRandomNumberStatus();

G4debug << "Random number status at the start of the event: " << status << G4endl;

```

イベントを開始したときの、乱数発生器の状態を取得できます。
この状態値を保存することで、同じシミュレーション結果を再現できます。

:::{seealso}

- [](./geant4-random.md)
- [](./geant4-run-random.md)

:::
