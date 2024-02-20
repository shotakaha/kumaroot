# ハイパーリンクしたい（``#link``）

```text
#link(URL)[表示名]
```

[#link](https://typst.app/docs/reference/model/link/)を使ってハイパーリンクを作成できます。
``[表示名]``は省略できます。
``http://``や``https://``で始まる文字列は自動でリンクに変換されます。

:::{note}

Markdownのリンクの書き方と要素は同じですが、順番が逆になっています。

```md
// .md
[表示名](URL)
```

```text
// .typ
#link(URL)[表示名]
```

すぐに間違えそう。

:::

:::{seealso}

- [](../latex/latex-hyperref.md)

:::
