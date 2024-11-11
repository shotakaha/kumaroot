# シートを開きたい（`getSheetByName`）

```js
const book = SpreadsheetApp.getActiveSpreadsheet();
const sheetName = "シート名";
const sheet = book.getSheetByName(sheetName);

Logger.log(`シート名: ${sheet.getName()}`);
Logger.log(`シート名: ${sheet.getSheetName()}`);
Logger.log(`シートID: ${sheet.getSheetId()}`);
Logger.log(`シートのインデックス: ${sheet.getIndex()}`);
```

`Spreadsheet.getSheetByName`でシート名を指定してシートを取得できます。

## シートを追加したい（`insertSheet`）

```js
function getOrInsertSheet() {
    const book = SpreadsheetApp.getActiveSpreadsheet();
    const sheetName = "シート名";
    const sheet = book.getSheetByName(sheetName) || book.insertSheet(sheetName);
    return sheet;
};
```

`Spreadsheet.insertSheet`でシートを追加できます。

## すべてのシートを取得したい（`getSheets`）

```js
const book = SpreadsheetApp.getActiveSpreadsheet();
const sheets = book.getSheets();
Logger.log(sheets.length);

for (const sheet of sheets) {
    Logger.log(sheet.getName());
}
```

``Spreadsheet.getSheets``（複数形）で複数のシートを配列として取得できます。

## リファレンス

- [Class Spreadsheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)
- [Spreadsheet.getSheetByName](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheetbynamename)
- [Spreadsheet.insertSheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#insertsheetsheetname)
- [Spreadsheet.getSheets](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheets)
