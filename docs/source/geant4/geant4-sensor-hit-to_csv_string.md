# CSV文字列にしたい（``SensorHit::ToCsvString``）

```cpp
#include <sstream>

G4String SensorHit::ToCsvString() const
{
    std::sstream ss;
    ss << fRunID;
    ss << "," << fEventID;
    ss << "," << fTrackID;
    ss << "," << fStepID;
    ss << "," << fTrackParentID;
    // G4Step
    ss << "," << fEnergyDeposit;
    ss << "," << fTrackLength;
    ss << "," << fStepLength;
    ss << "," << fStepXYZ.getX();
    ss << "," << fStepXYZ.getY();
    ss << "," << fStepXYZ.getZ();

    G4String line{ss.str()};

    return line;
};
```
