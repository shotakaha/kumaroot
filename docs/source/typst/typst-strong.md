# 強調したい（`#strong` / `#emph`）

```typst
#strong[本文]
#emph[本文]
```

[#strong](https://typst.app/docs/reference/model/strong/)もしくは[#emph](https://typst.app/docs/reference/model/emph/)を使ってテキストを強調できます。

:::{note}

`#strong`は**太字（ボールド）**、
`#emph`は __斜体（イタリック）__
で強調します。

和文の場合は `#strong` を使えばよいと思います。

:::

## ウェイトしたい（`delta`）

```typst
#strong(delta: 500)[強調したい文章]
```

`delta`オプションで、ウェイトを変更できます。
現在のウェイトからの差分で指定します。
デフォルトは300です。

## 文字色したい

```typst
#show strong: set text(red)

#show strong: it => {
  text(red, it.body)
}
```

`show`ルールで文字色を変更します。

## 数字の色を変更したい

```typst
#set regex("\d"): text(blue)
```

``#set regex``で正規表現を使って、色を変更する箇所を指定できます。
上記サンプルでは数字を青色に変更しています。

:::{seealso}

- [](../latex/latex-xcolor.md)

:::
