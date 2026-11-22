# C++のコーディングガイドライン

Geant4固有の慣習は[Geant4のコーディングスタイル](geant4-cpp-geant4)を参照してください。
このページでは、一般的なC++の書き方（Googleのスタイルガイド）を扱います。

C/C++の書き方については[Googleが作ったC++のスタイルガイド](https://google.github.io/styleguide/cppguide.html)が参考になります。
よい書き方／よくない書き方の例に加え、メリット／デメリットなども書いてあるため、自分のアプリケーションで採用するかどうかの判断材料になります。
また、`cpplint`というリンターもあります。

:::{note}

`cpplint`はもともとGoogleが開発したオープンソースのリンターです。
現在は GitHub の [cpplint/cpplint](https://github.com/cpplint/cpplint) で開発が続いています。

:::

## インクルードガード（`#ifndef` / `#endif`）

```cpp
#ifndef Geometry_h
#define Geometry_h 1

// ヘッダーファイルの内容

#endif
```

インクルードガード（もしくは `#define` ガード）は、
同じヘッダーファイルが複数回インクルードされるのを防ぐために
ファイルの先頭に`#ifndef`を使ってチェックする書き方です。

ガード名の付け方はプロジェクトによって異なります。

| 種類 | ガード名の例 | 付け方 |
|---|---|---|
| Googleスタイル | `FOO_BAR_BAZ_H_` | `<PROJECT>_<PATH>_<FILE>_H_` |
| Geant4本体 | `G4Event_hh` | `<クラス名>_hh`（`_h`、`_HH`も混在） |
| 附属サンプル（B1） | `B1EventAction_h` | サンプル名＋クラス名＋`_h` |

Geant4のヘッダーファイルはほとんどがガードを定義しています。
自分が作るアプリでも、自作ヘッダーにガードを付けるとよいです。
ガード名はアプリ内で1つの形式にそろえます。

:::{note}

`#ifndef`を使う伝統的な書き方の代わりに、`#pragma once`という書き方も広く使われています。
1行で書けて分かりやすい反面、C++の標準規格には含まれていない拡張機能です。
Googleスタイルガイドでは伝統的な書き方が推奨されています。
Geant4本体のヘッダーにも、`#pragma once`を使っているものがあります。

:::

## インクルードの順番

```cpp
#include "DetectorConstruction.hh"  // 1. 自分に対応するヘッダー

#include <vector>                   // 2. C++標準ライブラリ

#include "G4LogicalVolume.hh"       // 3. 他のライブラリ（Geant4）

#include "MaterialUtils.hh"         // 4. プロジェクト内のヘッダー（例）
```

Googleスタイルガイドでは、次の順番でインクルードを並べることを勧めています。
各グループの中はアルファベット順にし、グループの間には空行を入れます。

1. 自分に対応するヘッダー（`foo.cc`なら`foo.hh`）
2. C言語の標準ライブラリ
3. C++の標準ライブラリ
4. 他のライブラリ（Geant4など）
5. プロジェクト内のヘッダー

`clang-format`のGoogleプリセット（`BasedOnStyle: Google`）を使うと、この順番に自動で整えられます。
`cpplint`の`build/include_order`で、順番を検査することもできます。

Geant4本体では、Geant4標準クラスのヘッダーが最初にくるように`IncludeCategories`が設定されています。
自作アプリの場合、Googleの順番か、Geant4の順番か、ユーザーが好みのスタイルを選んで構いません。
Geant4の順番にしたい場合は、自分で`IncludeCategories`を設定する必要があります。
Googleの順番にしたい場合は、`BasedOnStyle: Google`の1行で十分です。
おすすめはGoogleスタイルです。

## 前方宣言

```cpp
#include "G4UserEventAction.hh"  // 基底クラスは完全な定義が必要なのでinclude

class G4Event;  // 引数はポインタなので前方宣言で足りる

class EventAction : public G4UserEventAction
{
  public:
    void BeginOfEventAction(const G4Event* event) override;
    void EndOfEventAction(const G4Event* event) override;
};
```

ヘッダーファイルをインクルードする代わりに`class クラス名;`と書くことを前方宣言と呼びます。
「こういう名前のクラスがあるよ」ということをあらかじめお知らせすることで、コンパイルエラーを避けることができます。

前方宣言だけでコンパイルできるのは、
そのクラスをポインタ（`G4Event*`）や参照（`G4Event&`）として使う場合に限られます。
値そのものをメンバー変数として持ったり、
そのクラスのメソッドを呼び出したりする場合は、
クラスの完全な定義（＝`#include`）が必要です。

Googleスタイルガイドでは、前方宣言はできるかぎり避けることが推奨されています。
一方で、Geant4本体のヘッダーでは、前方宣言が多く使われています。
迷ったら`#include`を選び、理由があるときだけ前方宣言を使う、と考えるとよさそうです。

:::{note}

前方宣言を避けたほうがよいとされる理由は、
依存関係が見えにくくなったり（`#include`ならヘッダーを見ただけで依存先が分かる）、
値渡しやメンバー変数に変更したときにコンパイルエラーの原因が分かりにくくなったりするためです。

一方で、循環参照を避けたい場合や、
Geant4本体のような大規模フレームワークでコンパイル時間を短縮したい場合には、
前方宣言が積極的に使われています。

:::

## 名前空間（`namespace`）

```cpp
// EventAction.hh
namespace B1
{

class EventAction : public G4UserEventAction
{
  public:
    void BeginOfEventAction(const G4Event* event) override;
    void EndOfEventAction(const G4Event* event) override;
};

}  // namespace B1
```

名前空間は、同じ名前のクラスや関数が衝突するのを防ぐための仕組みです。
ユーザーアプリでは、名前空間で囲んでおくのが一般的です。
附属サンプルも、サンプルごとに`B1`、`B5`などの名前空間を使っています。

Googleスタイルガイドでは、次のルールが推奨されています。

- ヘッダーファイルで`using namespace`を書かないようにします。そのヘッダーを読んだすべての人に、名前空間が持ち込まれてしまうためです。
- `.cc`ファイルでは、名前のない名前空間（`namespace { ... }`）で、そのファイルだけの補助関数やクラスを隠すとよいです。
- 名前空間を閉じる`}`の後ろには、`// namespace B1`のようなコメントを付けます。

Geant4の附属サンプルでは、サンプルごとに名前空間を分けています。
自作アプリも、アプリ全体を1つの名前空間（`MyApp`）にまとめるとGeant4の標準クラス（`G4*`）と名前が衝突しません。
また、読むときにも自分で実装した部分であることが区別しやすくなります。

## 所有権とスマートポインタ

```cpp
#include <memory>

// 所有者が1つだけなら std::unique_ptr
auto detector = std::make_unique<DetectorConstruction>();

// 所有しない参照は、生のポインタで表す
G4LogicalVolume* logicalVolume = detector->GetScoringVolume();
```

Googleスタイルガイドでは、所有者が1つなら`std::unique_ptr`を使い、複数で共有するときだけ`std::shared_ptr`を使うよう勧めています。
生のポインタ（`T*`）は、所有しないことを表すのに使います。

:::{note}

Geant4には、生のポインタを受け取って後始末を任せる形が多くあります。
附属サンプルでも、`new`で作ったオブジェクトを渡しています（例: `SetUserAction(new PrimaryGeneratorAction)`）。
この場合、所有権は Geant4 側に移るので、自分で`delete`しないでください。

:::

自作アプリでは、自分だけが持つオブジェクトは、`std::unique_ptr`で管理します。
Geant4 に渡すオブジェクト（例: `SetUserAction`に渡すもの）は、Geant4 側の後始末に任せ、自分では`delete`しません。
渡す前にその処理が所有権を引き受けるかどうかを、ヘッダーのコメントで確認します。

## 出力引数

```cpp
// 入力は値か const 参照で受け取る
G4double ComputeEnergy(const G4ThreeVector& position);

// 出力（書き戻す）引数はポインタで受け取る
void GetPosition(const G4Track* track, G4ThreeVector* position);

// 呼び出し側では & を付けて、値が変わることを示す
G4ThreeVector position;
GetPosition(track, &position);
```

Googleスタイルガイドでは、関数の中で値を書き換える引数は、参照ではなくポインタにするよう勧めています。
呼び出し側に`&`が付くので、値が変わることが読み手にも分かります。

ソースを読むときは、引数が`const`参照なら入力、`const`でない参照やポインタなら出力の可能性がある、と見分けられます。

自作アプリの場合、値を書き換える関数は、まず戻り値で返せないかを考えます。
戻り値で返せない場合だけ、ポインタの引数を使います。
