# ステップ点の時刻をしりたい（``GetLocalTime`` / ``GetGlobalTime`` / ``GetProperTime``）

```cpp
auto pre_step = aStep->GetPreStepPoint();
G4double local_time = pre_step->GetLocalTime();
G4double global_time = pre_step->GetGlobalTime();
G4double proper_time = pre_step->GetProperTime();
```

ステップの時刻を取得するメソッドは3種類あります。

``GetLocalTime``でトラックが生成されてからの経過時間、
``GetGlobalTime``でトラックが含まれるイベントが生成されてからの経過時間、
``GetProperTime``で固有時間（トラックが生成されてからの経過時間の静止系の時刻）を取得できます。

:::{seealso}

- [G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)

:::
