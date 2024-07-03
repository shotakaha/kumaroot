# ステップ情報したい（``G4Step``）

```cpp
// 始点
auto pre_step = aStep->GetPreStepPoint()

// 終点
auto post_step = aStep->GetPostStepPoint()
```

[G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)はステップ情報を管理するクラスです。
ユーザーアクション設定の[SteppingAction](./geant4-steppingaction.md)でステップ情報を取得したいときに使います。
ステップはGeant4シミュレーションの基本単位で、
**始点**（``PreStepPoint``）と
**終点**（``PostStepPoint``）で構成されています。

始点と終点は[G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)クラスのオブジェクトになっており、それぞれの点での粒子の状態を取り出すことができます。
現在のステップの物理量を取得する場合は、
基本的に``PreStepPoint``のメソッドを使います。
ステップが持つ情報を積算して、イベント情報を計算できます。

```cpp
aStep->GetTotalEnergyDeposit();
```

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)

:::
