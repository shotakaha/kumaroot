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

関数を変数に代入できます。

## アロー関数したい

```js
const 関数名 = (引数) => 返り値;
const add = (a, b) => a + b;
```

アロー関数はES6で導入された書式です。
単純な処理は、アロー関数で書くとよいみたいです。

## 関数定義の書式について

歴史的な経緯からJavaScriptには関数を定義する書式が複数あります。
まずは、`function`を使った書式を体得すればよいと思います。
この書式は、初期のJSから使えるものですが、
JSでは後方互換性を保つことが大事にされているため、モダンJSでも動作します。

アロー関数はES6で新機能として導入された書式です。
利用可能な環境であれば積極的に使えばよいと思います。
いろいろと省略できるため、`function`書式に比べてコード行数を圧倒的に減らすことができます。

ただし、しばらく使ってみた感想として、複雑な処理を書くとあとで分かりにくいなと感じました。
それぞれ機能と構文が異なりますが、可読性の観点からも、書式の使い分けを考えてもよさそうです。
