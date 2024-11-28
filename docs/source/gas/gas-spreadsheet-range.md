# セル操作したい（`Range`）

```js
const range = sheet.getRange("A1:C3");
range.setFontColorObject("#fff");
range.setBackgroundbject("#000");
```

`Range`オブジェクトで、シート上の選択した範囲に対して操作できます。

## すべてのデータを選択したい（`getDataRange`）

```js
// すべてのデータの範囲
const range = sheet.getDataRange()

// 見出しを除外したデータの範囲
const range = sheet.getDataRange.slice(1);
```

`Sheet.getDataRange`で、シート上のデータが存在する範囲をすべて選択できます。
データに見出しを含みたくない場合は``slice(1)``するとよいです。

```js
// 別の選択方法
const nrows = sheet.getLastRow();
const ncols = sheet.getLastColumns();
const range = sheet.getRange(2, 1, nrows, ncols);
```

シートにあるデータの行数、列数を取得して、範囲選択することもできます。

```js
const lastRow = sheet.getLastRow();
const newRange = sheet.getRange(lastRow+1, 1);
```

データを読み込むときより、既存のデータを追記したいときに利用します。

## セル選択したい（`getRange`）

```js
// A1表記で指定
const range = sheet.getRange("セル番地");
const range = sheet.getRange("セル番地:セル番地");
// 行番号／列番号で指定
const range = sheet.getRange("行番号", "列番号");
const range = sheet.getRange("行番号", "列番号", "行数");
const range = sheet.getRange("行番号", "列番号", "行数", "列数");
```

`Sheet.getRange`で、セル名や番地（行番号と列番号）を使ってセル（の範囲）を選択できます。

```js
// B2セルを選択
const range = sheet.getRange("B2");
const range = sheet.getRange("b2");
```

セル番地は大文字でも小文字でもOKです。

```js
// B列を全選択
const range = sheet.getRange("B1:B");

// 2行目を全選択
const range = sheet.getRange("A2:2");

// これはエラー
const range = sheet.getRange("B");
// -> Exception: Range not found
```

列全体は`getRange(開始セル:列番号)`、
行全体は`getRange(開始セル:行番号)`で選択できます。
`getRange(列番号 or 行番号)`だけだとエラーになります。

```js
// 選択範囲を確認
range.activate();
```

`activate`メソッドで、実際に選択された範囲をシート上で確認できます。
デバッグ時など、選択範囲が正しいか確認するときに便利です。

## 値を読み込みたい（`getValues`）

```js
const dataTable = range.getValues();
```

`getValues`メソッドで、選択した範囲の値を2次元配列として取得できます。

## 値を書き込みたい（`setValues`）

```js
const dataTable = [[二次元配列]];
const nrows = dataTable.length;   // 行の数
const ncols = dataTable[0].length;  // 見出しの数＝列の数
sheet.getRange(1, 1, nrows, ncols).setValues(dataTable);
```

`setValues`メソッドで、選択した範囲に2次元配列の値を書き込めます。
書き込みたい2次元配列のシェイプ（＝行数と列数）と、選択範囲のサイズは揃っている必要があるため、`nrows`と`ncols`を`dataTable`から取得しています。

## リファレンス

- [Sheet.getDataRange](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getdatarange)
- [Sheet.getRange](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getrangerow,-column)
