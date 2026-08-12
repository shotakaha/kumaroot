# ピボットテーブルを操作したい（`PivotTable`）

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

## ピボットテーブルを作成したい（`createPivotTable`）

```js
// ピボットテーブルに使用する範囲
const readRange = readSheet.getRange("A1:D10");

// ピボットテーブルを出力するセルを選択
const pivotRange = writeSheet.getRange("A1");

// （空の）ピボットテーブルを作成
const pivotTable = pivotRange.createPivotTable(readRange);

// 行グループを追加（1列目）
pivotTable.addRowGroup(1);

// 列グループを追加（2列目）
pivotTable.addColumnGroup(2);

// ピボット値を追加（3列目をCOUNTAで集計）
const method = SpreadsheetApp.PivotTableSummarizeFunction.COUNTA;
pivotTable.addPivotValue(3, method);

// フィルターを追加（4列目が空でない行のみ表示）
const criteria = SpreadsheetApp.newFilterCriteria().whenCellNotEmpty().build();
pivotTable.addFilter(4, criteria);
```

`createPivotTable`メソッドで、ピボットテーブルを作成できます。
作成するときに、**使用するデータの範囲** と **ピボットテーブルを出力するセル** の`Range`オブジェクトの指定が必要です。

:::{note}

ピボットテーブルは、利用するデータ範囲と同じシートに作成できます。
そのときは、選択したデータ範囲と重ならないようにする必要があります。

```js
const readRange = readSheet.getRange("A1:D10");

// 行方向に作成する場合
const lastRow = readSheet.getLastRow();
const pivotRange = readSheet.getRange(lastRow + 2, 1);

// 列方向に作成する場合
const lastCol = readSheet.getLastColumn();
const pivotRange = readSheet.getRange(1, lastCol + 2);
```

`Sheet.getLastRow`や`Sheet.getLastColumn`を使って、
出力範囲の選択を自動化できます。

:::

## 行や列を追加したい（`addRowGroup` / `addColumnGroup`）

```js
const rowGroup = pivotTable.addRowGroup(1);
const colGroup = pivotTable.addColumnGroup(2);
```

`PivotTable.addRowGroup`で行グループ、
`PivotTable.addColumnGroup`で列グループを追加できます。

引数には対象カラムの列番号（1はじまり）を渡します。
ひとつの`PivotTable`に対して複数の行グループ／列グループを追加できます。

返り値は`PivotGroup`オブジェクトが新規作成されます。
このオブジェクトに対してソートしたり、総計を表示したり、設定できます。

## ピボット値を追加したい（`addPivotValue`）

```js
const headers = ["カラム1", "カラム2", "カラム3", "カラム4"];
const col = "カラム2";
const index = headers.indexOf(col) + 1;
const method = SpreadsheetApp.PivotTableSummarizeFunction.COUNTA;
pivotTable.addPivotValue(index, method);
```

## フィルターを追加したい（`addFilter`）

```js
const headers = ["カラム1", "カラム2", "カラム3", "カラム4"];
const col = "カラム3";
const index = headers.indexOf(col) + 1;
const criteria = SpreadsheetApp.newFilterCriteria().whenCellNotEmpty().build();
pivotTable.addFilter(index, criteria);
```

`addFilter`でフィルターを追加できます。
フィルター条件は[](./gas-spreadsheet-filter.md)を参考に`FilterCriteria`オブジェクトを作成します。

## 行グループ／列グループの表示順や名前を変更したい（`PivotGroup`）

```js
const rowGroup = pivotTable.addRowGroup(1);

// 降順に並び替え
rowGroup.sortDescending();

// 表内に合計値を表示
rowGroup.showTotals(true);

// 表示名を変更
rowGroup.setDisplayName("集計項目");
```

`addRowGroup` / `addColumnGroup`が返す`PivotGroup`オブジェクトを操作して、
表示順や合計表示、表示名などを設定できます。

## 日時を集計したい（`PivotGroup.setDateTimeGroupingRule`）

```js
const headers = ["タイムスタンプ", "カラム2", "カラム3"];
const index = headers.indexOf("タイムスタンプ") + 1;

const pivotRow = pivotTable.addRowGroup(index);
const byHour = SpreadsheetApp.DateTimeGroupingRuleType.HOUR;
pivotRow.setDateTimeGroupingRule(byHour);
pivotRow.setDisplayName("時刻");

const pivotCol = pivotTable.addColumnGroup(index);
const byDay = SpreadsheetApp.DateTimeGroupingRuleType.DAY_OF_WEEK;
pivotCol.setDateTimeGroupingRule(byDay);
pivotCol.setDisplayName("曜日");

const method = SpreadsheetApp.PivotTableSummarizeFunction.COUNTA;
const pivotVal = pivotTable.addPivotValue(index, method);
```

`PivotGroup.setDateTimeGroupingRule`で日時データをグルーピングできます。
設定値は`SpreadsheetApp.DateTimeGroupingRuleType`の中で定義されている値から選択します。

:::{note}

日時でないカラムを渡してもエラーはでません。

:::

## ヒストグラムにしたい（`PivotGroup.setHistogramGroupingRule`）

```js
// 3列目の値を、0〜100の範囲で10刻みのビンに分ける
const pivotRow = pivotTable.addRowGroup(3);
pivotRow.setHistogramGroupingRule(0, 100, 10);
```

`PivotGroup.setHistogramGroupingRule`で行グループ／列グループを、任意のビン数でヒストグラム（度数分布）にできます。
行／列に指定したカラムの値が連続値の場合にとても便利です。

## リファレンス

- [Class PivotTable](https://developers.google.com/apps-script/reference/spreadsheet/pivot-table)
- [Class PivotGroup](https://developers.google.com/apps-script/reference/spreadsheet/pivot-group)
- [Class PivotValue](https://developers.google.com/apps-script/reference/spreadsheet/pivot-value)
- [Class FilterCriteriaBuilder](https://developers.google.com/apps-script/reference/spreadsheet/filter-criteria-builder)
