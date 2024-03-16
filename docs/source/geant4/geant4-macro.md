# マクロしたい

```cpp
int main(int argc, char** argv)
{
  // Construct the default run manager
  auto runManager = G4RunManagerFactory::CreateRunManager();

  // Set mandatory initialization classes
  runManager->SetUserInitialization(new DetectorConstruction);
  runManager->SetUserInitialization(new FTFP_BERT);
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

実行プログラムの引数で、マクロファイルを読み込めるようにしたメイン関数です。
``G4UImanager``でマクロを読み込めるようにしています。
