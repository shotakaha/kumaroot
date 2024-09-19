# GETリクエストしたい（`doGet`）

```js
function doGet(e) {

    // https://script.google.com/macros/s/スクリプトID/exec?name=John へのアクセス

    // クエリから値を取得（?name=John）
    const name = e.parameter.name;

    // コンテンツを作成
    const message = "Hello, " + (name ? name : "world") + "!";

    // レスポンスを返す
    return ContentService.createTextOutput(message).setMimeType(ContentService.MimeType.TEXT);
};
```

`doGet`関数は、GASでGETリクエストを処理するための関数です。
レスポンスは`ContentService.createTextOutput`などで生成し、ウェブアプリとしてデプロイできます。

上のサンプルでは、
`https://script.google.com/macros/s/スクリプトID/exec?name=John`へのアクセス（HTTP GET）を想定しています。
このアクセスのクエリは`?name=John`となっているので、
`e.parameter.name`で`John`という値を取得できます。

この`name`を使って`message`の文字列を作成しています。
そして``ContentService.createTextOutput``を使ってレスポンスを作成しています。
今回はただのテキスト情報なので、MIMEタイプをTEXTにしています。

クエリを`?name=Smith`に変更すると、レスポンスも変わることが想像できると思います。

## デプロイしたい

GASのエディターからデプロイできます。

1. `[デプロイ]` > `[新しいデプロイ]`
2. 種類の選択: `ウェブアプリ`
3. 説明: `（アプリの説明）`
4. 次のユーザーとして実行: `[自分]`
5. アクセスできるユーザー: `[全員]`

## シート名ごとに処理したい

```js
function doGet(e) {

    // クエリからシート名を取得
    const sheetName = e.parameter.sheetName;

    // クエリが見つからない場合
    if (!sheetName) {
        msg = "シート名が指定されていません"
        return ContentService.createTextOutput(msg).setMimeType(ContentService.MimeType.TEXT);
    }

    // スプレッドシートを取得
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = spreadsheet.getSheetByName(sheetName);

    // シート名が見つからない場合
    if (!sheet) {
        msg = `指定されたシートが存在しません: ${sheetName}`
        return ContentService.createTextOutput(msg).setMimeType(ContentService.MimeType.TEXT);
    }

    // シートの内容をJSON形式に変換する処理
    // ...
}
```

`doGet`関数の実用的な（？）サンプルです。
ここでは、あるスプレッドシートに複数のシートがある場合を想定しています。
そして、シートごとに内容をJSON形式で公開し、外部からデータ処理できるようにしたいと考えています。

GASで公開したウェブアプリは
`https://script.google.com/macros/s/スクリプトID/exec`
でアクセスできるようになります。
クエリに`?sheetName=シート名`とすることで、該当するシートのコンテンツにアクセスできます。
