# TGraph編

## グラフに順に点を足していきたい

- 方眼紙にプロットするように、１点ずつ点を打つようなグラフ（散布図）を作りたい人向け
- FADCの波形データをプロットした場合を例に示す

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

## エラーバー付きのグラフを作成した

- TGraphErrorsクラスを使う

```cpp
const int npoints = 10;
double x[npoints] = {1, 2, 4, 8, 16, 3, 9, 18, 5, 25};

TGraphErrors *gre;
gre = new TGraphErrors(npoints);

for (int i = 0; i < npoints; i++){
    gre->SetPoint(i, x[i], 3*x[i]-x[i]);
    gre->SetPointError(i, 0.5, TMath::Sqrt(x[i]));
}

gre->Draw("ap");
```

## TMultiGraph

```cpp
TMultiGraph *mg = new TMultiGraph("mg", "mg")
TGraph *g[4];
for (Int_t i = 0; i < 4; i++) {
    g[i] = new TGraph(0);
    mg->Add(g[i], "pl");
}
mg->Draw()
```

- TMultiGraphでGetXaxis()するときには、以下のtipsが必要
  - [[http://root.cern.ch/phpBB3/viewtopic.php?f=3&t=4041]]
