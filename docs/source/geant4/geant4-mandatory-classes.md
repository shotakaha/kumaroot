# 必須クラス

```cpp
// RunManagerを作成
G4RunManager *runManager = new G4RunManager;

// 必須ユーザークラスを設定
runManager->SetUserInitialization(new MYDetectorConstruction);
runManager->SetUserInitialization(new MYPhysicsList);
runManager->SetUserInitialization(new MYActionInitialization);

// Geant4のカーネルを初期化
runManager->Initialize()
```

``MYDetectorConstruction``、
``MYPhysicsList``、
``MYActionInitialization``は
ユーザーが必ず作成しないといけない必須クラスです。

ソースコードを読むときにこのことを知っていると、
内容を読み解くときの助けになるはずです。

アプリケーションを作成したい場合、
これらを順番に実装していけばOKです。

## ``DetectorConstruction``クラス

測定器を定義するためのクラスです。
``G4VUserDetectorConstruction``クラスを継承して作成します。

このクラスの中で実験室（worldと呼びます）を作成し、
その中にその中に測定器を配置します。
使っている物質の組成や性質、検出器の要素などもこのクラスで定義します。

## ``PhysicsList``クラス

粒子と物質の相互作用を定義するためのクラスです。
``G4VUserPhsyicsList``クラスもしくは
``G4ModularPhysicsList``クラスを継承して作成します。

Geant4にいくつかの定義済みの相互作用モデルがあるので、
まずはそれを使ってみるとよいと思います。

## ``ActionInitialization``クラス

一次粒子の条件を定義するクラスです。
