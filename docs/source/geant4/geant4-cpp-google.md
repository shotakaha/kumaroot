# C++のコーディングガイドライン

C/C++の書き方については[Googleが作ったC++のスタイルガイド](https://google.github.io/styleguide/cppguide.html)が参考になります。
よい書き方／よくない書き方の例に加え、メリット／デメリットなども書いてあるため、自分のアプリケーションで採用するかどうかの判断材料になります。
また、``cpplint``というリンターもあります。

:::{note}

``cpplint``はもともとGoogleが開発していたオープンソースプロジェクトでしたが、現在ではGoogleの手を離れたプロジェクトになっているようです。

:::

## インクルードガード

```cpp
#ifndef Geometry_h
#define Geometry_h 1

// ヘッダーファイルの内容

#endif
```

インクルードガード（もしくは ``#define`` ガード）は、
同じヘッダーファイルが複数回インクルードされるのを防ぐために
ファイルの先頭に``#ifndef``を使ってチェックする書き方です。

Geant4のヘッダーファイルはすべてガードが定義されています。
自分が作るコードも同じようにガードするとよいです。

## 前方宣言

```cpp
// #include "G4Event.hh"
// インクルードする代わりに前方宣言する
class G4Event;

class EventAction : public G4UserEventAction
{
  public:
    void BeginOfEventAction(G4Event* aEvent);
    void EndOfEventAction(G4Event* aEvent);
    // 引数はG4Eventへのポインタ型なので
    // クラスの完全な定義がなくても
    // 前方宣言だけでコンパイルできる。
};
```

ヘッダーファイルをインクルードする代わりに``class クラス名;``と書くことを前方宣言と呼びます。
「こういう名前のクラスがあるよ」ということをあらかじめお知らせすることで、コンパイルエラーを避けることができます。

Geant4では多用されていますが、Googleスタイリングガイドでは、できるかぎり使わないことが推奨されています。
なので、僕はあまり使わないようにしています。
