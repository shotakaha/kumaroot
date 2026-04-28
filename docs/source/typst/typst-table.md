# 表したい（`#table`）

```typst

// | セル1 | セル2 | セル3 |
// | --- | --- | --- |
// | セル4 | セル5 | セル6 |
// | セル7 | セル8 | セル9 |

// 関数マークアップ
#table(
  columns: (1fr, auto, auto),
  inset: 1em,
  align: horizon,
  table.header(
    [セル1][セル2][セル3]
  ),
  [セル4],
  [セル5],
  [セル6],
  [セル7],
  [セル8],
  [セル9],
)
```

`table`関数で表をマークアップできます。
`columns`オプションで、列の幅を指定できます。
`table.header`関数で表の見出しを指定できます。

## 表を設定したい（`#set table`）

```typst
#set table(
  stroke: (x, y) => {
    let thick: 2pt
    let thin: 0.5pt
    (
      top: if y == 0 or y == 1 { thick } else { thin },
      bottom: thick,
      left: none,
      right: none,
    )
  },
  inset: 1em,
)
```

setルール（`set table(...)`）で、表全体のスタイルを変更できます。
デフォルトでは、表全体に縦横の罫線が引かれています。
上記のサンプルは、横罫線のみに変更し、見出しの上下と一番下の罫線を太くしています。
学術論文では、このような横罫線だけの表が好まれることが多いです。

## 表を装飾したい（`#show table`）

```typst
#show table.cell.where(y: 0): set text(weight: bold)
```

`show`ルールで、表の特定のセルや行、列を装飾できます。
上記のサンプルは、見出し行（`y: 0`）を太字にしています。

## 表キャプションしたい（`figure` / `figure.caption`）

```typst
#figure(
  #table(...),
  caption: [表のキャプション],
  <fig-table>
)
```

表キャプションは、`figure`要素の`caption`オプションで設定できます。
デフォルトのスタイルは、図版のキャプションと同じですが、`show`ルールで変更できます。

:::{seealso}

- [](./typst-figure.md)

:::



## リファレンス

- [table](https://typst.app/docs/reference/model/table/)
