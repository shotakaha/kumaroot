# 横軸に時間を使いたい（ ``SetTimeFormat`` , ``SetTimeDisplay`` ）

```cpp
gStyle->SetTimeOffset(-788918400);    // set diff. btw Unix and ROOT epoch
graph->GetXaxis()->SetTimeDisplay(1);
graph->GetXaxis()->SetTimeFormat("%Y-%m-%dT%H:%M:%S");
graph->GetXaxis()->SetTimeOffset(0, "gmt");    // set GMT+0
```

Unixのepoch timeは
1970年01月01日00時00分00秒から始まるのに対し、
ROOTのepoch timeは
1995年01月01日00時00分00秒から始まります。
その差をオフセットとして設定する必要があります。

```python
from ROOT import gStyle
gStyle.SetTimeOffset(-788918400);
```

## Unix epoch と ROOT epochの差を計算する

```python
years = 1995 - 1970  # 25 years
days = 365           # days/year
leap_days = 6        # 6 leap years in 25 years
hh = 24              # hours/day
mm  = 60             # minutes / hour
ss  = 60             # seconds / min

(years * days + leap_days) * hh * mm * ss
# 788918400 [seconds]
```

簡単な計算なので確かめてみました。
1970年から1995年までの25年間に、閏年が6回あることを考慮して計算します。

## GMT+0にしたい（``SetTimeOffset``）

```cpp
graph->GetXaxis()->SetTimeOffset(0, "gmt");
```

理由は忘れましたが、上の設定をしないと軸の時間がずれてしまってたはずです。
epochの時間ではなく、作成したグラフ／ヒストグラムの軸に対して設定します。

## 月日と時刻を2段にして表示したい

```cpp
graph->GetXaxis()->SetTimeFormat("#splitline{%m-%d}{%H:%M}");
```

長時間測定した場合、時刻の他に、日付も表示したほうがわかりやすくなります。
1行で収まらない場合は2段にできます。
