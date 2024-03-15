# クラスリファレンスの使い方

Geant4のアプリケーションを開発するときにお世話になるのが[Class Reference Guide](https://geant4.kek.jp/Reference/)です。
ここから自分が使っているバージョンを選択し、該当するクラス名やメソッドなどを探します。

Geant4公式の[コーディング・ガイドライン](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)があったので、一度読んでおくとよいと思いますが、ユーザーのアプリケーションに対してコーディング規約を強制するスタンスはとっていません。

## 基本はステップ（``G4Step``）

トラッキングの基本単位はステップ（``G4Step``）です。
[G4Step](https://geant4.kek.jp/Reference/11.2.0/classG4Step.html)や
[G4StepPoint](https://geant4.kek.jp/Reference/11.2.0/classG4StepPoint.html)に
目を通し、できること（得られる物理量など）を把握しておくと、
自分のアプリケーション作成に役立つはずです。

## クラス名

クラス名は``PascalCase``が使われています。
Geant4が提供するクラスの接頭辞は``G4*``が使われています。
さらに抽象クラスは``G4V*``、
ユーザー設定のためのフック用クラスは``G4User*``もしくは``G4VUser*``が使われています。

## 関数名

関数名は``PascalCase``が使われています。
また、セッター（``Set*``）とゲッター（``Get*``）は

## 変数名

変数名は``PascalCase``が使われています。
また、ゆるめのシステムハンガリアン記法が使われている気がします。

プライベートなメンバー変数の接頭辞には``f*``を使っていることが多く、
変数がポインターの場合は``p*``や``fp*``、
引数の場合は``aValue``や``&aValue``、``&apValue``を使っていることが多いです。

```cpp
// G4Trackのメソッドを抜粋
G4Track::SetTrackID(const G4int aValue)
G4Track::SetPosition(const G4ThreeVector &aValue)
G4Track::SetTouchableHandle(const G4TouchableHandle &apValue)
```

ただし、20年近くの開発の歴史があるためなのか、命名規則が混在している印象です。
なので、関数名／変数名でやっていることがよく分からない場合は
結局ソースコードを眺めてみるのが一番です。

:::{note}

おそらく、ごそっとリファクターするのが難しく、
新しく追加したり、書き直す必要があった部分が、
上記のような書き方になっているのかなと思います。

:::

## 定数

定数（``const``な変数）や``enum``数は``k*``を接頭辞にした``PascalCase``が使われています。



## プロジェクトの構造

```console
$ tree プロジェクト名
プロジェクト名
|--- CMakeLists.txt
|--- include/*.hh
|--- src/*.cc
|--- プロジェクト名.cc
|--- README
|--- vis.mac
|--- run1.mac
```

Geant4アプリケーションで推奨されるディレクトリ構造です。
``cmake``でビルドできるように``CMakeLists.txt``を作成します。
メインプログラム名は``CMakeLists.txt``で設定し、それに合わせて``プロジェクト名.cc``を作成します。
``include/``にヘッダファイル、``src/``には実装したコードを配置します。
``.mac``はマクロファイルです。

## ファイル名

ヘッダーファイルは``include/クラス名.hh``、
ソースファイルは``src/クラス名.cc``に作成します。

ヘッダーファイルにはクラスの定義、
ソースファイルにはそのメンバー関数の実装が書かれています。

Geant4が提供しているクラスは[オンラインのリファレンス](https://geant4.kek.jp/Reference/)で参照できます。
どんなメンバー関数を持つかはヘッダーファイル、
それぞれの引数が受け付ける値はソースファイルを確認する感じです。

## インクルードガード

```cpp
#ifndef PROJECT_PATH_FILENAME_H_
#define PROJECT_PATH_FILENAME_H_ 1

// クラスの定義

#endif // PROJECT_PATH_FILENAME_H_
```

ヘッダーファイルが2回以上読み込まれることを防ぐために、インクルードガードしてあることが多いです。
マクロ名が重複しないように、パス名を利用したものにするとよいみたいです。

## ヘッダーファイル

```cpp
#include "この自作クラスのヘッダー.hh"

#include <C関連のヘッダー.h>

#include <C++関連のヘッダー>

#include "Geant4関係のヘッッダー.hh"

#include "その他の自作クラスのヘッダー.hh"
```

ヘッダーファイルの読み込み順です。
ファイルの中で使用するヘッダーファイルはすべて書いておきます。
ヘッダー／ソース間の依存関係が隠れてしまうことを避けるためです。
インクルードガードするのもこのためです。

## クラス名

クラス名は``PascalCase``が使われています。
Geant4が提供するクラスの接頭辞は``G4*``が使われています。
さらに抽象クラスは``G4V*``、ユーザー設定のためのフック用クラスは``G4User*``もしくは``G4VUser*``が使われています。

ユーザーが作成したクラスも``G4``を、ユーザーのプロジェクトに由来した接頭辞に置き換えることが多いようです。
また、サンプルはプロジェクトごとの名前空間（``namespace``）の中に入れてあります。

```cpp
// B1DetectorConstruction.hh と
// B1DetectorConstruction.cc の両方に記載

namespace B1 {
    class DetectorConstruction: public G4VUserDetectorConstruction {
        ...
    }
}
```





## 変数の型名

変数の型宣言はGeant4が提供する``G4*``型（``G4int``、``G4double``、``G4String``）を使うことが推奨されています。

## 標準入出力

``std::cout``などの代わりに``G4cout``、``G4cerr``、``G4cin``、``G4debug``、``G4endl``を使うことが推奨されています。

