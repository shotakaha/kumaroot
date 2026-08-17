# スプレッドシートを操作したい（`SpreadsheetApp`）

```js
// アクティブなブックを取得する
const book = SpreadsheetApp.getActiveSpreadsheet();
// アクティブなシートを取得する
const sheet = book.getActiveSheet();
// シートにあるすべてのデータを2次元配列で取得する
const arrays = sheet.getDataRange().getValues();

// 見出しとデータに分割
const headers = arrays[0];
const data = arrays.slice(1);

Logger.log(`見出し: ${headers}`);
Logger.log(`データ数: ${data.length}`);

// 書き込むシートを取得する（なければ作成する）
const name = "writeSheet";
const sheetToWrite = book.getSheetByName(name) || book.insertSheet(name);

// 範囲を指定してデータを書き込む
const arraysToWrite = [headers, ...data];
const rows = arraysToWrite.length;
const cols = arraysToWrite[0].length;
sheetToWrite.getRange(1, 1, rows, cols).setValues(arraysToWrite);
```

[SpreadsheetApp](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app)クラスで、Googleスプレッドシートを操作できます。

スプレッドシートには`ブック` > `シート` > `セル`という構造があります。
それぞれ
[Spreadsheetクラス](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)、
[Sheetクラス](https://developers.google.com/apps-script/reference/spreadsheet/sheet)、
[Rangeクラス](https://developers.google.com/apps-script/reference/spreadsheet/range)
のオブジェクトが対応しています。

:::{note}

このドキュメントでは、Excelでの呼び方を参考に、
`Spreadsheet`オブジェクトを「ブック」、
`Sheet`オブジェクトを「シート」、
`Range`オブジェクトを「セル」と呼ぶことにします。

公式リファレンスやサンプルコードでは`Spreadsheet`オブジェクトも「スプレッドシート」と呼ばれることが多く、
ファイル全体（ブック）を指すのか、単一の表（シート）を指すのか紛らわしいためです。

変数名もこれにあわせて`book`、`sheet`を使います。

:::

上記のコードサンプルでは、取得したシートにある値を`getDataRange`ですべて選択し、`getValues`することで2次元配列のデータにしています。

最後に中身を確認するために`Logger.log`しています。
ここに処理を追加してCSVにしたり、JSONにしたり、ウェブAPIっぽくしたりもできます。

```{toctree}
---
maxdepth: 1
---
gas-spreadsheet-book
gas-spreadsheet-sheet
gas-spreadsheet-range
gas-spreadsheet-create
gas-spreadsheet-pivottable
gas-spreadsheet-filter
gas-spreadsheet-chart
```

## カスタムメニューを追加したい（`getUi`）

```js
function onOpen() {
    const ui = SpreadsheetApp.getUi();
    const menu = ui.createMenu("メニュー名");
    menu.addItem("アイテム名1", "関数名1");
    menu.addItem("アイテム名2", "関数名2");
    menu.addSeparator();
    menu.addItem("アイテム名3", "関数名3");
    menu.addToUi();
}
```

スプレッドシートにカスタムメニューを追加できます。
シートを開いたときに、メニューに追加するため`onOpen`関数の中で定義します。
