# データフレームしたい（`RDataFrame`）

```cpp
ROOT::RDataFrame df("treeName", "ファイル名.root");
```

```python
import ROOT
df = ROOT.RDataFrame("treeName", "ファイル名.root")
```

`RDataFrame`は[pandas](../pandas/pandas-usage.md)のような使い勝手を目指した高レベルAPIです。
2017年ころに導入され、最新のROOTで推奨されているデータ形式です。

:::{note}

ROOTは1995年にリリースされたときから`TTree`というデータ構造を軸にしていました。
しかし、LHC Run4の開始に合わせた`RDataFrame`や`RNTuple`といった
よりモダンなフレームワークへと置き換えるというロードマップを描いています。

:::


## リファレンス

- [ROOT::RDataFrame](https://root.cern/doc/master/classROOT_1_1RDataFrame.html)
- [RNTuple: Where are we now and what's next](https://root.cern/blog/rntuple-update/)
