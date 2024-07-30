# カスタム入射したい（``G4PrimaryParticle`` / ``G4PrimaryVertex``）

```cpp
// 入射粒子の設定
G4PrimaryParticle *particle = G4PrimaryParticle{};

// 入射点の設定
G4PrimaryVertex *vertex = G4PrimaryVertex{};

// イベントに入射点を追加
aEvent->AddPrimaryVertex(vertex);
```

``G4PrimaryParticle``と``G4PrimaryVertex``を使って
ユーザーが入射粒子を定義できます。
