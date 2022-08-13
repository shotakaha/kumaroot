# TLegend編

TLegendやTTextとかも含めて、凡例表示に関して

## 凡例を表示したい

[TLegend](https://root.cern.ch/doc/master/classTLegend.html)を使ってプロットの凡例を表示できます。

```cpp
TLegend *leg = new TLegend(0.2, 0.7, 0.5, 0.9, "");
leg->AddEntry(gre1, Form("RUN%d", nrun1), "lp");
leg->AddEntry(gre2, Form("RUN%d", nrun2), "lp");
leg->SetFillStyle(0);
leg->Draw();
```

- ``TLegend``オブジェクトにはさまざまなROOTオブジェクトを追加（``AddEntry``）することができる（はず）
- 凡例のラベル表示のオプション
  - ``l`` --- 線を表示；SetLineColorした色が表示される
  - ``p`` --- 点を表示；SetMarkerStyle, SetMarkerColorしたマーカー・、色が表示される
  - ``f`` --- 背景を表示；SetFillStyle, SetFillColorがした色、スタイルが表示される
- ``TLegend``の背景は、デフォルトで灰色なので、SetFillStyle(0)（背景なし）、もしくはSetFillColor(0)（白塗り）する必要がある

## 任意の位置に文字を表示したい

``TText``を使って任意の位置に文字を表示できます。

```cpp
TText *t = new TText(0.5, 0.5, "");
t->DrawTextNDC(0.2, 0.75, Form("Relative Q.E = %.2f", p1));
```

## 任意の位置に文字を表示したい

``TPaveText``を使うとより複雑な文字を表示できます。

```cpp
TPaveText *pt=new TPaveText(0.15,0.6,0.45,0.8,"brNDC");
pt->SetFillStyle(0);
pt->SetBorderSize(0);
TText* tt;
tt=pt->AddText(Form("Mean = %.2f", mean));
tt=pt->AddText(Form("RMS  = %.2f", rms));
tt=pt->AddText(Form("R/M  = %.2f %%", rms/mean * 100));
tt->SetTextColor(kRed);
pt->Draw();
```

- AddText()した後に、SetTextColor()をすることで、その文字列だけ色を変更できる
