# 一次粒子したい（``G4VUserPrimaryGeneratorAction``）

```cpp
#include "G4VUserPrimaryGeneratorAction.hh"

class PrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{
    public:
        PrimaryGeneratorAction();
        ~PrimaryGeneratorAction() override;

        void GeneratePrimaries(G4Event *aEvent) override;
}
```

```cpp
void PrimaryGeneratorAction::GeneratePrimaries(G4Event *aEvent)
{

}
```
