# POSTリクエストを処理したい（`doPost`）

```js
function doPost(e) {
    // JSON形式のリクエストボディを想定
    const data = JSON.parse(e.postData.contents);
    const name = data.name || "world";
    return ContentService.createTextOutput(`Hello, ${name}!`);
}
```

`doPost`関数は、ウェブアプリとして公開したGASがPOSTリクエストを受け取ったときに呼ばれる関数です。
GASのエディターから`ウェブアプリ`としてデプロイすると、
`https://script.google.com/macros/s/スクリプトID/exec`
に対してPOSTリクエストを送れるようになります。

`doPost`関数は、ひとつのプロジェクトにひとつだけ定義できます。

## 引数したい（`e`）

`doPost(e)`の引数`e`には、リクエストの情報が入っています。
GETと違い、リクエストボディが`e.postData`に入ります。

| プロパティ | 内容 |
| --- | --- |
| `e.postData.contents` | リクエストボディの文字列 |
| `e.postData.type` | リクエストボディのMIMEタイプ（`application/json`など） |
| `e.postData.length` | リクエストボディのバイト数 |
| `e.parameter` | クエリの値。同じ名前が複数あるときは最後の値 |
| `e.parameters` | クエリの値。同じ名前が複数あるときは配列 |
| `e.queryString` | クエリ文字列そのもの（`name=John`） |

JSON形式でPOSTされたときは、`e.postData.contents`を`JSON.parse`でオブジェクトに変換します。
`application/x-www-form-urlencoded`形式でPOSTされたときは、GETと同じように`e.parameter`から値を取得できます。

## MIMEタイプしたい（`ContentService`）

レスポンスは`ContentService.createTextOutput`で作成します。
デフォルトのMIMEタイプは`TEXT`なので、テキストを返すだけなら`setMimeType`は不要です。

```js
// JSON形式で返すときはMIMEタイプを明示する
return ContentService.createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
```

## リファレンス

- [ウェブアプリ | Apps Script](https://developers.google.com/apps-script/guides/web?hl=ja)
- [Class ContentService | Apps Script](https://developers.google.com/apps-script/reference/content/content-service?hl=ja)
