# 必須クラス

```cpp
// RunManagerを作成
G4RunManager *runManager = new G4RunManager;

// 必須ユーザークラスを設定
runManager->SetUserInitialization(new MYDetectorConstruction);
runManager->SetUserInitialization(new MYPhysicsList);
runManager->SetUserInitialization(new MYActionInitialization);

// Geant4のカーネルを初期化
runManager->Initialize()
```

``MYDetectorConstruction``、
``MYPhysicsList``、
``MYActionInitialization``は
ユーザーが必ず作成しないといけない必須クラスです。

ソースコードを読むときにこのことを知っていると、
内容を読み解くときの助けになるはずです。

アプリケーションを作成したい場合、
これらを順番に実装していけばOKです。
