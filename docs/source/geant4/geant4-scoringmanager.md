# スコアリングしたい（``G4ScoringManager``）

```cpp
G4ScoringManager *scoringManager = G4ScoringManager::GetScoringManager();
scoringManager->SetVerboseLevel(1);
```

```cfg
# メッシュを設定
/score/create/boxMesh メッシュ名
/score/mesh/boxSize Di Dj Dk 単位
/score/mesh/nBin Ni Nj Nk

# 測定量を設定
/score/quantity/物理量 スコアラー名 単位
/score/quantity/nOfStep
/score/filter/

# メッシュを閉じる
/score/close/

# ランを開始する
/run/beamOn 1

# 測定結果をファイルに書き出す
/score/dumpQuantityToFile メッシュ名 測定値名 ファイル名
/score/dumpAllQuantityToFile メッシュ名 ファイル名
```

``G4ScoringManager``を使って、物理量を測定できます。
マクロで測定したい物理量を変更できます。

## メッシュしたい（``/score/create/``）

```cfg
// 直方体メッシュ
/score/create/boxMesh meshName
/score/mesh/boxSize dX dY dZ unit
/score/mesh/nBin dX dY dZ

// 円柱メッシュ
/score/create/cylinderMesh meshName
/score/mesh/cylinderSize dR dZ unit
/score/mesh/nBin dR dZ dPhi
```

``/score/create/メッシュ形状``でメッシュを作成できます。
メッシュ形状は直方体と円柱があります。

``/score/mesh/形状``でメッシュ全体の大きさを設定、
``/score/mesh/nBin``でメッシュの分割数を設定できます。

## 物理量したい（``/score/quantity/``）

```cfg
/score/quantity/touch quantityName
/score/quantity/energyDeposit quantityName unit  # エネルギー損失
/score/quantity/cellCharge quantityName unit # 電荷の合計
/score/quantity/cellFlux quantityName unit #
/score/quantity/passageCellFlux
/score/quantity/nOfStep quantityName bFlag       # Number of step scorer
/score/quantity/nOfSecondary quantityName  # Number of secondary scorer
/score/quantity/trackLength quantityName bWeight bKineticEnergy bVelocity unit   # トラックの長さ
/score/quantity/nOfCollision  quantityName bWeight # Number of collision scorer
/score/quantity/nOfTrack quantityName dDirection bWeight # Number of track scorer
/score/quantity/nOfTerminatedTrack quantityName bWeight      # Number of terminated track scorer
/score/quantity/volumeFlux quantityName bCosTheta dDirection    # Number of particles getting into the volume without normalized by the surface area
/score/quantity/population quantityName bWeight
```

## フィルターしたい（``/score/filter/``）

```cfg
/score/filter/charged filterName # Charged particle filter
/score/filter/neutral filterName # Neutral particle filter
/score/filter/kineticEnergy filterName Elow Ehigh unit # Kinetic energy filter
/score/filter/particle filterName particleNames  # Particle filter
/score/filter/particleWithKineticEnergy filterName Elow Ehigh unit particleNames
```

``/score/filter/フィルター``で、測定する対象をフィルターできます。
