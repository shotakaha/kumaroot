# ステップ操作したい（`G4Step`）

```cpp
// void UserSteppingAction(const G4Step* aStep) の中

// ステップの始点
auto pre_step = aStep->GetPreStepPoint();

// ステップの終点
auto post_step = aStep->GetPostStepPoint();
```

`G4Step`はステップ情報を管理するクラスです。

**ステップ** はGeant4が粒子輸送のシミュレーションを進行する基本単位です。
このステップを進める処理を**ステッピング**と呼びます。

ステップは
**始点**（`PreStepPoint`）と
**終点**（`PostStepPoint`）で構成されていて、
ステッピングすると前のステップの終点が、次のステップの始点になります。

始点と終点はそれぞれ`G4StepPoint`クラスのオブジェクトになっています。
現在のステップの情報は、基本的に始点（`PreStepPoint`）から取得できます。
終点（`PostStepPoint`）からは、ステップが終わった時点の情報を取得できます。

:::{note}

ステップの終点は、
そのステップの粒子輸送が終わったとき、もしくは、
ジオメトリの境界に到達したときに作成されます。

始点／終点ともに`G4StepPoint`オブジェクトなので、
同じ名前のメソッドが使えますが、取得できる情報が異なることがあるため留意が必要です。

:::

ユーザーアクション設定の
[UserSteppingAction](geant4-user-steppingaction)や
[SensitiveDetectorのProcessHits](geant4-sensor-sensitivedetector)などで
以下のようなステップおよびステップポイントに紐づいた物理量を取得したいときに使います。

```{toctree}
---
maxdepth: 1
---
geant4-step-totalenergydeposit
geant4-step-track
geant4-step-length
geant4-step-secondary
geant4-step-steppoint
geant4-step-steppoint-status
geant4-step-steppoint-boundary
geant4-step-steppoint-volume
geant4-step-steppoint-mass
geant4-step-steppoint-position
geant4-step-steppoint-time
geant4-step-steppoint-momentum
geant4-step-steppoint-velocity
geant4-step-steppoint-charge
geant4-step-steppoint-energy
geant4-step-steppoint-touchable
```

:::{hint}

「ステップを制するものは、Geant4を制す」
・・・とは言われていませんが、それくらい重要なコンセプトだと思っています。

:::

:::{seealso}

- [](geant4-user-steppingaction)
- [](geant4-sensor-sensitivedetector)
- [](geant4-sensor-hit-fill)

:::

## リファレンス

- [G4Step](https://geant4.kek.jp/Reference/11.4.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.4.0/classG4StepPoint.html)
