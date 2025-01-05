# ファインマン図したい（`tikz-feynman`）

```latex
\usepackage[compat=1.1.0]{tikz-feynman}
```

`tikz-feynman`パッケージで、TikZをベースにしたファインマン図を描くことができます。
`[compat=1.1.0]`オプションを使って、パッケージに変更があった場合に警告されるようにしています。

```latex
\feynmandiagram [horizontal=a to b] {
i1 -- [fermion] a -- [fermion] i2,
a -- [photon] b,
f1 -- [fermion] b -- [fermion] f2,
};
```

基本コマンドは`\feynmandiagram{...};`です。
末尾の`;`は必須です。

このコマンドの中に
始状態（initial state）と終状態（final state）、
粒子の種類、頂点（vertex）など、必要な要素を定義して、
ファインマン図を描きます。
それぞれの要素は自動的に配置されます。

:::{note}
末尾の`;`は必須です。
`;`はTikZの構文のようです。
:::
