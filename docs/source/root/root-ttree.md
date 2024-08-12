# TTreeしたい（``TTree``）

```{code-block} cpp
---
linenos: true
emphasize-lines: 1
---
// TTree::TTree("name", "title", splitlevel)
TTree *tree = new TTree("t1", "test measurement");
tree->ReadFile("入力ファイル名", "列1/I:列2/I:列3/D", ",");  // CSVを読み込んだ想定
tree->Draw("列1");  // 列1のヒストグラムを作成
```

``TTree::TTree``でTTreeオブジェクトを作成できます。
第1引数は、TTreeオブジェクトの名前を設定します。
他のオブジェクトと重複しないようにします。

第2引数は、データの説明などを設定します。
``TFile``で開いたときに表示される文字列です。
空欄でも構いませんが、1行くらいの簡単な説明をつけておくとよいです。

第3引数は``splitlevel``です。
デフォルト値は99です。
使ったことがないので、デフォルト値のままでよいと思います。


```{note}
「さるROOT」や他のウェブサイトでは
``TNtuple``をコードサンプルとして紹介している場合がありますが、
そういった情報はちょっと古いかなと感じます。

``TTree``は``TNtuple``を含んでいるはずなので、
どんどん読み替えていってよいと思います。
```

```python
from ROOT import TTree

t = TTree("tree", "tree description");
```

## リファレンス

- [TTree](https://root.cern.ch/doc/master/classTTree.html)
