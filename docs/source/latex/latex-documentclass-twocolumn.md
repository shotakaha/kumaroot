# 二段組したい（`twocolumn`）

```latex
% 2段組に設定
\documentclass[twocolumn]{jlreq}

% 段間を調整
\documentclass[twocolumn, column_gap=2zw]{jlreq}
```

`twocolumn`オプションで、ドキュメント全体を2段組にできます。
`column_gap`オプションで段間（＝段と段のアキ）を変更できます。

`minipage`環境を使うと、ページの途中に段組を追加できます。

:::{seealso}

- [](./latex-minipage.md)

:::

```latex
\documentclass[twocolumn]{ltjsarticle}
\setlength{\columnsep}{2\zw}
```

`ltjsclasses`の場合は、
`\columnsep`で段間を変更します。

```latex
\documentclass[uplatex, dvipdfmx, twocolumn]{jsarticle}
\setlength{\columnsep}{2\zw}
```

`jsclasses`も同様です。
