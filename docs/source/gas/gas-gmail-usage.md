# MailAppの使い方

```js
MailApp.sendEmail("メッセージオブジェクト");
MailApp.sendEmail("宛先", "件名", "本文");
MailApp.sendEmail("宛先", "件名", "本文", "オプション");
```

GASからメールするには[MailApp](https://developers.google.com/apps-script/reference/mail/mail-app)を使う方法
[GmailApp](https://developers.google.com/apps-script/reference/gmail/gmail-app)を使う方法の2通りあります。

``MailApp``の方がシンプルに使えて、ちょっと複雑なことをしたい場合は``GmailApp``を使います。

## ドキュメントから本文を読み込んでメールしたい

```js
function sendMail(mailTo, docId) {
    // mailTo = 宛先アドレス
    // docId = GoogleドキュメントのID

    const doc = DocumentApp.openById(docId);
    const mailTitle = doc.getName();
    const mailBody = doc.getBody().getText();
    const mailOption = {
        name: "送信元の名前",
        cc: "CCの宛先,
        bcc: "BCCの宛先",
        }
    MailApp.sendEmail(mailTo, mailTitle, mailBody, mailOption);
}
```

Googleドキュメントと連携してメールを送信できます。
``sendEmail("宛先", "件名", "本文")``を使うのが一番理解しやすいと思います。
ドキュメントのタイトルをメールの件名にし、内容をメールの本文として読み込んでいます。
メールの宛先（``to`` / ``cc`` / ``bcc``）は``,（カンマ）``で区切って複数指定できます。
オプションで``name``を定義すると、メールの送信元の名前を設定できます。

## スプレッドシートからデータを読み込んでメールしたい

```js
function sendMail(mailTo, sheetId, sheetName) {
    // mailTo = 宛先のアドレス
    // sheetId = GoogleプレッドシートのID
    // sheetName = シートの名前

    const sheet = SpreadsheetApp.openById(sheedId).getSheetByName(sheetName);
    const data = sheet.getDataRange().getValues();
    const mailTitle = sheet.getName();
    const mailBody = // dataをなんとかして文字列に変換する
    MailApp.sendEmail(mailTo, mailTitle, mailBody);
}
```

Googleスプレッドシートと連携することもできます。
シートの内容をメールで送信する場合を考えてみました。

## メールの残り回数をしりたい

```js
const quota = MailApp.getRemainingDailyQuote();
Logger.info("残り回数 = " + quota);
```

GASで送信できる1日のメール回数には制限あります。
[getRemainingDailyQuota](https://developers.google.com/apps-script/reference/mail/mail-app?hl=ja#getremainingdailyquota)を使って残り回数を取得できます。
デバッグ中は``console.log``や``Logger.info``を使って確認しながら作業するとよいでしょう。

## 下書きを作成してからメールしたい

```js
const draft = GmailApp.createDraft("宛先", "件名", "本文", "オプション")
Logger.info("draft = " + draft)
// メールを送信する
// draft.send();
```

``GmailApp.createDraft``でメールの下書きが作成できます。
この段階ではまだメールが送信されないので、デバッグ作業に重宝します。
メールを送りたいときは``send()``します。
