# 対話モードしたい

```cpp
#include "G4RunManagerFactory.hh"
#include "G4UIExecutive.hh"
#include "G4UImanager.hh"
#include "G4VisExecutive.hh"

int main(int argc, char** argv)
{
    // 対話モードのセッションを作成
    auto ui = new G4UIExecutive(argc, argv);

    auto rm = G4RunManagerFactory::CreateRunManager();
    // ユーザー初期化クラス（ジオメトリ、物理リスト、アクション）の設定は省略

    // 可視化の設定
    auto vis = new G4VisExecutive(argc, argv);
    vis->Initialize();

    // 初期化マクロを実行してから、対話モードを開始
    auto UImanager = G4UImanager::GetUIpointer();
    UImanager->ApplyCommand("/control/execute init_vis.mac");
    ui->SessionStart();

    delete ui;
    delete vis;
    delete rm;
    return 0;
}
```

このコードは、対話モードを起動する最小限の形です。
読むときは、次のポイントを押さえてください。

- `G4UIExecutive`：対話モードで使う画面（セッション）を用意します。
- `ui->SessionStart()`：ここで対話モードが始まり、コマンドを待ちます。`exit`と入力すると終わり、次の行に進みます。
- `init_vis.mac`：対話モードに入る前に自動で読み込まれるマクロです。可視化の初期設定など、起動直後に実行したい命令を書いておきます。
- `G4VisExecutive`：`/vis/`から始まるコマンドを使うために必要です。
- ジオメトリや物理リストなどの設定は省略しています。そのため、このコードだけではランを実行できません。

`main()`関数の全体は[](./geant4-main.md)を参照してください。

対話モードでは、キーボードでコマンドを入力して、アプリケーションを操作できます。
Qtを有効にしてビルドしていれば、Qtウィンドウの中でもコマンドを操作できます。

このページでは、付属のサンプルで使いそうなコマンドを紹介します。
あわせて、対応すると思われるソースコードも載せています。

## 終了したい（`exit`）

```cfg
exit
```

`exit`で、対話モードを終了します。
コマンド先頭の`/`は不要です。

## ウィンドウ表示したい（`/vis/open`）

```cfg
/vis/open OGL

# /vis/open OGL          Qtウィンドウ（デフォルト）
# /vis/open RayTracer    静止画（高品質レンダリング）
# /vis/open VRML2FILE    ブラウザで表示するファイル
# /vis/open gMocrenFile  放射線治療などの表示
# /vis/open HepRepFile   描画要素のピッキング
# /vis/open ATree        構造の点検（テキスト表示）
```

`/vis/open`で可視化ドライバーを変更できます。
Qtを有効にしてビルドしている場合、`OGL`を指定するとQtウィンドウが使えます。

## ランを開始したい（`/run/beamOn`）

```cfg
/run/initialize

/run/beamOn イベント数
/run/beamOn 1
/run/beamOn 100
```

`/run/beamOn`でビームを照射してランを開始します。
引数にイベント数を指定します。

:::{caution}

ランを開始する前に、`/run/initialize`で初期化しておく必要があります。

:::

:::{seealso}

```cpp
auto rm = G4RunManagerFactory::CreateRunManager();
rm->Initialize();
rm->beamOn(イベント数);
```

:::

## 粒子数を変更したい（`/gun/number`）

```cfg
/gun/number 粒子数
/gun/number 1
/gun/number 100
```

`/gun/number 粒子数`で、1イベントで入射する粒子の数を変更できます。

:::{seealso}

```cpp
gun->SetNumberOfParticles(粒子数);
```

:::

## 粒子を変更したい（`/gun/particle`）

```cfg
/gun/particle 粒子名
/gun/particle mu-
/gun/particle e-
```

`/gun/particle 粒子名`で、1イベントで入射する粒子の種類を変更できます。

:::{seealso}

```cpp
G4ParticleTable *table = G4ParticleTable::GetParticleTable();
G4ParticleDefinition *particle = table->FindParticle("粒子名");
gun->SetParticleDefinition(particle);
```

:::

