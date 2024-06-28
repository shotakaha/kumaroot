# スコアリングの流れ

**スコアリング**は、Geant4の世界で物理量を測定することです。

Geant4では、測定器（ジオメトリ）を設置して、ビームを入射しただけでは、何も測定できません。
論理ボリュームに対して、``G4ScoringManager``や``G4MultiFunctionalDetector``、``G4VSensitiveDetector``を適切に設定して、
自分が測定したい物理量を実装する必要があります。

## 対話モード（``G4ScoringManager``）

```cpp
int main()
{
    auto *rm = G4RunManagerFactory::CreateRunManager();
    auto *sm = G4ScoringManager::GetScoringManager();
}
```

対話モードやマクロを使ってスコアリングする場合は``G4ScoringManager``を使います。
RunManagerを作成したあとに、ScoringManagerを作成して有効にします。
このマネージャーを使うと**イベントごと**のスコアリング結果を収集できるようになります。
