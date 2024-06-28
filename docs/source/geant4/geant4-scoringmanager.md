# スコアリングしたい（``G4ScoringManager``）

```cpp
int main(int argc, char** argv)
{
    auto *rm = new G4RunManagerFactory::CreateRunManager();
    auto *sm = G4ScoringManager::GetScoringManager();
    // sm->SetVerboseLevel(1);
}
```

``main()``関数で``G4ScoringManager``を有効にし、
マクロを使ってスコアリング方法を設定します。

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

``G4ScoringManager``は、スコアリングするときに、
メッシュ付きのボリュームを**パラレルワールド**に作成します。
マクロの中で``DetectorConstruction``した測定器の配置に合うように、位置／サイズを指定する必要があります。

:::{caution}

メッシュボリュームと、測定器のボリュームの境界面がずれていると、標準出力に警告が表示されます。

:::

## メッシュしたい（``/score/create/``）

```cfg
# 直方体メッシュ
/score/create/boxMesh meshName
/score/mesh/boxSize dX dY dZ unit
/score/mesh/nBin dX dY dZ

# 円柱メッシュ
/score/create/cylinderMesh meshName
/score/mesh/cylinderSize dR dZ unit
/score/mesh/nBin dR dZ dPhi
```

``/score/create/メッシュ形状``でメッシュを作成できます。
メッシュ形状は直方体（``boxMesh``）と円柱（``cylinderMesh``）があります。

``/score/mesh/形状``でメッシュ全体の大きさを設定、
``/score/mesh/nBin``でメッシュの分割数を設定できます。

## 物理量したい（``/score/quantity/``）

```cfg
/score/quantity/touch quantityName

# エネルギー損失
/score/quantity/energyDeposit quantityName unit

# 電荷量
/score/quantity/cellCharge quantityName unit
/score/quantity/cellFlux quantityName unit #
/score/quantity/passageCellFlux

# Number of step scorer
/score/quantity/nOfStep quantityName bFlag

# Number of secondary scorer
/score/quantity/nOfSecondary quantityName

# トラックの長さ
/score/quantity/trackLength quantityName bWeight bKineticEnergy bVelocity unit

# Number of collision scorer
/score/quantity/nOfCollision  quantityName bWeight

# Number of track scorer
/score/quantity/nOfTrack quantityName dDirection bWeight

# Number of terminated track scorer
/score/quantity/nOfTerminatedTrack quantityName bWeight
# Number of particles getting into the volume without normalized by the surface area
/score/quantity/volumeFlux quantityName bCosTheta dDirection
/score/quantity/population quantityName bWeight
```

## フィルターしたい（``/score/filter/``）

```cfg
# 荷電粒子のフィルター
/score/filter/charged filterName

# 中性粒子のフィルター
/score/filter/neutral filterName

# 運動エネルギーのフィルター
/score/filter/kineticEnergy filterName Elow Ehigh unit

# 粒子名のフィルター
/score/filter/particle filterName particleNames

# 粒子名と運動エネルギーのフィルター
/score/filter/particleWithKineticEnergy filterName Elow Ehigh unit particleNames
```

``/score/filter/フィルター``で、測定する対象をフィルタリングできます。

:::{note}

```cfg
/score/filter/charged chargedParticleFilter
```

たとえば、荷電粒子フィルターは、以下の条件分岐に相当します。

```cpp
// G4Step *aStepとする
if( aStep->GetTrack()->GetParticleDefinition()->GetPDGCharge() != 0 )
{
    // 荷電粒子に対する処理
}
```


:::
