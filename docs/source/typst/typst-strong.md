# 強調したい（``#strong``）

```text
#strong[本文]
#emph[本文]
```

[#strong](https://typst.app/docs/reference/model/strong/)もしくは[#emph](https://typst.app/docs/reference/model/emph/)を使ってテキストを強調できます。

## 文字色したい

```text
#show strong: set text(red)
```

強調したいときに、文字色を変更したり、下線を引いたりしたい場合は表示ルールを設定します。

## 数字の色を変更したい

```typst
#set regex("\d"): text(blue)
```

``#set regex``で正規表現を使って、色を変更する箇所を指定できます。
上記サンプルでは数字を青色に変更しています。

:::{seealso}

- [](../latex/latex-usepackage-xcolor.md)

:::
