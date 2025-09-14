# 箇条書きしたい（`#list`）

```typst
// ページ全体で設定
#set list(
    indent: 1.2em,
    body-indent: 0.5em,
    spacing: 1em
)
```

```typst
// 個別設定
#list(オプション)[りんご][ばなな][ぶどう]
```

```typst
// Typst記法
- りんご
  - あか
- ばなな
  - きいろ
- ぶどう
  - むらさき
```

:::{seealso}

- [list | Element | Typst](https://typst.app/docs/reference/model/list/)

:::

## 箇条書きしたい（`#enum`）

```typst
// ページ全体で設定
#set enum(
    indent: 1.2em,
    body-indent: 0.5em,
    spacing: 1em
)
```

```typst
// 個別設定
#enum(オプション)[りんご][ばなな][むらさき]
```

```typst
// Typst記法
+ りんご
  - あか
+ ばなな
  - きいろ
+ ぶどう
  - むらさき
```

:::{seealso}

- [enum | Element | Typst](https://typst.app/docs/reference/model/enum/)

:::

## 説明リストしたい（``#terms``）

```text
/ 単語: 説明
/ りんご: あか
/ ばなな: きいろ
/ ぶどう: むらさき
/ 複数行: 説明は改行しても
 先頭にスペースをいれたら
 ひとつづきにできるよ

#set terms(オプション)
#terms.item[単語][説明]
#terms.item[りんご][あか]
#terms.item[ばなな][きいろ]
#terms.item[ぶどう][むらさき]
#terms.item[複数行][説明は改行しても先頭にスペースをいれたらひとつづきにできるよ]
```
