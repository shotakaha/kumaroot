# 吸収したい（``G4OpAbsorption``）

```cpp
#include "G4OpAbsorption.hh"
```

## プロパティしたい

| プロパティ名 | 種類 | 説明 | 単位 |
|---|---|---|---|
| ``ABSLENGTH`` | Energy-dependent | 吸収長 | Length |

``ABSLENGTH``で、光子のエネルギーに応じた吸収長を設定できます。
吸収長は、物質（媒体）の中で光子が吸収されるまでに進む平均自由行程（Mean Free Path）です。
ユーザーが実測した値を設定します。

## マクロで設定したい（``/process/optical/absorption/``）

```cfg
/process/optical/absorption/verbose 1
```
