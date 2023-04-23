# スプレッドシートしたい（``SpreadsheetApp``）

```js
const spreadsheet = SpreadsheetApp.getActive()
const sheet = spreadsheet.getActiveSheet();
const data = sheet.getDataRange().getValues().slice(1);
console.log(data);
```

GASでGoogleスプレッドシートを扱うには[SpreadsheetApp](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app)クラスを使います。
スプレッドシートには``スプレッドシート`` > ``シート`` > ``セル``という構造がありますが、それぞれ
[Spredsheetクラス](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)、[Sheetクラス](https://developers.google.com/apps-script/reference/spreadsheet/sheet)、[Rangeクラス][https://developers.google.com/apps-script/reference/spreadsheet/range]のオブジェクトが対応します。

上記のコードサンプルでは、取得したシートにある値を``getDataRange``ですべて選択し、``getValues``することで2次元配列のデータにしています。
最後に中身を確認するために``console.log``しています。
ここに処理を追加してCSVにしたり、JSONにしたり、ウェブAPIっぽくしたりもできます。

## スプレッドシートを開きたい（``openById``）

```js
const spreadsheet = SpreadsheetApp.getActive();
const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
const spreadsheet = SpreadsheetApp.openById("スプレッドシートのID");
const spreadsheet = SpreadsheetApp.openByUrl("スプレッドシートのURL");
```

スプレッドシートにバインドしたスクリプトの場合、``getActive...``でスプレッドシートを開くことができます。
他の場所にあるスプレッドシートを開きたい場合は、``openBy...`を使います。

## シートを開きたい（``getSheetByName``）

```js
const sheet = SpreadsheetApp.getActiveSheet();
const sheet = SpreadsheetApp.openById("スプレッドシートID").getSheetsByName("シート名");
const sheets = SpreadsheetApp.getActiveSpreadsheet().getSheets();

```

シートはスプレッドシートの中にあるので、``Spreadsheetクラス``のオブジェクトを通してアクセスできます。
スプレッドシートIDとシート名を使って、あるスプレッドシートを開くことができます。
``getSheets``（複数形）で複数のシートを配列として取ってくることもできます。

### シートを操作したい

```js
// シート名を変更したい
sheet.setName("変更後のシート名");
```

```js
// シートを削除したい
spreadsheet.deleteSheet(spreadsheet.getSheetByName("シート名"););
```

シートを削除する場合は、``Spreadsheet``オブジェクトに対して操作します。

## セルを選択したい（``getRange``）

```js
const cell = sheet.getRange("セル名");
const cell = sheet.getRange("行番号", "列番号");
const cells = sheet.getRange("セル名:セル名");
const cells = sheet.getRange("行番号", "列番号", "行数");
const cells = sheet.getRange("行番号", "列番号", "行数", "列数");
const data = sheet.getRange(1, 1, sheet.getLastRow(), sheet.getLastColumns());
const data = sheet.getDataRange().slice(1);
```

セル名や番地（行番号と列番号）を使ってセルを選択できます。
``getDataRange``でデータが存在する範囲をすべて選択できます。
データに見出しを含みたくない場合は``slice(1)``するとよいかもしれません。

### セル書式を変更したい

```js
const cells = sheet.getRange(範囲); // 開始行, 開始列, 行数, 列数
cells.setFontSize(整数);
cells.setFontFamily("フォント名");
cells.setFontWeight("ウェイト名"); // "normal", "bold"
cells.setFontStyle("スタイル名");  // "normal", "italic"
cells.setFontLine("ライン名");    // "none", "underline", "line-through"
cells.setFontColors("色");
cells.setBackgrounds("色");
```

選択したセルに対して、フォントやスタイル、文字色などを設定できます。

## 組み込み関数したい（``setFormula``）

```js
const cell = sheet.getRange("セル名");
cell.setFormula("=SUM(セル名:セル名)");
```

``setFormula``を使って、スプレッドシートの組み込み関数を利用できます。

## グラフしたい

```js
const chart = sheet.newChart()
    .asBarChart()
    .addRange(データの範囲)
    .setPosition(表示位置)
    .setOption("height", 高さ)
    .setOption("width", 幅)
    .setOption("title", タイトル)
    .build();
sheet.insertChart(chart);
```

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
