# 測定器したい（``G4VUserDetectorConstruction``）

測定器の構造を定義するクラスは、必須クラスのひとつで、
``G4VUserDetectorConstruction``クラスを継承して作成します。

## 親クラス

- [G4VUserDetectorConstruction](https://geant4.kek.jp/Reference/11.2.0/classG4VUserDetectorConstruction.html)

```cpp
G4VUserDetectorConstruction() = default;
virtual ~G4UserDetectorConstruction() = default;
virtual G4VPhysicalVolume* Construct() = 0;
virtual void ConstructSDandField();
```

親クラスのメンバー関数を抜粋しました。
コンストラクターとデストラクターは、この設定を引き継げばよさそうです。
``Construct()``は、Geant4で使う測定器を作るための関数です。
純粋仮想関数になっているため、自作クラスでoverrideが必要です。
``ConstructSDandField()``は、論理ボリュームに対して
有感検出器（SensitiveDetector）を設定するための関数です。
マルチスレッド環境で実行する場合は、自作クラスでoverrideが必要です。

:::{note}

シングルスレッドで実行する場合は、
``ConstructSDandField``ではなく、
``Construct``の中で設定すればよいはずです。

``ConstructSDandField``はGeant4.10で追加されたようなので、
それ以前はそうしてたはず。

:::

## Geometryクラス

```cpp
// //////////////////////////////////////////////////
// include/Geometry.hh
// //////////////////////////////////////////////////

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
    // コンストラクタとデストラクタは
    // 親クラスを引き継ぐことにする
    Geometry() = default;
    ~Geometry() = default;

  public:
    // これらの関数は override する
    G4PhysicalVolume* Construct() override;
    void ConstructSDandField() override;

  // __________________________________________________
  // これ以降は僕のベストプラクティス
  private:
    // ワールドを設定するための関数とパラメーター
    G4LogicalVolume* SetupWorldVolume();
    G4String fWorldLVName = "World";
    G4String fWorldMaterial = "G4_AIR";
    G4double fWorldX = 15. * cm;
    G4double fWorldY = 15. * cm;
    G4double fWorldZ = 15. * cm;

  private:
    // 測定器を設定するための関数とパラメーター
    // 測定器ごとに用意する
    G4LogicalVolume* SetupDetectorVolume();
    G4String fDetectorLVName = "Detector";
    G4String fDetectorMaterial = "G4_WATER";
    G4double fDetectorX = 5. * cm;
    G4double fDetectorY = 5. * cm;
    G4double fDetectorZ = 5. * cm;

  public:
    // main()関数から測定器のパラメーターを確認・変更するメソッド
    G4String GetDetectorLVName() const { return fDetectorLVName; };
    void SetDetectorLVName(const G4String &name) { fDetectorLVName = name};

    G4String GetDetectorMaterial() const { return fDetectorMaterial; };
    void SetDetectorMaterial(const G4String &name) { fDetectorMaterial = name};

    G4double GetDetectorX() const { return fDetectorX; };
    void SetDetectorX(const G4double length) { fDetectorX = length; };

    G4double GetDetectorY() const { return fDetectorY; };
    void SetDetectorY(const G4double length) { fDetectorY = length; };

    G4double GetDetectorZ() const { return fDetectorZ; };
    void SetDetectorZ(const G4double length) { fDetectorZ = length; };

};

}; // namespace ToyMC

#endif
```

自作クラス名を``Geometry``として作成しています。
``namespace``は``ToyMC``（お遊びのモンテカルロの意味）としました。

また、必要な論理物体（G4LogicalVolume）を作成する関数も用意しました。

```cpp
public:
    Geometry() = default;
    ~Geometry() = default;
```

コンストラクターとデストラクターは親クラスを引き継ぐことにしました。

## Geometry::Construct

```cpp
public:
    G4PhysicalVolume* Construct() override;
    void ConstructSDandField() override;
```

``override``キーワードを設定し、親クラスが持っている（純粋）仮想関数を上書きすることを明示しました。
また、overrideをつけておくと、関数名をタイポしていた場合にコンパイルエラーで指摘してくれます。

- [](./geant4-geometry-construct.md)
- [](./geant4-geometry-constructSDandField.md)

## メンバー変数

```cpp
private:
    // ワールドを設定するための関数とパラメーター
    G4LogicalVolume* SetupWorldVolume();
    G4String fWorldLVName = "World";
    G4String fWorldMaterial = "G4_AIR";
    G4double fWorldX = 15. * cm;
    G4double fWorldY = 15. * cm;
    G4double fWorldZ = 15. * cm;
```

これ以降は、僕がカスタマイズするときのベストプラクティス（と思っている）な書き方です。参考までにどうぞ。
ここでは、ワールドの大きさのパラメーターと、それをセットアップする関数を宣言しています。
具体的な中身は[](./geant4-geometry-world.md)を参照してください。

```cpp
private:
    // 測定器を設定するための関数とパラメーター
    // 測定器ごとに用意する
    G4LogicalVolume* SetupDetectorVolume();
    G4String fDetectorLVName = "Detector";
    G4String fDetectorMaterial = "G4_WATER";
    G4double fDetectorX = 5. * cm;
    G4double fDetectorY = 5. * cm;
    G4double fDetectorZ = 5. * cm;

public:
    // main()関数から測定器のパラメーターを確認・変更するメソッド
    G4String GetDetectorLVName() const { return fDetectorLVName; };
    void SetDetectorLVName(const G4String &name) { fDetectorLVName = name};

    G4String GetDetectorMaterial() const { return fDetectorMaterial; };
    void SetDetectorMaterial(const G4String &name) { fDetectorMaterial = name};

    G4double GetDetectorX() const { return fDetectorX; };
    void SetDetectorX(const G4double length) { fDetectorX = length; };

    G4double GetDetectorY() const { return fDetectorY; };
    void SetDetectorY(const G4double length) { fDetectorY = length; };

    G4double GetDetectorZ() const { return fDetectorZ; };
    void SetDetectorZ(const G4double length) { fDetectorZ = length; };
```

実験室の中に配置する物体を作成する部分です。
配置する測定器の種類の数だけ、コピペが必要です。

ここでは大きさをprivateで定義し、それにアクセスするためのセッター／ゲッターをpublicで定義しました。
これにより``main()``関数から測定器のパラメーターを変更できます。

## メイン関数

```cpp
#include "Geometry.hh"

int main(int argc, char** argv)
{
    auto rm = G4RunManagerFactory::CreateRunManager();

    auto geometry = new Geometry{};
    geometry->SetDetectorMaterial("G4_Pb");  // 測定器の素材を"G4_Pb"に変更
    rm->SetUserInitialization(geometry);

}
```

``main()``関数の中で、
``Geometry``クラスのインスタンスを作成し、
``SetUserInitialization``でRunManagerに追加します。

publicなセッターを作成しておいたため、``geometry->SetDetectorMaterial``のように変更できます。

:::{hint}

実験の最適なセットアップを検討している段階では、検出器や標的の素材を変えたり、厚みを変えたりしたいはずです。
``main()``関数から変更できるようにしておくと、そのようなスタディがはかどります。

:::

:::{seealso}

- [](./geant4-physicalvolume-pvplacement.md)
- [](./geant4-physicalvolume-pvreplica.md)
- [](./geant4-geometry-world.md)

:::

