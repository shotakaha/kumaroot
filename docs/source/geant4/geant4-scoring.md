# スコアリングの流れ

**スコアリング**は、Geant4の世界で物理量を測定することです。

測定器（ジオメトリ）を設置しただけでは、ビームを入射しても何も測定できます。
論理ボリュームに対して、``G4ScoringManager``や``G4MultiFunctionalDetector``、``G4VSensitiveDetector``を
適切に設定して、検出器が吸収したエネルギーだったり、通過した粒子の時刻や方向だったりを
測定できるようにする必要があります。

## 対話モード（``G4ScoringManager``）

```cpp
int main()
{
    auto *rm = G4RunManagerFactory::CreateRunManager();
    auto *sm = G4ScoringManager::GetScoringManager();
}
```

対話モードやマクロを使ってスコアリングする場合は``G4ScoringManager``を使います。
RunManagerを作成したあとに、ScoringManagerを作成すると有効にできます。
**イベントごと**のスコアリング結果を収集できます。

## 多機能検出機（``G4PrimitiveScorer``）

## カスタマイズ（``G4VSensitiveDetector``）
