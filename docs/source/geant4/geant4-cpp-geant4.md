# Geant4のコーディングガイド

Geant4にはユーザー向けの明確なコーディングのガイドラインは存在しません。
Geant4は開発の歴史が長く、すでに広く利用されているツールキットであることから、
それぞれのアプリケーション側のコーディングスタイルを尊重し、
Geant4側から強制はしないというスタンスのようです。

とはいえ、附属サンプルコードやリファレンスガイドを読んでいると「暗黙の慣習」のようなものを感じます。
このページでは、Geant4を使っていて感じる「慣習のようなもの」を整理してみました。
（C++一般の慣習なのか、Geant4固有の慣習なのか、は区別できていません）。

:::{note}

20年以上にわたる開発の歴史のためか、命名規則にはばらつきがあり、
内部のソースコードや附属サンプルでもスタイルが一貫してないと感じる箇所もありました。
結局のところ、多くのサンプルを読みながら「雰囲気」に慣れていくのが一番の近道かもしれません。

:::

## ファイル名の命名規則

Geant4のファイル名は`PascalCase`が使われています。
また、クラス名とファイル名は一致しており、
ヘッダーファイルは`include/クラス名.hh`、
ソースファイルは`src/クラス名.cc`が使われています。

## クラス名の命名規則

Geant4のクラス名には`PascalCase`が使われています。

`G4*`からはじまるクラス名は、Geant4が提供する標準クラスです。
その中でも、`G4V*`からはじまるクラスは、純粋仮想関数をもつ抽象基底クラスであり、
ユーザーが継承して実装すること前提となっています。
とくに
`G4VUser*`および`G4User*`クラスは、ユーザーによる拡張や設定を行うためのフック用クラスです。

### G4VUserクラスとG4Userクラスの違い

`G4VUser*`クラスは、ユーザーが必ず継承して実装すべき抽象クラスで、
`G4User`クラスは、必要に応じて継承・オーバーライド可能な具象クラスです。

### ユーザー定義クラスの命名規則（の慣習）

```cpp
class DetectorConstruction : public G4VUserDetectorConstruction
{
    // 自作クラスの実装
}
```

ユーザー定義クラスについては、
上記ように継承元のクラス名を明示的にクラス名に残すことで、
クラスの役割を明確にする命名が一般的です。

## 関数名の命名規則

関数名は`PascalCase`が使われています。
セッターには``Set*``、
ゲッターには``Get*``という接頭辞に使われています。

## 変数名の命名規則

Geant4の変数名には、基本的に`camelCase`が基本的に使われています。
また、ゆるめのシステム・ハンガリアン記法が一部で採用されており、
変数の種類や役割が名前からわかるようになっています。

### ローカル変数

ローカル変数には、`aStep`や`theTrack`のように、
接頭辞として不定冠詞や定冠詞が使われることがあります。
`a`（`an`）（不定冠詞）は任意のインスタンス、
`the`（定冠詞）は特定のインスタンスを指します。

```cpp
const G4Step* aStep = ...;
const G4Track* theTrack = ...;
```

### メンバー変数

クラスのメンバー変数には、接頭辞として`f*`（fieldの略）が使われます。

```cpp
G4int fNumberOfChambers = 5;
G4LogicalVolume *fLogicalChamber = nullptr;
```

### ポインター変数

ポインター型の変数には、接頭辞として
`p*`（pointerの略）や
`fp*`（field pointerの略）が使われることがあります。

```cpp
G4Material *pMaterial;
G4VPhysicalVolume *fpWorld;
```

### 引数

関数の引数には、`aValue`や`anEvent`のように、接頭辞として不定冠詞の`a`や`an`が使われる傾向があります
参照型では`&aValue`、
ポインター型では`&apValue`のように使われます。

```cpp
// G4Trackのメソッドを抜粋
G4Track::SetTrackID(const G4int aValue)
G4Track::SetPosition(const G4ThreeVector &aValue)
G4Track::SetTouchableHandle(const G4TouchableHandle &apValue)
```

### 定数

定数（`const`な変数）や`enum`定数には、接頭辞として`k*`（constantの意味）使われます。

```cpp
const G4double kMaxStepLength = 10.0 * mm;
enum State { kAlive, kDead, kStopButAlive };
```

:::{note}

定数の接頭辞を`k*`とする由来は諸説あるようです。
数学分野で$k$を定数として扱う習慣に由来するという説、
constantの頭文字を音的にもじったという説、
などがありますが、いずれも決定的な根拠があるわけではなく、
慣習的に広まったと考えられています。

:::

## 型エイリアス

Geant4では`G4*型`の型エイリアスを使うことが推奨されています。
これらのエイリアスは、
プラットフォームごとの型実装の違いを吸収するために設けられています。

```cpp
// #include "globals.hh" // 非推奨（古い一括ヘッダー）
#include "G4Types.hh"    // v10.6以降の推奨ヘッダー

G4String name = "Geant4";     // std::stringに相当
G4int numberOfParticles = 1;  // int に相当
G4double energy = 1.0 * GeV;  // double に相当
// 他にもある
```

## 入出力ストリーム（`G4cout` / `G4cerr` / `G4debug` / `G4endl`）

Geant4では、C++標準の`std:cout`や`std:cerr`の代わりに、
専用の出力ストリームを使うことが推奨されています。

```cpp
G4cout << "標準出力" << G4endl;
G4err << "標準エラー出力" << G4endl;
G4debug << "デバッグ用出力" << G4endl;
```

これらはGeant4の出力システムと統合されており、
UIやログのふるまいと一貫性を保つことができます。
とくに、`G4debug`はQt上で赤色でハイライト表示されるため、デバッグ時の視認性が高く、オススメです。

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
