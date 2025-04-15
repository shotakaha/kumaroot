# シート操作したい（`Sheet`）

```js
const book = SpreadsheetApp.getActiveSpreadsheet();
const sheet = book.getActiveSheet();
```

`Sheet`オブジェクトで単一のシートを操作できます。

## シートの情報を確認したい

```js
const id = sheet.getId();
const name = sheet.getName();
const sheetName = sheet.getSheetName();

const index = sheet.getIndex();
const lastRow = sheet.getLastRow();
const lastCol = sheet.getLastColumn();
```

## リファレンス

- [Class Spreadsheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)
- [Spreadsheet.getSheetByName](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheetbynamename)
- [Spreadsheet.insertSheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#insertsheetsheetname)
- [Spreadsheet.getSheets](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheets)
