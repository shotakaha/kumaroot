# マクロしたい

```cpp
int main(int argc, char** argv)
{
  // Construct the default run manager
  auto runManager = G4RunManagerFactory::CreateRunManager();

  // Set mandatory initialization classes
  runManager->SetUserInitialization(new DetectorConstruction);
  runManager->SetUserInitialization(new QGSP_BERT);
  runManager->SetUserInitialization(new ActionInitialization);

  // Initialize G4 kernel
  runManager->Initialize();

  //read a macro file of commands
  G4UImanager* uiManager = G4UImanager::GetUIpointer();
  G4String command = "/control/execute ";
  G4String fileName = argv[1];
  uiManager->ApplyCommand(command+fileName);

  // job termination
  delete runManager;
  return 0;
}
```

マクロファイルを実行できるようにした``main()``関数です。
``G4UImanager``でマクロを読み込めるようにしています。

```batch
# verbose levelの設定
# 0: 非表示
/run/verbose 1       # RunManager
/control/verbose 1
/event/verbose 1     # EventManager
/tracking/verbose 1  # TrackingManager
/process/verbose 1
/particle/verbose 1
/cuts/verbose 1
/material/verbose 1
/vis/verbose 1

# 入射粒子の設定

/gun/particle mu-
/gun/energy 2 GeV
/run/beamOn 100
```

マクロファイルはテキストファイルで用意します。
出力内容の表示レベルや可視化ツールの選択、入射粒子の条件を設定します。

基本的に対話モードで使うコマンドを順番にならべるだけなので、
対話モードでできることはすべて設定できます。

拡張子はなんでもよいはずですが、``.mac``にするのが慣習のようです。

## 表示レベル

```console
### Run 18 starts.

========================================================================================
--> G4TaskRunManager::CreateAndStartWorkers() --> Creating 1 tasks with 1 events/task...
========================================================================================

G4WT5 > ### Run 4 starts on worker thread 5.
G4WT5 > --> Event 0 starts with initial seeds (721009,89655465).
G4WT5 > >>> Event: 0
G4WT5 >     127 trajectories stored in this event.
G4WT5 >     126 hits stored in this event
```

すべて``verbose 0``にしたときの出力です。

```console
/run/verbose 0
/run/verbose 1
/run/verbose 2
```

どのスレッドで、いくつのイベントがプロセスされたかを表示してくれます。
とくに有効にする必要はないと思います。

```console
/event/verbose 0
/event/verbose 1
/event/verbose 2
```

イベントに含まれる（トラックID、親トラックID）と``G4TrackingManager``、``G4StackingManager``とのやりとりの一覧を表示してくれます。
とくに有効にする必要はないと思います。

```macro
/tracking/verbose 1

*********************************************************************************************************
G4WT1 > * G4Track Information:   Particle = e-,   Track ID = 5,   Parent ID = 1
G4WT1 > *********************************************************************************************************
G4WT1 >
G4WT1 > Step#       X          Y          Z         KineE         dEStep    StepLeng   TrakLeng    Volume     Process
G4WT1 >     0   28.21 um  -2.324 um  -2.441 m    7.017 MeV          0 eV       0 fm       0 fm     Target   initStep
G4WT1 >     1  -148.1 um   40.48 um   -2.44 m    5.336 MeV      1.167 MeV  922.8 um   922.8 um     Target       eBrem
G4WT1 >     2  -144.8 um   429.6 um   -2.44 m    4.719 MeV      486.3 keV  527.5 um    1.45 mm     Target       eBrem
G4WT1 >     3     227 um   595.3 um  -2.441 m    2.172 MeV      2.402 MeV  1.947 mm   3.397 mm     Target       eBrem
G4WT1 >     4   102.6 um   614.5 um  -2.441 m      617 keV      997.5 keV  907.5 um   4.304 mm     Target       eBrem
G4WT1 >     5   106.7 um   597.4 um  -2.441 m        0 eV         617 keV  401.8 um   4.706 mm     Target       eIoni
```

トラック（``G4Track``）の情報と、そのトラックに含まれるステップの情報を表示してくれます。
``/tracking/verbose 2``にすると、二次粒子のトラック情報も表示してくれます。
デバッグしているときは表示を有効にするとよいと思います。
トラック数が多くなるときは非表示にしたほうがいいかもしれません。

```
/hits/verbose 2

### Run 8 starts.

========================================================================================
--> G4TaskRunManager::CreateAndStartWorkers() --> Creating 1 tasks with 1 events/task...
========================================================================================

G4WT3 > ### Run 1 starts on worker thread 3.
G4WT3 > --> Event 0 starts with initial seeds (74052786,96299938).
G4WT3 >
G4WT3 > -------->Hits Collection: in this event they are 62 hits in the tracker chambers:
G4WT3 >   trackID: 1 chamberNb: 0Edep: 26.5511 keV Position: 0.0129978 0.0132076 -1.6189 m
G4WT3 >   trackID: 1 chamberNb: 0Edep: 6.67485 keV Position: 0.0133023 0.0135155 -1.60077 m
G4WT3 >   trackID: 1 chamberNb: 1Edep:  7.5801 keV Position: 2.76542 2.8269 -73.6655 cm
G4WT3 >   trackID: 1 chamberNb: 1Edep: 8.52071 keV Position: 2.80304 2.86481 -71.465 cm
G4WT3 >   trackID: 1 chamberNb: 1Edep: 6.03534 keV Position: 2.82801 2.88993 -70 cm
G4WT3 >   trackID: 1 chamberNb: 2Edep: 2.32864 keV Position: 3.84702 3.93215 -9.4504 cm
G4WT3 >   trackID: 1 chamberNb: 3Edep: 4.85005 keV Position: 5.18896 5.28624 71.7211 cm
G4WT3 >   trackID: 1 chamberNb: 4Edep:  12.901 keV Position: 0.0651043 0.0666541 1.53151 m
G4WT3 >   trackID: 1 chamberNb: 4Edep: 57.2757 keV Position: 0.0677765 0.0694952 1.7 m
G4WT3 >   trackID: 48 chamberNb: 2Edep: 1.37334 keV Position:  4.1489 4.24615 8.72265 cm
G4WT3 >   trackID: 47 chamberNb: 2Edep: 6.24286 keV Position: 4.04783 4.1603 2.87766 cm
G4WT3 >   trackID: 46 chamberNb: 2Edep: 5.83071 keV Position: 4.04159 4.13947 2.50117 cm
G4WT3 >   trackID: 44 chamberNb: 2Edep: 2.45685 keV Position: 3.87492 3.98083 -6.67294 cm
G4WT3 >   trackID: 44 chamberNb: 2Edep:  6.0642 keV Position: 3.87319 3.98335 -6.66787 cm
G4WT3 > >>> Event: 0
G4WT3 >     93 trajectories stored in this event.
G4WT3 >     62 hits stored in this event
```

``/hits/verbose 2``にするとヒット情報を表示してくれます。
トラックIDと、どのボリュームの、どの場所で、どれくらいエネルギーを落としたかがわかります。
