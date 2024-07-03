# ステップの境界状態をしりたい（``GetStepStatus``）

```cpp
// 始点の状態
auto pre_step = aStep->GetPreStepPoint();
G4StepStatus status = pre_step->GetStepStatus();

// 終点の状態
auto post_step = aStep->GetPostStepPoint();
G4StepStatus status = post_step->GetStepStatus();
```

``GetStepStatus``で、ステップ点の境界の状態を取得できます。
``fWorldBoundary``はステップ点がワールド境界に到達した状態、
``fGeomBoundary``はステップ点が物質の境界に到達した状態です。
他の状態は[enum G4StepStatus](https://geant4.kek.jp/lxr/source//track/include/G4StepStatus.hh)で確認できます。

:::{hint}

シミュレーションの結果を保存する際、測定器の中で起きたステップかどうかを毎回確認する必要があります。
そのあたりを適切に処理してくれるのが``G4VSensitiveDetector``クラスです。

:::

## ステップがジオメトリの中にあるかしりたい

```cpp
auto pre_step = aStep->GetPreStepPoint();
auto status = pre_step->GetStepStatus();
if (status == fGeomBoundary) {
    // ジオメトリ内にある場合の処理
}
```

## ステップがワールドの外にあるかしりたい

```cpp
auto post_step = aStep->GetPostStepPoint();
auto status = post_step->GetStepStatus();
if (status != fWorldBoundary) {
    // ワールドの中にある場合の処理
}
```
