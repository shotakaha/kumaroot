# ランマネージャーしたい（``G4RunManager``）

```cpp
#include "G4RunManager.hh"

int main(int argc, char **argv)
{
    // RunManagerを作成
    G4RunManager *runManager = new G4RunManager;

    // 測定器を追加
    runManager->SetUserInitialization(ジオメトリ);

    // 物理モデル（相互作用など）を追加
    runManager->SetUserInitialization(物理モデル);

    // ユーザー設定を追加
    runManager->SetUserAction(一次粒子発生);

    // ランを開始
    runManager->BeamOn(イベント数);

    // RunManagerを削除
    delete runManager;

    return 0;
}
```

[G4RunManager](https://geant4.kek.jp/Reference/11.2.0/classG4RunManager.html)を使って、Geant4アプリケーション全体を管理／設定します。
``main()``関数の中で作成した``G4RunManager``オブジェクトに対して、測定器のジオメトリ設定、素粒子反応の物理モデル設定、入射させる一次粒子の設定を追加する、というのが基本的な使い方です。
このフローを理解しておけば、サンプルコードなどが読めるようになると思います。
