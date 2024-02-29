# 対話モードしたい（``G4UImanager``）

```cpp
G4UImanager *ui = G4UImanager::GetUIpointer();
ui->ApplyCommand("/control/execute vis.mac");
```

``G4UImanager``は対話モードの管理者です。
コマンド指示ができます。
