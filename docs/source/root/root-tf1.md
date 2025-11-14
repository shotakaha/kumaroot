# フィット関数を定義したい（`TF1`）

```cpp
#include <TF1.h>
#include <cmath>

TF1 *f = new TF1("f", "sin(x)*cos(x)", 0, 2*M_PI);

// 関数を描画
f->Draw();
```

`TF1`クラスで数学関数を定義し、描画やフィットに使用できます。
関数は数式文字列、C++関数、またはラムダ式で指定できます。

```python
import ROOT
import math

f = ROOT.TF1("f", "sin(x)*cos(x)", 0, 2*math.pi)

# 関数を描画
f.Draw()
```

## メソッドのシグネチャ

```cpp
TF1(const char* name,
    const char* formula,
    Double_t xmin,
    Double_t xmax)

TF1(const char* name,
    Double_t (*fcn)(Double_t*),
    Double_t xmin,
    Double_t xmax)
```

### 引数と戻り値

**引数**:

- **name** - 関数の名前
- **formula** - 数式文字列（`sin(x)`、`x*x+2*x+1`など）または関数ポインター
- **xmin** - 関数の定義域下限
- **xmax** - 関数の定義域上限

**戻り値**:

- TF1オブジェクト

## 数式からフィット関数を定義したい（`TF1`）

```cpp
#include <TF1.h>
#include <TCanvas.h>
#include <cmath>

TF1 *f1 = new TF1("f1", "sin(x)", 0, 2*M_PI);
TF1 *f2 = new TF1("f2", "x*x", -5, 5);
TF1 *f3 = new TF1("f3", "exp(-x*x/2)", -3, 3);

TCanvas *c = new TCanvas("c", "Functions", 900, 300);
c->Divide(3, 1);

c->cd(1);
f1->Draw();

c->cd(2);
f2->Draw();

c->cd(3);
f3->Draw();
```

数式の文字列でフィット関数を定義できます。
ROOTが提供する数学関数（`sin`、`cos`、`exp`、`sqrt`など）が使用できます。

## カスタム関数からフィット関数を定義したい（`TF1`）

```cpp
#include <TF1.h>

Double_t myFunc(Double_t *x, Double_t *par) {
    // x[0]は独立変数、par[0]以降はパラメータ
    return par[0] * sin(x[0]) + par[1];
}

TF1 *f = new TF1("f", myFunc, 0, 2*M_PI, 2);

// パラメータを初期化
f->SetParameter(0, 1.0);   // 振幅
f->SetParameter(1, 0.0);   // オフセット

f->Draw();
```

カスタム関数で複雑なフィット関数を定義できます。
パラメーターを持つ関数も定義できます。

## ラムダ式からフィット関数を定義したい（`TF1`）

```cpp
#include <TF1.h>

auto lambda = [](double *x, double *p) {
    return p[0] * exp(-0.5 * pow((x[0] - p[1]) / p[2], 2));
};

TF1 *f = new TF1("gauss", lambda, 0, 10, 3);
f->SetParameter(0, 1.0);   // 振幅
f->SetParameter(1, 5.0);   // 平均値
f->SetParameter(2, 1.0);   // 標準偏差

f->Draw();
```

ラムダ式を使用して、関数をコンパクトに定義できます。

## パラメーターを持つフィット関数を定義したい（`SetParameter`）

```cpp
#include <TF1.h>
#include <TCanvas.h>

TF1 *f = new TF1("f", "[0]*sin([1]*x+[2])", 0, 2*M_PI);

// パラメータを設定: [0]=振幅、[1]=周波数、[2]=位相
f->SetParameter(0, 1.0);
f->SetParameter(1, 1.0);
f->SetParameter(2, 0.0);

f->SetLineColor(2);
f->SetLineWidth(2);
f->Draw();

// パラメータを変更して再度描画
f->SetParameter(0, 2.0);
f->SetParameter(1, 0.5);
f->DrawCopy("same");
```

`"[0]*sin([1]*x+[2])"`のように数式に`[0]`、`[1]`などの記号を使用してパラメーターを指定できます。
パラメーターの初期値は`SetParameter`メソッドで設定します。

## 関数の最小値・最大値を求めたい（`GetMinimum`、`GetMaximum`）

```cpp
#include <TF1.h>
#include <iostream>

TF1 *f = new TF1("f", "x*x-4*x+3", -1, 5);

Double_t xmin = f->GetMinimumX(0, 5);
Double_t ymin = f->GetMinimum(0, 5);

Double_t xmax = f->GetMaximumX(0, 5);
Double_t ymax = f->GetMaximum(0, 5);

std::cout << "Minimum: (" << xmin << ", " << ymin << ")" << std::endl;
std::cout << "Maximum: (" << xmax << ", " << ymax << ")" << std::endl;
```

関数の最小値と最大値、およびそれらの位置を求めることができます。

## 関数を評価したい（`Eval`）

```cpp
#include <TF1.h>
#include <iostream>

TF1 *f = new TF1("f", "sin(x)*cos(x)", 0, 2*M_PI);

// x=1.0での関数値を計算
Double_t y = f->Eval(1.0);

std::cout << "f(1.0) = " << y << std::endl;
```

`Eval()`で指定したx値に対する関数値を計算できます。

## 関連メソッド

- [SetParameter](./root-tf1-setparameter.md) - パラメーターを設定
- [SetLineColor](./root-tf1-setlinecolor.md) - 線の色を設定
- [Draw](./root-tf1-draw.md) - 関数を描画
- [Fit](./root-th1-fit.md) - ヒストグラムにフィット

## 参考リンク

- [ROOT TF1 Documentation](https://root.cern/doc/master/classTF1.html)
- [ROOT Mathematical Functions](https://root.cern/doc/master/group__MathCore.html)
