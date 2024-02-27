# コーディング・ガイドライン

附属のサンプルコードや過去に先輩が書いてくれたコードを再確認しながら、
Geant4の慣習的な書き方など、気づいたことを整理しておきます。

ちなみに、Geant4公式の[コーディング・ガイドライン](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)があったので、一度読んでおくとよいと思います。
Geant4のクラスの接頭辞を``G4*``にすることや、``G4*``型の使用を推奨すること、``std::cout``などの代わりに``G4cout``、``G4cerr``、``G4cin``、``G4endl``を利用することなどについても書いてありました。
こういうのを知っておくと、ソースコードを読むときの助けになります（たぶん）。

## プロジェクトの構造

```console
$ tree プロジェクト名
プロジェクト名
|--- CMakeLists.txt
|--- include/
|--- src/
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

## クラス名したい

Geant4のクラスの接頭辞は``G4*``です。
さらに、抽象クラスの接頭辞は``G4V*``です。

ユーザー定義のクラスを追加するときは、継承したGeant4クラスの接頭辞を自分のプロジェクト固有の接頭辞に置き換える場合が多いです。

```cpp
#include "G4VUserDetectorConstruction.hh"

class B1DetectorConstruction : public G4VUserDetectorConstruction
{
    public:
        DetectorConstruction() = default;
        ~DetectorConstruction() override = default;
}
```

## 変数名したい

``kVariableName``、``fVariableName``のように、
定数のような変数は``k*``、メンバー変数は``f*``という変数名にすることが多いようです。

:::{note}

ROOTもこのコーディング規約を採用していると思います。
Geant4だけでなくCERNのプロジェクトの慣習なのかもしれません。
もしかすると、もっと広く使われている規約なのかもしれません。

:::
