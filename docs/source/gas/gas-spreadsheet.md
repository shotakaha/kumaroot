# スプレッドシートしたい（``SpreadsheetApp``）

```js
const spreadsheet = SpreadsheetApp.getActive()
const sheet = spreadsheet.getActiveSheet();
const data = sheet.getDataRange().getValues().slice(1);
console.log(data);
```

GASでGoogleスプレッドシートを扱うには[SpreadsheetApp](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app)クラスを使います。
GASが紐づけてあるスプレッドシートの場合、``getActive``でアクセスできるようになります。
スプレッドシートが複数のシートを持つ場合は、さらに``getActiveSheet``することで選択中のシートにアクセスできるようになります。

上記のコードサンプルでは、取得したシートにある値を``getDataRange``ですべて選択し、``getValues``することで2次元配列のデータにしています。
最後に中身を確認するために``console.log``しています。
ここに処理を追加してCSVにしたり、JSONにしたり、ウェブAPIっぽくしたりもできます。

## シートを開きたい（``openById`` / ``getSheetByName``）

```js
const spreadsheet = SpreadsheetApp.openById("シートID");
const sheet = spreadsheet.getSheetByName("シート名");
```

スプレッドシートIDとシート名を使って、あるスプレッドシートを開くことができます。

## シート名を変更したい（``setName``）

```js
sheet.getSheetByName("シート名").setName("変更後のシート名");
```

## シートを削除したい（``deleteSheet``）

```js
sheet.deleteSheet(sheet.getSheetByName("シート名"));
```

## データを選択したい（``getRange`` / ``getDataRange``）

```js
const data = sheet.getRange(1, 1, 行数, 列数).getValues();
const data = sheet.getRange(1, 1, ss.getLastRow(), ss.getLastColumn()).getValues();
const data = sheet.getDataRange().getValues().slice(1);
```

``getRange``で範囲を指定してデータを配列として取得できます。
シートのすべてのデータを取得したいときは、``getLastRow``と``getLastColumn``でデータ全体の行数と列数を指定するか、``getDataRange``で全範囲を指定します。
データに見出しを含みたくない場合は``slice(1)``するとよいです。

## 組み込み関数したい（``setFormula``）

```js
var cell = sheet.getRange("セル名");
cell.setFormula("=SUM(セル名:セル名)");
```

``setFormula``を使って、スプレッドシートの組み込み関数を利用できます。

## セルの書式を変更したい

```js
var cells = sheet.getRange(範囲); // 開始行, 開始列, 行数, 列数
cells.setFontSize(整数);
cells.setFontFamily("フォント名");
cells.setFontWeight("ウェイト名"); // "normal", "bold"
cells.setFontStyle("スタイル名");  // "normal", "italic"
cells.setFontLine("ライン名");    // "none", "underline", "line-through"
cells.setFontColors("色");
cells.setBackgrounds("色");
```

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
