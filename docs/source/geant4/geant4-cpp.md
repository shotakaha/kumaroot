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

### 定数

定数（``const``な変数）や``enum``数は``k*``を接頭辞にした``PascalCase``が使われています。

## リファレンス

- [Geant4 Coding Guidelines](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)
- [Geant4 Coding-style Guidelines Motivations](https://geant4-internal.web.cern.ch/collaboration/coding_style_guidelines_motivations)
