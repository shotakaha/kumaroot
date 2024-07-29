# ステップポイントの速度をしりたい（``G4StepPoint::GetVelocity``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double velocity = pre_step->GetVelocity();
```

``GetVelocity``で速度を取得できます。

## ステップ点のベータをしりたい（``G4StepPoint::GetBeta``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double beta = pre_step->GetBeta();
```

``GetBeta``でβを取得できます。

:::{math}

\beta = \frac{v}{c}

:::

## ステップ点のガンマをしりたい（``G4StepPoint::GetGamma``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double gamma = pre_step->GetGamma();
```

``GetGamma``でγファクターを取得できます。

:::{math}

\gamma = \frac{1}{\sqrt{1 - \beta^{2}}}

:::
