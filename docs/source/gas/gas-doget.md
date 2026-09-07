# GETリクエストを処理したい（`doGet`）

```js
function doGet(e) {
    // https://script.google.com/macros/s/スクリプトID/exec?name=John へのアクセス
    const name = e.parameter.name || "world";
    return ContentService.createTextOutput(`Hello, ${name}!`);
}
```

`doGet`関数は、ウェブアプリとして公開したGASがGETリクエストを受け取ったときに呼ばれる関数です。
GASのエディターから`ウェブアプリ`としてデプロイすると、
`https://script.google.com/macros/s/スクリプトID/exec`
でアクセスできるようになります。

`doGet`関数は、ひとつのプロジェクトにひとつだけ定義できます。

## 引数`e`について

`doGet(e)`の引数`e`には、リクエストの情報が入っています。

| プロパティ | 内容 |
| --- | --- |
| `e.parameter` | クエリの値。同じ名前が複数あるときは最後の値 |
| `e.parameters` | クエリの値。同じ名前が複数あるときは配列 |
| `e.queryString` | クエリ文字列そのもの（`name=John`） |
| `e.pathInfo` | `/exec`より後ろのパス |
| `e.contextPath` | 常に空文字（仕様） |

`?name=John`というクエリでアクセスすると、`e.parameter.name`で`John`を取得できます。
`?tag=a&tag=b`のように同じ名前を繰り返すときは、`e.parameters.tag`で`["a", "b"]`を取得できます。

## レスポンスについて

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
