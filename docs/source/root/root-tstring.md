# 文字列したい（`TString`）

```cpp
#include <TString.h>

// 文字列の初期化
TString str = "ROOT string";

// フォーマット文字列を作成
TString name;
name.Form("histogram_%d", i);

// 文字列データを取得
const char* cstr = name.Data();
```

`TString`はROOTの文字列クラスです。
`TString`を使うことで、C文字列ポインターのメモリ管理の煩雑さを排除でき、`printf`と同じようなフォーマット指定子で柔軟に文字列を生成できます。
C/C++の文字や文字列の扱いの面倒くささを解消してくれます。

さらに`TH1`や`TTree`などのROOTオブジェクトと直接連携可能なため、データ分析のワークフローで非常に便利です。

```python
from ROOT import TString

# 文字列の初期化
str_obj = TString("ROOT string")

# フォーマット文字列を作成
name = TString()
name.Form("histogram_%d", i)

# 文字列データを取得
cstr = name.Data()
```

:::{seealso}

C++標準ライブラリを使う場合

```cpp
#include <string>
#include <cstdio>

// 文字列の初期化
std::string str = "ROOT string";

// フォーマット文字列を作成（C++20以降）
std::string name = std::format("histogram_{}", i);

// または snprintf を使う場合
char buffer[256];
snprintf(buffer, sizeof(buffer), "histogram_%d", i);
std::string name(buffer);

// 文字列データを取得
const char* cstr = name.c_str();
```

C++標準ライブラリでも同様のことができますが、
`TString`の方が記述が簡潔で、ROOTオブジェクトとの連携がスムーズです。

:::

## フォーマット文字列したい（`TString::Form`）

```cpp
#include <TString.h>

TString str;
str.Form("Hist%d", 5);
// 結果: "Hist5"

TString name;
name.Form("h_%02d_%s", 3, "data");
// 結果: "h_03_data"
```

``TString::Form``メソッドで、``printf``と同じようにフォーマット指定子を使って文字列を作成できます。
ループ処理中にファイル名やオブジェクト名を自動生成する場合に便利です。

## 文字列を取得したい（`TString::Data`）

```cpp
#include <TString.h>

TString name;
name.Form("histogram_%d", 10);

// C文字列として取得
const char* cstr = name.Data();
printf("Name: %s\n", cstr);
```

``TString::Data``メソッドで、``TString``オブジェクトをC文字列（`const char*`）として取得できます。
`TH1`や`TTree`などのコンストラクターに渡す場合に使います。

## 実践例：ループ処理で複数のヒストグラムを作成したい

```cpp
#include <TString.h>
#include <TH1D.h>

const Int_t nhist = 10;
TString hname, htitle;

for (Int_t i = 0; i < nhist; i++) {
    // オブジェクト名を生成
    hname.Form("h%02d", i);

    // タイトルを生成
    htitle.Form("%s;%s;%s", hname.Data(), "x axis", "y axis");

    // ヒストグラムを作成
    h[i] = new TH1D(hname.Data(), htitle.Data(), xbin, xmin, xmax);
}
```

このサンプルでは、
``TString``を使って異なるオブジェクト名を自動生成して、複数のヒストグラムを作成しています。

- ``Form``で毎回新しい文字列を生成できるため、異なるオブジェクト名を作成可能
- 同じのオブジェクト名のヒストグラムは作成できないため、ループ番号を含ませる工夫が必要

## 関連メソッド

- [TString::Length](https://root.cern/doc/master/classTROOT_1_1Math_1_1LorentzVector.html) - 文字列の長さを取得
- [TString::Contains](https://root.cern) - 部分文字列を含むかチェック
- [TString::Index](https://root.cern) - 部分文字列の位置を検索

## 参考資料

- [ROOT Documentation - TString](https://root.cern/doc/master/classTString.html)
