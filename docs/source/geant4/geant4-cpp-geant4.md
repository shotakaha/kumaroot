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

## 命名の基本

| 対象 | 書き方 | 例 |
|---|---|---|
| ファイル名 | `PascalCase`。クラス名と一致させる | `DetectorConstruction.hh` / `.cc` |
| クラス名 | `PascalCase` | `G4Track`, `G4RunManager` |
| 関数名 | `PascalCase`。セッターは `Set*`、ゲッターは `Get*` | `SetTrackID`, `GetEventManager` |
| 変数名 | `camelCase`に、役割を示す接頭辞を付ける | `fNumberOfChambers` |

ファイル名は、ヘッダーが `include/クラス名.hh`、ソースが `src/クラス名.cc` という形で対応しています。

## クラス名の接頭辞

クラス名の接頭辞を見ると役割がわかります。

- **`G4*`**: Geant4 が提供する標準クラスです。
- **`G4V*`**: 抽象基底クラスです。ユーザーが継承して実装する前提です。
  - 例: `G4VUserDetectorConstruction`、`G4VUserPrimaryGeneratorAction`
- **`G4User*`**: 必要に応じて継承して、動作を変えるクラスです。
  - 例: `G4UserRunAction`、`G4UserEventAction`

`G4VUser*` は「必ず継承して実装するもの」、`G4User*` は「必要なものだけ継承するもの」と覚えておくと便利です。

### 自作クラスの名前

自作クラスには、継承元の役割を表す名前を付けるのが一般的です。
サンプルでもこの形が使われています。

```cpp
class DetectorConstruction : public G4VUserDetectorConstruction
{
  // ...
};
```

## 変数名の接頭辞

Geant4の変数名では、接頭辞で役割を示す慣習が広く使われています。
最初に覚えておくと読みやすくなるものを、表にまとめます。

| 役割 | 接頭辞 | 例 |
|---|---|---|
| クラスのメンバー変数 | `f`（field） | `fVerbose`, `fParticleChange` |
| メンバーのポインター | `fp`（field pointer） | `fpCommand`, `fpWorld` |
| 関数の引数 | `a` / `an`（不定冠詞） | `aTrack`, `anEvent`, `aValue` |
| 定数・`enum` の値 | `k`（constant） | `kInfinity`, `kMinimumStep` |

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

### ローカル変数

ローカル変数には、`aStep` や `theTrack` のように冠詞を付けた名前がよく見られます。
ソースを読むときは、「`a` は引数や一時的な値」「`the` は保持している値」くらいのニュアンスで読むと十分です。
ただし、この使い分けは厳密な規則ではありません。

```cpp
const G4Step* aStep = ...;
const G4Track* theTrack = ...;
```

### 古いコードの書き方

古いコードには、`m*` で始まるメンバー変数や、接頭辞のない変数も見られます。
新しく書くときは、上の表に沿うのが無難です。

## 定数

`const` な値や `enum` の値には、`k` を付けるのが基本です。

```cpp
constexpr G4double kMinimumStep = 0.01 * CLHEP::mm;  // 本体ソースでの例
enum State { kAlive, kDead, kStopButAlive };         // 書き方の例
```

:::{note}

`k` の由来は諸説あるようですが、確かな根拠は見つかっていません。
慣習として広まったと考えられています。

:::

## 型

Geant4 では、標準の型の代わりに `G4*` の型エイリアスを使うのが基本です。
プラットフォームによる型の違いを吸収するために設けられています。

```cpp
G4String name = "Geant4";     // std::stringに相当
G4int numberOfParticles = 1;  // intに相当
G4double energy = 1.0 * GeV;  // doubleに相当
```

ヘッダーは `G4Types.hh` と `globals.hh` のどちらも本体内で使われています。
サンプルでは `globals.hh` を見かけることが多いので、読むときはどちらが出てきても問題ありません。

## 出力（`G4cout` / `G4cerr` / `G4endl`）

Geant4 では、`std::cout` や `std::cerr` の代わりに、専用のストリームを使います。
本体のソースでも `G4cout` を使う箇所が圧倒的に多いです。

```cpp
G4cout << "標準出力" << G4endl;
G4cerr << "標準エラー出力" << G4endl;
G4debug << "デバッグ用出力" << G4endl;
```

- `G4cout` と `G4cerr` は、Geant4 の出力システムを通ります。
- `G4debug` はデバッグ用の出力先です。表示の強調は、実行環境（UI）によって異なります。
- `G4endl` は `std::endl` と同じ意味です。

## マネージャーのシングルトン

RunManager などの主要なマネージャーは、シングルトンとして設計されています。
どこからでも同じ方法で同じオブジェクトを参照できます。

```cpp
auto em = G4EventManager::GetEventManager();
auto sm = G4SDManager::GetSDMpointer();
auto nm = G4NistManager::Instance();
```

取得用の関数名は、クラスごとに異なります（`Instance()`、`GetXxxManager()`、`GetSDMpointer()` など）。
クラスごとに違うと覚えておき、ヘッダーを見て確認するのが確実です。

RunManager は、`main()` の中で生成します。
生成には `G4RunManagerFactory::CreateRunManager()` を使うのが、附属サンプルでの一般的な書き方です。

## 書式

附属サンプルと本体は、リポジトリ直下の `.clang-format` に沿って整形されています。
主な設定は次のとおりです。

- インデントは半角スペース2つ
- 1行は最大100文字
- ポインターの `*` は型の側に寄せる（例: `G4Step* aStep`）
- クラス・関数・制御文の `{` は次の行に書く

自分のアプリを書くときも、`clang-format` を使って同じ書式にそろえると、サンプルとの行き来が楽になります。

## リファレンス

- [Geant4 Coding Guidelines](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)（開発者向け）
- [Geant4 Coding-style Guidelines Motivations](https://geant4-internal.web.cern.ch/collaboration/coding_style_guidelines_motivations)（開発者向け）
- [G4cout, G4cerr and G4debug](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html#g4cout-g4cerr-and-g4debug)
