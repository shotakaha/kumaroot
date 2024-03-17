# ランアクションしたい（``G4UserRunAction``）

ランごとのデータを収集したい場合は、
``G4UserRunAction``クラスを継承したクラスを作成します。

```cpp

#include "G4UserRunAction.hh"

class RunAction: public G4UserRunAction
{
    public:
        RunAction();
        ~RunAction() override = default;

        void BeginOfRunAction(const G4Run *aRun) override;
        void EndOfRunAction(const G4Run *aRun) override;
    private:
        fEnergyDeposit = -1;
}
```

## ラン開始したい（``BeginOfRunAction``）

```cpp
void RunAction::BeginOfRunAction(const G4Run *aRun)
{
    // 内部変数（プライベート変数など）の初期化など
    fEnergyDeposit = 0;
}
```

``BeginOfRunAction``はラン開始に実行されるメソッドです。
ランごとのデータを代入するために用意した変数は、ここで初期化できます。

## ラン終了したい（``EndOfRunAction``）

```cpp
void RunAction::EndOfRunAction(const G4Run *aRun)
{


}
```

``EndOfRunAction``はランの終わりに実行されるメソッドです。
すべてのイベントのデータを集計して、ランサマリーを表示できたりします。
