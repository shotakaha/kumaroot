# スプレッドシートを作りたい（`create`）

```js
const book = SpreadsheetApp.create("スプレッドシート名");
```

`SpreadsheetApp.create`メソッドでスプレッドシートを新規作成できます。
作成直後のスプレッドシートには、`シート1`という名前のシートが1枚だけ入っています。

## 行数・列数を指定して作りたい（`create`）

```js
const book = SpreadsheetApp.create("スプレッドシート名", 10, 5);
```

`SpreadsheetApp.create`の第2・第3引数で、初期状態の行数・列数を指定できます。

## 作成直後のブック・シートを確認したい

```js
const book = SpreadsheetApp.create("スプレッドシート名");
const id = book.getId();
const name = book.getName();
const url = book.getUrl();

const sheet = book.getActiveSheet();
const lastRow = sheet.getLastRow();
const lastCol = sheet.getLastColumn();
```

`getId` / `getName` / `getUrl`はブック（`Spreadsheet`）のメソッドですが、
`getLastRow` / `getLastColumn`はシート（`Sheet`）のメソッドです。
シートの情報を確認したいときは、`getActiveSheet`などでシートを取得してから呼び出してください。
ブック・シートの操作については
[ブックを操作したい](./gas-spreadsheet-book.md)、
[シートを操作したい](./gas-spreadsheet-sheet.md)
を参照してください。

## リファレンス

- [SpreadsheetApp.create](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app#createname)
