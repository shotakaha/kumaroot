# スプレッドシートを開きたい（`openById` / `openByUrl`）

```js
// IDを指定する
const book = SpreadsheetApp.openById("スプレッドシートのID");

// URLを指定する
const book = SpreadsheetApp.openByUrl("スプレッドシートのURL");
```

`SpreadsheetApp.openById`を使ってスプレッドシートIDを指定してアクセスできます。
スタンドアロンなスクリプトや、他のスクリプトからも開くことができるため、非常によく使うメソッドのひとつです。

`SpreadsheetApp.openByUrl`を使ってURLを直接指定して開くことができます。

## バインドしたスプレッドシートを開きたい（`getActiveSpreadsheet）

```js
// バインドされたスクリプト
const book = SpreadsheetApp.getActive();
const book = SpreadsheetApp.getActiveSpreadsheet();
```

スプレッドシートにバインドしたスクリプトの場合、
`getActive` もしくは `getActiveSpreadsheet` で、
紐づいているスプレッドシートにアクセスできます。
