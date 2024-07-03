# 論理ボリュームに電磁場を追加したい（``SetFieldManager``）

```cpp
auto logical_volume = G4LogicalVolume{...};
logical_volume->SetFieldManager(field);
```
