# フィット関数を積分したい（`TF1::Integral`）

```cpp
#include <TF1.h>
#include <iostream>

TF1 *f = new TF1("f", "x*x", 0, 5);

// x^2をx=0からx=5まで積分
Double_t integral = f->Integral(0, 5);

std::cout << "Integral from 0 to 5: " << integral << std::endl;
// 正確な値: 5^3/3 = 41.667
```

`TF1::Integral`メソッドでフィット関数の積分を計算できます。
数値積分を使用して計算されます。
