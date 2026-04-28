# 強調したい（`#strong` / `#emph`）

```typst
// 簡易マークアップ
*太字で強調* したテキストです。
_斜体で強調_ したテキストです。

// 関数マークアップ
#strong[太字で強調] したテキストです。
#emph[斜体で強調] したテキストです。
```

`*`で **太字（ボールド）** 、
`_`で __斜体（イタリック）__ 、
で強調表示できます。

:::{caution}

Markdown記法では、
太字は`**`、
斜体は`__`です。
互換性がないので注意してください。

:::

## 太字したい（`#strong`）

```typst
ここは #strong[太字で強調した] テキストです。
ここは #strong(delta: 900)[さらに太くして強調した] テキストです。
```

[#strong](https://typst.app/docs/reference/model/strong/)関数で、
指定した文字列を**太字で強調**できます。
`delta`オプションで、ウェイトを変更できます。
ウェイトは現在からの差分で指定します。
デフォルトは300です。

## 斜体したい（`#emph`）

```typst
ここは #emph[斜体で強調した] テキストです。
```

[#emph](https://typst.app/docs/reference/model/emph/)関数で、
指定した文字列を __斜体で強調__ できます。
本文のフォントが斜体（"italic" or "oblique"）の場合は、常体で表示されます。

:::{note}

和文フォントには基本的に斜体の字形がないため、
太字（`strong`）で強調するのがよいと思います。

:::

## 強調の文字色したい

```typst
// 文中で適用
ここは#strong[text(red, 赤色の文字で強調した)] テキストです。

// 全体に適用
#show strong: set text(red)

// 上と同じ
#show strong: it => {
  text(red, it.body)
}
```

`show`ルールで強調するときの文字色を変更できます。

## 数字の色を変更したい

```typst
#set regex("\d"): text(blue)
```

`#set regex`で正規表現を使って、色を変更する箇所を指定できます。
上記サンプルでは数字（`\d`）を青色に変更しています。

:::{seealso}

- [](../latex/latex-xcolor.md)

:::
