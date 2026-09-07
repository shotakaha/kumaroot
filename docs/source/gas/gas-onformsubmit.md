# フォーム送信時に処理したい（`onFormSubmit`）

```js
function onFormSubmit(e) {
    // スプレッドシートにバインドした場合
    const email = e.namedValues["メールアドレス"][0];
    const name = e.namedValues["お名前"][0];
    GmailApp.sendEmail(email, "受付完了", `${name}さま、送信を受け付けました。`);
}
```

`onFormSubmit`関数は、Googleフォームが送信されたときに呼ばれる関数です。

`onFormSubmit`は**インストーラブルトリガー**なので、
`onOpen`や`onEdit`と違い、事前にトリガーの登録が必要です。
そのかわり、メールの送信など認可が必要な操作もできます。

```{seealso}
トリガーの登録方法は [トリガーを作成したい（`ScriptApp.newTrigger`）](./gas-trigger.md) を参照してください。
```

## 引数したい（`e`）

`onFormSubmit(e)`の引数`e`は、**トリガーをどこに登録したか**で中身が変わります。

### スプレッドシートに登録した場合

回答が追記されたスプレッドシートの行として渡されます。

| プロパティ | 内容 |
| --- | --- |
| `e.namedValues` | 質問名をキー、回答を配列にしたオブジェクト（`{"お名前": ["山田"]}`） |
| `e.values` | 回答を左から順に並べた配列（`["2026/09/08 10:00", "山田", ...]`） |
| `e.range` | 追記された行の範囲（`Range`） |

`e.namedValues["質問名"][0]`のように、`[0]`で値を取り出します。

### フォームに登録した場合

フォームの回答オブジェクトとして渡されます。

| プロパティ | 内容 |
| --- | --- |
| `e.response` | 送信された回答全体（`FormResponse`） |
| `e.source` | フォーム本体（`Form`） |

```js
function onFormSubmit(e) {
    const items = e.response.getItemResponses();
    items.forEach(item => {
        Logger.log(`${item.getItem().getTitle()}: ${item.getResponse()}`);
    });
}
```

## リファレンス

- [インストール可能なトリガー | Apps Script](https://developers.google.com/apps-script/guides/triggers/installable?hl=ja)
- [イベントオブジェクト | Apps Script](https://developers.google.com/apps-script/guides/triggers/events?hl=ja)
