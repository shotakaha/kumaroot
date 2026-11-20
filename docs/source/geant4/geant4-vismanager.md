# 可視化したい（`G4VisManager`）

```cpp
#include "G4VisExecutive.hh"

int main(int argc, char** argv)
{
    G4VisManager* visManager = new G4VisExecutive(argc, argv);
    visManager->Initialize();

    // ...（シミュレーションの処理）

    delete visManager;
}
```

`main()`関数の中で`G4VisExecutive`を生成し、`Initialize()`を呼び出すことで、
シミュレーションの結果をOpenGL/Qt画面などに表示できます。

:::{note}

`G4VisManager`は可視化の基底クラスで、`G4VisExecutive`はその具体的な実装です。
通常は`G4VisExecutive`を生成して使います。

:::

対話モードでは、`G4UIExecutive`で画面を開き、`vis.mac`を読み込んで可視化の設定をします。

```cpp
#include "G4UIExecutive.hh"

G4UIExecutive* ui = new G4UIExecutive(argc, argv);
ui->SessionStart();
```

- [](geant4-visattributes)

## リファレンス

- [Adding Visualization to Your Executable](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Visualization/visexecutable.html)
