# ユーザー設定したい

測定器シミュレーションの詳細は、基本的にユーザーが自分で実装する必要があります。
Geant4には``G4VUser*``からはじまる抽象クラス（純粋仮想関数あり）と、
``G4User*``からはじまる仮想クラス（純粋仮想関数なし）が用意されており、
これらのユーザーフック用クラスを継承して、独自クラスを作成します。

## 測定器を作りたい

```cpp
class MyDetectorConstruction : public G4VUserDetectorConstruction
{

}
```

測定器を作る場合は``G4VUserDetectorConstruction``クラスを継承します。
この親クラスは抽象クラスなので、コンストラクターを自分で作成する必要があります。

## 相互作用を作りたい

```cpp
class MyPhysicsList : public G4VUserPhysicsList
{

}
```

```cpp
class MyPhysicsList : public G4VModularPhysicsList
{

}
```

相互作用を作る場合は``G4VUserPhysicsList``クラスもしくは``G4VModularPhysicsList``を継承します。
この親クラスは抽象クラスなので、コンストラクターを自分で作成する必要があります。

## 入射粒子を作りたい

```cpp
class MyPrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction
{

}
```

入射粒子を作る場合は``G4VUserPrimaryGeneratorAction``クラスを継承します。
この親クラスは抽象クラスなので、コンストラクターを自分で作成する必要があります。
