# 表組みしたい（``booktabs``）

```latex
\usepackage{booktabs}
```

表の見た目をよくするパッケージです。
**縦線と二重線は絶対に使わない** という方針で設計されています。

``\toprule`` / ``\midrule`` / ``\bottomrule``の3つが主なコマンドです。
これまで表を区切るときに使っていた``\hline``の代わりに使えばOKです
（作者曰く、イギリスではlineのことをruleと呼ので、この慣習にならってコマンド名をつけているそうです）。
これらのコマンドは``longtable``パッケージと同時に使えます。

## リファレンス

- {command}`texdoc booktabs`
