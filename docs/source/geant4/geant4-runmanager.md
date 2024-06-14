# ランマネージャーしたい（``G4RunManagerFactory``）

```cpp
#include "G4RunManagerFactory.hh"

int main(int argc, char** argv) {
    auto rm = G4RunManagerFactory::CreateRunManager();

    rm->Initialize();
    delete rm;
    return 0
}
```

``G4RunManagerFactory::CreateRunManager()``で、環境に応じたインスタンスを作成します。
具体的には、マルチスレッドが有効な場合は``G4MTRunManager``、
無効な場合は``G4RunManager``のインスタンスになります。

:::{hint}

``auto``はC++11から利用できるようになった型名です。
初期化されたインスタンスから適切な型を推測します。
インスタンスがポインターである場合は``auto*``が使えます。

:::

## シングルスレッドしたい（``G4RunManager``）

```cpp
#include "G4RunManager.hh"

auto rm = new G4RunManager();
```

## マルチスレッドしたい（``G4MTRunManager``）

```cpp
#include "G4RunManager.hh"

auto rm = new G4MTRunManager();
rm->SetNumberOfThreads(8);
```

マルチスレッド機能を有効にしてビルドしていると、使うことができます。

## マクロしたい

```cfg
/run/numberOfThreads 8
/run/initialize
```

使用するスレッドの数は、マクロでも変更できます。
