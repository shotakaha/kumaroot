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

Geant4には``G4*``もしくは``G4V*``からはじまる抽象クラスがたくさん定義されています。
基本的に、これらの抽象クラスを継承して、プロジェクト独自のクラスを作成します。
独自クラスはプロジェクト固有の接頭辞をつけるようにします。

```cpp
#include "G4VUserDetectorConstruction.hh"

class B1DetectorConstruction : public G4VUserDetectorConstruction
{
    public:
        DetectorConstruction() = default;
        ~DetectorConstruction() override = default;
}
```
