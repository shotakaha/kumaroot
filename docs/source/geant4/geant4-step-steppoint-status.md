# ステップポイントの境界判断したい（``G4StepPoint::GetStepStatus``）

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

## ステップがジオメトリに入ったことをしりたい

```cpp
auto step_point = aStep->GetPreStepPoint();
auto status = step_point->GetStepStatus();
if (status == fGeomBoundary) {
    // ジオメトリ内にある場合の処理
}
```

ステップが新しいジオメトリに入ったことは
「始点がfGeomBoundary」かどうかで判断できます。

## ステップがジオメトリから出たことをしりたい

```cpp
auto step_point = aStep->GetPostStepPoint();
auto status = step_point->GetStepStatus();
if (status == fGeomBoundary) {
    // ジオメトリ内にある場合の処理
}
```

ステップが現在のジオメトリから出たことは
「終点がfGeomBoundary」かどうかで判断できます。
