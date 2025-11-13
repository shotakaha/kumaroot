# 軸の目盛り間隔を変更したい（`gStyle->SetNdivisions`）

```cpp
#include <TStyle.h>

// デフォルト: 50分割（10分割×5分割）
gStyle->SetNdivisions(000510);

// 100分割にしたい
gStyle->SetNdivisions(020510);

// 20分割にしたい（シンプル）
gStyle->SetNdivisions(000520);
```

`gStyle->SetNdivisions`メソッドで、
グラフやヒストグラムの軸の目盛り間隔を制御できます。

```python
from ROOT import gStyle

# デフォルト: 50分割
gStyle.SetNdivisions(000510)

# 100分割
gStyle.SetNdivisions(020510)

# 20分割
gStyle.SetNdivisions(000520)
```

## パラメーターの意味を理解したい

`SetNdivisions`の引数は、TTSSPP形式の6桁の整数です。

| 桁 | パラメーター | 説明 |
|---|----------|------|
| PP（右2桁） | Primary | 軸全体の分割数 |
| SS（中央2桁） | Secondary | PP分割された各セグメント内の分割数 |
| TT（左2桁） | Tertiary | SS分割された各セグメント内の分割数 |

### デフォルト値（000510）の説明

```text
000510 = TT(00) + SS(05) + PP(10)
```

- `PP=10`: 軸を10セグメントに分割
- `SS=05`: 各セグメントをさらに5分割
- `TT=00`: 3段階目の分割なし

結果として、軸全体は10×5=50の目盛りになります。

## 異なる分割数を使いたい

### 100分割にしたい

```cpp
#include <TStyle.h>

gStyle->SetNdivisions(020510);
```

- `PP=10`: 軸を10分割
- `SS=05`: 各セグメントを5分割
- `TT=02`: さらに2分割

計算: 10×5×2 = 100分割

### 20分割にしたい（シンプル）

```cpp
#include <TStyle.h>

gStyle->SetNdivisions(000520);
```

- `PP=20`: 軸を20分割
- `SS=05`: 各セグメントを5分割
- `TT=00`: 3段階目の分割なし

計算: 20×5 = 100目盛り

### カスタム分割（少ない目盛り）

```cpp
#include <TStyle.h>

// 5分割のシンプルな表示
gStyle->SetNdivisions(000505);
```

- `PP=05`: 5分割のみ
- `SS=05`, `TT=00`: セグメント内分割なし

計算: 5目盛り

## 特定の軸だけを変更したい

```cpp
#include <TStyle.h>

// X軸の目盛り数を指定
gStyle->SetNdivisions(006, "X");

// Y軸の目盛り数を指定
gStyle->SetNdivisions(010, "Y");

// Z軸の目盛り数を指定
gStyle->SetNdivisions(008, "Z");
```

`SetNdivisions`の第2引数で軸を指定できます。
軸全体の分割数のみ指定する簡潔な方法です。

## 実用例

### 論文用（見やすく、シンプル）

```cpp
#include <TStyle.h>

gStyle->SetNdivisions(005, "X");
gStyle->SetNdivisions(005, "Y");
```

5分割という少ない目盛りで、見やすくシンプルな表示です。

### データ分析用（詳細な読み取り）

```cpp
#include <TStyle.h>

gStyle->SetNdivisions(020510);
```

100分割で細かく値を読み取ることができます。

### プレゼンテーション用（視認性重視）

```cpp
#include <TStyle.h>

gStyle->SetNdivisions(010);
```

10分割のシンプルで見やすい表示です。

## リファレンス

- [ROOT TStyle::SetNdivisions Documentation](https://root.cern/doc/master/classTStyle.html#a91b3e91d5abef9ac6f3e73f2c90a35ef)
