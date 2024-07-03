# ステップ情報したい（``G4Step``）

```cpp
// 始点
auto pre_step = aStep->GetPreStepPoint()

// 終点
auto post_step = aStep->GetPostStepPoint()
```

[G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)はステップ情報を管理するクラスです。
ステップはGeant4シミュレーションの基本単位で、
**始点**（``PreStepPoint``）と
**終点**（``PostStepPoint``）で構成されています。

このステップを進める処理を**ステッピング**と呼びます。
前のステップの終点が、次のステップの始点になります。
ステップ情報は、ユーザーアクション設定の[SteppingAction](./geant4-steppingaction.md)で設定して取得します。
このユーザーアクションの中で、必要なステップ情報の取得＆集計して、イベント情報を計算します。

始点と終点は[G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)クラスのオブジェクトになっています。
ステップの終点は、そのステップの粒子輸送が終わるときと、
ジオメトリの境界に到達したときに作成されます。
同じ名前のメソッドが使えますが、それぞれの始点／終点によって取得できる情報が異なることがあります。

現在のステップの物理量を取得したい場合は、
基本的に``PreStepPoint``のメソッドを使えばよいさそうです。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)
- [G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)

:::
