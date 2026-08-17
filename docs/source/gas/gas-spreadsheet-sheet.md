# シートを操作したい（`Sheet`）

```js
const book = SpreadsheetApp.openById("スプレッドシートのID");
const sheet = book.getSheetByName("シート名");
```

`Sheet`オブジェクトで単一のシートを操作できます。
ブックの取得方法については[ブックを操作したい](./gas-spreadsheet-book.md)を参照してください。

## シートのIDと名前を確認したい（`getId` / `getName`）

```js
const id = sheet.getId();
const name = sheet.getName();
```

`Sheet.getId`でシートのID（ブック内でシートを一意に識別する数値）を、
`Sheet.getName`でシート名を取得できます。

:::{hint}

`Sheet.getSheetName`という同名のメソッドもありますが、
`getName`と同じ値を返す旧API互換のためのエイリアスです。
新しく書く場合は`getName`を使えばよいです。

:::

## シートの位置を確認したい（`getIndex`）

```js
const index = sheet.getIndex();
```

`Sheet.getIndex`で、ブック内でのシートの位置（1はじまり）を取得できます。

## 最終行・最終列を確認したい（`getLastRow` / `getLastColumn`）

```js
const lastRow = sheet.getLastRow();
const lastCol = sheet.getLastColumn();
```

`Sheet.getLastRow`でデータが入っている最終行の行番号を、
`Sheet.getLastColumn`でデータが入っている最終列の列番号を取得できます。
どちらもデータが1件もない場合は`0`が返ります。

## 行を操作したい（`appendRow` / `deleteRow`）

```js
// データのカラム数と同じ要素の配列を作成
const data = ["A", "B", "C", "D"];
// データをシート末尾に追記
sheet.appendRow(data);

// 2行目を削除
sheet.deleteRow(2);
```

`Sheet.appendRow`で既存のシート末尾にデータを追加できます。
`Sheet.deleteRow`で行番号を指定して行ごと削除できます。

## 列を操作したい（`insertColumnBefore` / `insertColumnAfter` / `deleteColumn`）

```js
// 3列目の前に列を追加
sheet.insertColumnBefore(3);

// 3列目の後に列を追加
sheet.insertColumnAfter(3);

// 3列目を削除
sheet.deleteColumn(3);
```

`Sheet.insertColumnBefore`、`Sheet.insertColumnAfter`で、指定した列番号の前後に新しい列を追加できます。
`Sheet.deleteColumn`で、指定した列番号の列を削除できます。

```js
const values = sheet.getDataRange().getValues();
const headers = values[0];
const columnIdx = headers.indexOf("名前") + 1;
sheet.insertColumnBefore(columnIdx);
```

## シートを複製したい（`copyTo`）

```js
const source = SpreadsheetApp.openById("コピー元のID");
const target = SpreadsheetApp.openById("コピー先のID");
const sheet = source.getSheetByName("複製したいシート名");
const copied = sheet.copyTo(target);
```

`Sheet.copyTo`で指定したシートを複製できます。

## シート名を変更したい（`setName`）

```js
sheet.setName("変更後のシート名");
```

`Sheet.setName`でシート名を変更できます。
同じ名前のシートは作れません。

## シートを保護したい（`protect`）

```js
// シート全体を保護
const protection = sheet.protect();

// セル範囲を保護
const range = sheet.getRange("A2:D6");
const protection = range.protect();

// 保護の理由を追加
protection.setDescription("説明");
```

`Sheet.protect`（または`Range.protect`）でシートや選択したセルを保護できます。
`Protection.setDescription`で保護の理由を追加できます。

## セル範囲のデータを削除したい（`clearContent`）

```js
// 範囲を指定して削除
const range = sheet.getRange("A2:D6");
range.clearContent();
```

`Range.clearContent`で指定したセル範囲のデータを削除できます。

## カラム番号を取得したい（`getHeaders` / `getColumnIndex`）

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
  if (index === undefined) {
    throw new Error(`Column "${name}" not found`);
  }
  return index;
}

// Usage
const headers = getHeaders(sheet);
const nameColIndex = getColumnIndex(headers, "名前");
```

シート操作は、基本的にカラム番号（1はじまり）が前提となっていますが、カラム追加や順番の変更に弱いです。

このサンプルでは、ヘッダー行をMap型（`Map<string, number>`）に変換することで、カラム名から安全かつ可読性の高い形でカラム番号を取得できるようにしています。
カラム名で操作できるようになるので、
シートのカラム構成の変更にも強くなります。

## 行を安全に追加したい（`appendRow`のラッパー）

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

スタンドアロンスクリプトで、複数のシートを扱う場合、列数のチェックを追加した`Sheet.appendRow`のラッパーを作成しておくと便利です。

:::{hint}

`SpreadsheetApp.openById`などでシートを取得する処理は時間がかかります。
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
    .getRange(sheet.getLastRow() + 1, 1, rows.length, width)
    .setValues(rows);
}

const rows: Row[] = [
  ["A", "B"],
  [1, 2],
];
appendRows(sheet, rows);
```

`Sheet.appendRow`の処理は時間がかかります。
大量のデータを追加する場合は、
2次元配列を作成し`Range.setValues`で書き出すほうがよいです。

## データの重複を探したい（`findDuplicateRow`）

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
    throw new Error("Length doesn't match: colIndices and values");
  }

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return -1;

  const maxCol = Math.max(...colIndices);

  const rows = sheet
    .getRange(2, 1, lastRow - 1, maxCol)
    .getValues() as Cell[][];

  for (let i = 0; i < rows.length; i++) {
    const rowIndex = i + 2;
    if (rowIndex === excludeRowIndex) continue;

    const row = rows[i];

    const isMatch = colIndices.every(
      (col, j) => toKey(row[col - 1]) === toKey(values[j])
    );
    if (isMatch) return rowIndex;
  }
  return -1;
}
```

## リファレンス

- [Class Sheet](https://developers.google.com/apps-script/reference/spreadsheet/sheet)
- [Sheet.getId](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getid)
- [Sheet.getName](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getname)
- [Sheet.getIndex](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getindex)
- [Sheet.getLastRow](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getlastrow)
- [Sheet.getLastColumn](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getlastcolumn)
- [Sheet.appendRow](https://developers.google.com/apps-script/reference/spreadsheet/sheet#appendrowrowcontents)
- [Sheet.deleteRow](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deleterowrowposition)
- [Sheet.insertColumnBefore](https://developers.google.com/apps-script/reference/spreadsheet/sheet#insertcolumnbeforecolumnposition)
- [Sheet.insertColumnAfter](https://developers.google.com/apps-script/reference/spreadsheet/sheet#insertcolumnaftercolumnposition)
- [Sheet.deleteColumn](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deletecolumncolumnposition)
- [Sheet.copyTo](https://developers.google.com/apps-script/reference/spreadsheet/sheet#copytospreadsheet)
- [Sheet.setName](https://developers.google.com/apps-script/reference/spreadsheet/sheet#setnamename)
- [Sheet.protect](https://developers.google.com/apps-script/reference/spreadsheet/sheet#protect)
