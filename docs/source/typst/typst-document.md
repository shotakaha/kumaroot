# メタデータしたい（``document``）

```typst
#set document(
  title: [すごいタイトル],
  author: ("すごい著者"),
  description: [すごい説明],
  keywords: (),
  date: auto,
)
```

[document要素](https://typst.app/docs/reference/model/document/)は、文書の全体のメタデータを設定できます。
このメタデータはPDFファイルなどに埋め込まれる情報で、本文には表示されません。

ユーザーが独自の`document`要素を作ることはできず、setルール（`#set document`）の形でのみ設定できます。

## タイトルしたい（`title`）

```typst
#set document(
  title: [文書全体のタイトル]
)
```

`title`オプションで、文書のタイトルを埋め込むことができます。
コンテンツブロックで指定できるので、マークアップしたタイトルや改行付きのタイトルも設定できます。

:::{note}

マークアップしたタイトルがPDFにどのように埋め込まれるのかは気になります（ただ調べてないだけ）。

:::

## 著者したい（`author`）

```typst
#set document(
  author: ("著者1", "著者2")
)
```

`author`オプションで、文書の著者情報を埋め込むことができます。
配列で指定できるので、複数の著者を設定できます。

## 説明したい（`description`）

```typst
#set document(
  description: [文書全体の説明]
)
```

`description`オプションで文書の説明を埋め込むことができます。

## キーワードしたい（`keywords`）

```typst
#set document(
  keywords: ("キーワード1", "キーワード2")
)
```

`keywords`オプションで、文書のキーワードを埋め込むことができます。

## 日付したい（`date`）

```typst
#set document(
  date: datetime(year: 2026, month: 1, day: 17)
)
```

`date`オプションで、文書の作成日を埋め込むことができます。
デフォルトは`auto`になっていて、ビルド時の日付が適用されます。
`datetime`オブジェクトを使用して、特定の日付を設定できます。

## リファレンス

- [document - Typst](https://typst.app/docs/reference/model/document/)
