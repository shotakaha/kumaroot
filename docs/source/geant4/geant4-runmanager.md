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

[G4RunManagerFactory](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)で、環境に応じたインスタンスを作成します。
具体的には、マルチスレッド機能が有効な場合は``G4MTRunManager``、
無効な場合は``G4RunManager``のインスタンスになります。

:::{hint}

``auto``はC++11から利用できるようになった型名です。
初期化されたインスタンスから適切な型を推測します。
インスタンスがポインターである場合は``auto*``が使えます。

:::

## シングルスレッドしたい（``G4RunManager``）

```cpp
#include "G4RunManager.hh"

auto* rm = G4RunManager();
```

``G4RunManager``でシングルスレッドのアプリを作成できます。

:::{hint}

Geant4.11からマルチスレッド対応していますが、出力結果が正しいかどうかは研究者が確認する必要があります。
Geant4講習会では、マルチスレッドのアプリはデバッグが超大変と言ってました。
まず、シングルスレッドで十分テスト＆デバッグしてから、マルチスレッド化にトライするのがよいそうです。

``G4RunManagerFactory::CreateRunManager``でシングルスレッド指定（``G4RunManagerType::Serial``）することもできます。

```cpp
#include "G4RunManagerFactory.hh"

auto* rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Serial);
```

:::

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

## ランマネージャーを取得したい（``GetRunManager``）

```cpp
auto* rm = G4RunManager::GetRunManager();
auto* rm = G4RunManagerFactory::GetMasterRunManager();
```

作成済みのランマネージャーへのポインターを取得できます。

## リファレンス

- [G4RunManagerFactory - Geant4 Doxygen](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)
- [G4RunManager - Geant4 Doxygen](https://geant4.kek.jp/Reference/11.2.0/classG4RunManager.html)
