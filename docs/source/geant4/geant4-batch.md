# バッチモードしたい

```cpp
#include "G4RunManager.hh"

#include "MYDetectorConstruction.hh"
#include "MYPhysicsList.hh"
#include "MYActionInitialization.hh"

int main()
{
    // RunManagerを作成
    G4RunManager *runManager = new G4RunManager;

    // 必須ユーザークラスを設定
    runManager->SetUserInitialization(new MYDetectorConstruction);
    runManager->SetUserInitialization(new MYPhysicsList);
    runManager->SetUserInitialization(new MYActionInitialization);

    // Geant4のカーネルを初期化
    runManager->Initialize()

    // ランを開始
    G4int numberOfEvent = 10
    runManager->BeamOn(numberOfEvent);

    // RunManagerを削除
    delete runManager;
    return 0;
}
```

バッチモードで実行する場合の``main()``関数です。
実行時の引数は必要ありません。
イベント数もハードコードしてあります。
