# フォームしたい（``FormApp``）

## 回答時にレスポンス取得したい（`onFormSubmit`）

```js
/**
 * @params {FormSubmitEvent} e - 送信トリガーが発生したときに自動的に渡されるイベントオブジェクト
 *
function onFormSubmit(e) {
    // 回答をまとめて取得する
    const itemResponses = e.response.getItemResponses();

    // 回答を「質問名：回答」の形式に変換
    const fallback = itemResponses.map(function(itemResponse) {
        const title = itemResponse.getItem().getTitle();
        const response = itemResponse.getResponse();
        return `${title}: ${response}`;
    }).join("\n");

    // 質問1: 回答1\n
    // 質問2: 回答2\n
    // 質問3: 回答3\n
}
```

`onFormSubmit`は、回答者がフォームを送信したときにトリガーされる関数です。
引数`e`にはイベントオブジェクトが自動的に渡されます。
`e.response.getItemResponses`で回答（`ItemResponse`オブジェクト）の配列を取得できます。

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

入力時のタイムスタンプは``getTimeStamp``で取得できます。
そのままだと日付の表示形式が米国風なので、[Utilities.formatDate](https://developers.google.com/apps-script/reference/utilities/utilities#formatDate(Date,String,String))を使ってISO8601形式に変換しています。
``MM``が月で、``mm``が分です（Pythonと逆なので紛らわしいです）

回答内容は[getItemResponses](https://developers.google.com/apps-script/reference/forms/form-response#getItemResponses())で得られる[ItemResponseクラス](https://developers.google.com/apps-script/reference/forms/item-response)に入っています。
ウェブを検索すると``e.values``で回答内容を取得できるという記事を見かけるのですが、``Undefined``が返ってきます。
適切なドキュメントが見つけられないので、``itemResponses.map``して、回答内容を配列にしています。

:::{seealso}

``itemResponses.map(...)``している部分は、おそらくPythonのリスト内容表表記と同じことをしているはずです。

```python
responses = [itemResponse.getResponse() for itemResponse in itemResponses]
```

:::

## フォーム入力時にカスタムメールを送信したい

```js
function onFormSubmit(e) {
    const message = response_to_text(e.response);
    // test_send_to_group(message);
    send_to_group(message);
}
```

上述した``onFormSubmit関数``で取得した``e.response``を実際に活用する方法です。
おそらく、フォームに入力があった場合には、メールやSlackなどで関係者に通知したいことが多いと思います。

::: {seealso}

Googleフォームの共同編集者にアサインしたアカウントであれば、標準機能を使って各人で通知設定の可否を設定できます。
また、回答者に回答内容のコピーを自動で送信できます。
今回のケースは「カスタム」したメッセージなどを送りたいケースを想定しています。

:::
