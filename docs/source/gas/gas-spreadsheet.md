# スプレッドシートしたい（`SpreadsheetApp`）

```js
// アクティブなスプレッドシート（＝ブック）を取得する
const book = SpreadsheetApp.getActiveSpreadsheet();
// アクティブなシートを取得する
const sheet = book.getActiveSheet();
// アクティブなセル範囲を取得する
const range = sheet.getActiveRange();
// セルの値を2次元配列で取得する
const arrays = range.getValues();

// 見出しとデータに分割代入
const { headers, ...data } = arrays;

Logger.log(`見出し: ${headers}`);
Logger.log(`データ数: ${data.length}`);

// 読み込んだデータをあれこれ
const arraysToWrite = ...;

// 書き込むシートを取得する（なければ作成する）
const name = "writeSheet";
const sheetToWrite = sheet.getSheetByName(name) || sheet.insertSheet(name);

// 範囲を指定してデータを書き込む
const rows = arraysToWrite.length;
const cols = arraysToWrite[0].length;
sheetToWrite.getRange(1, 1, rows, cols).setValues(arraysToWrite);
```

[SpreadsheetApp](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app)クラスで、Googleスプレッドシートを操作できます。

スプレッドシートには``ブック（スプレッドシート）`` > ``シート`` > ``セル``という構造があります。
それぞれ
[Spredsheetクラス](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)、
[Sheetクラス](https://developers.google.com/apps-script/reference/spreadsheet/sheet)、
[Rangeクラス](https://developers.google.com/apps-script/reference/spreadsheet/range)
のオブジェクトが対応しています。

上記のコードサンプルでは、取得したシートにある値を``getDataRange``ですべて選択し、``getValues``することで2次元配列のデータにしています。

最後に中身を確認するために``Logger.log``しています。
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

## スプレッドシート全体を複製したい（`copy`）

```js
const book = SpreadsheetApp.openById("コピー元のID");
const copied = book.copy("コピー先のファイル名");
```

`copy`メソッドでスプレッドシート全体を複製できます。
新しいブックが作成されるため、URLも新規発行されます。

## シートを複製したい（`copyTo`）

```js
const source = SpreadsheetApp.openById("コピー元のID");
const target = SpreadsheetApp.openById("コピー先のID");
const sheet = source.getSheetByName("複製したいシート名");
const copied = sheet.copyTo(target);
```

`copyTo`で指定したシートを複製できます。

## カスタムメニューしたい（``getUi``）

```js
function onOpen() {
    var ui = SpreadsheetApp.getUi();
    var menu = ui.createMenu("メニュー名");
    menu.addItem("アイテム名1", "関数名1");
    menu.addItem("アイテム名2", "関数名2");
    menu.addSeparator();
    menu.addItem("アイテム名3", "関数名3");
    menu.addToUi();
}
```

スプレッドシートにカスタムメニューを追加できます。
シートを開いたときに、メニューに追加するため``onOpen``関数の中で定義します。
