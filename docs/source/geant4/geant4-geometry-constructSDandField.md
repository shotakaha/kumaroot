# Geometry::ConstructSDandField

```cpp
void Geometry::ConstructSDandField()
{
    auto sensor = new Sensor("SensorName");
    SetSensitiveDetector("名前", sensor);

    auto sm = G4SDManager::GetSDMpointer();
    sm->AddNewDetector(sensor);

}
```

- [](./geant4-sensor-sensitivedetector.md)
- [](./geant4-sensor-sdmanager.md)
