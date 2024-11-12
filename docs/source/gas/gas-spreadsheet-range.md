# セル操作したい（`Range`）

```js
const range = sheet.getRange("A1:C3");
range.setFontColorObject("#fff");
range.setBackgroundbject("#000");
```

`Range`オブジェクトで、シート上の選択した範囲に対して操作できます。

## すべてのデータを選択したい（`getDataRange`）

```js
// すべてのデータの範囲
const range = sheet.getDataRange()

// 見出しを除外したデータの範囲
const range = sheet.getDataRange.slice(1);

// 別の選択方法
const nrows = sheet.getLastRow();
const ncols = sheet.getLastColumns();
const range = sheet.getRange(2, 1, nrows, ncols);
```

`Sheet.getDataRange`で、シート上のデータが存在する範囲をすべて選択できます。
データに見出しを含みたくない場合は``slice(1)``するとよいです。

## セル選択したい（`getRange`）

```js
const range = sheet.getRange("セル番地");
const range = sheet.getRange("行番号", "列番号");
const range = sheet.getRange("セル番地:セル番地");
const range = sheet.getRange("行番号", "列番号", "行数");
const range = sheet.getRange("行番号", "列番号", "行数", "列数");
```

`Sheet.getRange`で、セル名や番地（行番号と列番号）を使ってセル（の範囲）を選択できます。

## リファレンス

- [Sheet.getDataRange](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getdatarange)
- [Sheet.getRange](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getrangerow,-column)
