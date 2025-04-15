# ブック操作したい（`Spreadsheet`）

```js
const book = SpreadsheetApp.getActiveSpreadsheet();
const book = SpreadsheetApp.openById("スプレッドシートのID");
const book = SpreadsheetApp.openByUrl("スプレッドシートのURL");
```

`Spreadsheet`はスプレッドシート全体を管理するオブジェクトです。
サンプルコードでは`ss`が使われますが、僕は`book`という変数名を使います。

## 現在のスプレッドシートを開きたい（`getActiveSpreadsheet`）

```js
const book = SpreadsheetApp.getActiveSpreadsheet();
Logger.log(`name: ${book.getName()}`);
Logger.log(`ID: ${book.getId()}`);
Logger.log(`URL: ${book.getURL}`);
```

`SpreadsheetApp.getActiveSpreadsheet()`で、
スクリプトがバインドされているスプレッドシートを取得できます。

## スプレッドシートを開きたい（`openById` / `openByUrl`）

```js
// IDを指定する
const book = SpreadsheetApp.openById("スプレッドシートのID");

// URLを指定する
const book = SpreadsheetApp.openByUrl("スプレッドシートのURL");
```

`SpreadsheetApp.openById`でIDを指定してスプレッドシートを取得できます。
スタンドアロンなスクリプトや、他のスクリプトからも開くことができるため、
非常によく使うメソッドのひとつです。

また、`SpreadsheetApp.openByUrl`でURLを直接指定してスプレッドシートを取得できます。

## シートを取得したい（`getSheetByName`）

```js
const sheet = book.getSheetByName("シート名") || book.insertSheet("シート名");
```

`getSheetByName`でシート名を指定してシートを取得できます。

## シートを追加したい（`insertSheet`）

```js
const newSheet = book.insertSheet("新しいシート名");
```

`insertSheet`で新しいシートを作成できます。

```js
const sheetName = "シート名"
const sheet = book.getSheetByName(sheetName) || book.insertSheet(sheetName);
```

上のように、シートが存在しない場合に新しく作る、というパターンでよく使います。

## すべてのシートを取得したい（`getSheets`）

```js
const sheets = book.getSheets();
const nSheets = sheets.length
Logger.log("シートの数: " + nSheets);
sheets.forEach(sheet => {
    Logger.log(sheet.getName());
    // その他のsheetに対する処理
})
```

`getSheets`でスプレッドシートにあるすべてのシートの配列を取得できます。
この配列の要素数（`.length`）でシートの数を確認できます。
また、この配列に対して`forEach`でループ処理できます。

## シートを削除したい（`deleteSheet`）

```js
const sheetToDelete = book.getSheetByName("不要なシート名");
book.deleteSheet(sheetToDelete);
```

`deleteSheet`でシートを削除できます。
引数な`Sheet`オブジェクトです。
名前（`String`）ではない点に気をつけてください。

## 共同編集したい（`addEditor` / `removeEditor`）

```js
book.addEditor("someone@example.com");
book.removeEditor("someone@example.com");
```

`addEditor`でアクセス権を付与できます。
`removeEditor`でアクセス権を削除できます。
