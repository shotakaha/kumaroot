# 物理記号したい（``physics``）

```latex
\usepackage{physics}
```

[physics](https://www.ctan.org/pkg/physics)パッケージを使って、物理学に関係した数式記号を簡単に記述できるようになります。

大学で物理学や数学のレポートを作成する場合、ベクトル、微分記号、ブラケット記号などを多用しますが、標準の数式環境だけで書くのはなかなか大変です。

:::{hint}

実際に``amsmath``で定義されている数式記号だけを使って書くのはものすごく大変でした。
学生のときに一番知っておきたかったパッケージです。

:::

:::{note}

調べてみると[physics](https://www.ctan.org/pkg/physics)パッケージは（LaTeX的に）内部のお行儀が悪いようです。
また、2012年に開発が止まっています。

代替パッケージ案もいくつか提案されているようです。
そのあたりは[このQiita記事](https://qiita.com/Yarakashi_Kikohshi/items/131e2324f401c3effb84)が詳しいので、参考にしてください。

:::

## ベクトルを表示したい

```latex
\vb{a}    % ベクトルを太字で表現
\va{a}    % 矢印を使って表現
\vu{a}    % 単位ベクトル（^）
```

## 微分記号を表示したい

```latex
\dd
\dd{x}
\dd[2]{x}
```

```latex
\dv{x}
\dv{f}{x}
```

```latex
\pdv{x}
\pdv{f}{x}
\pdv[n]{f}{x}  % n階の偏微分
```
