# スプレッドシートしたい（``SpreadsheetApp``）

```js
// アクティブなスプレッドシート（＝ブック）を取得する
const book = SpreadsheetApp.getActive()
// アクティブなシートを取得する
const sheet = book.getActiveSheet();
// アクティブなセル範囲を取得する
const range = sheet.getActiveRange();
// セルの値を2次元配列で取得する
const rows = range.getValues();

// 見出しとデータに分割
const headers = rows[0];
const data = rows.slice(1);

Logger.log(`見出し：${headers}`);
Logger.log(data);
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
gas-spreadsheet-create
gas-spreadsheet-book
gas-spreadsheet-sheet
gas-spreadsheet-range
gas-spreadsheet-pivottable
gas-spreadsheet-filter
gas-spreadsheet-chart
```

## データを取得したい（`getValues`）

```js
const range = sheet.getDataRange();
const rows = range.getValues();
```

`getValues`で選択した範囲オブジェクトの値を2次元配列で取得できます。

```js
// シートからデータを読み込む汎用的な関数
// @param {Sheet} sheet - Sheetオブジェクト
// @param {numbers} skiprows - スキップする行の数
function readDataFromSheet(sheet, skiprows=0) {
    // 1行目を見出し（=カラム名）にする
    const rows = sheet.getDataRange().getValues().slice(skiprows);

    // 見出しとデータを分割
    const [headers, ...data] = rows;

    Logger.log(`rows: ${rows.length}`);
    Logger.log(`headers: ${headers.length}`);
    Logger.log(`data: ${data.length}`);

    return {"headers": headers, "data": data};
}

//
// テスト関数
//
// フォームで収集したマスターデータを読み込みテストに利用
function testReadDataFromSheet() {
    const book = SpreadsheetApp.getActiveSpreadsheet();
    // シート名は"masterData"とする
    const sheet = book.getSheetByName("masterData");
    // 分割代入で返り値を受け取る
    const {headers, data} = readDataFromSheet(sheet);
}
```

スプレッドシートからデータを取得するときによく使う関数のサンプルです。

## 選択範囲のデータを取得したい（`getActiveRange`）

```js
function getCurrentRowData() {
    const book = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = book.getActiveSheet();
    // 選択されたセルの範囲を取得
    const range = sheet.getActiveRange();
    // 選択されたセルの行番号を取得
    const row_number = range.getRow();

    Logger.log(`選択した行: ${row_number}`);

    const row = sheet.getRange(row_number, 1, 1, sheet.getLastColumn());
    const data = row.getValues();

    Logger.log(`行のデータ: ${data}`);

    return data;
}
```

スプレッドシート上で選択したセルの範囲を操作するサンプルです。
`getActiveRange`で**シート上で選択した範囲**の値を取得しています。

## データをフィルターしたい

```js
function filterData(data) {
    const filtered = data.filter(function(要素, インデックス, 配列) {
        return 条件;
    })
}
```

`filter`メソッドを使って、条件に一致した要素を抽出できます。

## データをマッピングしたい

```js
function parseData(data) {
    const parsed = data.map(d => {
        const item = {
            timestamp: d[0],
            name: d[3],
            email: d[2],
            ...
        };
        return item;
    });
    return parsed;
}

const data = readData();
const filtered = filterData(data);
const parsed = parseData(filtered);
```

`map`メソッドを使って、データを整形できます。
フォームで集めたデータを、任意の順番に並べ替えたいときに使います。

## データを追加したい（``appendRow``）

```js
// データのカラム数と同じ要素の配列を作成
const data = ["A", "B", "C", "D"];
// データをシート末尾に追記
sheet.appendRow(data);
```

`appendRow`で既存のシート末尾にデータを追加できます。

:::{note}

`appendRow`の処理は時間がかかるので、大量のデータを追加する場合は、
配列で作成し`setValues`で書き出すほうがよいです。

:::

## データを書き出したい（``setValues``）

```js
function updateData() {}
    // （シート取得は省略）

    // データは二次元配列で作成する
    const data = [
        ["A1", "B1", "C1"],
        ["A2", "B2", "C2"],
        ["A3", "B3", "C3"],
        ["A4", "B4", "C4"],
        ];

    // 配列のサイズを求める
    const nrows = data.length
    const ncols = data[0].length

    // 範囲を指定してデータをセットする
    const range = sheet.getRange(1, 1, nrows, ncols);
    range.setValues(data);
};
```

`setValues`で、指定したデータをセル範囲に一括出力できます。
シートの一部を更新するときに利用できます。

## データを削除したい（`deleteRow`）

```js
function deleteData() {
    // （シート取得は省略）

    // 2行目を削除
    sheet.deleteRow(2);

    // 範囲を指定して削除
    const range = sheet.getRange("A2:D6");
    range.clearContent();
}
```

`deleteRow`で行番号を指定してデータを削除できます。
`clearContent`で指定したセル範囲のデータを削除できます。

## 組み込み関数したい（``setFormula``）

```js
const cell = sheet.getRange("セル名");
cell.setFormula("=SUM(セル名:セル名)");
```

``setFormula``を使って、スプレッドシートの組み込み関数を利用できます。

## シート名を変更したい（``setName``）

```js
const book = SpreadsheetApp.openById("移動元のID");
const sheet = book.getSheetByName("変更前のシート名");
sheet.setName("変更後のシート名");
```

`setName`でシート名を変更できます。
同じ名前のシートは作れません。

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

## シートを削除したい（``deleteSheet``）

```js
const book = SpreadsheetApp.openById("ID");
const sheet = book.getSheetByName("削除したいシート名");
book.deleteSheet(sheet);
```

`deleteSheet`でシートを削除できます。
シートの削除は``Spreadsheet``オブジェクトに対して操作します。

## シートを保護したい（``protect``）

```js
// シート全体を保護
const protection = sheet.protect()

// セル範囲を保護
const range = sheet.getRange("A2:D6");
const protection = range.protect()

// 保護の理由を追加
protection.setDescription("説明")
```

`protect`でシートや選択したセルを保護できます。
`setDescription`で保護の理由を追加できます。

## セルの書式を変更したい

```js
const range = sheet.getRange(範囲); // 開始行, 開始列, 行数, 列数
range.setFontSize(整数);
range.setFontFamily("フォント名");
range.setFontWeight("ウェイト名"); // "normal", "bold"
range.setFontStyle("スタイル名");  // "normal", "italic"
range.setFontLine("ライン名");    // "none", "underline", "line-through"
range.setFontColors("色");
range.setBackgrounds("色");
```

選択したセルに対して、フォントやスタイル、文字色などを設定できます。

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
