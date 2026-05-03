# 箇条書きしたい（`#list` / `#enum` / `#terms`）

```typst
// Typst記法
- りんご
  - あか
- ばなな
  - きいろ
- ぶどう
  - むらさき
```

番号なしリストのマークアップには`-`を使います。

```typst
// Typst記法
+ りんご
  - あか
+ ばなな
  - きいろ
+ ぶどう
  - むらさき
```

番号ありリストのマークアップには`+`を使います。

```text
/ 単語: 説明
/ りんご: あか
/ ばなな: きいろ
/ ぶどう: むらさき
/ 複数行: 説明は改行しても
 先頭にスペースをいれたら
 ひとつづきにできるよ
```

説明付きリストのマークアップには`/`を使います。

## 番号なしの箇条書きしたい（`#list`）

```typst
// 簡易マークアップ
- りんご
- ばなな
- ぶどう

// 関数マークアップ
#list[りんご][ばなな][ぶどう]
```

番号なしリストのマークアップは
`#list`要素のエイリアスです。

```typst
// ページ全体で設定
#set list(
  body-indent: 0.5em,
  indent: 1em,
  spacing: 1em,
)
```

:::{seealso}

- [list | Element | Typst](https://typst.app/docs/reference/model/list/)
- [](../latex/latex-itemize.md)
:::

## 番号ありの箇条書きしたい（`#enum`）

```typst
// 簡易マークアップ
+ りんご
+ ばなな
+ ぶどう

// 関数マークアップ
#enum[りんご][ばなな][ぶどう]
```

番号ありリストのマークアップは
`#enum`要素のエイリアスです。

```typst
// ページ全体で設定
#set enum(
  body-indent: 0.5em,
  indent: 1em,
  spacing: 1em
)
```

:::{seealso}

- [enum | Element | Typst](https://typst.app/docs/reference/model/enum/)
- [](../latex/latex-enumerate.md)

:::

## 説明付きリストしたい（`#terms`）

```typst
// 簡易マークアップ
/ りんご: あか
/ ばなな: きいろ
/ ぶどう: むらさき

// 関数マークアップ
#terms.item[りんご][あか]
#terms.item[ばなな][きいろ]
#terms.item[ぶどう][むらさき]
```

説明付きリストのマークアップは
`#terms`要素のエイリアスです。
個人的には`/`より`#terms.item`を使う方がわかりやすくてよいと思います。

```typst
#set terms(
  body-indent: 0.5em,
  indent: 1em,
  spacing: 1em
)

#terms.item[単語][説明]
#terms.item[りんご][あか]
#terms.item[ばなな][きいろ]
#terms.item[ぶどう][むらさき]
#terms.item[複数行][説明は改行しても先頭にスペースをいれたらひとつづきにできるよ]
```

:::{seealso}

- [terms | Element | Typst](https://typst.app/docs/reference/model/terms/)
- [](../latex/latex-description.md)

:::
