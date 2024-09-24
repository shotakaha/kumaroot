# C++の豆知識

ひさしぶりにC++を使ってみたら、いろいろな機能が増えていました。
Geant4のサンプルコードを読むときに知っておくとよさそうだと思ったことを整理しておきます。

## スタイリングガイド

```{toctree}
---
maxdepth: 1
---
geant4-cpp-google
geant4-cpp-geant4
```

## C++の変遷

| C++ | リリース年 | ISO |
|---|---|---|
| C++98 | 1998 |  ISO/IEC 14882:1998 |
| C++03 | 2003 |  ISO/IEC 14882:2003 |
| C++11 | 2011 |  ISO/IEC 14882:2011 |
| C++14 | 2014 |  ISO/IEC 14882:2014 |
| C++17 | 2017 |  ISO/IEC 14882:2017 |
| C++20 | 2020 |  ISO/IEC 14882:2020 |
| C++23（予定） | 2023 | ISO/IEC 14882:2023 |

C++11以降を「モダンC++」と呼ぶそうです。
C++11で、ラムダ式や``auto``キーワードなど、大幅に機能が追加されました。
以前使っていたのはC++98/C++03だと思うので、どうりで機能が増えているはずです。

Geant4（v4.11.2）はC++17に対応しています。
Geant4のバージョンが対応しているC++などの情報は
[](./geant4-versions.md)に整理しました。

## STL（Standard Template Library）

```cpp
#include <vector>  // std::vector
#include <map>     // std::map
#include <tuple>   // std::tuple
// などなど
```

STLはC++98から標準ライブラリとして採用されているそうです。
大学院生のころ（2010年ころ）は、使い方がよく分からず避けてきましたが、いまなら使えそうな気がします。

## 一様初期化

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

C++11からインスタンスの初期化に``{}``（中括弧／波括弧）が使えるようになっていました。

```cpp
// 配列の初期化
int array[] = {1, 2, 3, 4, 5};

// 配列の一様初期化
int array[]{1, 2, 3, 4, 5};
```

・・・なんで括弧の使い方を増やしてしまったんだと思いましたが、変数、配列・コンテナー、構造体、クラスなどを同じ書式で初期化できるのがメリットのようです。

```cpp
// コンテナーの初期化
std::vector<int> vec;
vec.push_back(1);
vec.push_back(2);
vec.push_back(3);

// コンテナーの一様初期化
std::vector<int> vec{1, 2, 3};
```

とくに``std::vector``の初期化が簡単に書けるようになっています。
また、型安全性も向上していて、モダンC++での使用が推奨されている初期化スタイルだそうです。

:::{seealso}

- [一様初期化 - C++日本語リファレンス](https://cpprefjp.github.io/lang/cpp11/uniform_initialization.html)

:::

## autoキーワード

```cpp
// 型を指定
G4NistManager *nm = new G4NistManager::Instance();

// 型を推論
auto nm = G4NistManager::Instance();
```

``auto``は型推論で変数の型を指定するためのキーワードです。
使いたい型が分かりきっている場合や、返り値の型名が長い場合に使うと可読性が向上します。
Geant4はクラス名が長いものが多いため、どんどん使ってよいと思います。

ただし、すべて``auto``になってしまうと、逆に読みづらくなることもあるため、自分（やチーム）の中でルールを決めて使うのがよさそうです。

:::{seealso}

- [変数の型推論のためのauto - C++日本語リファレンス](https://cpprefjp.github.io/lang/cpp11/auto.html)

:::

## C++の参考サイト

- [ISO C++](https://isocpp.org/): C++の公式サイト
- [C++ Reference](https://en.cppreference.com/w/): C++標準ライブラリのリファレンス
- [Learn C++](https://www.learncpp.com/): C++学習サイト。ハンズオンではなく読みもの
- [Modern C++ Features](https://github.com/AnthonyCalandra/modern-cpp-features): モダンC++の各機能の簡易まとめ
- [C++ Support in Clang](https://clang.llvm.org/cxx_status.html)
- [C++ Standards Support in GCC](https://gcc.gnu.org/projects/cxx-status.html)
