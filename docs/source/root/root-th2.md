# 2次元ヒストグラムしたい（`TH2`）

```cpp
TH2D *h = new TH2D("h2d", "title", 100, -1, 1, 100, -5, 5);
for (int i = 0; i < 100000; i++) {
    h->Fill(gRandom->Gaus(0, 1), gRandom->Gaus(0,1))
}
h->Draw();
```

`TH2`は2次元ヒストグラムの基本クラスです。
[TH1](./root-th1.md)と同じように、
データに合わせて派生クラスを利用します。
