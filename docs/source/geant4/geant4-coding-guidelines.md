# コーディング規約

Geant4公式の[コーディング・ガイドライン](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)があったので、一度読んでおくとよいと思います。
ユーザーのアプリケーションに対してコーディング規約を強制するスタンスはとっていませんが、慣習的なものを知っておくと、サンプルコードをはじめとしたソースコードが理解しやすくなると思います。



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

## 関数名

関数名は``PascalCase``が使われています。

## 変数名

Geant4の変数名は``PascalCase``が使われています。
また、クラスのメンバー変数は接頭辞に``f*``を使うことが多いみたいです。
（Google Style Guideによると変数名は``snake_case``を使うようです）

## 定数

定数（``const``な変数）や``enum``数は``kConstantName``のように``k*``を接頭辞にした``PascalCase``が使われています。

## 変数の型名

変数の型宣言はGeant4が提供する``G4*``型（``G4int``、``G4double``、``G4String``）を使うことが推奨されています。

## 標準入出力

``std::cout``などの代わりに``G4cout``、``G4cerr``、``G4cin``、``G4debug``、``G4endl``を使うことが推奨されています。

