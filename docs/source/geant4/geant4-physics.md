# 相互作用したい

シミュレーションする粒子に働く相互作用はユーザーが指定する必要があります。
とはいえ、ユーザーが0からすべて定義するのは大変です。
Geant4の開発チームが「モジュール型物理リスト（`G4VModularPhysicsList`）」を用意しているので、その中から選択して指定するのが推奨されています。

## 物理リストしたい

```{toctree}
geant4-physics-ftfp-bert
geant4-physics-qbbc
```

## 物理モジュールしたい

```{toctree}
geant4-physics-opticalphysics
```

## 物理プロセスしたい

```{toctree}
geant4-physics-opticalphoton
geant4-physics-absorption
geant4-physics-cerenkov
geant4-physics-scintillation
```

## 自作したい

```{toctree}
geant4-physics-constructparticle
geant4-physics-constructprocess
```
