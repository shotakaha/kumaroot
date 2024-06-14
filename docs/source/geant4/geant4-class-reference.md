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

## ステップ（``G4Step``）が基本

```cpp
// G4Step *aStep は事前に定義済み
G4double energy_deposit = aStep->GetTotalEnergyDeposit();
```

トラッキングの基本単位はステップ（``G4Step``）です。
[G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)や
[G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)に
目を通し、できること（得られる物理量など）を把握しておくと、
自分のアプリケーション作成に役立つはずです。

## ファイル名

ファイル名は``PascalCase``が使われています。
ヘッダーファイルは``include/クラス名.hh``、
ソースファイルは``src/クラス名.cc``にあります。

## クラス名

クラス名は``PascalCase``が使われています。
Geant4が提供するクラスの接頭辞は``G4*``が使われています。
さらに抽象クラスは``G4V*``、
ユーザー設定のためのフック用クラスは``G4User*``もしくは``G4VUser*``が使われています。

## 関数名

関数名は``PascalCase``が使われています。
セッターは``Set*``、ゲッターは``Get*``が接頭辞に使われています。

## 変数名

変数名は``PascalCase``が使われています。
また、ゆるめのシステムハンガリアン記法が使われている気がします。

プライベートなメンバー変数の接頭辞には``f*``を使っていることが多く、
変数がポインターの場合は``p*``や``fp*``、
引数の場合は``aValue``や``&aValue``、``&apValue``を使っていることが多いです。

```cpp
// G4Trackのメソッドを抜粋
G4Track::SetTrackID(const G4int aValue)
G4Track::SetPosition(const G4ThreeVector &aValue)
G4Track::SetTouchableHandle(const G4TouchableHandle &apValue)
```

ただし、20年近くの開発の歴史があるためなのか、命名規則が混在している印象です。
なので、関数名／変数名でやっていることがよく分からない場合は
結局ソースコードを眺めてみるのが一番です。

:::{note}

おそらく、ごそっとリファクターするのが難しく、
新しく追加したり、書き直す必要があった部分が、
上記のような書き方になっているのかなと思います。

:::

## 定数

定数（``const``な変数）や``enum``数は``k*``を接頭辞にした``PascalCase``が使われています。



---

