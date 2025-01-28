# 和文クラスしたい（`jsclasses`）

```latex
% jsclasses
\documentclass[uplatex, dvipdfmx]{jsarticle}
\documentclass[uplatex, dvipdfmx]{jsreport}
\documentclass[uplatex, dvipdfmx]{jsbook}
```

`jsclasses`は三重大の奥村さんが作成した和文クラスです。
(u)pLaTeXを利用するときにお世話になるクラスです。
オプションにエンジン（`uplatex`）とドライバー（`dvipdfmx`）は必須です。
また、他に追加したほうがよいパッケージもいくつかあります。

ウェブ検索したときに、まだまだ多数ヒットする情報だと思うので、知っておくとよいです。

:::{note}

``(u)pLaTeX + jsclasses系``のサンプルも、わかる範囲で載せておきます。

:::

## トンボを表示したい

```latex
\documentclass[tombow]{ltjsarticle}
\documentclass[uplatex, dvipdfmx, tombo]{jsarticle}
```

## リファレンス

- {command}`texdoc jsclasses`
- {command}`texdoc ltjsclasses`
