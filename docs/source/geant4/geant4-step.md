# ステップ操作したい（``G4Step``）

```cpp
// G4Step *aStep

// ステップの始点
auto pre_step = aStep->GetPreStepPoint()

// ステップの終点
auto post_step = aStep->GetPostStepPoint()
```

**ステップ** はGeant4が粒子輸送のシミュレーションを進行する基本単位で、このステップを進める処理を**ステッピング**と呼びます。

:::{hint}

「ステップを制するものは、Geant4を制す」
・・・とは言われていませんが、それくらい重要なコンセプトだと思っています。

:::

ステップは
**始点**（``PreStepPoint``）と
**終点**（``PostStepPoint``）で構成されていて、
ステッピングすると前のステップの終点が、次のステップの始点になります。

[G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)はステップ情報を管理するクラスです。
始点と終点は[G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)クラスのオブジェクトになっています。

現在のステップの情報は、基本的に始点（``PreStepPoint``）から取得できます。

終点（``PostStepPoint``）からは、次のステップの情報を取得できます。

:::{note}

ステップの終点は、
そのステップの粒子輸送が終わったとき、もしくは、
ジオメトリの境界に到達したときに作成されます。

始点／終点ともに``G4StepPoint``オブジェクトなので、
同じ名前のメソッドが使えますが、取得できる情報が異なることがあるため留意が必要です。

:::

ステップ情報は、ユーザーアクション設定の[SteppingAction](./geant4-steppingaction.md)で設定して取得します。
このユーザーアクションの中で、必要なステップ情報の取得＆集計して、イベント情報を計算します。

```{toctree}
---
maxdepth: 1
---
geant4-step-length
geant4-step-energy
geant4-step-track
geant4-step-status
geant4-step-boundary
% geant4-step-totalenergydeposit
% geant4-step-secondary
geant4-step-volume
geant4-step-mass
geant4-step-position
geant4-step-time
geant4-step-momentum
geant4-step-velocity
geant4-step-charge
geant4-steppingaction
```

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)

:::
