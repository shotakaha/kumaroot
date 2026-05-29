# カラムを追加したい（`RDataFrame::Define`）

```cpp
auto df = ROOT::RDataFrame(100)
    .Define("x", "gRandom->Gaus(0, 1)")
    .Define("y", "gRandom->Gaus(0, 1)");
df.Describe();
```

`RDataFrame::Define`は、既存のデータフレームに新しいカラムを追加するためのメソッドです。
イミュータブルな操作で、元のデータフレームを変更せずに新しいデータフレームを返します。
