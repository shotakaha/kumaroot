# ステッピングアクションしたい（``G4UserSteppingAction``）

ステップごとのデータを収集したい場合は、
``G4UserSteppingAction``クラスを継承したクラスを作成します。

:::{hint}

測定器のヒット情報を取得するときにステップ情報へのアクセスが必要になります。
その場合は、迷わず[G4VSensitiveDetectorクラス](./geant4-sensor-sensitivedetector.md)を使いましょう。

:::

:::{seealso}

- [](./geant4-step.md)
- [](./geant4-sensor-sensitivedetector.md)

:::

## 親クラス

- [G4UserSteppingAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserSteppingAction.html)

```cpp
G4UserSteppingAction();
virtual ~G4UserSteppingAction() = default;
virtual void UserSteppingAction(const G4Step*){};
```

親クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``UserSteppingAction()``は、ステッピング処理で実行される関数です。
仮想関数になっているため、設定は必須ではありません。
必要に応じて自作クラスでoverrideします。

## SteppingActionクラス

```cpp
// include/SteppingAction.hh

#ifndef SteppingAction_h
#define SteppingAction_h 1

#include "G4UserSteppingAction.hh"

namespace ToyMC
{

class SteppingAction : public G4UserSteppingAction
{
  public:
    SteppingAction() = default;
    ~SteppingAction() = default;

    void UserSteppingAction(const G4Step* aStep) override;
}

}  // namespace ToyMC

#endif
```

ステッピングアクションは``G4UserSteppingAction``を継承したクラスを自作します。
仮想関数として定義されている``UserSteppingAction``を実装します。

## UserSteppingAction

```cpp
void SteppingAction::UserSteppingAction(const G4Step *aStep)
{
    G4coud << "UserSteppingAction" << G4endl;

    G4int parent_id = aStep->GetTrack()->GetParentID();

    // 入射粒子の位置を表示
    if (parent_id == 0) {
        G4int track_id = aStep->GetTrack()->GetTrackID();
        G4int step_id = aStep->GetTrack()->GetCurrentStepNumber();
        auto p = aStep->GetPreStepPoint()->GetPosition() / mm;
        auto q = aStep->GetPostStepPoint()->GetPosition() / mm;
        G4cout << "TrackID: " << track_id << G4endl;
        G4cout << "StepID: " << step_id << G4endl;
        G4cout
          << "Pre : (" << p.getX()
          << ", " << p.getY()
          << ", " << p.getZ()
          << ") [mm]"
          << G4endl;
        G4cout
          << "Post: (" << q.getX()
          << ", " << q.getY()
          << ", " << q.getZ()
          << ") [mm]"
          << G4endl;
    }
}
```

入射した粒子のステッピング処理を確認するため、ステップ番号とその両端の座標を表示してみました。
このようにデバッグ的に``UserSteppingAction``をしてみるのはよいと思いますが、測定器のヒット情報は``G4VSensitiveDetector::ProcessHits``に定義したほうがよいと思います。

:::{seealso}

- [](./geant4-sensor-sensitivedetector.md)

:::

## 境界判断したい

```cpp

void SteppingAction::UserSteppingAction(const G4Step *aStep)
{
    auto pre_step = aStep->GetPreStepPoint();
    auto status = pre_step->GetStepStatus();

    if (status == fWorldBoundary) { G4cout << "ワールド境界の外に到達" << G4endl; };
    if (status == fGeomBoundary) { G4cout << "ジオメトリ境界に到達 = いまのボリュームに入射した" << G4endl; };
    if (status == fUserDefinedLimit) { G4cout << "ユーザー設定のリミットに到達" << G4endl; };
    if (status == fUndefined) { G4coud << "ステップが未定義" << G4endl; };
};
```
