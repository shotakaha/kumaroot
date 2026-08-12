# スプレッドシートを作りたい（`create`）

```js
// シート名のみ指定
const book1 = SpreadsheetApp.create("スプレッドシート名");

// 行数・列数も指定
const book2 = SpreadsheetApp.create("スプレッドシート名", 10, 5);
```

`SpreadsheetApp.create`メソッドでスプレッドシートを新規作成できます。
作成直後のスプレッドシートには、`シート1`という名前のシートが1枚だけ入っています。

```js
const book = SpreadsheetApp.create("スプレッドシート名");
const id = book.getId();
const name = book.getName();
const url = book.getUrl();

const sheet = book.getActiveSheet();
const nrows = sheet.getLastRow();
const ncols = sheet.getLastColumn();
```

`getId` / `getName` / `getUrl`は`Spreadsheet`（ブック）のメソッドですが、
`getLastRow` / `getLastColumn`は`Sheet`のメソッドです。
行数・列数を確認したいときは、`getActiveSheet`などでシートを取得してから呼び出してください。
