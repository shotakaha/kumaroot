# 重み付きデータのエラーしたい（`TH1::Sumw2`）

```cpp
h->Sumw2();

// Loop over data points
// Fill the histogram with values and weights
for (int i = 0; i < n; ++i) {
    double value = ...;  // データポイントの値
    double weight = ...; // データポイントの重み
    h->Fill(value, weight);
}
```

`TH1::Sumw2`は、重み付きデータの統計誤差を正しく計算するためのメソッドです。
ヒストグラムにデータを追加する前に、呼び出す必要があります。

`Fill(x)`は、1つのイベントを追加する操作です。
ヒストグラムの増加分は $\Delta k = 1$ です。
このとき、この増加分に対する誤差$\sigma_{k}$は、ポアソン近似で
$\sigma_{k} = \sqrt{\Delta k} = 1$
です。

`Fill(x, w)`は、1つのイベントに重み $w$ をつけて追加する操作です。
ヒストグラムの増加分は $\Delta n = w \cdot \Delta k = w$ です。
このとき、この増加分に対する誤差$\sigma_{n}$は、
誤差伝搬の公式から
$\sigma_{n} = w \cdot \sigma_{k} = w$
です。

複数イベントを合計した場合、ヒストグラムの増加分は
$N = \sum \Delta n = \Delta n_{1} + \Delta n_{2} + \cdots + \Delta n_{m} = w_{1} + w_{2} + \cdots + w_{m}$
です。
このとき、この増加分に対する誤差 $\sigma_{N}$ は
誤差伝搬の公式から
$\sigma_{N} = \sqrt{\sigma_{n_{1}}^{2} + \sigma_{n_{2}}^{2} + \cdots + \sigma_{n_{m}}^{2}} = \sqrt{w_{1}^{2} + w_{2}^{2} + \cdots + w_{m}^{2}} = \sqrt{\sum w_{i}^{2}}$
となります。

`TH1::Sumw2`は、
この誤差伝搬の計算に必要な誤差の二乗和
$\sum w_{i}^{2}$
を、`Fill`のたびに内部配列に保存します。

```cpp
TH1::SetDefaultSumw2(kTRUE);
```

`TH1::SetDefaultSumw2(kTRUE)`で、
すべてのヒストグラムに対して`Sumw2`が有効になります。
マクロの先頭で呼び出しておくとよいです。

:::{note}
このモードは、ROOT開発の初期に、メモリ消費を節約するためにデフォルトで無効になっているようです。
現在のように個人パソコンでもメモリが十分にある解析環境では、マクロ全体で有効にしても問題ありません。
また、`RDataFrame`では`Sumw2`はデフォルトで有効になっています。
:::
