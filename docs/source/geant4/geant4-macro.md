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

``/tracking/verbose 1``にすると、トラック情報を出力してくれます。
``/tracking/verbose 2``にすると、二次粒子のトラック情報も出力してくれます。

