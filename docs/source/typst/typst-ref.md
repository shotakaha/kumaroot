# 相互参照したい（`#ref` / `#label`）

```typst
#set page(numbering: "1")
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

= 第1章のタイトル <section1>

これについては
#ref(<section1>)
を参照してください。
```

`#ref`要素と`#label`型の組み合わせで相互参照できます。
まず、参照したい要素に`#label`型のラベル名を設定します。
このラベル名は、いわゆるアンカーで、このラベル名を使って、本文中の任意の箇所で`#ref`要素を使って参照できます。

## ラベルしたい（`#label`）

```typst
参照したい要素 <ラベル名>
参照したい要素 #label("ラベル名")
```

`<ラベル名>`によるマークアップ、
もしくは`#label`要素でラベルを設定します。
ラベル名は日本語も設定できます。

現在（v0.14.0）では
見出し（`#heading`）、
図版（`#figure`）、
数式（`#equation`）、
脚注（`#footnote`）の要素に対して
ラベルを設定できます。

:::{note}

あとで検索する可能性を考えると
`#label`要素を使うほうがよいと思います。

:::

## 参照したい（`#ref`）

```typst
それは#ref(<ラベル名>)を参照してください。
```

`#ref`要素でラベルを指定し、参照情報を取得できます。
第一引数は`<ラベル型>`を指定します。
ラベルを設定した要素に応じて`要素名 番号`の形式で表示されます。
要素名の文字列は`page.lang`設定により自動判別されます。

| 要素 | `lang: "en"` | `lang: "ja"` |
| --- | --- | --- |
| `#heading` | `Section 6.1` | `節 6.1` |
| `#figure` | `Figure 2` | `図 2` |
| `#math.equation` | `Equation 4` | `式 4` |
| `#footnote` | $^6$ | $^6$ |
| ページ参照 | `Page 3` | `ページ 3` |

:::{note}

上の表を整理してわかったことは、
デフォルトの日本語対応はイマイチだということです。

```typst
#set page(numbering: "1", supplement: "Page")
#set heading(numbering: "1.", supplement: "Figure")
#set math.equation(numbering: "(1)", supplement: "Equation")
```

きっと`show`ルールを考えれば対応できるのだと思いますが、
ひとまず日本語設定であっても、
`supplement`を一括して英語表記に設定して回避することにしています。

:::

## ページ参照したい（`#ref.form`）

```typst
#ref(<ラベル名>, form: "page")
```

`form: "page"`オプションで、
ラベルした要素があるページ番号を参照できます。

## 要素名したい（`#ref.supplement`）

```typst
#ref(<ラベル名>, supplement: [図版])
```

`supplement`オプションで、表示する文字列を変更できます。

## リファレンス

- [ref | Element | Typst](https://typst.app/docs/reference/model/ref/)
- [label | Typst](https://typst.app/docs/reference/foundations/label/)
