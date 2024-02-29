# 相互作用したい（``G4VModularPhysicsList``）

``PhysicsList``で粒子と物質の相互作用のモデルを設定できます。
まずは``G4VModularPhysicsList``を継承された、あらかじめ定義されたモデルから選択するのがよいそうです。
定義済みのモデルの内容は[Gude for Physics Lists](https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/index.html)で確認できます。

リストにない相互作用が必要な場合は``G4VUserPhysicsList``を継承してカスタマイズした相互作用を設定できるようになっています。
