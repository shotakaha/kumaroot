# MultiGraphしたい（``TMultiGraph``）

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
- http://root.cern.ch/phpBB3/viewtopic.php?f=3&t=4041
