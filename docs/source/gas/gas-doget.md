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

上のサンプルでは、あるシートに紐づいた`doGet`関数を定義しています。
GETリクエストは
`https://script.google.com/macros/s/スクリプトID/exec?name=John`
を想定しています。
クエリが`?name=John`となっているので、
`e.parameter.name`で`John`という値を取得できます。

また`name`を使って`message`の文字列を作成しています。
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

## テストしたい

```js
function testDoGetParameters() {
    const e = {
        "parameter": {
            "name": "John"
        }
    };
    const response = doGet(e);
    const content = response.getContent();
    Logger.log(`content: ${content}`)
}

function testDoGetURL() {
    const base_url = ScriptApp.getService().getUrl();
    Logger.log(`Base URL: ${base_url}`)
    const query = "?name=John"
    Logger.log(`Query: ${query}`)

    const url = base_url + query

    const options = {
        "method": "GET",
        "followRedirects": true,
    };
    const response = UrlFetchApp.fetch(url, options)
    Logger.log(`response: ${response}`)
}
```

[UrlFetchApp](./gas-request.md)で、`doGet`関数の動作確認ができます。

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

## 複数GETしたい

```js
DOGET = {
    "action1": doGetOne,
    "action2": doGetTwo,
    "action3": doGetThree,
}

function doGet(e) {
    const action = e.parameter.action
    return DOGET[action](e)
}

function doGetOne(e){ ... }
function doGetTwo(e){ ... }
function doGetThree(e){ ... }
```

`doGet`関数は、ひとつのプロジェクトで、ひとつしか定義できない、特殊な関数です。
しかし、スタンドアロンなプロジェクトから、
複数のプロジェクトを操作したいこともあります。
その場合、クエリーを使って分岐させます。
