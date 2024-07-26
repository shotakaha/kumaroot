# トラッキングアクションしたい（``G4UserTrackingAction``）

## 親クラス

- [G4UserTrackingAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserTrackingAction.html)

```cpp
G4UserTrackingAction();
virtual ~G4UserTrackingAction() = default;
virtual void PreUserTrackingAction(const G4Track*){};
virtual void PostUserTrackingAction(const G4Track*){};
```

:::{seealso}

- [](./geant4-track.md)

:::
