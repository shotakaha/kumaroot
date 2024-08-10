# グラフしたい（``TGraph``）

```cpp
TGraph *g;
g->SetPoint(g->GetN(), x1, y1);
g->SetPoint(g->GetN(), x2, y2);
g->SetPoint(g->GetN(), x3, y3);
```

``TGraph::SetPoint``で、データ点を順番に追加できます。
方眼紙にプロットするように、1点ずつ点を打つようなグラフ（散布図）を作りたい人に向いています。

## FADCの波形データをプロットしたい

```cpp
const Int_t N = t->GetEntries();
TGraph *gr[N];        // 各イベントのFADC波形をグラフにしたいとする

for (Int_t igraph = 0; graph < N; igraph++) {
    gr[igraph] = new TGraph(0);  // 0個の点のグラフとしてTGraphオブジェクトを作成
}

for (Int_t ientry = 0; ientry < N; ientry++) {
    t->GetEntry(ientry);    // ここで、FADCの各サンプリング点データの詰まったvectorが得られるとする（変数名をadcとする）
    Int_t Nsamp = (Int_t)adc.size();    // vector変数の大きさを調べる
    for (Int_t isamp = 0; isamp < Nsamp; isamp++) {
        gr[ientry]->SetPoint(gr[ientry]->GetN(), isamp, adc->at(isamp));
            // GetN()で、今の点の数を取ってきているのがミソ
            // あとは、xの値、yの値を指定する
    }
}
```

上記サンプルは、FADCの波形データをプロットした場合のものです。

## エラーを付ける際の注意点

- 上のループはTGraphErrorsでも使用可能
- なので、エラーを付けることもできるが、以下の点に注意する

```cpp
// これは間違い
gre->SetPoint(gre->GetN(), x, y);             // とりえあずGetN()してプロットする
gre->SetPointError(gre->GetN(), xerr, yerr);  // しかし、これだと、GetN()が次のになってしまって、正しい位置にエラーがつかない

// 正しくは以下のようにする
Int_t npt = gre->GetN();
gre->SetPoint(npt, x, y);
gre->SetPoint(npt, xerr, yerr);  // 第一引数の値を一緒にする
```
