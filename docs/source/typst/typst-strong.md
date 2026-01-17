# 強調したい（`#strong` / `#emph`）

```typst
*太字で強調* する部分と
_斜体で強調_ する部分です。
```
`*`で**太字（ボールド）**、
`_`で__斜体（イタリック）__、
で強調表示できます。

:::{caution}

Markdown記法では、
太字は`**`、
斜体は`__`です。
互換性がないので注意してください。

:::

## 太字したい（`#strong`）

```typst
ここは #strong[太字で強調] できます
```

[#strong](https://typst.app/docs/reference/model/strong/)関数で、
指定した文字列を**太字で強調**できます。

## 斜体したい（`#emph`）

```typst
ここは #emph[斜体で強調] できます。
```

[#emph](https://typst.app/docs/reference/model/emph/)関数で、
指定した文字列を__斜体で強調__できます。

:::{note}

和文ドキュメントの場合は
`#strong`
を使えばよいです。

:::

## さらに太字したい（`#strong.delta`）

```typst
ここは #strong[太字にした文字列] です。
ここは #strong(delta: 900)[さらに太くした文字列] です。
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
