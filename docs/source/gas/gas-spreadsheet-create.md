# スプレッドシートを作りたい（`create`）

```js
const book = SpreadsheetApp.create("スプレッドシート名");
const book = SpreadsheetApp.create("スプレッドシート名", 行数, 列数);

const id = book.getId();
const name = book.getName();
const url = book.getUrl();
const nrows = book.getLastRow();
const ncols = book.getLastColumn();
```

`SpreadsheetApp.create`メソッドでスプレッドシートを新規作成できます。
