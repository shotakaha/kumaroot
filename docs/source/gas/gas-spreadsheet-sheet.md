# シート操作したい（`Sheet`）

```js
const book = SpreadsheetApp.getActiveSpreadsheet();
const sheet = book.getActiveSheet();
```

`Sheet`オブジェクトで単一のシートを操作できます。

## シートの情報を確認したい

```js
const id = sheet.getId();
const name = sheet.getName();
const sheetName = sheet.getSheetName();

const index = sheet.getIndex();
const lastRow = sheet.getLastRow();
const lastCol = sheet.getLastColumn();
```

## 行データを追加したい（`appendRow`）

```js
// データのカラム数と同じ要素の配列を作成
const data = ["A", "B", "C", "D"];
// データをシート末尾に追記
sheet.appendRow(data);
```

`appendRow`で既存のシート末尾にデータを追加できます。

```ts
type Cell = string | number | boolean | Date | null;
type Row = Cell[];

function appendRow(
  sheet: GoogleAppsScript.Spreadsheet.Sheet,
  row: Row
) {
  const width = sheet.getLastColumn();
  if (width !== 0 && row.length !== width) {
    throw new Error("列数が一致していません");
  }

  sheet.appendRow(row);
}

const row: Row = ["A", 123, true, new Date(), null];
appendRow(sheet, row);
```

スタンドアロンなスクリプトで、複数のシートを扱う場合、列数のチェックを追加した`appendRow`のラッパーを作成しておくと便利です。

:::{hint}

`openById`などでシートを取得する処理は時間がかかります。
ラッパー関数の中で毎回呼び出すのではなく、
あらかじめ取得したシートを引数として渡すとよいです。

:::

```ts
type Cell = string | number | boolean | Date | null;
type Row = Cell[];

function appendRows(
  sheet: GoogleAppsScript.Spreadsheet.Sheet,
  rows: Row[]
) {
  if (rows.length === 0) return;

  const width = rows[0].length;

  // すべての行のカラム数をチェック
  if (!rows.every(row => row.length === width)) {
    throw new Error("すべての行の列数が一致していません");
  }

  sheet
    .getRange(sheet.getLastRow() + 1, 1, rows.length, width.length)
    .setValues(rows);
}

const rows: Row[] = [
  ["A", "B"],
  [1, 2],
];
appendRows(sheet, rows);
```

`appendRow`の処理は時間がかかります。
大量のデータを追加する場合は、
2次元配列を作成し`setValues`で書き出すほうがよいです。

## カラム番号を取得したい

```ts
function getHeaders(
  sheet: GoogleAppsScript.Spreadsheet.Sheet
): Map<string, number> {
  const headers = sheet
    .getRange(1, 1, 1, sheet.getLastColumn())
    .getValues()[0];

  const map = new Map<string, number>();

  headers.forEach((h, i) => {
    const key = String(h).trim();
    if (key) {
      map.set(key, i + 1);
    }
  });
  return map;
}

function getColumnIndex(
  headers: Map<string, number>,
  name: string
): number {
  const index = headers.get(name.trim());
  if (!index) {
    throw new Error(`Column "${name}" not found`);
  }
  return index;
}

// Usage
const headers = getHeaders(sheet);
const nameColIndex = getColumnIndex(headers, "名前");
```

スプレッドシート操作は、基本的にカラム番号（1はじまり）が前提となっていますが、カラム追加や順番の変更に弱いです。

このサンプルでは、ヘッダー行をMap型（`Map<string, number>`）に変換することで、カラム名から安全かつ可読性の高い形でカラム番号を取得できるようにしています。
カラム名で操作できるようになるので、
シートのカラム構成の変更にも強くなります。

## データの重複を探したい（`findDuplicateRows`）

```ts
type Cell = string | number | boolean | Date | null;
type Row = Cell[];

function toKey(v: Cell): string {
  if (v instanceof Date) return String(v.getTime());
  if (v === null) return "null";
  return String(v);
}

function findDuplicateRow(
  sheet: GoogleAppsScript.Spreadsheet.Sheet,
  colIndices: number[],
  values: Cell[],
  excludeRowIndex?: number
): number {
  if (colIndices.length != values.length) {
    throw new Error("Length doesn't match: colIndices and values")
  }

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return -1;

  const maxCol = Math.max(...colIndices);

  const rows = sheet
    .getRange(2, 1, lastRow - 1, maxCol)
    .getValues() as Cell[][];

  for (let i = 0; i < row.length; i++) {
    const rowIndex = i + 2;
    if (rowIndex === excludeRowIndex) continue;

    const row = rows[i];

    const isMatch = colIndices.every((col, j) => toKey(row[col - 1] === toKey(values[j]))
    );
    if (isMatch) return rowIndex;
  }
  return -1
}
```

## データを削除したい（`deleteRow`）

```js
// 2行目を削除
sheet.deleteRow(2);
```

`deleteRow`で行番号を指定してデータを削除できます。

## データを削除したい（`clearContent`）

```js
// 範囲を指定して削除
const range = sheet.getRange("A2:D6");
range.clearContent();
```

`clearContent`で指定したセル範囲のデータを削除できます。

## シート名を変更したい（``setName``）

```js
sheet.setName("変更後のシート名");
```

`setName`でシート名を変更できます。
同じ名前のシートは作れません。

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

## リファレンス

- [Class Spreadsheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet)
- [Spreadsheet.getSheetByName](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheetbynamename)
- [Spreadsheet.insertSheet](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#insertsheetsheetname)
- [Spreadsheet.getSheets](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#getsheets)
