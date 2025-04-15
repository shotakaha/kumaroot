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

## 行データを追加したい（`appendRow`）

```js
// データのカラム数と同じ要素の配列を作成
const data = ["A", "B", "C", "D"];
// データをシート末尾に追記
sheet.appendRow(data);
```

`appendRow`で既存のシート末尾にデータを追加できます。

:::{note}

`appendRow`の処理は時間がかかるので、大量のデータを追加する場合は、
配列で作成し`setValues`で書き出すほうがよいです。

:::

## データを削除したい（`deleteRow`）

```js
// 2行目を削除
sheet.deleteRow(2);
```

`deleteRow`で行番号を指定してデータを削除できます。

## データを削除したい（`clearContent`）

```js
// 範囲を指定して削除
const range = sheet.getRange("A2:D6");
range.clearContent();
```

`clearContent`で指定したセル範囲のデータを削除できます。

## シート名を変更したい（``setName``）

```js
sheet.setName("変更後のシート名");
```

`setName`でシート名を変更できます。
同じ名前のシートは作れません。

## シートを保護したい（``protect``）

```js
// シート全体を保護
const protection = sheet.protect()

// セル範囲を保護
const range = sheet.getRange("A2:D6");
const protection = range.protect()

// 保護の理由を追加
protection.setDescription("説明")
```

`protect`でシートや選択したセルを保護できます。
`setDescription`で保護の理由を追加できます。

## リファレンス

- [Class Spreadsheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)
- [Spreadsheet.getSheetByName](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheetbynamename)
- [Spreadsheet.insertSheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#insertsheetsheetname)
- [Spreadsheet.getSheets](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheets)
