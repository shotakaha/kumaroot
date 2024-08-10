# エラーバー付きのグラフしたい（``TGraphErrors``）

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
