# C++/Geant4のスタイリングガイド

C/C++の書き方については[Googleが作ったC++のスタイルガイド](https://google.github.io/styleguide/cppguide.html)が参考になります。
よい書き方／よくない書き方の例に加え、メリット／デメリットなども書いてあるため、自分のアプリケーションで採用するかどうかの判断材料になります。
また、``cpplint``というリンターもあります。

Geant4には明確なコーディングガイドがありません。
Geant4は開発の歴史も長く、すでに広く利用されているツールキットであるため、
それぞれのアプリケーションのコーディングルールを尊重し、
Geant4側から強制はしないというスタンスのようです。
しかし、附属サンプルを使ってみたり、リファレンスガイドを参照したとき「慣習」のようなものを感じました
（C++の慣習なのか、Geant4の慣習なのかは区別できていません）。

:::{note}

``cpplint``はもともとGoogleが開発していたオープンソースプロジェクトでしたが、現在ではGoogleの手を離れたプロジェクトになっているようです。

:::

## C++の豆知識

ひさしぶりにC++を使ってみたら、いろいろな機能が増えていました。
Geant4のサンプルコードを読むときに知っておくとよさそうだと思ったことを整理しておきます。

### C++の変遷

| C++ | リリース年 | ISO |
|---|---|---|
| C++98 | 1998 |  ISO/IEC 14882:1998 |
| C++03 | 2003 |  ISO/IEC 14882:2003 |
| C++11 | 2011 |  ISO/IEC 14882:2011 |
| C++14 | 2014 |  ISO/IEC 14882:2014 |
| C++17 | 2017 |  ISO/IEC 14882:2017 |
| C++20 | 2020 |  ISO/IEC 14882:2020 |
| C++23（予定） | 2023 | ISO/IEC 14882:2023 |

C++11で、ラムダ式や``auto``キーワードなど、大幅に機能が追加されました。
以前使っていたのはC++98/C++03だと思うので、どうりで機能が増えているはずです。
ちなみに、C++以降を「モダンC++」と呼ぶそうです。

:::{seealso}

Geant4（v4.11.2）はC++17に対応しています。

- [](./geant4-versions.md)

:::

### STL（Standard Template Library）

```cpp
#include <vector>  // std::vector
#include <map>     // std::map
#include <tuple>   // std::tuple
// などなど
```

STLはC++98から標準ライブラリとして採用されているそうです。
大学院生のころ（2010年ころ）は、よく分からないまま使うのを避けてきた気がします。

### 一様初期化

```cpp
// 変数の初期化
int x = 100;
double y(3.14);
char z = "z";

// 変数の一様初期化
int x{100};
double y{3.14};
char z{"z"};

```

```cpp
// 配列の初期化
int array[] = {1, 2, 3, 4, 5};
// 配列の一様初期化
int array[]{1, 2, 3, 4, 5};
```

```cpp
// コンテナーの初期化
std::vector<int> vec;
vec.push_back(1);
vec.push_back(2);
vec.push_back(3);

// コンテナーの一様初期化
std::vector<int> vec{1, 2, 3};
```

C++11からインスタンスの初期化に``{}``（中括弧／波括弧）が使えるようになっていました。

・・・なんで括弧の使い方を増やしてしまったんだと思いましたが、変数、配列・コンテナー、構造体、クラスなどを同じ書式で初期化できるのがメリットのようです。
とくに``std::vector``の初期化が簡単に書けるようになっています。
また、型安全性も向上していて、モダンC++での使用が推奨されている初期化スタイルだそうです。

## Geant4のコーディングガイド

Geant4を使っていて感じる「慣習のようなもの」を整理しました。

:::{note}

20年近くの開発の歴史があるせいなのか、命名規則が混在している印象です。
内部のソースコードや附属サンプルも一貫してないと感じる箇所もありました。
これはもう、いっぱいサンプルを読んで、雰囲気に慣れるしかなさそうです。

:::

### ファイル名

ファイル名は``PascalCase``が使われています。
ヘッダーファイルは``include/クラス名.hh``、
ソースファイルは``src/クラス名.cc``にあります。

### クラス名

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

### 関数名

関数名は``PascalCase``が使われています。
セッターは``Set*``、ゲッターは``Get*``が接頭辞に使われています。

関数の引数名は、`G4Step *aStep`、``G4Event *anEvent``のように``a``からはじまる変数名が多いです。

### 変数名

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

### 定数

定数（``const``な変数）や``enum``数は``k*``を接頭辞にした``PascalCase``が使われています。

### 型の名前

```cpp
G4String name = "Geant4";     // String型
G4int numberOfParticles = 1;  // int型
G4double energy = 1.0 * GeV;  // double型
// 他にもある
```

``G4*型``を使うことが推奨されています。
プラットフォームによる型の実装の違いを吸収してくれます（たぶん）。

### 出力ストリーム

```cpp
G4cout << "標準出力" << G4endl;
G4err << "標準エラー出力" << G4endl;
G4debug << "デバッグ用出力" << G4endl;
```

ターミナルへの出力は、C++標準の``std::cout``や``std::cerr``の代わりに
Geant4が用意している``G4cout``、``G4cerr``、``G4debug``を使うのがよいそうです。

``G4debug``はQtで表示すると赤色でハイライトされるので、デバッグ時の確認がしやすいのでオススメです。

## リファレンス

- [Geant4 Coding Guidelines](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)
- [Geant4 Coding-style Guidelines Motivations](https://geant4-internal.web.cern.ch/collaboration/coding_style_guidelines_motivations)
- [G4cout, G4cerr and G4debug](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/GettingStarted/mainProgram.html#g4cout-g4cerr-and-g4debug)
