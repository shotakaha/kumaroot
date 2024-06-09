# C++のスタイリングガイド

C/C++の書き方については[Googleが作ったC++のスタイルガイド](https://google.github.io/styleguide/cppguide.html)が参考になります。
よい書き方／よくない書き方の例に加え、メリット／デメリットなども書いてあるため、自分のアプリケーションで採用するかどうかの判断材料になります。
また、``cpplint``というリンターもあります。

:::{note}

``cpplint``はもともとGoogleが開発していたオープンソースプロジェクトでしたが、現在ではGoogleの手を離れたプロジェクトになっているようです。

:::

## Geant4のコーディングガイド

Geant4には明確なコーディングガイドがありません。
すでに広く利用されているツールキットであるため、
それぞれのアプリケーションのコーディングルールを尊重し、
Geant4側から強制はしないというスタンスのようです。

しかし、内部のソースコードや付属サンプルにも一貫性がないみたいで、
ちょっと読みづらいです。
いっぱいサンプルを読んで、慣れるしかなさそうです。

以下は、いくつかのサンプルを使ってみて感じた「慣習」のようなものをリストしました。（C++の慣習なのか、Geant4の慣習なのかは区別できていません）

:クラス名:
`class DetectorConstruction : public G4VUserDetectorConstruction`のように継承したクラス名がわかるように、主要な部分を残して使うことが多いようです。

:プライベート変数名:
`fNumberOfChambers`、`fLogicalChamber`のように`f`からはじまる変数名が多いようです。

:関数の引数名:
`aStep`、``anEvent``のように``a``からはじまる変数名が多いようです。

## リファレンス

- [Geant4 Coding Guidelines](https://geant4-internal.web.cern.ch/collaboration/coding_guidelines)
- [Geant4 Coding-style Guidelines Motivations](https://geant4-internal.web.cern.ch/collaboration/coding_style_guidelines_motivations)
