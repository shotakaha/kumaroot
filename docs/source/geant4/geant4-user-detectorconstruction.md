# 測定器したい（`G4VUserDetectorConstruction`）

```cpp
// 疑似コード
class Geometry : public G4VUserDetectorConstruction {
  public:
    G4VPhysicalVolume* Construct() override;  // 必須
    void ConstructSDandField() override;      // 任意
};

G4VPhysicalVolume* Geometry::Construct() {
    // ソリッド、論理ボリューム、物理ボリュームを作成して配置する
    return physWorld;  // ワールドの物理ボリュームを返す
}

void Geometry::ConstructSDandField() {
    // 有感検出器（SensitiveDetector）や場（Field）を設定する
}
```

`G4VUserDetectorConstruction`は、ユーザーが測定器の構造を定義するための抽象クラスです。
Geant4アプリの測定器は、このクラスを継承した自作クラスで定義します。

## 測定器のクラスを作りたい（`G4VUserDetectorConstruction`）

自作クラスは、`G4VUserDetectorConstruction`を`public`に継承します。

```cpp
class Geometry : public G4VUserDetectorConstruction {
  // ...
};
```

`G4VUserDetectorConstruction`の、コンストラクタとデストラクタは、デフォルトのままで構いません。

## 測定器を組み立てたい（`Construct`）

```cpp
G4VPhysicalVolume* Construct() override;
```

`Construct()`は、測定器の構造を作成して配置する関数です。
`G4VUserDetectorConstruction`では純粋仮想関数なので、自作クラスで必ず実装します。

`Construct()`の中では、次の3つを作成します。

- ソリッド（形状）：`G4Box`、`G4Tubs`など
- 論理ボリューム（`G4LogicalVolume`）：ソリッドと材質を組み合わせる
- 物理ボリューム（`G4VPhysicalVolume`）：論理ボリュームを、親のボリュームの中に配置する

最後に、ワールドの物理ボリュームを返します。
具体的な書き方は、[](./geant4-geometry-construct.md)と[](./geant4-geometry-world.md)を参照してください。

## 有感検出器や場を設定したい（`ConstructSDandField`）

```cpp
void ConstructSDandField() override;
```

`ConstructSDandField()`は、`Construct()`で作成した論理ボリュームに、有感検出器や場を設定する関数です。
有感検出器や場を使わないなら、実装しなくても構いません。

マルチスレッドで実行する場合、この関数はワーカースレッドからも呼ばれます。
そのため、有感検出器や場は、この関数の中で作成します。
Geant4 4.10で、ワーカースレッドからも呼ばれるようになりました。

具体的な書き方は、[](./geant4-geometry-constructSDandField.md)を参照してください。

## 親クラスのメソッドを確認したい

親クラス（`G4VUserDetectorConstruction`）の主なメンバー関数は、次のとおりです。

```cpp
G4VUserDetectorConstruction() = default;
virtual ~G4VUserDetectorConstruction() = default;
virtual G4VPhysicalVolume* Construct() = 0;
virtual void ConstructSDandField();
```

- `Construct()`は純粋仮想関数です。自作クラスで必ず`override`します。
- `ConstructSDandField()`は仮想関数で、既定では何もしません。必要なときだけ`override`します。
- `override`を付けると、関数名を間違えたときにコンパイラーが指摘します。

親クラスの詳しい説明は、[G4VUserDetectorConstruction](https://geant4.kek.jp/Reference/11.4.0/classG4VUserDetectorConstruction.html)を参照してください。

## 自作クラスの例を見たい（`Geometry`）

```cpp
// include/Geometry.hh

#ifndef Geometry_h
#define Geometry_h 1

#include "G4VUserDetectorConstruction.hh"
#include "G4LogicalVolume.hh"
#include "G4SystemOfUnits.hh"

namespace ToyMC
{

class Geometry : public G4VUserDetectorConstruction
{
  public:
    G4VPhysicalVolume* Construct() override;
    void ConstructSDandField() override;

  private:
    G4LogicalVolume* SetupWorldVolume();
    G4String fWorldLVName = "World";
    G4String fWorldMaterial = "G4_AIR";
    G4double fWorldX = 15. * cm;
    G4double fWorldY = 15. * cm;
    G4double fWorldZ = 15. * cm;

    G4LogicalVolume* SetupDetectorVolume();
    G4String fDetectorLVName = "Detector";
    G4String fDetectorMaterial = "G4_WATER";
    G4double fDetectorX = 5. * cm;
    G4double fDetectorY = 5. * cm;
    G4double fDetectorZ = 5. * cm;

  public:
    G4String GetDetectorMaterial() const { return fDetectorMaterial; }
    void SetDetectorMaterial(const G4String& name) { fDetectorMaterial = name; }

    G4double GetDetectorX() const { return fDetectorX; }
    void SetDetectorX(G4double length) { fDetectorX = length; }
};

}  // namespace ToyMC

#endif
```

この例では、ワールドと検出器の大きさや材質を、メンバー変数として持っています。
メンバー変数は`private`にして、外から変えるときは`Set...()`を使います。
`Set...()`を使えば、`main()`関数からパラメーターを変えられます。

ワールドと検出器は、それぞれ`SetupWorldVolume()`と`SetupDetectorVolume()`で作成します。
`Construct()`は、この2つを呼んで、ワールドの物理ボリュームを返します。
検出器の種類が増えたら、`SetupXXXVolume()`を追加します。

## main()関数から変更したい

```cpp
#include "Geometry.hh"

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    auto geometry = new ToyMC::Geometry{};
    geometry->SetDetectorMaterial("G4_Pb");  // 検出器の材質を変更する
    rm->SetUserInitialization(geometry);

    // ...

    return 0;
}
```

`main()`関数で、`Geometry`のインスタンスを作成し、`SetUserInitialization()`で`RunManager`に登録します。
作成した後で`Set...()`を呼べば、検出器の材質や大きさを変えられます。

:::{hint}

検出器の材質や厚みを変えて比べたいときは、`main()`関数からパラメーターを変えられると便利です。
マクロや引数で値を受け取るようにすると、再ビルドせずに条件を変えられます。

:::

:::{seealso}

- [](./geant4-user-actioninitialization.md)
- [](./geant4-physicalvolume-pvplacement.md)
- [](./geant4-physicalvolume-pvreplica.md)
- [](./geant4-geometry-world.md)

:::
