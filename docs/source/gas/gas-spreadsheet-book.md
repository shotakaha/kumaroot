# ブックを操作したい（`Spreadsheet`）

```js
const book = SpreadsheetApp.openById("スプレッドシートのID");
const book = SpreadsheetApp.openByUrl("スプレッドシートのURL");

// アクティブなブックを取得（バインドスクリプトの場合）
const book = SpreadsheetApp.getActiveSpreadsheet();
```

`Spreadsheet`はブック全体を管理するオブジェクトです。
公式リファレンスやサンプルコードでは変数名に`ss`が使われますが、
このドキュメントでは`book`という変数名を使います。

## ブックを開きたい（`openById` / `openByUrl`）

```js
// IDを指定する
const book = SpreadsheetApp.openById("スプレッドシートのID");

// URLを指定する
const book = SpreadsheetApp.openByUrl("スプレッドシートのURL");
```

`SpreadsheetApp.openById`でIDを指定してブックを取得できます。
また、`SpreadsheetApp.openByUrl`でURLを直接指定してブックを取得できます。

スタンドアロンスクリプトや、他のスクリプトからも開くことができるため、
非常によく使うメソッドのひとつです。

:::{hint}

URL: `https://docs.google.com/spreadsheets/d/【ID】/edit`

ブックのURLの書式は上記のとおりです。
`【ID】`のランダムな文字列がIDです。

:::

## 現在のブックを開きたい（`getActiveSpreadsheet`）

```js
// バインドスクリプトの場合
const book = SpreadsheetApp.getActiveSpreadsheet();
Logger.log(`name: ${book.getName()}`);
Logger.log(`ID: ${book.getId()}`);
Logger.log(`URL: ${book.getUrl()}`);
```

`SpreadsheetApp.getActiveSpreadsheet()`で、現在アクティブになっているブックを取得できます。
ただし、コンテナバインドスクリプトからしか使えません。
スタンドアロンスクリプトの場合は、`openById`や`openByUrl`を使ってください。

## ブックを共同編集したい（`addEditor` / `removeEditor`）

```js
book.addEditor("someone@example.com");
book.removeEditor("someone@example.com");
```

`SpreadsheetApp.addEditor`で、ブックに対するアクセス権を付与できます。
反対に`SpreadsheetApp.removeEditor`でアクセス権を削除できます。

## ブック全体を複製したい（`copy`）

```js
const book = SpreadsheetApp.openById("コピー元のID");
const copied = book.copy("コピー先のファイル名");
```

`SpreadsheetApp.copy`メソッドでブック全体を複製できます。
新しいブックが作成されるため、URLも新規発行されます。

## シートを取得したい（`getSheetByName`）

```js
const sheet = book.getSheetByName("シート名");
```

`getSheetByName`でシート名を指定してシートを取得できます。
指定した名前のシートが存在しない場合は`null`が返ります。

## シートを追加したい（`insertSheet`）

```js
const newSheet = book.insertSheet("新しいシート名");
```

`SpreadsheetApp.insertSheet`で新しいシートを作成できます。

```js
const sheetName = "シート名";
const sheet = book.getSheetByName(sheetName) || book.insertSheet(sheetName);
```

`getSheetByName`と組み合わせて、シートが存在しない場合だけ新しく作る、
というパターンでよく使います。

## すべてのシートを取得したい（`getSheets`）

```js
const sheets = book.getSheets();
const nSheets = sheets.length;
Logger.log("シートの数: " + nSheets);
sheets.forEach(sheet => {
    Logger.log(sheet.getName());
    // その他のsheetに対する処理
})
```

`getSheets`でブックにあるすべてのシートの配列を取得できます。
この配列の要素数（`.length`）でシートの数を確認できます。
また、この配列に対して`forEach`でループ処理できます。

## シートを削除したい（`deleteSheet`）

```js
const sheetToDelete = book.getSheetByName("不要なシート名");
book.deleteSheet(sheetToDelete);
```

`SpreadsheetApp.deleteSheet`でシートを削除できます。
引数は`Sheet`オブジェクトです。
シート名（`String`）ではない点に気をつけてください。

## リファレンス

- [Class Spreadsheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)
- [SpreadsheetApp.getActiveSpreadsheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app#getactivespreadsheet)
- [SpreadsheetApp.openById](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app#openbyidid)
- [SpreadsheetApp.openByUrl](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app#openbyurlurl)
