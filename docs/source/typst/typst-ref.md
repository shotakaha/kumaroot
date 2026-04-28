# 相互参照したい（`#ref`）

```typst
#set page(numbering: "1")
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

= 第1章のタイトル <section1>

これについては
#ref(<section1>)
を参照してください。
```

`#ref`要素でラベルを指定し、参照情報を取得できます。
ラベルを設定した要素に応じて`要素名 番号`の形式で表示されます。

:::{seealso}

- [](./typst-label.md)

:::

## 参照名したい（`#ref.supplement`）

```typst
#ref(<ラベル名>, supplement: [図版])
```

`supplement`オプションで、参照したラベルを表示するときの文字列を変更できます。
デフォルトは`supplement: "auto"`で、`#page.lang`で設定した言語に応じて自動的に表示されます。

`lang: "en"`と`lang: "ja"`で確認した結果は以下の表のとおりです。

| 要素 | `lang: "en"` | `lang: "ja"` |
| --- | --- | --- |
| `#heading` | `Section 6.1` | `節 6.1` |
| `#figure` | `Figure 2` | `図 2` |
| `#math.equation` | `Equation 4` | `式 4` |
| `#footnote` | $^6$ | $^6$ |
| ページ参照 | `Page 3` | `ページ 3` |

この表を見るとわかるように、
日本語設定時の表示名はイマイチです。

```typst
#set page(numbering: "1", supplement: "Page")
#set heading(numbering: "1.", supplement: "Figure")
#set math.equation(numbering: "(1)", supplement: "Equation")
```

ひとまず日本語設定であっても、
それぞれの要素の
`supplement`
を英語表記に設定して回避することにしています。

:::{note}

きっと`show`ルールを考えれば対応できるのだと思いますが、試していません。

:::

## ページ参照したい（`#ref.form`）

```typst
#ref(<ラベル名>, form: "page")
```

`form`オプションで、参照する基準を変更できます。
デフォルトは`form: "normal"`で、要素名と番号を参照します。
`form: "page"`に設定すると、要素があるページ番号を参照できます。



## リファレンス

- [ref | Element | Typst](https://typst.app/docs/reference/model/ref/)
- [label | Typst](https://typst.app/docs/reference/foundations/label/)
