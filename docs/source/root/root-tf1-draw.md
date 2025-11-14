# フィット関数を描画したい（`TF1::Draw`）

```cpp
#include <TH1D.h>
#include <TF1.h>
#include <TRandom3.h>
#include <TCanvas.h>

TH1D *h = new TH1D("h", "Gaussian Fit", 100, -5, 5);

TRandom3 random;
for (int i = 0; i < 5000; i++) {
    h->Fill(random.Gaus(0, 1));
}

TF1 *f = new TF1("f", "gaus", -5, 5);
h->Fit(f);

TCanvas *c = new TCanvas("c", "Fit Result", 600, 400);
h->Draw();
f->SetLineColor(2);
f->SetLineWidth(2);
f->Draw("same");

c->BuildLegend();
```

`TF1::Draw`でフィット曲線を描画できます。
`"same"`オプションでヒストグラムとフィット曲線を重ねて描画できます。
