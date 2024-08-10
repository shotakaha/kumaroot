# ROOTの使い方

``ROOT``と高エネルギー物理学分野で広く使われている解析フレームワークです。
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

## インストールしたい

```{toctree}
---
maxdepth: 1
---
root-install
root-config
root-pyroot
```

## チュートリアルしたい

```{toctree}
root-tutorial
```

## 全体設定したい

```{toctree}
root-groot
root-gstyle
root-gsystem
```

```{toctree}
---
maxdepth: 1
---
root-ttree
root-hist
root-chain
root-tfile
root-tstring
root-canvas
root-tgraph
root-tlegend
root5-root6
root-emacs
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
    あと、これを書いているときに気づいたのですが、
    はじめての方は[ROOT Primer](https://root.cern/primer/)にも目を通してみると良いかもしれません。

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
