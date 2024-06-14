# クラスリファレンスの使い方

Geant4が持つクラスの使い方は[Class Reference Guide](https://geant4.kek.jp/Reference/)で確認できます。
自分が使っているバージョンを選択し、右上の検索窓やブランザの検索機能を使って、該当するクラス名やメソッドなどを検索します。

クラスの実装は[Code Cross Reference](https://geant4.kek.jp/LXR/)で確認できます。``File Name Search``のボックスにクラス名を入力して検索できます。

:::{caution}

クラスリファレンスもコードリファレンスも
検索窓があいまい検索（fuzzy match）に対応していません。

Geant4のクラス名は、``V``があったりなかったり、``User``があったりなかったりするため、前方から正しく入力しないと検索候補がヒットしないのは、ちょっと不便です。

ローカル環境にインストールした場合は、[fd](../command/command-fd.md)や[mdfind](../command/command-mdfind.md)などコマンドラインを使って、ローカルにあるGeant4のソースコードを検索できます。
この方法なら、クラス名が分からない場合でも、あいまい検索できます。

:::

## リファレンスのリファレンス

僕がよく使う参照する項目のリストにしました。
Geant4 v11.2.0 のDoxygenを参照しています。

### ユーザーフックに使うクラス

自作クラスで継承するクラスたちです。
純粋仮想関数や、ユーザーフック関数の名前を確認するために参照します。

- [G4VUserDetectorConstruction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserDetectorConstruction.html)
- [G4VUserPhysicsList](https://geant4.kek.jp/Reference/11.2.0/classG4VUserPhysicsList.html)
- [G4VUserActionInitialization](https://geant4.kek.jp/Reference/11.2.0/classG4VUserActionInitialization.html)
- [G4VUserPrimaryGeneratorAction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserPrimaryGeneratorAction.html)
- [G4UserRunAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserRunAction.html)
- [G4UserEventAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserEventAction.html)
- [G4UserSteppingAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserSteppingAction.html)
- [G4UserTrackingAction](https://geant4.kek.jp/Reference/11.2.0/classG4UserTrackingAction.html)

### 測定器の作成に必要なクラス

測定器の形状を定義したり、配置するためのクラスです。
ソリッドを作る場合は、物理物体を配置するクラスは、引数の順番を覚えることが難しいため、たびたび参照しています。

- [G4Box](https://geant4.kek.jp/Reference/11.2.0/classG4Box.html)
- [G4Tubs](https://geant4.kek.jp/Reference/11.2.0/classG4Tubs.html)
- [G4LogicalVolume](https://geant4.kek.jp/Reference/11.2.0/classG4LogicalVolume.html)
- [G4PVPlacement](https://geant4.kek.jp/Reference/11.2.0/classG4PVPlacement.html)
- [G4PVReplica](https://geant4.kek.jp/Reference/11.2.0/classG4PVReplica.html)
- [G4RunManager](https://geant4.kek.jp/Reference/11.2.0/classG4RunManager.html)
- [G4RunManagerFactory](https://geant4.kek.jp/Reference/11.2.0/classG4RunManagerFactory.html)

