# SpreadsheetAppの使い方

## スプレッドシートを開きたい（``openById``）

```js
const sheet = SpreadsheetApp.openById("シートID");
```

## シートを選択したい（``getSheetByName``）

```js
sheet.getActiveSheet();
sheet.getSheetByName("シート名");
```

現在選択しているシートは``getActiveSheet``で選択できます。
``getSheetByName``を使うと、シート名で選択できます。

## シート名を変更したい（``setName``）

```js
sheet.getSheetByName("シート名").setName("変更後のシート名");
```

## シートを削除したい（``deleteSheet``）

```js
sheet.deleteSheet(sheet.getSheetByName("シート名"));
```

## データを選択したい（``getRange``）

```js
const data = sheet.getRange(1, 1, ss.getLastRow(), ss.getLastColumn()).getValues();
```

シートのすべてのデータを配列として取得できます。
``getLastRow``と``getLastColumn``を使うことで、データが更新されて行数や列数に変更があっても対応できます。

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
