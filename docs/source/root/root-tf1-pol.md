# 多項式でフィットしたい（`TF1` with `"pol"`）

```cpp
#include <TGraphErrors.h>
#include <TF1.h>
#include <TRandom3.h>

const int n = 50;
double x[n], y[n], ey[n];
TRandom3 random;

for (int i = 0; i < n; i++) {
    x[i] = 20 + (60.0 / n) * i;
    y[i] = 2 * x[i] + 100;
    ey[i] = 5;
}

TGraphErrors *g = new TGraphErrors(n, x, y, nullptr, ey);
TF1 *f = new TF1("polynomial", "pol1", 20, 80);
g->Fit(f);
```

多項式関数`"pol<n>"`でデータをフィットできます。
`<n>`は多項式の次数を指定してください。

## 定数でフィットしたい（`pol0`）

```cpp
#include <TGraphErrors.h>
#include <TF1.h>

const int n = 50;
double x[n], y[n], ey[n];

for (int i = 0; i < n; i++) {
    x[i] = 20 + (60.0 / n) * i;
    y[i] = 50;
    ey[i] = 2;
}

TGraphErrors *g = new TGraphErrors(n, x, y, nullptr, ey);
TF1 *f = new TF1("polynomial", "pol0", 20, 80);
g->Fit(f);
```

`pol0`は定数でフィットします。

## 一次関数でフィットしたい（`pol1`）

```cpp
#include <TGraphErrors.h>
#include <TF1.h>

const int n = 50;
double x[n], y[n], ey[n];

for (int i = 0; i < n; i++) {
    x[i] = 20 + (60.0 / n) * i;
    y[i] = 2 * x[i] + 100;
    ey[i] = 3;
}

TGraphErrors *g = new TGraphErrors(n, x, y, nullptr, ey);
TF1 *f = new TF1("polynomial", "pol1", 20, 80);
g->Fit(f);
```

`pol1`は一次関数（直線）でフィットします。

## 二次関数でフィットしたい（`pol2`）

```cpp
#include <TGraphErrors.h>
#include <TF1.h>

const int n = 50;
double x[n], y[n], ey[n];

for (int i = 0; i < n; i++) {
    x[i] = 20 + (60.0 / n) * i;
    y[i] = x[i] * x[i] - 50 * x[i] + 3000;
    ey[i] = 10;
}

TGraphErrors *g = new TGraphErrors(n, x, y, nullptr, ey);
TF1 *f = new TF1("polynomial", "pol2", 20, 80);
g->Fit(f);
```

`pol2`は二次関数（放物線）でフィットします。