## 入射エネルギーを変更したい（`/gun/energy`）

```cfg
/gun/energy エネルギー 単位
/gun/energy 1. GeV
/gun/energy 500. MeV
```

入射エネルギーを変更できます。
単位を間違えるとエラーになります。

:::{seealso}

```cpp
G4double energy = 500. * MeV;
gun->SetParticleEnergy(energy);
```

:::

## 入射位置を変更したい（`/gun/position`）

```cfg
/gun/position x y z 単位
/gun/position 10. 10. 10. cm
```

入射位置を変更できます。
単位を間違えるとエラーになります。

:::{seealso}

```cpp
G4ThreeVector position = G4ThreeVector(0., 0., -10. * cm);
gun->SetParticlePosition(position);
```

:::

## 入射方向を変更したい（`/gun/direction`）

```cfg
/gun/direction ex ey ez
/gun/direction 0 0 1  # z軸方向
/gun/direction 0 1 1  # y-z平面内でz軸から45度
/gun/direction 0 1 2  # y-z平面内でz軸から約26.6度（tan = 1/2）
```

入射方向を、入射位置からのベクトルで設定できます。
単位は不要です。

:::{seealso}

```cpp
G4ThreeVector direction = G4ThreeVector(0., 0., 1.);
gun->SetParticleMomentumDirection(direction);
```

:::

## 利用できる粒子を確認したい（`/particle/list`）

```cfg
/particle/list
```

`/particle/list`で利用可能な粒子名を確認できます。
素粒子物理学、原子核物理学で主に使う粒子と反粒子が含まれています。

以下は、素粒子物理学で使いそうな粒子名を抜粋してみました。

```text
gamma,
opticalphoton
alpha, anti_alpha
neutron, anti_neutron
proton, anti_proton,
pi+, pi-, pi0,

// レプトン
e+, e-,
mu+, mu-,
tau+, tau-,

// ニュートリノ
nu_e, anti_nu_e,
nu_mu, anti_nu_mu,
nu_tau, anti_nu_tau,

// 仮想粒子（たぶん）
geantino,
```

粒子名そのものや、記号で表現します。
反粒子は`anti_*`ではじまるものがほとんどですが、
荷電レプトン（とパイ中間子）は、そのまま`*-`／`*+`と書きます。

## カット長を確認したい（`/cuts/dump`）

```cfg
/cuts/dump
```

```text
========= Table of registered couples ============================

Index : 0     used in the geometry : Yes
 Material : G4_AIR
 Range cuts        :  gamma  700 um     e-  700 um     e+  700 um  proton 700 um
 Energy thresholds :  gamma  990 eV     e-  990 eV     e+  990 eV  proton 70 keV
 Region(s) which use this couple :
    DefaultRegionForTheWorld

Index : 1     used in the geometry : Yes
 Material : G4_BGO
 Range cuts        :  gamma  700 um     e-  700 um     e+  700 um  proton 700 um
 Energy thresholds :  gamma  64.4521 keV    e-  770.195 keV    e+  731.433 keV proton 70 keV
 Region(s) which use this couple :
    DefaultRegionForTheWorld

==================================================================
```

`/cuts/dump`で二次粒子を生成するかどうかの閾値を確認できます。
閾値は **カット長（＝粒子の飛程）** で設定されていて、デフォルトだと、ガンマ線、電子、陽電子、陽子の飛程の閾値はすべて 700 um になっていました。
エネルギーの閾値は、設定した物体の材料の情報から、自動で計算されます。

:::{hint}

検出器シミュレーションでは、エネルギー損失により粒子が停止するまで計算します。

「粒子が停止したこと」を判定するために、運動エネルギーを使って閾値を設定する手法もありますが、Geant4では **運動エネルギーがゼロになるまできちんと計算** する手法をとっています。

この手法だと、停止点の位置情報や、エネルギー損失の誤差をなくすことができます。
一方で、一次粒子から生成される二次粒子や、さらにその後に生成される粒子が発生した場合に計算量が膨らみます。
そこで、二次粒子生成の閾値を設定することで、計算量の増大を回避しています。

:::
