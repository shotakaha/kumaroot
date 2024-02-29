# 対話モードしたい（``G4UImanager``）

```cpp
G4UIExecutive *ui = new G4UIExecutive;
auto UImanager = G4UImanager::GetUIpointer();
UImanager->ApplyCommand("/control/execute vis.mac");
ui->SessionStart();
delete ui;
```
