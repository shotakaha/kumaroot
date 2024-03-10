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
