# トラッキングアクションしたい（``G4UserTrackingAction``）

## 親クラス

- [G4UserTrackingAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserTrackingAction.html)

```cpp
G4UserTrackingAction();
virtual ~G4UserTrackingAction() = default;
virtual void PreUserTrackingAction(const G4Track*){};
virtual void PostUserTrackingAction(const G4Track*){};
```

親クラスのメンバー変数を確認しました。

:::{note}

このクラスを実装したサンプルを見ていないので、
どういう目的で使うのか、いまいち分かっていません。

:::

:::{seealso}

- [](./geant4-track.md)

:::
