# 実験したい（``G4RunManager``）

```cpp
#include "G4RunManager.hh"

#include "MYDetectorConstruction.hh"
#include "MYPhysicsList.hh"
#include "MYActionInitialization.hh"

int main(int argc, char **argv)
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

``main()``関数の中で[G4RunManager](https://geant4.kek.jp/Reference/11.2.0/classG4RunManager.html)を作成します。
``G4RunManager``はいわば実験責任者のような存在で、Geant4アプリケーション全体を管理／設定します。

:::{hint}

他のプロジェクトのコードをみても、``main()``関数の中身はほとんど変わらないと思います。

どういう測定器を使っているのかな？
どういう相互作用を仮定しているのかな？
どういうビームを使っているのかな？
という気持ちでソースを読めば、
どういうシミュレーションなのか、雰囲気はつかめると思います。

:::

:::{note}

4.9.x系までは入射粒子は``SetUserAction``メソッドで設定していましたが、
4.10.x系から``SetUserInitialization``メソッドでできるようになったそうです。

実際に、過去の自分のプロジェクトは次のようになっていました。

```cpp
// ActionInitialization
runManager->SetUserAction(一次粒子発生);
```

:::

