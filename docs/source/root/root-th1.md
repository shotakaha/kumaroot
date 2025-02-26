# 1次元ヒストグラムしたい（`TH1`）

```cpp
TH1D *h = new TH1D("h1", "Random", 200, -2, 2);
for (Int_t i = 0; i < 100000; i++) {
    h->Fill(gRandom-Gaus(0, 1));
}
h->Draw();
```

`TH1`は1次元ヒストグラムの基本クラスです。
解析したいデータに合わせて、以下の派生クラスを利用します。

| クラス名 | データ型 | データ長 |
|---|---|---|
| TH1C | `char` | 8bit 整数 |
| TH1S | `short` | 16bit 整数 |
| TH1I | `int` | 32bit 整数 |
| TH1F | `float` | 32bit 浮動小数点 |
| TH1D | `double` | 64bit 浮動小数点 |

データが整数値の場合は`TH1I`、
連続値の場合は`TH1F`もしくは`TH1D`を使えばOKです。

## タイトルしたい

```cpp
TH1D *h = new TH1D("h1", "title", xbin, xmin, xmax);
TH1D *h = new TH1D("h1", "title;x;y", xbin, xmin, xmax);
```

オブジェクトを初期化するときに、グラフのタイトルを指定できます。
`タイトル;X軸タイトル;Y軸タイトル`のように`;`（セミコロン）で区切ると
X軸とY軸のタイトルも同時に指定できます。
