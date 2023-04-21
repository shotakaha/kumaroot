# フォームしたい（``FormApp``）


## 回答後のメッセージをカスタマイズしたい

```js
function setConfirmedMessage() {
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
