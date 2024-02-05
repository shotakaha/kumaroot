# 表示方法を変更したい（``#show``）

```typst
#show 要素名: set 関数名(設定: 値)

#show raw: set block(fill: luma(235), inset: 2em, radius: 1em, width: 100%)
#show raw: set text(font: ("Roboto Mono", "Noto Sans CJK JP"))
```

``#show``関数を使って、表示方法を変更できます。
同じ要素に対して、何度も使うことができます。

公式ドキュメントには明記されてない書き方だと思いますが、Typst-like（もしくは Rust-like？）な書き方に慣れていなくても、なんとかなります。

## 文字列を置換したい

```typst
#show "文字列": "置換文字列"

#show "pi0": $pi^(0)$
#show "pi+": $pi^(+)$
#show "pi-": $pi^(-)$
```

Typstは文字列が簡単に置換できます。
上記サンプルではπ中間子の文字列を数式に置換しています。

:::{seealso}

- [](../latex/latex-newcommand.md)

:::
