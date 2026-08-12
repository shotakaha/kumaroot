# 関数したい（`function`）

```ts
type Cell = string | number | boolean | Date | null;

function getValues(
  book: GoogleAppsScript.Spreadsheet.Spreadsheet,
  sheetName: string
): Cell[][] {
  const sheet = book.getSheetByName(sheetName);

  if (!sheet) {
    throw new Error(`Sheet not found: ${sheetName}`)
  }
  return sheet.getDataRange().getValues();
}

// Usage
const book = SpreadsheetApp.getActiveSpreadsheet();
const values = getValues(book, "responses");
```

`function`を使って関数を定義できます。
GASプロジェクトは、この`function`を使った関数の集合体として作成することがほとんどです。
同じプロジェクト内で、ファイルを分けることができますが、すべてグローバルな関数として扱われるため、関数名が重複しないように気をつける必要があります。

## オプションしたい

```ts
type Cell = string | number | boolean | Date | null;

// オプション用の型名を定義
type GetDataOptions = {
  header?: boolean;
  limit?: number | null;
};

function getData(
  sheet: GoogleAppsScript.Spreadsheet.Sheet,
  options: GetDataOptions = {}
): Cell[][] {

  // オプションの初期値を設定
  const {
    header = true,
    limit = null,
  } = options;

  let data = sheet.getDataRange().getValues();

  if (!header) {
    data = data.slice(1);
  }

  if (limit !== null) {
    data = data.slice(0, limit);
  }

  return data;
}
```

TS/JSでは名前付きの引数を設定することができません。
しかし、オブジェクトを引数にすることで、名前付き引数のように動作させることができます。

## 関数式したい

```js
const add = function(a, b) {
    return a + b;
}
```

関数式（function expression）は、関数を値として扱い、変数に代入する書き方です。

## アロー関数したい

```js
const 関数名 = (引数) => 返り値;
const add = (a, b) => a + b;
```

アロー関数（arrow function）は、関数式の一種で、関数を簡潔に書くための構文です。
ES6（ES2015）で導入されました。
単純な処理は、アロー関数で書くとよいみたいです。

:::{note}

アロー関数は独自の`this`を持たない構文です。
小さな処理やコールバックでは、外側のスコープの`this`を安全に使うことができます。

一方で、オブジェクトやGAS特有の`this`を参照できないため、メソッドやトリガー関数には不向きです。

:::

## 使い分けについて

複雑な処理や、複数の`if`分岐・ループを含む処理は、
`function`で書いたほうがコードの見通しがよいことが多いです。
アロー関数はコンパクトに書けるぶん、詰め込みすぎるとかえって読みづらくなります。
処理の複雑さに応じて構文を使い分けるとよさそうです。
