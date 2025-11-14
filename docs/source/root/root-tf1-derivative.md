# フィット関数の導関数を求めたい（`TF1::Derivative`）

```cpp
#include <TF1.h>
#include <iostream>

TF1 *f = new TF1("f", "x*x*x", -2, 2);

// x=1.0での導関数の値を計算
Double_t derivative = f->Derivative(1.0);

std::cout << "Derivative at x=1.0: " << derivative << std::endl;
// f'(x) = 3x^2、x=1.0では3.0
```

`TF1::Derivative`メソッドで、指定した点でのフィット関数の導関数の値を計算できます。
