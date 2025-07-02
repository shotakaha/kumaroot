# 乱数シードを取得したい（`G4Event::GetRandomNumberStatus`）

```cpp
void MyEventAction::BeginOfEventAction(const G4Event* aEvent) {
    G4String status = aEvent->GetRandomNumberStatus();
    G4debug << "Random number status at the start of the event: " << status << G4endl;
}
```

`G4Event::GetRandomNumberStatus`で、それぞれのイベントの乱数状態を取得できます。
この状態値を使うと、同じシミュレーション結果を再現できます。

```cpp
void MyEventAction::EndOfEventAction(const G4Event* aEvent) {
    G4String status = aEvent->GetRandomNumberStatus();

    // ファイルに追記
    std::ofstream fout("randomStatus.txt", std::ios::app);
    fout << "EventID," << aEvent->GetEventID() << "," << status << "\n";
    fout.close();
}
```

`EndOfEventAction`で、この状態値を保存するのが一般的です。

:::{seealso}

- [](./geant4-random.md)
- [](./geant4-run-random.md)

:::
