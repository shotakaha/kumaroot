# 入射粒子を分布したい（``G4GeneralParticleSource``）

```cpp
auto particleGPS = G4GeneralParticleSource();
```

``G4GeneralParticleSource``はGeant4標準のPrimaryGeneratorのひとです。
``G4ParticleGun``と異なり、平面上に入射粒子を生成できます。
また、マクロのみで操作できます。

## GPSを設定したい

```cpp
// PrimaryGenerator.hhで
// メンバー変数として定義する
class PrimaryGenerator::G4VUserPrimaryGeneratorAction{
  private:
    G4GeneralParticleSource *fParticleGPS;
}

// __________________________________________________
PrimaryGenerator::PrimaryGenerator()
{
    // コンストラクターでGPS初期化
    fParticleGPS = G4GeneralParticleSource{};
}

// __________________________________________________
PrimaryGenerator::~PrimaryGenerator()
{
    // デストラクターでGPSを解放
    delete fParticleGPS
}

// __________________________________________________
void PrimaryGenerator::GeneratePrimaries(G4Event *aEvent)
{
    // G4EventにGPSを追加する
    fParticleGPS->GeneratePrimaryVertex(aEvent);
};
```

ヘッダーファイルで``G4GeneralParticleSource``のポインターをメンバー変数として定義します。
コンストラクターでGPSを初期化し、
``GeneratePrimaries``の中でイベントに追加します。

## 入射粒子のマクロしたい

| コマンド名 | 引数 | デフォルト値 | 内容 |
|---|---|---|---|
| ``/gps/list`` | | | 利用可能な粒子名のリストを表示する |
| ``/gps/particle`` | 粒子名 | geantino | 入射粒子名を設定 |
| ``/gps/direction`` | Px Py Pz | 1 0 0 | 入射方向を設定 |
| ``/gps/energy`` | E 単位 | 1 MeV | 入射エネルギーを設定 |
| ``/gps/position`` | X Y Z 単位 | 0 0 0 cm | 入射位置を設定 |
| ``/gps/time`` | t0 単位 | 0 ns | 入射時刻を設定 |
| ``/gps/number`` | N | 1 | 入射粒子数を設定 |
| ``/gps/source/multiplevertex`` | flag | false | trueにすると複数のvertexを生成できる |
| ``/gps/source/flatsampling`` | flag | false | trueにするとソースの強度が無視される |

## 入射位置のマクロしたい

| コマンド名 | 引数 | デフォルト値 | 内容 |
|---|---|---|---|
| ``/gps/pos/type`` | 分布の種類 | Point | 分布の種類を設定（Point / Beam / Surface / Volume） |
| ``/gps/pos/shape`` | 分布の形 | | Planeの場合: Circle / Annulus / Ellipse / Square / Rectangle |
| ``/gps/pos/centre`` | X Y Z 単位 | 0 0 0 cm | 中心座標を設定 |
| ``/gps/pos/halfx`` | X 単位 | 0 cm | X方向の幅 |
| ``/gps/pos/halfy`` | Y 単位 | 0 cm | X方向の幅 |
| ``/gps/pos/halfz`` | Z 単位 | 0 cm | X方向の幅 |

## 入射角度のマクロしたい

| コマンド名 | 引数 | デフォルト値 | 内容 |
|---|---|---|---|
| ``/gps/ang/type`` | 分布の種類 | iso | 分布の種類を設定（iso / cos / planar / beam1d / beam2d / focused / user） |
| ``/gps/ang/mintheta`` | $\theta$ 単位 | 0 rad | 最小値を設定 |
| ``/gps/ang/maxtheta`` | $\theta$ 単位 | $\pi$ rad | 最小値を設定 |

## リファレンス

- [G4GeneralParticleSource](https://geant4.kek.jp/Reference/11.2.0/classG4GeneralParticleSource.html)
- [Geant4 General Particle Source - Book For Application Developers](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/generalParticleSource.html)
