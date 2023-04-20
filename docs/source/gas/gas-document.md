# ドキュメントしたい（``DocumentApp``）

```js
const doc = DocumentApp.openById("ドキュメントID");
const txt = doc.getBody().getText();
```

[DocumentAppクラス](https://developers.google.com/apps-script/reference/document/document-app)を使ってGoogleドキュメントを操作できます。
[メールの送信](./gas-gmail.md)と組み合わせると最強です。
