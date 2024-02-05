# タイトルしたい（``document``）

```typst
#let title = "すごいタイトル"

// 中央揃え
#align(center)[#title]

#align(center)[
    #text(size: 2em)[
        #title
        ]
    ]
```

タイトルを中央に寄せました。

## 著者したい

```typst
#let authors = ("すごい著者1", "すごい著者2)
#authors
```

## メタデータしたい

```typst
#set document(
    title: "すごいタイトル",
    author: ("すごい著者",
    keywords: (),
    date: auto,
)
```

[document要素](https://typst.app/docs/reference/model/document/)で、文書のメタデータを設定できます。
この情報は、PDFのメタデータなどに利用されます。
ドキュメントには表示されません。
