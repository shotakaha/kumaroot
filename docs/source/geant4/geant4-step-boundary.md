# ステップ点の境界判断したい（``IsFirstStepInVolume`` / ``IsLastStepInVolume``）

```cpp
G4StepPoint pre_step = aStep->GetPreStepPoint();

// ボリュームで最初のステップかどうか
if (pre_step->IsFirstStepInVolume()) {...}

// ボリュームで最後のステップかどうか
if (pre_step->IsLastStepInVolume()) {...}
```

ジオメトリの境界に到達するとステップ（の終点）が作成されます。
`G4StepPoint`クラスには、
``IsFirstStepInVolume()``と
``IsLastStepInVolume()``のメソッドが用意されており、
簡単に境界判断できるようになっています。

:::{seealso}

- [](./geant4-step-status.md)

:::

