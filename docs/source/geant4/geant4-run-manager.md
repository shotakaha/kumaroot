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

**ランマネージャー**は、クラス名の通り、実験責任者の役割を担うインスタンスです。
ユーザーがこのランマネージャーに対して、ジオメトリの作り方、相互作用モデル、入射粒子の設定などを指示することで、Geant4シミュレーションが実行できます。

以前は``G4RunManager``を直接呼んでいましたが、v4.11以降では、
[G4RunManagerFactory](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)を通じて、インスタンスを作成するのがよいみたいです。

このクラスは、Geant4本体をビルドした環境に応じたランマネージャーを作成します。
具体的には、マルチスレッド機能が有効な場合は``G4MTRunManager``、
無効な場合は``G4RunManager``のインスタンスを作成します。

:::{hint}

``auto``はC++11から利用できるようになった型名です。
初期化されたインスタンスから適切な型を推測します。
インスタンスがポインターである場合は``auto*``が使えます。

:::

## シングルスレッドしたい（``G4RunManager``）

```cpp
#include "G4RunManagerFactory.hh"

auto* rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Serial);
```

``CreateRunManager``の引数を``G4RunManagerType::Serial``にすると
シングルスレッドモードになります。

:::{hint}

Geant4.11からマルチスレッドに対応しており、シミュレーションをマルチスレッドで実行できるようになっています。
しかし、マルチスレッドで実行できることと、その結果が正しいかどうかは別物です。
Geant4はあくまでシミュレーションをするためのツールキットであり、
その出力が正しいかどうかはユーザーが確認＆判断する必要があります。

Geant4講習会2024に参加し、エキスパートたちに聞いたところ、
マルチスレッドのアプリはデバッグが超大変だよと言ってました。
まず、シングルスレッドで十分テスト＆デバッグしてから、
マルチスレッド化にトライするのがよいそうです。

:::

## マルチスレッドしたい（``G4MTRunManager``）

```cpp
#include "G4RunManagerFactory.hh"

auto rm = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Default);
rm->SetNumberOfThreads(8);
```

マルチスレッド機能を有効にしてビルドしていると、
デフォルトでマルチスレッドモードになります。
``SetNumberOfThreads``でスレッド数を変更できます。

## マクロしたい

```cfg
/run/numberOfThreads 8
/run/initialize
```

マルチスレッドモードのアプリの場合、
使用するスレッドの数は、マクロでも変更できます。

## ランマネージャーを取得したい（``GetRunManager``）

```cpp
auto* rm = G4RunManager::GetRunManager();
auto* rm = G4RunManagerFactory::GetMasterRunManager();
```

作成済みのランマネージャーへのポインターを取得できます。

:::{seealso}

- [G4RunManagerFactory - Geant4 Doxygen](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)
- [G4RunManager - Geant4 Doxygen](https://geant4.kek.jp/Reference/11.2.0/classG4RunManager.html)

:::
