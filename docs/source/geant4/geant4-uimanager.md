# 対話モードしたい（``G4UImanager``）

```cpp
G4UImanager *ui = G4UImanager::GetUIpointer();
ui->ApplyCommand("/control/execute vis.mac");
```

``G4UImanager``は対話モードの担当者です。
``ApplyCommand``メソッドでコマンド指示ができます。
