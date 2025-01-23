# 表組みしたい（`booktabs`）

```latex
\usepackage{booktabs}
```

`booktabs`は表の見た目をよくするパッケージです。
**縦線と二重線は絶対に使わない** という方針で設計されています。

`\toprule` / `\midrule` / `\bottomrule`の3つが主なコマンドです。
これまで表を区切るときに使っていた`\hline`の代わりに使えばOKです。
これらのコマンドは`longtable`パッケージと同時に使えます。

:::{note}

作者によると、イギリスではlineのことをruleと呼ぶため、
この慣習にならってコマンド名をつけているそうです。

:::
