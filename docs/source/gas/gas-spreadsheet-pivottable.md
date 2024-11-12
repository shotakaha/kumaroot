# ピボットテーブルしたい（`PivotTable`）

スプレッドシートのデータを整理するとき、ピボットテーブルはとても便利です。

1. データを選択する
2. `[挿入]` → `[ピボットテーブル]`
3. `[挿入先]`を選択
   - 新しいシート
   - 既存のシート → 挿入先のセルを選択
4. 「行」を追加
5. 「列」を追加
6. 「値」を追加
7. 「フィルタ」を追加

データを多角的に確認したい場合は、同じデータに対して、
複数のピボットテーブルを作成することもあります。

## 行を追加したい（`addRowGroup`）

```js
const headers = ["カラム1", "カラム2", "カラム3", "カラム4"];
const row = {name: "カラム1", order: "descending" };
const index = headers.indexOf(row.name);
const pivotRowGroup = pivotTable.addRowGroup(index);
if (row.order === "descending") {
    // 降順に並べる
    pivotRowGroup.sortDescending();
};
```

`PivotTable.addRowGroup`で行グループを追加できます。
引数にインデックスを指定する必要があるため、見出し行に対して`indexOf`して取得するとよいです。

返り値は`PivotGroup`オブジェクトが新規作成されます。
このオブジェクトに対してソートしたり、
総計を表示したり、設定できます。

## 列を追加したい（`addColumnGroup`）

```js
const headers = ["カラム1", "カラム2", "カラム3", "カラム4"];
const col = "カラム2";
const index = headers.indexOf(col);
pivotTable.addColumnGroup(index);
```

`PivotTable.addColumnGroup`で列グループを追加できます。
引数にインデックスを指定する必要があるため、
見出し行に対して`indexOf`して取得するとよいです。

## リファレンス

- [Class PivotTable](https://developers.google.com/apps-script/reference/spreadsheet/pivot-table)
- [Class PivotGroup](https://developers.google.com/apps-script/reference/spreadsheet/pivot-group)
- [Class PivotValue](https://developers.google.com/apps-script/reference/spreadsheet/pivot-value)
