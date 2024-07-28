# Geant4のコーディングガイド

Geant4には明確なコーディングガイドがありません。
Geant4は開発の歴史も長く、すでに広く利用されているツールキットであるため、
それぞれのアプリケーションのコーディングルールを尊重し、
Geant4側から強制はしないというスタンスのようです。

しかし、附属サンプルを使ってみたり、リファレンスガイドを参照したとき「慣習」のようなものを感じました
（C++の慣習なのか、Geant4の慣習なのかは区別できていません）。
以下では、Geant4を使っていて感じる「慣習のようなもの」を整理してみました。

:::{note}

20年近くの開発の歴史があるせいなのか、命名規則が混在している印象です。
内部のソースコードや附属サンプルも一貫してないと感じる箇所もありました。
これはもう、いっぱいサンプルを読んで、雰囲気に慣れるしかなさそうです。

:::

## ファイル名

ファイル名は``PascalCase``が使われています。
ヘッダーファイルは``include/クラス名.hh``、
ソースファイルは``src/クラス名.cc``にあります。

## クラス名

クラス名は``PascalCase``が使われています。
Geant4が提供するクラスの接頭辞は``G4*``が使われています。
さらに抽象クラスは``G4V*``、
ユーザー設定のためのフック用クラスは``G4User*``もしくは``G4VUser*``が使われています。

```cpp
class DetectorConstruction : public G4VUserDetectorConstruction
{
    // 自作クラスの実装
}
```

のように継承したクラス名がわかるように、主要な部分を残して使うことが多いようです。

## 関数名

関数名は``PascalCase``が使われています。
セッターは``Set*``、ゲッターは``Get*``が接頭辞に使われています。

関数の引数名は、`G4Step *aStep`、``G4Event *anEvent``のように``a``からはじまる変数名が多いです。

## 変数名

変数名は``PascalCase``が使われています。
また、ゆるめのシステムハンガリアン記法が使われている気がします。

プライベートなメンバー変数の接頭辞には``f*``が使われています。

```cpp
G4int fNumberOfChambers = 5;
G4LogicalVolume *fLogicalChamber = nullptr;
```

変数がポインターの場合は``p*``や``fp*``、
引数の場合は``aValue``や``&aValue``、``&apValue``を使っていることが多いです。

```cpp
// G4Trackのメソッドを抜粋
G4Track::SetTrackID(const G4int aValue)
G4Track::SetPosition(const G4ThreeVector &aValue)
G4Track::SetTouchableHandle(const G4TouchableHandle &apValue)
```

## 定数

定数（``const``な変数）や``enum``数は``k*``を接頭辞にした``PascalCase``が使われています。

## 型の名前

```cpp
G4String name = "Geant4";     // String型
G4int numberOfParticles = 1;  // int型
G4double energy = 1.0 * GeV;  // double型
// 他にもある
```

``G4*型``を使うことが推奨されています。
プラットフォームによる型の実装の違いを吸収してくれます（たぶん）。

## 入出力ストリーム

```cpp
G4cout << "標準出力" << G4endl;
G4err << "標準エラー出力" << G4endl;
G4debug << "デバッグ用出力" << G4endl;
```

ターミナルへの出力は、C++標準の``std::cout``や``std::cerr``の代わりに
Geant4が用意している``G4cout``、``G4cerr``、``G4debug``を使うのがよいそうです。

``G4debug``はQtで表示すると赤色でハイライトされるので、デバッグ時の確認がしやすいのでオススメです。

## シングルトン

```cpp
auto rm = G4RunManagerFactory::CreateRunManager();
auto em = G4EventManager::GetEventManager();
auto sm = G4SDManager::GetSDMpointer();
auto nm = G4NistManager::Instance();
auto am = G4AnalysisManager::Instance();
```

RunManagerをはじめとするマネージャークラスは、シングルトンで設計されています。
コードのどこからでも、同じ方法で同じオブジェクトを参照できるようになっています。

:::{note}

マネージャークラスごとにシングルトンへのアクセス方法が異なるので注意してください。
関数名がブレているのは歴史的経緯なのではと推測しています。

:::

## リファレンス

- [Geant4 Coding Guidelines](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)
- [Geant4 Coding-style Guidelines Motivations](https://geant4-internal.web.cern.ch/collaboration/coding_style_guidelines_motivations)
- [G4cout, G4cerr and G4debug](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html#g4cout-g4cerr-and-g4debug)
