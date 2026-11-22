# Geant4のコーディングスタイル

Geant4にはユーザー向けの公式なコーディングガイドは見当たりません。
長く開発されてきたツールキットで、利用者のコードスタイルを強制しない方針のようです。

ただし、附属サンプル（`examples/`）や本体のソースを読むと、命名や書き方に一定の傾向があります。
このページでは、初学者がGeant4のソースやサンプルを読むとき、そして自分のアプリを書くときに役立つ「大きな方向性」を整理します。
細かな例外や歴史的経緯は省いています。

:::{note}

確認したソースは Geant4 v11.4.3 です。
20年以上の開発史があるため、古いコードや一部のサンプルには、ここで述べない書き方も含まれます。
まずは附属サンプルを何本か読み、雰囲気をつかむのが近道です。

:::

## 書式（`.clang-format`）

```yaml
IndentWidth: 2
ColumnLimit: 100
PointerAlignment: Left
BreakBeforeBraces: Custom
```

本体のソース（`source/`）は`.clang-format` の設定に沿って整形されています。
主な設定は次のとおりです。

- `IndentWidth`: インデントは半角スペース2つ
- `ColumnLimit`: 1行は最大100文字
- `PointerAlignment`: ポインターの `*` は型の側に寄せる（例: `G4Step* aStep`）
- `BreakBeforeBraces`: クラス・関数・制御文の `{` は次の行に書く

自分のアプリを書くときも、`clang-format` を使って同じ書式にそろえると、サンプルとの行き来が楽になります。

## 命名の基本

```cpp
class DetectorConstruction : public G4VUserDetectorConstruction
{
  public:
    void SetNumberOfChambers(G4int aValue);
    G4int GetNumberOfChambers() const;

  private:
    G4int fNumberOfChambers = 5;
};
```

| 対象 | 書き方 | 説明 | 例 |
|---|---|---|---|
| ファイル名 | `PascalCase` | クラス名と一致させる | `DetectorConstruction.hh` / `.cc` |
| クラス名 | `PascalCase` | 接頭辞で役割がわかる（下の節を参照） | `G4Track`, `G4RunManager` |
| 関数名 | `PascalCase` | セッターは `Set*`、ゲッターは `Get*` | `SetTrackID`, `GetEventManager` |
| 変数名 | `camelCase` | 役割を示す接頭辞を付ける（下の表を参照） | `fNumberOfChambers` |

ファイル名は、ヘッダーが `include/クラス名.hh`、ソースが `src/クラス名.cc` という形で対応しています。

## クラス名の接頭辞

```cpp
#include "G4Step.hh"                       // G4*: Geant4の標準クラス
#include "G4VUserDetectorConstruction.hh"  // G4V*: 継承して実装する
#include "G4UserRunAction.hh"              // G4User*: 必要なものだけ継承
```

クラス名の接頭辞を見ると役割がわかります。

- **`G4*`**: Geant4 が提供する標準クラスです。
- **`G4V*`**: 抽象基底クラスです。ユーザーが継承して実装する前提です。
  - 例: `G4VUserDetectorConstruction`、`G4VUserPrimaryGeneratorAction`
- **`G4User*`**: 必要に応じて継承して、動作を変えるクラスです。
  - 例: `G4UserRunAction`、`G4UserEventAction`

`G4VUser*` は「必ず継承して実装するもの」、`G4User*` は「必要なものだけ継承するもの」と覚えておくと便利です。

### 自作クラスの名前

```cpp
class DetectorConstruction : public G4VUserDetectorConstruction
{
  // ...
};
```

自作クラスには、継承元の役割を表す名前を付けるのが一般的です。
サンプルでもこの形が使われています。

検出器まわりのクラスでは、対象の名前に役割の語を付けることもあります。

```cpp
class EmCalorimeterHit : public G4VHit
{
  // ...
};

class EmCalorimeterSD : public G4VSensitiveDetector
{
  // ...
};
```

- `Hit`: 検出器で記録する1回分のヒット（検出情報）を表します。
- `SD`: Sensitive Detector（有感検出器）の略です。

## 変数名の接頭辞

