# セレクターしたい（`#show: ...where`）

特定の条件を満たす要素だけをスタイリングしたいときは、`.where` メソッドを使ってセレクターを絞り込みます。

## 基本的な使い方

### 見出しのレベル別スタイリング

レベル1の見出しは中央揃え、レベル2は赤色にしたいとき：

```typst
// レベル1の見出しを中央揃え
#show heading.where(level: 1): set align(center)

// レベル2の見出しを赤色
#show heading.where(level: 2): set text(red)
```

### コードブロックの種類別スタイリング

インラインコード（`code`）とブロックコード（```code```）を別々にスタイリング：

```typst
// インラインコードのスタイル
#show raw.where(block: false): box.with(
  fill: luma(240),
  inset: (x: 3pt, y: 0pt),
  radius: 2pt,
)

// ブロックコードのスタイル
#show raw.where(block: true): block.with(
  fill: luma(240),
  inset: 10pt,
  radius: 4pt,
)
```

## `where`メソッドとは

:::{note}

`.where` は、要素のプロパティに基づいて**条件付きで要素を選択**するメソッドです。

- `heading.where(level: 1)` は「レベルが1の見出しのみ」という意味のセレクターを返します
- `#show:` で左側（セレクター側）に使用して、特定の条件を満たす要素だけに処理を適用します
- `with` メソッドとの違い：`where` は選択・フィルタリング、`with` は引数の事前設定です

:::

## よくある使用シーン

### シーン1: 見出しの階層的スタイリング

```typst
// レベル1: 中央揃え、大きめ
#show heading.where(level: 1): it => {
  set align(center)
  set text(size: 14pt, weight: "bold")
  it.body
}

// レベル2: 斜体
#show heading.where(level: 2): it => {
  text(style: "italic", it.body + [.])
}

// レベル3以降: スタイルなし
#show heading.where(level: 3): set heading(numbering: none)
```

### シーン2: 図表の自動リスト生成

```typst
// 画像のリストだけを作成
#outline(
  title: [図一覧],
  target: figure.where(kind: image),
)

// 表のリストだけを作成
#outline(
  title: [表一覧],
  target: figure.where(kind: table),
)
```

### シーン3: ページヘッダーで動的に見出しを表示

```typst
#set page(header: context {
  // 現在位置より前のレベル1見出しを取得
  let headings = query(
    heading.where(level: 1).before(here())
  )
  if headings.len() > 0 {
    let current = headings.last()
    emph(current.body)
  }
})
```

## 利用可能な要素と条件

### heading要素

- `level`: 見出しレベル（1, 2, 3など）
- `outlined`: アウトラインに含めるか
- `numbering`: ナンバリング形式

### raw要素（コード）

- `block`: ブロックコード（true）またはインラインコード（false）
- `lang`: 言語の指定（"python"、"rust"など）

### figure要素（図表）

- `kind`: 図表の種類（image, table など）
- `caption`: キャプションの有無

## `where` と `with` の組み合わせ

`.where` でセレクターを絞り込み、`.with` で関数の引数を事前設定する例：

```typst
// ブロックコード（block: true）に fill と inset を設定
#show raw.where(block: true): block.with(
  fill: luma(240),
  inset: 10pt,
  radius: 4pt,
)
```

この場合：

- `.where(block: true)` で「ブロックコードのみ」を選択
- `.with(...)` で `block` 関数の引数を事前設定
- 結果として、ブロックコードに統一されたスタイルが自動適用されます

## より複雑な条件

複数のプロパティを組み合わせることも可能です：

```typst
// レベル1で、アウトラインに含まれる見出しのみ
let chapters = query(
  heading.where(
    level: 1,
    outlined: true,
  )
)
```
