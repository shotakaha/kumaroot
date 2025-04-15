# セル操作したい（`Range`）

```js
const range = sheet.getDataRange();
const range = sheet.getRange("A1:C3");
```

`Range`オブジェクトは、シート上の選択した範囲を操作できます。

## データを選択したい（`getRange`）

```js
// A1表記で指定
// sheet.getRange("セル番地");
// sheet.getRange("セル番地:セル番地");

// A1セルを選択
const range = sheet.getRange("A1");

// A1セルからB3までの範囲を選択
const range sheet.getRange("A1:B3");
```

`getRange`でセル（やセル範囲）を指定して選択できます。
セル番地は大文字でも小文字でもOKです。

```js
// 行番号／列番号で指定
// sheet.getRange("行番号", "列番号");
// sheet.getRange("行番号", "列番号", "行数");
// sheet.getRange("行番号", "列番号", "行数", "列数");

// 2行目3列目（=C2セル）を選択
const range = sheet.getRange(2, 3);

// 2行目3列目（=C2）から2行目2列目（=D3）の範囲を取得
const range = sheet.getRange(2, 3, 2, 2);
```

`getRange`はR1C1表記にも対応しています。

## データを列選択したい

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

## データを全選択したい（`getDataRange`）

```js
// すべてのデータの範囲
const range = sheet.getDataRange()
```

`getDataRange`で、シートにあるデータを全選択できます。
余計な空行・空列は含まれないので、シート全体でデータを管理している場合によく使います。

```js
// 見出しを除外したデータの範囲
const range = sheet.getDataRange.slice(1);
```

シートの1行目は、見出しに設定している場合があります。
見出しを含みたくない場合は`.slice(1)`するとよいです。

```js
// 別の選択方法
const nrows = sheet.getLastRow();
const ncols = sheet.getLastColumns();
const range = sheet.getRange(2, 1, nrows, ncols);
```

シートにあるデータの行数、列数を取得して、`getRange`して範囲選択することもできます。

```js
const lastRow = sheet.getLastRow();
const newRange = sheet.getRange(lastRow+1, 1);
```

データを読み込むときより、既存のデータを追記したいときに利用します。

## セル選択したい（`getRange`）

```js
// 選択範囲を確認
range.activate();
```

`activate`メソッドで、実際に選択された範囲をシート上で確認できます。
デバッグ時など、選択範囲が正しいか確認するときに便利です。

## 値を読み込みたい（`getValues`）

```js
const values = range.getValues();
```

`getValues`メソッドで、選択した範囲の値を2次元配列として取得できます。

## 値を書き込みたい（`setValues`）

```js
const arrays = [[二次元配列]];
const rows = dataTable.length;   // 行の数
const cols = dataTable[0].length;  // 見出しの数＝列の数
sheet.getRange(1, 1, rows, cols).setValues(arrays);
```

`setValues`メソッドで、選択した範囲に2次元配列の値を書き込めます。
書き込みたい2次元配列のシェイプ（＝行数と列数）と、選択範囲のサイズは揃っている必要があるため、`rows`と`cols`を2次元配列から取得しています。

## リファレンス

- [Sheet.getDataRange](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getdatarange)
- [Sheet.getRange](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getrangerow,-column)
