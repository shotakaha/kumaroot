# メールを送りたい

```js
MailApp.sendEmail(mailTo, mailTitle, mailBody)
```

## ドキュメントを読み込んで本文を作成したい

```js
function sendMail(mailTo, docId) {
    // mailTo = 宛先アドレス
    // docId = GoogleドキュメントのID

    const doc = DocumentApp.openById(docID);
    const mailTitle = doc.getName();
    const mailBody = doc.getBody().getText();
    MailApp.sendEmail(mailTo, mailTitle, mailBody);
}
```

Googleドキュメントと連携してメールを送る方法です。
ドキュメントのタイトルをメールの件名にし、内容をメールの本文として利用しています。
