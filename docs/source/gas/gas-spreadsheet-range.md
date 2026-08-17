# セルを操作したい（`Range`）

```js
const range = sheet.getRange("A1:C3");
```

`Range`オブジェクトは、シート上の選択した範囲を操作できます。
`Range`の取得方法（`getRange` / `getDataRange`）については[シートを操作したい](./gas-spreadsheet-sheet.md)を参照してください。

## 値を読み込みたい（`getValues`）

```js
const values = range.getValues();
```

`Range.getValues`メソッドで、選択した範囲の値を2次元配列として取得できます。

```js
const values = sheet.getDataRange().getValues();
const headers = values[0];
const rows = values.slice(1);
```

1行目を見出しとして扱っている場合は、上のように`headers`と`rows`に分けて取得すると扱いやすいです。

## 値を書き込みたい（`setValues`）

```js
const arrays = [
  ["名前", "年齢"],
  ["田中", 20],
  ["鈴木", 30],
];
const rows = arrays.length;      // 行の数
const cols = arrays[0].length;   // 列の数
sheet.getRange(1, 1, rows, cols).setValues(arrays);
```

`Range.setValues`メソッドで、選択した範囲に2次元配列の値を書き込めます。
書き込みたい2次元配列のシェイプ（＝行数と列数）と、選択範囲のサイズは揃っている必要があるため、`rows`と`cols`を2次元配列から取得しています。

## セル範囲のデータを削除したい（`clearContent`）

```js
// 範囲を指定して削除
const range = sheet.getRange("A2:D6");
range.clearContent();
```

`Range.clearContent`で指定したセル範囲のデータを削除できます。

## 選択範囲を確認したい（`activate`）

```js
// 選択範囲を確認
range.activate();
```

`Range.activate`メソッドで、実際に選択された範囲をシート上で確認できます。
デバッグ時など、選択範囲が正しいか確認するときに便利です。

## スプレッドシートの関数を使いたい（`setFormula`）

```js
const cell = sheet.getRange("D1");
cell.setFormula("=SUM(A1:C1)");
```

`Range.setFormula`で`SUM`などのスプレッドシートの関数を設定できます。

## セルの書式を変更したい

```js
const range = sheet.getRange(1, 1, 3, 2); // 開始行, 開始列, 行数, 列数
range.setFontSize(12);
range.setFontFamily("Arial");
range.setFontWeight("bold");   // "normal", "bold"
range.setFontStyle("italic");  // "normal", "italic"
range.setFontLine("underline"); // "none", "underline", "line-through"
range.setFontColor("red");
range.setBackground("yellow");
```

`Range.setFontSize`などで、選択したセルに対してフォントやスタイル、文字色などを設定できます。

## リファレンス

- [Class Range](https://developers.google.com/apps-script/reference/spreadsheet/range)
- [Range.getValues](https://developers.google.com/apps-script/reference/spreadsheet/range#getvalues)
- [Range.setValues](https://developers.google.com/apps-script/reference/spreadsheet/range#setvaluesvalues)
- [Range.clearContent](https://developers.google.com/apps-script/reference/spreadsheet/range#clearcontent)
- [Range.activate](https://developers.google.com/apps-script/reference/spreadsheet/range#activate)
- [Range.setFormula](https://developers.google.com/apps-script/reference/spreadsheet/range#setformulaformula)
- [Range.setFontSize](https://developers.google.com/apps-script/reference/spreadsheet/range#setfontsizesize)
