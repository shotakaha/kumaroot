# バッチモードしたい

```cpp
#include "DetectorConstruction.hh"
#include "PhysicsList.hh"
#include "ActionInitialization.hh"

#include "G4RunManagerFactory.hh"

int main(int argc, char** argv)
{
    // RunManagerを作成
    auto rm = G4RunManagerFactory::CreateRunManager();

    // 測定器
    auto* detector = new DetectorConstruction;
    rm->SetUserInitialization(detector);

    // 相互作用
    auto* physics = new PhysicsList;
    rm->SetUserInitialization(physics);

    // ユーザー設定
    auto* actions = new ActionInitialization;
    rm->SetUserInitialization(actions);

    // Geant4のカーネルを初期化
    rm->Initialize()

    // ランを開始
    // 第一引数: イベント数
    G4int numberOfEvent = argv[1]
    rm->BeamOn(numberOfEvent);

    // RunManagerを削除
    delete rm;

    return 0;
}
```

バッチモードで実行する場合の必要最低限の``main()``関数です。
第一引数をイベント数としました。
