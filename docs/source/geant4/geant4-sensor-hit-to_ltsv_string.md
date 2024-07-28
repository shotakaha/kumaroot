# LTSV文字列にしたい（``SensorHit::ToLtsvString``）

```cpp
#include <sstream>

G4String SensorHit::ToLtsvString() const
{
    std::sstream ss;
    ss << "run_id:" << fRunID;
    ss << "," << "event_id:" << fEventID;
    ss << "," << "track_id:" << fTrackID;
    ss << "," << "step_id:" << fStepID;
    ss << "," << "parent_id:" << fTrackParentID;
    // G4Step
    ss << "," << "energy_deposit:" << fEnergyDeposit;
    ss << "," << "track_length:" << fTrackLength;
    ss << "," << "step_length:" << fStepLength;
    ss << "," << "step_x:" << fStepXYZ.getX();
    ss << "," << "step_y:" <<fStepXYZ.getY();
    ss << "," << "step_z:" <<fStepXYZ.getZ();

    G4String line{ss.str()};

    return line;
}
```
