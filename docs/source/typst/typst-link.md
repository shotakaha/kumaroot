# ハイパーリンクしたい（``#link``）

```typst
// #link("リンク先")[表示名]
#link("https://kumaroot.readthedocs.io/ja/latest/")[KumaROOT]
```

[#link](https://typst.app/docs/reference/model/link/)
要素でハイパーリンクを作成できます。
リンク先は、ドキュメント内のラベルや外部URLなどを指定できます。

`[表示名]`は省略可能で、
`http://`や`https://`
で始まる文字列は自動でリンクに変換されます。

:::{seealso}

- [](../latex/latex-hyperref.md)

:::

:::{caution}

Markdown記法と要素の順番が逆になっています。

- Markdown: `[表示名](リンク先)`
- Typst: `#link("リンク先")[表示名]`

`[表示名]`は（トレイリング）コンテンツブロックなので、Typstの設計思想の通りですが、すぐに間違えそうです。

:::
