# TTree編

ROOTを使った解析において``TTree``（もしくは次の章の``TChain``）は
必ずおさえておくべきクラスだと考えています。

取得したデータはさっさと``TTree``に変換してしまって、データ解析を楽しみましょう。

```{toctree}
---
maxdepth: 1
---
root-tree-ttree
root-tree-readfile
root-tree-branch
```

```{note}
「さるROOT」や他のウェブサイトでは
``TNtuple``をコードサンプルとして紹介している場合がありますが、
そういった情報はちょっと古いかなと感じます。

``TTree``は``TNtuple``を含んでいるはずなので、
どんどん読み替えていってよいと思います。
```
