# 可視化したい（``G4VisManager``）

```cpp
#include "G4VisExecutive.hh"

int main(int argc, char** argv)
{
    auto vm = new G4VisExecutive(argc, argv);
}
```

``main()``関数の中で``G4VisManager``を呼び出すことで、
シミュレーションの結果を表示OpenGL/Qt画面などにできます。

:::{note}

``G4VisManager``クラスがありますが、
``G4VisExecutive``クラスを使えばよいみたいです。

:::

- [](./geant4-visattributes.md)

## リファレンス

- [Adding Visualization to Your Executable](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Visualization/visexecutable.html)
