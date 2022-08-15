# TTree編

ROOTを使った解析において``TTree``（もしくは次の章の``TChain``）は
必ずおさえておくべきクラスだと考えています。

取得したデータはさっさと``TTree``に変換してしまって、データ解析を楽しみましょう。

```{code-block} cpp
---
linenos: true
emphasize-lines: 1
---
TTree *tree = new TTree("t1", "test measurement");
tree->ReadFile("入力ファイル名", "列1/I:列2/I:列3/D", ",");  // CSVを読み込んだ想定
tree->Draw("列1");  // 列1のヒストグラムを作成
```

```cpp
TTree TTree(const char* name,
            const char* title,
            Int_t splitlevel = 99)
```

``name``
:   TTreeオブジェクトの名前です。
    他のオブジェクトと重複しないようにしてください。

``title``
:   データの説明です。
    ``TFile``で開いたときに表示される文字列です。
    なくても構いませんが、1行くらいの簡単な説明をきちんとつけておくとよいです。

``splitlevel``
:   使ったことがないです。


```{toctree}
---
maxdepth: 1
---
root-ttree-readfile
root-tree-branch
```

```{note}
「さるROOT」や他のウェブサイトでは
``TNtuple``をコードサンプルとして紹介している場合がありますが、
そういった情報はちょっと古いかなと感じます。

``TTree``は``TNtuple``を含んでいるはずなので、
どんどん読み替えていってよいと思います。
```
