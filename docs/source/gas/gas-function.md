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

アロー関数は、関数式の一種で、関数を簡潔に書くための構文です。
ES6（ES2015）で導入されました。
単純な処理は、アロー関数で書くとよいみたいです。

## 関数定義の構文について

JavaScriptには、歴史的な経緯から関数を定義する構文が複数あります。
まずは、基本となる`function`を使った構文を体得すればよいと思います。
この構文は、初期のJavaScriptから存在しており、
現在のモダンな環境でも問題なく動作します。

アロー関数はES2015で導入された新しい構文です。
関数式を簡潔に書けるのが特徴で、単純な処理ではコード量を大幅に減らせます。
利用可能な環境であれば積極的に使えばよいと思います。

ただし、複雑な処理では、記述がコンパクトすぎて、かえって読みづらくなることもあると感じました。
可読性を意識して構文を使い分けるとよさそうです。
