# 乱数シードをしりたい（``G4Run::GetRandomNumberStatus``）

```cpp
// G4Run *aRun
G4String status = aRun->GetRandomNumberStatus();

G4debug << "Random number status at the start of the run: " << status << G4endl;
```

ランを開始したときの、乱数発生器の状態を取得できます。
この状態値を保存することで、同じシミュレーション結果を再現できます。

:::{seealso}

- [](./geant4-random.md)
- [](./geant4-event-random.md)

:::
