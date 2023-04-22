# フォームしたい（``FormApp``）

## 回答後のメッセージをカスタマイズしたい

```js
function set_confirmation_message() {
    const from = FormApp.getActive();
    const doc = DocumentApp.openById("ドキュメントID");
    const txt = doc.getBody().getText();
    Logger.info(txt);
    form.setConfirmationMessage(txt)
}
```

フォーム回答後のメッセージはカスタマイズできます。
フォームの設定からもできますが、メッセージで改行ができません。
複雑な文章を掲載したい場合は、本文をGoogleドキュメントで作成し、``setConfirmationMessage``で読み込ませるとよいでしょう。
ドキュメントの内容を変更した場合は、再度``[実行]``を押し、読み込ませる必要があります。

## フォーム入力時にデータを取得したい

```js
function onFormSubmit(e) {
    // タイムスタンプ
    const timestamp = e.response.getTimeStamp();
    const datetime = Utilities.formatDate(timestamp, "JST", "yyyy-MM-dd'T'HH:mm:ss")
    // 回答したメールアドレス
    const respondentEmail = e.response.getRespondentEmail();
    // 回答内容
    const itemResponses = e.response.getItemResponses();
    const responses = itemResponses.map(function(itemResponse) {
        return itemResponse.getResponse();
    });
}
```

フォームに入力があった場合のデータは``onFormSubmit関数``で取得＆操作できます。
``e.response``は[FormResponseクラス](https://developers.google.com/apps-script/reference/forms/form-response)で、この変数からから情報を取得できます。

タイムスタンプは``getTimeStamp``で取得できます。
そのままだと日付の表示形式が米国風なので、[Utilities.formatDate](https://developers.google.com/apps-script/reference/utilities/utilities#formatDate(Date,String,String))を使ってISO8601形式に変換するとよいです。
``MM``が月で、``mm``が分です（Pythonと逆なので紛らわしいです）

ウェブを検索すると``e.values``で回答内容を取得できるという記事を見かけるのですが、もう廃止されているのか``Undefined``となってしまいました。
その代わりに``getItemResponses``して、[ItemResponseクラス](https://developers.google.com/apps-script/reference/forms/item-response)の配列として取得しています。
さらに、この配列から個別の質問項目の回答を``getResponse``して文字列を取得しています。

:::{seealso}

``itemResponses.map(...)``している部分は、おそらくPythonのリスト内容表表記と同じことをしているはずです。

```python
responses = [itemResponse.getResponse() for itemResponse in itemResponses]
```

:::