```cpp
class MyDetector
{
  private:
    G4int fNumberOfChambers = 5;
    G4LogicalVolume* fpChamber = nullptr;
};

void MyDetector::SetNumberOfChambers(G4int aValue)
{
  fNumberOfChambers = aValue;
}
```

Geant4の変数名では、接頭辞で役割を示す慣習が広く使われています。
最初に覚えておくと読みやすくなるものを、表にまとめます。

| 接頭辞 | 役割 | 例 |
|---|---|---|
| `f`（field） | クラスのメンバー変数 | `fVerbose`, `fParticleChange` |
| `fp`（field pointer） | メンバーのポインター | `fpCommand`, `fpWorld` |
| `a` / `an`（不定冠詞） | 関数の引数 | `aTrack`, `anEvent`, `aValue` |
| `k`（constant） | 定数・`enum` の値 | `kNumberOfChambers`, `kAlive` |

### ローカル変数

```cpp
const G4Step* aStep = ...;
const G4Track* theTrack = ...;
```

ローカル変数には、`aStep` や `theTrack` のように冠詞を付けた名前がよく見られます。
ソースを読むときは、「`a` は引数や一時的な値」「`the` は保持している値」くらいのニュアンスで読むと十分です。
ただし、この使い分けは厳密な規則ではありません。

### 古いコードの書き方

古いコードには、`m*` で始まるメンバー変数や、接頭辞のない変数も見られます。
新しく書くときは、上の表に沿うのが無難です。

## 定数

```cpp
constexpr G4int kNumberOfChambers = 5;       // 附属サンプル B5 を参考にした例
enum State { kAlive, kDead, kStopButAlive }; // 書き方の例
```

`const` な値や `enum` の値には、`k` を付けるのが基本です。

## 型

```cpp
G4String name = "Geant4";     // std::stringに相当
G4int numberOfParticles = 1;  // intに相当
G4double energy = 1.0 * GeV;  // doubleに相当
```

Geant4 では、標準の型の代わりに `G4*` の型エイリアスを使うのが基本です。
プラットフォームによる型の違いを吸収するために設けられています。

ヘッダーは `G4Types.hh` と `globals.hh` のどちらも本体内で使われています。
サンプルでは `globals.hh` を見かけることが多いので、読むときはどちらが出てきても問題ありません。

## 出力（`G4cout` / `G4cerr` / `G4endl`）

```cpp
#include "G4ios.hh"  // G4cout などの宣言

G4cout << "標準出力" << G4endl;
G4cerr << "標準エラー出力" << G4endl;
G4debug << "デバッグ用出力" << G4endl;
```

Geant4 では、`std::cout` や `std::cerr` の代わりに、専用のストリームを使います。
本体のソースでも `G4cout` を使う箇所が圧倒的に多いです。

- `G4cout` と `G4cerr` は、Geant4 の出力システムを通ります。
- `G4debug` はデバッグ用の出力先です。表示の強調は、実行環境（UI）によって異なります。
- `G4endl` は `std::endl` と同じ意味です。
- `G4cout` などは `G4ios.hh` で宣言されています。`globals.hh` を include していれば、`G4ios.hh` も読み込まれるので、追加の include は不要です。

## マネージャーのシングルトン

```cpp
auto em = G4EventManager::GetEventManager();
auto sm = G4SDManager::GetSDMpointer();
auto nm = G4NistManager::Instance();
```

RunManager などの主要なマネージャーは、シングルトンとして設計されています。
どこからでも同じ方法で同じオブジェクトを参照できます。

取得用の関数名は、クラスごとに異なります（`Instance()`、`GetXxxManager()`、`GetSDMpointer()` など）。
クラスごとに違うと覚えておき、ヘッダーを見て確認するのが確実です。

RunManager は、`main()` の中で生成します。
生成には `G4RunManagerFactory::CreateRunManager()` を使うのが、附属サンプルでの一般的な書き方です。

## リファレンス

- [Geant4 Coding Guidelines](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)（開発者向け）
- [Geant4 Coding-style Guidelines Motivations](https://geant4-internal.web.cern.ch/collaboration/coding_style_guidelines_motivations)（開発者向け）
- [G4cout, G4cerr and G4debug](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html#g4cout-g4cerr-and-g4debug)
