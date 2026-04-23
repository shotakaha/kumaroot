# ROOTの使い方

``ROOT``は高エネルギー物理学分野で広く使われている解析フレームワークです。
スイスにあるCERNを中心に開発されています。

**解析フレームワーク**と聞くと敷居が高そうに感じますが
「お絵かきソフトだ」と気軽に捉えて使えばよいと思っています。
もちろん、自由に絵を描くソフトとは異なり、
**自分が測定したデータ**を使って**ヒストグラムやグラフを描くことが中心**になります。

```{warning}
このドキュメントの大部分は``ROOT5``のときの使い方で書かれたものです。
少しずつ``ROOT6``に合った使い方に書き換えていこうと考えていますが、時間がかかりそうです。
うまく動かない箇所は、各自で``ROOT6``の使い方を調べてください。
```

## 環境構築したい

ROOTをインストールして、開発環境を準備する方法を説明します。

```{toctree}
---
maxdepth: 1
---
root-setup
```

## はじめての一歩

ROOTの対話型シェル（Rint）を使って、コンパイルなしにC++コードを実行できます。
まずはRintで簡単な計算やマクロを試してみましょう。

```{toctree}
---
maxdepth: 1
---
root-rint
root-rint-calculator
root-rint-macro
root-rint-quit
root-cling
```

## TBrowserしたい

```{toctree}
---
maxdepth: 1
---
root-tbrowser
```

## TCanvasしたい

```{toctree}
---
maxdepth: 1
---
root-tcanvas
root-tcanvas-divide
root-tcanvas-saveas
root-tcanvas-print
root-tcanvas-update
root-tcanvas-log
root-tcanvas-drawcolortable
```

## ヒストグラムしたい

```{toctree}
---
maxdepth: 1
---
root-th1
root-th2
root-th1-fill
root-th1-draw
root-th1-fit
root-th1-title
root-th1-integral
root-th1-scale
root-th1-stats
root-th1-mean
root-th1-rms
root-th1-binerror
root-th1-sumw2
```

## グラフしたい

```{toctree}
---
maxdepth: 1
---
root-tgraph
root-tgrapherrors
root-tgraph-point
root-tmultigraph
root-tlegend
```

## フィットしたい

```{toctree}
---
maxdepth: 1
---
root-tf1
root-tf1-draw
root-tf1-getparameter
root-tf1-getchisquare
root-tf1-setparameter
root-tf1-fixparameter
root-tf1-gaus
root-tf1-pol
root-tf1-crystalball
root-tf1-integral
root-tf1-derivative
```

## TTreeしたい

``TTree``はROOTのデータ構造の基本です。
CSVなどのテキスト形式で取得したデータをすぐに``TTree``に変換しておくと、ROOTを使ったデータ解析が捗ります。
複数のTTreeを読み込む場合は``TChain``クラスが便利です。

```{toctree}
---
maxdepth: 1
---
root-ttree
root-ttree-readfile
root-ttree-entries
root-ttree-entry
root-ttree-branch
root-ttree-fill
root-ttree-write
root-ttree-print
root-ttree-draw
```

## TChainしたい

```{toctree}
---
maxdepth: 1
---
root-tchain
```

## RNTupleしたい

```{toctree}
---
maxdepth: 1
---
root-rntuple
```

## RDataFrameしたい

```{toctree}
---
maxdepth: 1
---
root-rdataframe
root-rdataframe-csv
root-rdataframe-filter
root-rdataframe-stats
root-rdataframe-histo1d
```

## TFileしたい

```{toctree}
---
maxdepth: 1
---
root-tfile
```

## TStringしたい

```{toctree}
---
maxdepth: 1
---
root-tstring
```

## gROOTしたい

```{toctree}
---
maxdepth: 1
---
root-groot
```

## gStyleしたい

```{toctree}
---
maxdepth: 1
---
root-gstyle
```

## gSystemしたい

```{toctree}
---
maxdepth: 1
---
root-gsystem
```

## gEnvしたい

```{toctree}
---
maxdepth: 1
---
root-genv
```

## その他の話題

```{toctree}
---
maxdepth: 1
---
root5-root6
root-cint
root-emacs
root-history
```

## リファレンス

このKumaROOTに載っているROOTの情報は、下記のサイトを参考にしています。
だいたい自分で試してみて使い方を理解したもの載せています。
本当に詳しいことは下記の情報を自分で読んでみるのが一番だと思います。

[ROOT公式マニュアル](https://root.cern/manual/)
:   困ったらとりあえず読みましょう！
    [Basics](https://root.cern/manual/basics/) or [Functional parts](https://root.cern/manual/functional_parts/)から自分の目的に合ったドキュメントを探しましょう。
    とてーも長いので全部読もうとしてはいけません。
    **必要な時**に、**必要は箇所**を、**必要なだけ読む**ことが大切です。

[ROOT Primer](https://root.cern/primer/)
:   はじめての方向けの総合的なガイドです。
    ROOTの基本的な使い方から応用的な技法まで、体系的に学べます。

[ROOT公式リファレンスガイド](https://root.cern/doc/master/)
:   クラス名やそのメソッド名、内容、使い方を知りたい場合に使いましょう！
    といっても、このページから辿らなくても「``cern root ttree``」とググればだいたいヒットします。
    検索では「``cern``」と付けるのが重要です。
    でないと、管理者の意味の「root」がたくさんヒットしてしまいます。
    リファレンスガイドは「クラスの説明＋メソッド一覧」という構成になっています。
    最初は読むのに苦労するかもしれませんが、使いこなせるように頑張りましょう。
    自分のやりたい情報が得られるようになれば、もうROOT中級者です。

[ROOT公式チュートリアル](https://root.cern/doc/master/group__Tutorials.html)
:   付属のサンプルコードの説明です。
    ドキュメントやリファレンスを読むより、
    実際にコードを動かし、ソースを読むほうが早く身につきます。
    はじめて使うクラスなどはとりあえずサンプルを動かしてみましょう。

[ROOT公式コーディングガイド](https://root.cern/contribute/coding_conventions/)
:   ROOTのソースコードを読むときに役に立つと思います。
    なんとなく知っておくと良いです。
    覚える必要はまったくありません。

[ROOT解体新書](http://hep.planet-koo.com/index.php?g=root)
:   ``gROOT`` や ``gStyle`` の設定がすごく詳しいサイトです。
    他のページでは見られない項目がすごく詳しいです。
    残念ながらページのリンク切れを確認（2015-01-27）

[宇宙線実験の覚え書き（大学院生版）](http://blog.livedoor.jp/oxon/)
:   ``PyROOT`` のことがたくさん載っているoxonさんのブログです。
    現在は[宇宙線実験の覚え書き（社会人版）](https://oxon.hatenablog.com/)
    に引っ越しされたみたいです。
